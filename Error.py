x = 1869696997970879779978789797978797
assert (x>=0), "x is not positive"
try:
   Value = 10/9 
   number = int(input("Enter a number: "))
   print(number)
    
except ZeroDivisionError as err:
      print(err)
except ValueError:
    print("Invalid input")

else:
    print("Good code")
finally:
      print("cleaning up...") 
