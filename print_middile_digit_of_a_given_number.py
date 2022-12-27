# question 2
# write a program to print the middle digit of a given number


#---------method 1---------#
no = int(input("Enter a number : "))
nnn = str(no)
oup = ''
if len(nnn)%2==0:
    oup = oup+nnn[(len(nnn)//2)-1]+nnn[len(nnn)//2]
else:
    oup = oup+nnn[(len(nnn)//2)]
print(oup)

#---------method 2---------#
'''
no = int(input('Enter a number : '))
lss = [int(x) for x in str(no)]
if (len(lss)%2==0):
    print(lss[len(lss)//2-1],lss[len(lss)//2])
else:
    print(lss[len(lss)//2])
'''
