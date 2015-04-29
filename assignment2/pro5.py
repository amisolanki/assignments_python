print("This program calculate the salary of the employee according to gender and crieteria")
gender=str(input("Enter gender==>>"))
Current_Salary=int(input("Enter your current salary==>>"))

if gender=="male" and Current_Salary<1000:
    bonus=(Current_Salary*5)/100
    print("**********************************************************************************")
    print("Current salary=%d and gender=%s..."%(Current_Salary,gender))
    print("After adding the bonus=%f to the current salary...\nCurrent salary="%(bonus),bonus+Current_Salary)
    print("**********************************************************************************")
   
elif gender=="female" and Current_Salary<1000:
    bonus=(Current_Salary*5.5)/100
    print("*********************************************************************************")
    print("Current salary=%d and gender=%s..."%(Current_Salary,gender))
    print("After adding the bonus=%f to the current salary...\nCurrent salary="%(bonus),bonus+Current_Salary)
    print("*********************************************************************************")
else:
    bonus=(Current_Salary*5)/100
    print("*********************************************************************************")
    print("Current salary=%d and gender=%s...bonus is:"%(Current_Salary,gender))
    print("After adding the bonus=%f to the current salary...\nCurrent salary="%(bonus),bonus+Current_Salary)
    print("*********************************************************************************")
