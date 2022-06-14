def human_body():
    functions_in_the_body = input("What system is used to eat?")
    organs = input("What organ is like the boss of your body?")
    Bones = input("What is the name of the largest bone in your body?")
    Teeth = input("What is the name of hard outer covering of Teeth?")
    Blood_and_the_Heart = input("How many gallons of blood does the heart pump every day?")
    print(functions_in_the_body)
    if str(functions_in_the_body) == str("Digestive System"):
        print("You are right") 
    else:
        print("You are incorrect")
    print(organs)
    if str(organs) == str("The Brain"):
        print("You are right") 
    else:
        print("You are incorrect")    

    print(Bones)
    if str(Bones) == str("The Femur"):
        print("You are right") 
    else:
        print("You are incorrect")
    print(Teeth)
    if str(Teeth) == str("Enamel"):
        print("You are right") 
    else:
        print("You are incorrect")

    print(Blood_and_the_Heart)
    if str(Blood_and_the_Heart) == str("2000"):
        print("You are right") 
    else:
        print("You are incorrect")                 

human_body()


              