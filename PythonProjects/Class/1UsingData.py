

class Duck:
    def __init__(self, **kwargs):
        self.variables = kwargs

    def setVariable(self, k, v):
        self.variables[k] = v

    def getVariable(self, k):
        return self.variables.get(k, None)




def main():
    donald = Duck(feet = 2)
    print(donald.getVariable('feet'))

    print(donald.getVariable('color')) 


if __name__ == '__main__':
    main()
    