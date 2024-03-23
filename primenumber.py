def prime(num):
    flag = 0
    for i in range(2, num):
        if num % i == 0:
            flag = 1
            break
    if flag == 1:
        print("Not a prime number")
    else:
        print("A prime number")


number = int(input("Enter a number to check"))
prime(num=number)



