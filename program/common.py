from time import time
import json


code_msg = { 1:'success',
             0:'null',
            -1:'internal_error',
            -2:'exceeded_maximum_running_time',
            -3:'program is already running',
            -4:'program is not exsit'
}

def to_json(data):
    result = {'time':int(time()),'data':data}
    return(json.dumps(result))
    