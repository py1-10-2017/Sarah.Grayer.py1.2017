class MathDojo(object):
    #"""docstring for MathDojo."""
    def __init__(self):
        self.result = 0
        self.addition = 0
        self.subtraction = 0

    def add(self, *args):
        for i in args:
            if type (i) == list or type (i) == tuple:
                for k in i:
                    self.addition += k
            else:
                self.addition += i
        return self

    def subtract(self, *args):
        for i in args:
            if type (i) == list or type (i) == tuple:
                for k in i:
                    self.subtraction += k
            else:
                self.subtraction += i
        return self

    def total(self):
        self.result += self.addition - self.subtraction
        print self.result
        return self

md = MathDojo()
md.add(2).add(2,5).subtract(3,2). total()
md.add([1], 3, 4).add([3, 5, 7, 8],[2, 4.3, 1.25]).subtract(2, [2, 3],[1.1, 2.3]).total()
