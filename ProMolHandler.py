from ZSI import dispatch
from mod_python import apache

import MyHandler
mod = __import__('encodings.utf_8', globals(), locals(), '*')
mod = __import__('encodings.utf_16_be', globals(), locals(), '*')

def handler(req):
    dispatch.AsHandler(modules=(MyHandler,), request=req)
    return apache.OK
