
import importlib
from config import config

prog = {}

try:
    for prog_i in config['program_map']:
        for k,v in prog_i.items():
            prog[k] = importlib.import_module('program.%s'%v)
        
except:
    pass

print("eBPF program loaded")
print(prog)

def run_prog(prog_name,time):
    if(prog_name not in prog.keys()):
        return -4
    if(time > config['max_running_time']):
        return -2
    
    return prog[prog_name].run(time=time)



