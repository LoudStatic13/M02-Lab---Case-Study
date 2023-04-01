##James Peacock

##Dean's Honor List

##This program takes a student's name and GPA to see if they have made the Dean's List.



lastName = input("Please enter student's last name: ")

while lastName != "ZZZ":
    firstName = input("Please enter student's first name: ")
    gpa = float(input("Please enter " + firstName + " " + lastName +"'s GPA: "))

    if gpa >= 3.25 and gpa < 3.5:
        print(firstName + " " + lastName + " made the Honor Roll!\n")
    elif gpa >= 3.5:
        print(firstName + " " + lastName + " made the Dean's List!\n")    
    else:
        print("I'm so sorry, but " + firstName + " " + lastName + " did not make the Dean's List or Honor Roll.\n")

    lastName = input("Please enter student's last name: ")

if lastName == "ZZZ":
    print("Thank you!")


