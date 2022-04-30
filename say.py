import sys
from sayings import goodbye

if len(sys.argv) ==2:
    goodbye(sys.argv[1])

    # python say.py everyone
    # output =  goodbye, everyone, from sayings import
    # could use goodbye.sayings or import just sayings if using hello as well