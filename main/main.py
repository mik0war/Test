class MyClass:

    def __init__(self, name) -> None:
        super().__init__()
        self.name = name

    def test(self):
        print(self.name)

    @staticmethod
    def my_pow(a):
        return a*a




print(MyClass.my_pow(5))