num=int(input("Enter the number"))
if num>1:
    for i in range(2,num):
        if(num%i)==0:
            print(num,"number is not prime number")
            break
    else:
        print("number is prime")
else:
print(num,"number is not prime number")
