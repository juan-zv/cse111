print("This program is an implementation of the Rosenberg")
print("Self-Esteem Scale. This program will show you ten")
print("statements that you could possibly apply to yourself.")
print("Please rate how much you agree with each of the")
print("statements by responding with one of these four letters:")
print("\nD means you strongly disagree with the statement.")
print("d means you disagree with the statement.")
print("a means you agree with the statement.")
print("A means you strongly agree with the statement.")
Q1 = input("\n1. I feel that I am a person of worth, at least on an equal plane with others."
"Enter D, d, a, or A: ")
Q2 = input("\n2. I feel that I have a number of good qualities."
"Enter D, d, a, or A: ")
Q3 = input("\n3. All in all, I am inclined to feel that I am a failure."
"Enter D, d, a, or A: ")
Q4 = input("\n4. I am able to do things as well as most other people."
"Enter D, d, a, or A: ")
Q5 = input("\n5. I feel I do not have much to be proud of."
"Enter D, d, a, or A: ")
Q6 = input("\n6. I take a positive attitude toward myself."
"Enter D, d, a, or A: ")
Q7 = input("\n7. On the whole, I am satisfied with myself."
"Enter D, d, a, or A: ")
Q8 = input("\n8. I wish I could have more respect for myself."
"Enter D, d, a, or A: ")
Q9 = input("\n9. I certainly feel useless at times."
"Enter D, d, a, or A: ")
Q10 = input("\n10. At times I think I am no good at all."
"Enter D, d, a, or A: ")


overall = 0

if Q1 or Q2 or Q4 or Q6 or Q7 == "D":
    overall = overall
elif Q1 or Q2 or Q4 or Q6 or Q7 == "d":
    overall = overall + 1
elif Q1 or Q2 or Q4 or Q6 or Q7 == "a":
    overall = overall + 2
elif Q1 or Q2 or Q4 or Q6 or Q7 == "A":
    overall = overall + 3


if Q3 or Q5 or Q8 or Q9 or Q10 == "D":
    overall = overall + 3
elif Q3 or Q5 or Q8 or Q9 or Q10 == "d":
    overall = overall + 2
elif Q3 or Q5 or Q8 or Q9 or Q10 == "a":
    overall = overall + 1
elif Q3 or Q5 or Q8 or Q9 or Q10 == "A":
    overall = overall


print(f"\nYour score is {overall}."
"\nA score below 15 may indicate problematic low self-esteem.")