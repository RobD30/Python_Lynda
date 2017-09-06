#!/usr/bin/env python3

class myClass():
    lass
    myClass():

    def method1(self):
        print("myClass method1")

    def method2(self, someString):
        print("myClass method2: " + someString)


class anotherClass(myClass):
    def method2(self):
        print("anotherClass method2")

    def method1(self):
        myClass.method1(self);
        print("anotherClass method1")

    # exercise the class methods
    c = myClass()
    c.method1()
    c.method2("This is a string")
    c2 = anotherClass()
    c2.method1()


if __name__ == "__main__":
    main()
