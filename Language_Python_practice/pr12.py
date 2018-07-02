def swap_case(s):
    return ''.join([i.lower() if i.isupper()==True else i.upper() for i in s])
##using .swapcase() built-in function
##def swap_case(s):
##  return s.swapcase()
