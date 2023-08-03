def logger(func):
    def wrapper(*args, **kwargs):
        print("Logging execution")
        result = func(*args, **kwargs)
        print("Done logging")
    return wrapper

@logger
def sample():
    print("-- Inside sample function")

@logger
def hello(name):
    print(f"hello, {name}!")

def how(x):
    print(f'x={x}')
    return x**2

sample()
hello("James")

