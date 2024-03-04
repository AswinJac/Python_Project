import os
from art import logo as l
clear = lambda: os.system('cls')
flag="yes"
lot={}
clear()
print(l)
print("Welcome To Secret Bidding")
while flag!="no":
    name=input("Enter Name:")
    amount=int(input("Enter Amount:"))
    lot[name]=amount
    flag=input("Do you want to continue (yes/no)")
    if flag=="yes":
        clear()
clear()
list=[]
for key in lot:
    list.append(lot[key])
large=max(list)
for key in lot:
    if lot[key]==large:
        print("Auction Won By '",key,"' With an amount of '",large,"'")
        


    
     

