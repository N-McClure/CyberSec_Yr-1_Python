for m in range(1,11):
    for n in range(1,11):
        print(f"{m*n}", end="\t")
    print()

print()

name = str(input("Enter student name: "))
while name != "###":
    print(f"hello {name}")
    courseNum = int(input("How many courses do you have?: "))

    total = 0

    for i in range(1,courseNum+1):
        mark = int(input("Enter course Mark: "))
        total += mark
    if courseNum > 0 :
        print(f"Average: {total / courseNum}")

    name = str(input("Enter student name: "))