#ProMolHandler
#Must be identified in apache configuration file as the handler to use
#for the URI specifying the directory containing all of these programs.
from ZSI import dispatch
from mod_python import apache

import promoldaemon
mod = __import__('encodings.utf_8', globals(), locals(), '*')

def handler(req):
    dispatch.AsHandler(modules=(promoldaemon,), request=req)
    return apache.OK
