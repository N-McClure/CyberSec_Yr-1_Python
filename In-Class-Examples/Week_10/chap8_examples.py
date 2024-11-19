# Exercise from slide 13:
def p13_exercise(firstname, lastname, id):
    return firstname[:3] + lastname[:3] + str(id)[-3:]

loginName = p13_exercise("Nicholas","McClure",991693366)
print("Your Login is: " + loginName)

# Utilization of above exercise to try and generate Sheridan Logins:
def genSheridan(firstname, lastname):
    if len(lastname) + len(firstname) >= 9:
        login = lastname + firstname[:8-len(lastname):]
        print("Generated Sheridan username: " + login)
        
    elif len(lastname) + len(firstname) < 9:
        login = lastname + firstname
        print("Generated Sheridan username: " + login)
        
genSheridan("nicholas","mcclure")
genSheridan("samuel","gould")
genSheridan("mikkel","ugalde")