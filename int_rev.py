integer = int(input('Enter your digit: '))
l = []
l1 = []
found = False
change = str(integer)
for i in change:
    l.append(i)
    # print(l)
    found = True
    break

for i in change:
    l1.append(i)
    l4 = list(reversed(l1))
    l4.pop()
l.extend(l4)
u = ''.join(l)
print(int(u))

    
    
    
# print(list(reversed(l1)))


    
    # l1.pop()
    
    
# print(l1)
    
    
 
    
    

    
    

# rev = l[::-1]
# print(rev)

# back = int(rev)
# print(back)
    
