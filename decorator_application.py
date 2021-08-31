#Practical examples
#1)How many times a specific function has been called and with what arguments
#i.e Logging

## Decorators add extra functionality to my functions


def my_logger(original_function):
    import logging
    logging.basicConfig(filename='{}.log'.format(original_function.__name__),level=logging.INFO)

    def wrapper_function(*args,**kwargs):
        logging.info('Ran with args:{}, and kwargs:{}'.format(args,kwargs))
        return original_function(*args,**kwargs)

    return wrapper_function

def my_timer(original_function):
    import time

    def wrapper_function(*args,**kwargs):
        t1=time.time()
        result=original_function(*args,**kwargs)
        t2=time.time()-t1
        print('{} ran in : {} sec'.format(original_function.__name__,t2))

    return wrapper_function

import time

@my_timer
def display_info(name,age):
    time.sleep(1)
    print("display function ran with {} and {}".format(name,age))

#display_info=my_logger(display_info)

display_info('John',30)