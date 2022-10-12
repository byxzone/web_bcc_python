## How to use this project

- requirements: `bcc`,`flask`,`pyyaml`

- run web.py:`sudo ./web.py`

- open `http://localhost:8088/api/run_prog?prog=hello_world&time=1` (host,port defined in `config.yaml`)

## How to add BCC eBPF program to this project

### 1.edit your BCC program

- define a function called `run`, and an argument called `time`

- move the `attach_kprobe` statement to `run`

- add time count statement to run `time` seconds

- detach the kprobe when program finished

- return the result in json (use common.to_json)

`./program/template.py` is an example

### 2.add program_map in config.yaml

- open `./config.yaml`

- add item in `program_map`, in this format `- prog_name: prog_file_name`, like `- hello_world: template `

