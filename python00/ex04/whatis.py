import sys

def check_odd_even(arg):
    try:
        if len(arg) == 1:
            return
        assert len(arg) == 2, "more than one argument is provided"
        
        number = int(arg[1])
        if number % 2 == 0:
            print("I'm Even.")
        else:
            print("I'm Odd.")
    except ValueError:
        print("AssertionError: argument is not an integer")
    except AssertionError as error:
        print(f"AssertionError: {error}")

if __name__ == "__main__":
    check_odd_even(sys.argv)
