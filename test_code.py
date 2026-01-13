"""
Docstring for test_code
testing the decorater in 
"""

def main_dec(n):
    def dec1(func):
        def wrapper():
            print("Time started dec1")
            print("n value =", n)
            func()
            print("time ended dec1")
        return wrapper
    return dec1

@main_dec(5)
def my_sec():
    print("Just called my_sec")
    
my_sec()