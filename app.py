#!/usr/bin/python

"""These are import statements. From here, we can import modules that we install with pip,
or even modules that we create ourselves."""

# time is a built in module. It does not need to be installed
import time

# addwords and menus are modules that I made to break the code down into smaller files
# using the from keyword allows us to import individual functions from modules
from addwords import generate_insult, add_field
from menus import main_menu, add_menu, three_prints


# This is where the "real" code starts
def main():
    """main() starts the app and displays the main menu"""
    main_menu()

    # This is where user input is read and assigned to a variable
    # In Python 3, raw_input() has been replaced by input()
    # The = operator assigns a value to a variable
    choice = raw_input("Enter Your Selection: ")  # the argument is the prompt that will show in terminal

    # Try blocks allow the code to handle errors instead of exiting prematurely
    try:

        # Call functions based on user input
        # if means if. The == operator means 'is equal to'. other operators are !=, <=, >=
        if int(choice) == 1:

            # this code will be executed if the user inputs the number 1 in the terminal
            # this function comes from the menu module that we imported at the top of the file
            add_menu()

            # this should look familiar. Same as before.
            choice = raw_input("Enter your selection: ")

            try:
                if int(choice) == 1:
                    # add new directive
                    directive = raw_input("Type new directive: ")
                    add_field('directives', 'directive', directive)
                    three_prints()
                    print "Directive added"
                    three_prints()
                    time.sleep(2)
                    main()

                elif int(choice) == 2:
                    # add new adjective
                    adjective = raw_input("Type new adjective: ")
                    add_field('adjectives', 'adjective', adjective)
                    three_prints()
                    print "Adjective added"
                    three_prints()
                    time.sleep(2)
                    main()

                elif int(choice) == 3:
                    # add new name
                    name = raw_input("Type new name: ")
                    add_field('names', 'name', name)
                    three_prints()
                    print "Name added"
                    three_prints()
                    time.sleep(2)
                    main()

                elif int(choice) == 4:
                    # main menu
                    main()

                elif int(choice) == 5:
                    # exit
                    three_prints()
                    print "See you in hell, asshole!"
                    three_prints()
                    exit()

                else:
                    print
                    print "Sorry, I didn't understand you. Maybe you fat fingered your choice."
                    print

                    time.sleep(2)
                    main()

            except ValueError:

                three_prints()
                print "You fucked up. What are you, retarded?"
                three_prints()
                time.sleep(2)
                main()

        # elif (else if) code will be executed if the user inputs 2.
        # the int(function) transforms the choice variable into an integer
        elif int(choice) == 2:

            # this comes from the addwords module that we created
            # functions should be lower case and underscore separated
            three_prints()
            print generate_insult()
            three_prints()
            time.sleep(2)
            main()

        # another "else if" conditional with another block of code indented underneath
        elif int(choice) == 3:

            # In Python 3, the print statement has been replaced by the print() function
            # this would be 'print("well fuck off then")'
            three_prints()
            print "Well fuck off then"
            three_prints()

            # sleep puts code execution on hold, takes number of seconds as an argument
            time.sleep(2)

            # exit() terminates the program
            exit()

        # else covers every conditional not previously covered in an if or elif block
        else:
            print
            print "Sorry, I didn't understand you. Maybe you fat fingered your choice."
            print
            time.sleep(2)

            # You can call a function inside of itself. This is called recursion.
            # Recursion can be much more useful than this simple example. We will get to that.
            main()

    # this except block will handle all ValueError exceptions that can occur. In this instance, that would apply
    # to the user inputting anything other than a number when making a menu selection
    except ValueError:

        # here we tell the user to stop being a fucking dipshit
        three_prints()
        print "You fucked up. What are you, retarded?"
        three_prints()
        time.sleep(2)
        main()


# This statement is used to allow files to be run in terminal or imported as a module
# If the file is run directly, the interpreter will refer to it as __main__.
# In that case, the code after the conditional will be executed. In this case, main() will be called
if __name__ == "__main__":
    main()
