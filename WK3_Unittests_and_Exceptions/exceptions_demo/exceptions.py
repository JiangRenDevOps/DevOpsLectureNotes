class MyError(Exception):
    # Customise an exception; Inherit Exception

    def __init__(self, age):
        self.age = age

    def __str__(self):
        # __str__ for returning the description
        return f'age cannot be an negative number, your input is {self.age}'


def enter_your_age():
    age = int(input('Please enter your age:'))
    try:
        if age < 0:
            raise MyError(age)  # raise exception
    except MyError as exp:
        print(f"Found exception: {exp}")


def try_catch():
    try:
        print("May cause exceptions")
    except (IOError, NameError) as e:
        print(f"deal with specific exceptions {e}")
    except Exception as e:
        print(f"deal with exceptions {e}")
    else:
        print("Did not catch exceptions")
    finally:
        print("No matter what, execute this")


def file_not_found():
    try:
        with open('file.log') as file:
            read_data = file.read()
    except FileNotFoundError as fnf_error:
        print(fnf_error)


if __name__ == '__main__':
    try_catch()
    file_not_found()
    enter_your_age()

    import sys
    assert ('linux' in sys.platform), "This code runs on Linux only."
