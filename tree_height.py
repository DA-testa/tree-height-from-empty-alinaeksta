# python3

import sys
import threading
import numpy as np


def main():
  # implement input form keyboard and from files
  check_for_I = input().upper()

  if check_for_I == "I":
    n = int(input("Input n: "))
    # a=int(input("Size of array:"))

    parents = np.array(input("Element:").split())

    # print(parents[1])
    compute_height(n, parents)

  # let user input file name to use, don't allow file names with letter a
  # account for github input inprecision

  elif check_for_I == "F":
    file_name = input().strip()
    if 'a' in file_name:
      print("File name cannot contain letter 'a'!")
      return
    try:
      with open('test/' + file_name, 'r') as f:
        n = int(f.readline())
        parents = list(map(int, f.readline().split()))
        # print(compute_height(n, parents))
    except FileNotFoundError:
      print("File not found!")
      return


def compute_height(n, parents):
  # Write this function
  # heights = np.array()
  counter = 0
  # max_height = 0
  # Your code here
  for i in range(n):
    # node_height = 0
    if parents[i] == "-1":
      start = i
      counter = counter + 1
      break
                 
  for g in range (n):
    val = start
    if parents[g] == str(val):
      val = g
      counter = counter + 1

      

  

  print(counter)

  
      
   
      #print("trr")
    # parent = parents[i]
    # while parent != - 1:
    #     if heights[i]:
    #         node_height += heights[i]
    #         break
    #     node_height += 1
    #     parent = parents[parent]
    # heights[i] = node_height
    # max_height = max(max_height, node_height)

  # return max_height


#     # input number of elements
#     # input values in one variable, separate with space, split these values in an array
#     # call the function and output it's result

# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size
threading.Thread(target=main).start()
# print(numpy.array([1,2,3]))
