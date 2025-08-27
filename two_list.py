l1 = input('Enter your list1(without any space or commas): ')

l2 = input('Enter your list2(without any space or commas): ')
reve1 = l1[::-1]
reve2 = l2[::-1]
l3 = list(map(int,l1))
l4 = list(map(int,l2))
print(f'Your Given list1 {l3} and list2 is {l4}')
inter = int(reve1)
inter1 = int(reve2)
add = str(inter + inter1).split()

for i in add:
    lis = list(map(int,i))
rev = list(reversed(lis))
    
    
print(rev)
    
