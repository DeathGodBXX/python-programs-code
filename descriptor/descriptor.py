class person():
    def __init__(self, math=0):
        self.math = math

    @property
    def math(self):
        return self._math

    @math.setter
    def math(self, value: int):
        if 0 < value <= 100:
            self._math = value
        else:
            raise ValueError('integer must be in (0,100]')

    # 上面的self._math指的都是self.math初始化值，以区分属性函数math的调用

    def pp(self):
        print(self.math, self._math)


# try:
#     peo = person()
#     peo.math = 40
#     print(peo.math)
# except Exception as e:
#     print(e)

peo = person(30)
print(peo.math)
peo.math = 40
print(peo.math)
peo.pp()
