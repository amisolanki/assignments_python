print("The program to check whether the no. is prime or not")

num=int(input("Enter the no.=>>"))

a=int(num/2)


flag=0
for i in range(2,a):

    if num%i==0: 
        print("No. is not prime")

        flag=1
        break
    if flag==0:
        print("Given number is prime") 
    else:
        print("No. is  prime")
        
       
