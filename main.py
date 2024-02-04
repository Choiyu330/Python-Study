def say_hello():
    print("Hello How r u?")

# How to receive Parameters
def say_hello(name, age):
    print("Hello", name)
    print("You are", age, "years old")
    
say_hello("Anonymous", 26)

# Default Parameters
def say_hello2(name="Anonymous"):
    print("HELLO !", name)

say_hello2()