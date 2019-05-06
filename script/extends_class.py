# クラスの継承のサンプルをやってみる
#

class Parent():
    def __init__():

    parent_sample  = 0
    parent_sample2 = 1

    def method_sample(self, arg):
        print('method!:' + arg)

    @class_method
    def class_method_sample(cls, arg):
        print('class_method!:' + arg)

    @staticmethod
    def static_method_sample(arg):
        print('static_method!' + arg)


class Child(Parent):
    child_sample = '0'

    def child_method_sample():
        print('child_method_sample')


if __name__ == "__main__":
    child = Child()
    child.method_sample('abc')
    child.class_method_sample('args')
