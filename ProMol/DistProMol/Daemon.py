''':mod:`Daemon` --- Module for creating a daemon process
==================================================

.. module:: Daemon
    :platform: OS X
    :synopsis: Module for creating a daemon process.

.. moduleauthor:: Michael R. Bryan <Michael DOT Bryan AT mail DOT rit DOT edu>

'''

import os
from resource import getrlimit, RLIMIT_NOFILE, RLIM_INFINITY

def daemonize():
    """.. method:: daemonize()

              
    """
# daemonize
    # fork process allowing the cmd line process to exit
    try:
        pid=os.fork()
    except OSError as err:
        raise Exception, '{0} [{1}]'.format(err.strerror,err.errno)
    # in new child process, become session leader
    if pid == 0:
        os.setsid()
        # fork again
        try:
            pid=os.fork()
        except OSError as err:
            raise Exception, '{0} [{1}]'.format(err.strerror,err.errno)
        # in session leader parent of daemon process, exit 0
        if pid != 0:
            os._exit(0)
    else:
        # in parent cmd line process, exit 0
        os._exit(0)
    # node has been daemonized
    # collect resource usage information and close all open resources inherited from parent processes
    maxf = getrlimit(RLIMIT_NOFILE)[1]
    if maxf == RLIM_INFINITY:
        maxf = 1024
    for f in range(maxf):
        try:
            os.close(f)
        except OSError:
            pass
    # redirect std* to /dev/null
    os.open(os.devnull,os.O_RDWR)
    os.dup2(0,1)
    os.dup2(0,2)
    #return successfully
    return(0)
