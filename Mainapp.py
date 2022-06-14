from Student import Student   

Student1 = Student("Jim", "Business",3.1)
Student2 = Student("Rajeev", "Coder", 4.0)
Student3 = Student("Yohaan", "Coder", 3.549999)

val1 = Student1.on_honor_roll()
val2 = Student2.on_honor_roll()
print(bool(val1))
print(val2)
print(Student3.on_honor_roll())