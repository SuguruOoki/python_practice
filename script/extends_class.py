# クラスの継承のサンプルをやってみる
# python 継承の落とし穴参考記事
# https://qiita.com/Kodaira_/items/42dfe18c81af98bf0db3#%E3%81%95%E3%82%89%E3%81%AB%E5%9F%BA%E5%BA%95%E3%82%AF%E3%83%A9%E3%82%B9%E3%81%AEwarrior%E3%81%A8magician%E3%82%AF%E3%83%A9%E3%82%B9%E3%82%82super%E3%82%92%E4%BD%BF%E3%82%8F%E3%81%9A%E3%81%AB%E5%AE%9A%E7%BE%A9%E3%81%99%E3%82%8B%E3%81%A8
# pythonには、PHPでいうtraitが最初から準備されている模様。
# その場合は、クラスの引数を二つにし、コンストラクタ(?) の中でsuper.__init__()とすること
# そうしないと、呼び出しがおかしくなりやすい。その落とし穴については上記の記事を参照すること

class Parent():
    def __init__():
        self.parent_sample  = 0
        self.parent_sample2 = 1

    def method_sample(self, arg):
        print("method!:" + arg)

    @classmethod
    def class_method_sample(cls, arg):
        print("class_method!:" + arg)

    @staticmethod
    def static_method_sample(arg):
        print("static_method!" + arg)


class Child(Parent):
    def __init__(self):
        self.child_sample = "3"

    @classmethod
    def child_method_sample(self):
        print("child_method_sample" + self.child_sample)


if __name__ == "__main__":
    child = Child()
    child.method_sample("abc")
    child.class_method_sample("args")
    child.child_method_sample()
