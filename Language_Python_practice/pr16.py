input_data=input().split()
int_input_data=list(map(int, input_data))
counter=1
multiplier=1
while True:
    if counter<(int_input_data[0]//2)+1:
        print(('.|.'*(multiplier*2-1)).center(int_input_data[1],'-'))
        counter+=1
        multiplier+=1
    elif counter==(int_input_data[0]//2)+1:
        print('WELCOME'.center(int_input_data[1],'-'))
        counter+=1
    elif counter>(int_input_data[0]//2)+1:
        multiplier-=1
        print(('.|.'*(multiplier*2-1)).center(int_input_data[1],'-'))
        counter+=1
        if counter>int_input_data[0]:
            break
