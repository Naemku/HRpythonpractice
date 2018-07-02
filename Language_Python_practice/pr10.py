N = int(input())
storage=[]
for _ in range(N+1):
    command, *raw_item = input().split()
    int_item=list(map(int, raw_item))
    if command=='insert':
        storage.insert(int_item[0], int_item[1])
    elif command=='print':
        print(storage)
    elif command=='remove':
        storage.remove(int_item[0])
    elif command=='append':
        storage.append(int_item[0])
    elif command=='sort':
        storage.sort()
    elif command=='pop':
        storage.pop()
    elif command=='reverse':
        storage.reverse()
