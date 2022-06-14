
Gender_file = open("freeCodeCamp/print/Codes_That_Hold_Info/string_projects/Giraffe/genders.txt", "r")

print(Gender_file.readable) 
print(Gender_file.readline())
print(Gender_file.readline())
print(Gender_file.readline())
print(Gender_file.readline())
Gender_file.close()

Gender_file = open("Web.html", "w")

Gender_file.write("Evie - Female")

Gender_file.close()