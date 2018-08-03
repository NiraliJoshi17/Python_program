num1=float(input("enter 1 num"))
num2=float(input("enter 2 num"))
print("1 add 2 sub 3 mul 4 div 5 mod 6 pow")
operation=int(input())
if operation==1:
    print("add :",num1+num2)
    
elif operation==2:
    print("sub :",num1-num2)

elif operation==3:
    print("mul :",num1*num2)
    
elif operation==4:
    print("div :",num2/num2)
    
elif operation==5:
    print("mod :",num1%num2)
    
elif operation==6:
    print("pow :",num1**num2)

else:
    print("enter valid choise")
    
    
