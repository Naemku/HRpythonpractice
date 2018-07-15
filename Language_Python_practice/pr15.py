def wrap(string,max_width):
    pointer=0
    a=[]
    while True:
        if len(string[pointer:])>=max_width:
            a.append(string[pointer:pointer+max_width])
            pointer+=max_width
        elif len(string[pointer:])<max_width and len(string[pointer:])>0:
            a.append(string[pointer:])
            pointer=len(string)
        else:
            break
    result="\n".join(a)
    return result
