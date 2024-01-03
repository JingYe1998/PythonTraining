class Person:
    # __init__ 方法是在建立物件時被自動呼叫的特殊方法，用於初始化新建立的物件
    # 這裡的 __init__ 接受一個參數 name，並將其設定為該物件的 name 屬性。
    # 在 Python 中，self 是一個慣例，用於表示類別的實例（instance）。當你在類別中定義方法時，第一個參數通常被命名為 self，這是一個指向類別實例自身的參考

    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f"Hello, I am {self.name}")


john = Person("John")
john.talk()

bob=Person("Bob")
bob.talk()
