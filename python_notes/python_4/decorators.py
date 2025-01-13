
# decorators are used to modify another functions

def greet(fx):
    def mfx(*args,**kwargs):
        print("welcome to the functions")
        fx(*args,**kwargs)
    return mfx

@greet
def add(a,b):
    print(a+b)

@greet
def hello():
    print("hello how r u")

add(1,2)