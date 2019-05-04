class MyClass:
    """A simple example class"""         # 三重クォートによるコメント

    def __init__(self):                  # コンストラクタ
        self.name = "" # インスタンス変数

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

a = MyClass()     # クラスのインスタンスを生成
a.setName("Ohki") # setName()メソッドをコール
print a.getName() # getName()メソッドをコール
