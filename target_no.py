target = int(input('Enter your target no: '))
lis = list(map(int,input('Enter your list(separated by commas): ').split(',')))
found = False
for i in range(len(lis)):
    for j in range(i+1,len(lis)):
        if lis[i] + lis[j] == target:
            print(f'Numbers and index that makes {target}')
            print(f'Numbers: {lis[i]} , {lis[j]}')
            print(f'index: {i} , {j}')
            found = True
            break
    if found:
        break
            
            
    