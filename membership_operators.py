print("Enter marks obtaineed in 5 subjects:")

markOne = int(input("Subject 1: "))
markTwo = int(input("Subject 2: "))
markThree = int(input("Subject 3: "))
markFour = int(input("Subject 4: "))
markFive = int(input("Subject 5: "))

total = markOne + markTwo + markThree + markFour + markFive
avg = int(total / 5)

print("Average mark:", avg)

validRange = range(0, 101)

if avg not in validRange:
    print("Invalid input!")
elif avg in range (91, 101):
    print("Your grade is A+")
elif avg in range (81, 91):
    print("Your grade is A-")
elif avg in range(71, 81):
    print("Your grade is B+")
elif avg in range(61, 71):
    print("Your grade is B-")
elif avg in range(51, 61):
    print("Your grade is C+")
elif avg in range(41, 51):
    print("Your grade is C-")
elif avg in range(33, 41):
    print("Your grade is D")
elif avg in range(21, 33):
    print("Your grade is E")
elif avg in range(0, 21):
    print("Your grade is F")