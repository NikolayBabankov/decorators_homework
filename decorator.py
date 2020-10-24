import time
import datetime

def decorator_parameter(path):
    
    def decorator(test_function):

        def new_function(*args, **kwargs):
            result = test_function(*args, **kwargs)
            now = datetime.datetime.now()
            with open(path, 'a') as file:
                file.write(f'Function {test_function.__name__} worked in {now.strftime("%d-%m-%Y %H:%M")}' 
                            f' Function arguments {args} Execution result: {result} \n')
            return result
        return new_function
    return decorator
