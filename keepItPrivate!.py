class myclass:
    __privateVar = 27;

    def __privateMeth(self):
        print("I am inside the class myclass")

    def hello(self):
        print("private variable value: ", myclass.__privateVar)


foo = myclass()
foo.hello()
foo.__privateMeth