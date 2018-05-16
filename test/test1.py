def myGenerator(): 
    yield print(1)  
    yield print(2)

gen = myGenerator()  
next(gen)
next(gen)