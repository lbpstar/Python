def gen_generator():
    yield 1

def gen_value():
    return 1
    
if __name__ == '__main__':
    ret = gen_generator()
    print(type(ret),type(next(ret)))    #<class 'generator'> <class 'int'>
