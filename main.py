

class Bank:
    def __init__(self):
        self.amount = 0

    def getAmount(self):
        return self.amount
    
    def withDraw(self, amount):
        self.amount -= amount
        return self.amount
    
    def deposit(self, amount):
        self.amount += amount
        return self.amount
    