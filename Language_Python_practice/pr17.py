number=int(input("Type your number: "))
result=[]
fixed_width=len("{:b}".format(number))
for i in range(1,number+1):
    result.append("{number:{width}d} {number:{width}o} {number:{width}X} {number:{width}b} {space}".format(number=i, width=fixed_width, space="\n"))
result=''.join(result)
print(result)
