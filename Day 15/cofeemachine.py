from main import resources as res
from main import MENU as men
from art import logo
print(logo)
def report():
    print("Water:",res["water"])
    print("Milk:",res["milk"])
    print("Coffee",res["coffee"])
def make_drink(drink_name):
    drink=men[drink_name]
    ing=drink["ingredients"]
    for item in ing:
        if ing[item]>res[item]:
            print("Insufficent ",item,"please refil")
            return False
        else:
            res[item]-=ing[item]
    return True
def process_coin(coins):
    quart=int(input("Enter number of quarters\n"))
    dime=int(input("Enter number of dimes\n"))
    nic=int(input("Enter number of nickels\n"))
    pen=int(input("Enter number of pennis\n"))
    total=quart*0.25+dime*0.10+nic*0.05+pen*0.01
    if total-coins>0:
     print("Change : ",total-coins)
     return True
    elif total-coins<0:
     print("Money insufficient refunded")
     return False
    
while True:
    choice=input("What would you like?(espresso,latte,cappuccino)")
    if choice=='report':
        report()
    elif choice in ['espresso','latte','cappuccino']:
        if make_drink(choice):
            if(process_coin(men[choice]["cost"])):
                print("Order succcessfull enjoy your ☕")
    elif choice=='off':
        break;
    else:
        print("Enter valid option")
    
    