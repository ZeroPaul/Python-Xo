def get_int(msg):
    while True:
        try:
            i = int(input(msg))
            return i
        except ValueError as error:
            print (error)

number = get_int("enter a number: ")


