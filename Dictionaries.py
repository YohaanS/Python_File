
monthConversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December",
}

print(monthConversions["Jan"])
print(monthConversions.get("Aug"))
print(monthConversions.get("Luv", "Not a valid Key"))
mydict = {"name": "Max", "age": 30, "city": "New york"}
print(mydict)

mydict2 = dict(name="Mary", age=27, city="Boston")
print(mydict2)

value = mydict["name"]
print(value)
mydict["email"] = "coolmax@xyz.com"
mydict["password"] = "coolmax@28"
mydict["lastname"] = "John"
mydict["Job"] = "Coder"
print(mydict)

del mydict["password"]
mydict.pop("email")
mydict.popitem()
print(mydict)

try:
    print(mydict["Doctor"])
except:
    print("Error")
   
mydict.update(mydict2)
print(mydict)
my_dict = {3: 9, 6: 36, 9: 81}
print(mydict)

mytuple = (8, 7)
my_dict = {mytuple: 15}

print(my_dict)