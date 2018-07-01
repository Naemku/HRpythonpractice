n=int(input("The number of scores: "))
arr=list(set(map(int, input().split())))
arr.sort(reverse=True)
print(arr[1])

#Using sorted()
#n=int(input())
#arr=sorted(set(map(int,input().split())))
#print(arr[-2])
