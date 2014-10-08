''':mod:`Daemon` --- Module for creating a daemon process
==================================================

.. module:: Daemon
    :platform: OS X, Linux
    :synopsis: Module for creating a daemon process.

.. moduleauthor:: Michael R. Bryan <Michael DOT Bryan AT mail DOT rit DOT edu>

'''

import os
from resource import getrlimit, RLIMIT_NOFILE, RLIM_INFINITY

def daemonize():
    """.. method:: daemonize()

        This method daemonizes the process in which it is called. Currently, it is not intended for
        Windows platforms.
              
    """
# daemonize
    try:  # fork process allowing the cmd line process to exit
        pid=os.fork()
    except OSError as err:
        print err
        raise
    if pid == 0: # in new child process, become session leader
        os.setsid()
        try: # and fork again
            pid=os.fork()
        except OSError as err:
            print err
            raise
        if pid != 0: # in parent of daemon process, exit 0
            os._exit(0)
    else: # in parent cmd line process, exit 0
        os._exit(0)
    # collecting resource usage information and closing all open resources inherited
    # from parent processes is a best practice
    max_fd = getrlimit(RLIMIT_NOFILE)[1]
    if max_fd == RLIM_INFINITY:
        max_fd = 1024
    for fd in range(max_fd):
        try:
            os.close(fd)
        except OSError:
            pass
    # redirect std* to /dev/null
    os.open(os.devnull,os.O_RDWR)
    os.dup2(0,1)
    os.dup2(0,2)
    return 0
