# メソッド、クラスメソッド、スタティックメソッドの違いについて書いてみる
# [参考]
# https://atsuoishimoto.hatenablog.com/entry/20100807/1281169026
# https://qiita.com/ysk24ok/items/848daec3886f1030f587
# https://qiita.com/masaru/items/5ebf2e96d6524830511b
class MyClass:
    # メソッドはおなじみのインスタンスメソッドで、
    # 第一引数としてインスタンスを受け取り、
    # 呼び出す時には必ずインスタンスが必要となる。
    def method_sample(self, arg):
        print('method!')

    # クラスメソッドは第一引数としてクラスオブジェクトを受け取り、
    # インスタンスが無くとも呼び出すことが出来る。
    @class_method
    def class_method_sample(cls, arg):
        print('class_method!')

    # スタティックメソッドでは引数は特に追加されず、
    # インスタンスが無くとも呼び出すことが出来る。
    @staticmethod
    def static_method_sample(arg):
        print('static_method!')
