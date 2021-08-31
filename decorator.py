def decorator_function(original_function):
    def wrapper_function(*args, **kwargs):
        return original_function(*args, **kwargs)

    return wrapper_function


@decorator_function  # display=decorator_function(display)
def display():
    print("executed from display")


@decorator_function  # display_info=decorator_function(display_info)
def display_info(name, age):
    print("executed from display_info ({},{})".format(name, age))


display_info('John', 25)
display()
