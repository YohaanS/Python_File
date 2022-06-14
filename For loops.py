for letter in "Yohaan Singla":
    print(letter)
friends = ["Pranav","Nammer","Evie","Shmaika","Hussain","Danny"]
for friend in friends:
    print(friend)
for index in range(9):
    print(index)
for index in range(6, 9):
    print(index)
for index in range(len(friends)):
    print(friends[index])
for index in range(5):
    if index == 0:
        print("First Iteration") 
    else:
        print("Not first")
number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]

]

for row in number_grid:
    for col in row:
        print(col)