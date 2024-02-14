"""
CMPS 2200  Assignment 1.
See assignment-01.pdf for details.
"""
# no imports needed.

def foo(x):
  if x <= 1:
    return x
  else:
    return foo(x-2) + foo(x-1)

def longest_run(mylist, key):
  x = 0
  y = 0
  for num in mylist:
    if num==key:
      x+=1
    else:
      x = max(x,y)
      y = 0
  return max(x,y)


class Result:
    """ done """
    def __init__(self, left_size, right_size, longest_size, is_entire_range):
        self.left_size = left_size               # run on left side of input
        self.right_size = right_size             # run on right side of input
        self.longest_size = longest_size         # longest run in input
        self.is_entire_range = is_entire_range   # True if the entire input matches the key
        
    def __repr__(self):
        return('longest_size=%d left_size=%d right_size=%d is_entire_range=%s' %
              (self.longest_size, self.left_size, self.right_size, self.is_entire_range))
    

def to_value(v):
    """
    if it is a Result object, return longest_size.
    else return v
    """
    if type(v) == Result:
        return v.longest_size
    else:
        return int(v)
        
def longest_run_recursive(mylist, key):
  if len(mylist) < 2:
    if mylist and mylist[0] == key:
      return Result(1, 1, 1, True)
    else:
      return Result(0, 0, 0, False)



