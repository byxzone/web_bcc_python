from bcc import BPF
from time import sleep

try:
    from program.common import to_json
except:
    from common import to_json
        
# define BPF program
prog = """
int hello(void *ctx) {
    bpf_trace_printk("Hello, World!\\n");
    return 0;
}
"""

# load BPF program
b = BPF(text=prog)

def run(time:int): #define a function called "run" and a argument called 'time'
    b.attach_kprobe(event=b.get_syscall_fnname("clone"), fn_name="hello") #attach kprobe in function 'run'
    result = [] #save the result value
    while(time > 0):
        try:
            result.append(b.trace_readline().decode()) #save each time output to result
            sleep(1) #delay 1s
            time -= 1 #time count dec 1
        except ValueError:
            continue
    b.detach_kprobe(event=b.get_syscall_fnname("clone"), fn_name="hello") #detach kprobe when program finish
    return to_json(result) #return result when time=0
        
if __name__ == '__main__': #test (do not need to write)
    print(run(time=1))