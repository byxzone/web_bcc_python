from flask import Flask, request
import json
from program.common import code_msg
import prog
from time import time
from config import config

app = Flask(__name__)

def genReturnJson(code:int,data):
   result = {}
   result['code'] = code
   result['message'] = code_msg[code]
   result['timestamp'] = int(time())
   result['data'] = data
   return json.dumps(result)

@app.route('/api/test')
def test():
   return genReturnJson(1,'hello_world!')

@app.route('/api/run_prog')
def run_prog():
   prog_name = request.args.get("prog")
   time = int(request.args.get("time"))
   result = prog.run_prog(prog_name,time)
   if(type(result) == int):
       return genReturnJson(result,'')
   else:
      return genReturnJson(1,result)
    

if(__name__ == '__main__'):
   app.run(debug=False,host=config['host'],port=config['port'])