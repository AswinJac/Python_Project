import os
from art import logo as l
clear=lambda: os.system('cls')
def sum(a,b):
    return a+b
def pro(a,b):
    return a*b
def diff(a,b):
    return a-b
def div(a,b):
    return a//b
while(True): 
 print(l)
 ch='y'
 num1=int(input("Enter first number:"))
 while(ch!='n'):
    res=0
    print("+\n/\n-\n*")
    op=input("Enter Operator")
    num2=int(input("Enter Second number:"))
    if op=='+':
        res=sum(num1,num2)
        print(f"{num1} {op} {num2}=",res)
    elif op=='-':
        res=diff(num1,num2)
        print(f"{num1} {op} {num2}=",res)
    elif op=='/':
        res=div(num1,num2)
        print(f"{num1} {op} {num2}=",res)
    elif op=='*':
        res=pro(num1,num2)
        print(f"{num1} {op} {num2}=",res)
    ch=input(f"Type 'y' to continue calculating with {res} Type 'n' to start new calculation")
    num1=res
          
        
    