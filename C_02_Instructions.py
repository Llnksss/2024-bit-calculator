# Generates headings ( eg: ---- Heading ----)
def statement_generator(statement, decoration):
    print(f"/n{decoration * 5} {statement} {decoration * 5}")


# Displays instructions
def instructions():
    statement_generator("instructions", "-")

    print('''
Instructions go here.
- instruction 1
- int=struction 2
''')


# Main routine goes here

# Display instructions if requested
want_instructions = input("press <enter> to read the instructions"
                          "or any ket to continue")
