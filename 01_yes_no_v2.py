# functions go here
def yes_no(question):

    while True:
        response = input(question).lower()

        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
#main routine code

want_instructions = yes_no("Do you want to read the instructions? ")

if want_instructions == "yes" or want_instructions == "y":
    print("Instructions go here")

print("we are done")