#!/usr/bin/env python

# ------------------------------------------------------------------
# watch.py
#
# Call

"""
Usage of this script:

$ export DBUS_SESSION_BUS_ADDRESS="tcp:host=127.0.0.1,port=6666"
$ watch.py qdbus at.ac.ait.QkdModule.qkd_presift /data org.freedesktop.DBus.Properties.Get at.ac.ait.OIDStore detector_matrix

credits: Cristina Tamas, Oliver Maurhart, Andreas Poppe
""" 

import subprocess
import string
import sys
import time

def main():

    # this is the timeout in seconds, fractions allowed
    TIMEOUT_SEC = 0.250
    args = sys.argv[1:]

    # loop forever
    while True:
        
        # create and call process, store output and error in "o" and "e"
        p = subprocess.Popen(args, stdout = subprocess.PIPE)
        o, e = p.communicate()
        
        # show results to user
        sys.stdout.write(str(time.time()) + ": " + o)
        
        # wait for next turn
        time.sleep(TIMEOUT_SEC)

if __name__ == '__main__':
    main()
