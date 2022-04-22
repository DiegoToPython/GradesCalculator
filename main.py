print("How many grades do you have?")
note_number = input()

if int(note_number) == 1:
    print("What is your grade ?")
    first_note = input()
    calcul = int(first_note) / len(first_note)
    print(f"Your average grade is {calcul} !")

elif int(note_number) == 2:
    print("What is your first grade ?")
    first_note = input()
    print("What is your second grade ?")
    second_note = input()

    add = int(first_note) + int(second_note)

    calcul = add / 2
    print(f"Your average grade is {calcul} !")

elif int(note_number) == 3:
    print("What is your first grade ?")
    first_note = input()
    print("What is your second grade ?")
    second_note = input()
    print("What is your third grade ?")
    third_note = input()

    add = int(first_note) + int(second_note) + int(third_note)

    calcul = add / 3
    print(f"Your average grade is {calcul} !")

elif int(note_number) == 4:
    print("What is your first grade ?")
    first_note = input()
    print("What is your second grade ?")
    second_note = input()
    print("What is your third grade ?")
    third_note = input()
    print("What is your fourth grade ?")
    fourth_note = input()

    add = int(first_note) + int(second_note) + int(third_note) + int(fourth_note)

    calcul = add / 4
    print(f"Your average grade is {calcul} !")

elif int(note_number) == 5:
    print("What is your first grade ?")
    first_note = input()
    print("What is your second grade ?")
    second_note = input()
    print("What is your third grade ?")
    third_note = input()
    print("What is your fourth grade ?")
    fourth_note = input()
    print("What is your fifth grade ?")
    fifth_note = input()

    add = int(first_note) + int(second_note) + int(third_note) + int(fourth_note) + int(fifth_note)

    calcul = add / 5
    print(f"Your average grade is {calcul} !")

else:
    print("I can't handle more than 5 grades !")

# ...
