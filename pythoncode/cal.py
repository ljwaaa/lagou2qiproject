class calc():
    def add(self, a, b):
        return a + b

    def sub(self, a, b):
        return a - b

    def mul(self, a, b):
        return a * b

    def div(self, a, b):
        try:
            return a / b
        except:
            print("溢出")
        else:
            pass
