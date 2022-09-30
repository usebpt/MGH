import sys



def list_path_in_sys(print_out=1):
    print (__file__)
    for p in sys.path:
        if print_out:
            print (p)

    return sys.path
