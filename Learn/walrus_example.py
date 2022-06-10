choice = None


def do_job(choice):
    print(choice)


while choice != 0:
    if (choice := int(input())) != 0:
        do_job(choice)
