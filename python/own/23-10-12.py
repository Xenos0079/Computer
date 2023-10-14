# I want to test that whether i write a new program, then the Repository of git can receive it.
signal_1 = input("Enter a signal for further action.")
signal_1 = eval(signal_1)

if signal_1 is int:
    print("You have entered an integer.")
    print(type(signal_1))

if signal_1 is float:
    print("You have entered a float number.")
    print(type(signal_1))

if signal_1 is str:
    print("You have entered a string.")
    print(type(signal_1))