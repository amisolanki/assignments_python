print("This program is to check whether the given planet is inner or outer...")
Planet_Name=['Mercury','Venus','Earth','Mars','Jupiter','Saturn','Uranus','Neptune']
print(Planet_Name)

planet=input("Enter planet name:")


if planet!=Planet_Name[0:8]:
    print("Please provide acceptable input value...")

else:


    
    if planet in Planet_Name[0:2]:
        print("Inner planet is chosen by you")

    elif planet==Planet_Name[2]:
        print("You are on Earth")
   


    else:

        print("It's an outer planet")

     



    
