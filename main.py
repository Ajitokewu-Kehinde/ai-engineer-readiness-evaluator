# AI ENGINEER READINESS EVALUATOR

print("\n WELCOME TO AI ENGINEER READINESS EVALUATOR!\n")
print("This program will help you determine if you are ready to become an AI Engineer.\n")

python_hours = float(input("enter your python practice hours weekly: "))
math_level = int(input("enter your math comfort level (1-10): "))
projects_built = int(input("enter your number of built projects:"))

if python_hours >= 20:
    print("\nYou will have a strong foundation in python.")
elif python_hours > 10:
    print("\nYou will have a good foundation in python.")
else:
    print("\nYou will need to work on time management and dedicate more time for Learning.\n")

if math_level >= 7:
    print("Ready to Learn Linear Algebra")
else:
    print("I suggest you spend 15-20 minutes a day for studying math.\n")


if projects_built >= 0:
    print("Portfolio Status: Great job! Building is the best way to learn.")
else:
    print("portfolio Status: This scripts is your official Project #1!\n")

total_score = (python_hours * 0.5) + (math_level * 5) + (projects_built * 20)
print("Your total readiness score is: ", total_score)

if total_score >= 80:
    print("Status: Ready for advanced AI Engineer topic and projects!")
elif total_score >= 30:
    print("Status: Ready for intermediate python & API integration!")
else:
    print("Status: Ready to Finish python fundamentals and start building projects!.")

