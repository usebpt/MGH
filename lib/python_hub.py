import sys


#-----------------------------------------------------------------------------
# 
def list_path_in_sys(print_out=1):
    """
    func list_path_in_sys(print_out=1)
        get list of path that it is include into sys

    param:
        print_out is 1 if we need to print info to screen

    return 
        Array(str)
    """
    print (__file__)
    for p in sys.path:
        if print_out:
            print (p)

    return sys.path
