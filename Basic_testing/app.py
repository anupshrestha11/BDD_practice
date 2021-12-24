def incrementor(stride: int):
    def f(x: int):
        return stride + x

    return f


foo = incrementor(10)

print(foo(5))
