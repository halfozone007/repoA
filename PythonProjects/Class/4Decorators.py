

class Duck:
    def __init__(self, **kwargs):
        self.variables = kwargs

    def setVariable(self, k, v):
        self.variables[k] = v

    def getVariable(self, k):
        return self.variables.get(k, None)

    @property
    def color(self):
        return self.variables.get('color', None)

    @color.setter
    def color(self, c):
        self.variables['color'] = c
    
    @color.deleter
    def color(self):
        del self.variables['color']



def main():
    donald = Duck(feet = 2)
    donald.color = 'blue'
    print(donald.color)


if __name__ == '__main__':
    main()
    