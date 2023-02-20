# python3

import sys
import threading
import requests


def compute_height(n, parents):
    # Write this function
    max_height = 0
    # Your code here
    return max_height


def main():
    test_url = "https://github.com/DA-testa/steks-un-iekavas-alinaeksta/blob/main/test/0"
    check = input()
    if check.startswith("I"):
        text = input()
    else:
        text = requests.get(test_url).text
        
    # implement input form keyboard and from files
     

    # let user input file name to use, don't allow file names with letter a
    # account for github input inprecision
    
    # input number of elements
    # input values in one variable, separate with space, split these values in an array
    # call the function and output it's result


# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
