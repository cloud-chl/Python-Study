import time

def decorator(func):
    def wrapper(*args, **kwargs):
        print('begin call')
        return func(*args, **kwargs)
    return wrapper

@decorator
def func1(x,y):
    time.sleep(1)
    print('end call')


if  __name__ == '__main__':
    func1(1,2)