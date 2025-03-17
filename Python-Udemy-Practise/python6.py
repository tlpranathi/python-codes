# UDEMY PYTHON COURSE

# OBJECT ORIENTED PROGRAMMING

class Line:
    def __init__(self, coor1, coor2):
        self.coor1 = coor1
        self.coor2 = coor2

    def distance(self):
        return ((self.coor1[0]-self.coor2[0])**2 + (self.coor1[1]-self.coor2[1])**2)**0.5
    
    def slope(self):
        return (self.coor2[1] - self.coor1[1])/(self.coor1[0] - self.coor2[0])
    
    # OR

    def distance(self):
        x1,y1 = self.coor1
        x2,y2 = self.coor2
        return ((x2-x1)**2 + (y2-y1)**2)**0.5
    
    def slope(self):
        x1,y1 = self.coor1
        x2,y2 = self.coor2
        return (y2-y1)/(x2-x1)
    
coordinate1 = (3,2)
coordinate2 = (8,10)

li = Line(coordinate1,coordinate2)
print(li.distance())
print(li.slope())


class Cylinder:

    pi = 3.14

    def __init__(self, height = 1, radius = 1):
        self.height = height
        self.radius = radius


    def volume(self):
        return Cylinder.pi*self.height*self.radius**2

    def surface_area(self):
        return 2*Cylinder.pi*(self.radius*self.height + self.radius**2)
    
cy = Cylinder()
print(cy.volume())
print(cy.surface_area())

import time

class BankAccount:
    balance = 0

    def __init__(self, owner, balance = 0):
        self.owner = owner
        self.balance = balance
    
    def __str__(self):
        return f"Account owner: {self.owner} \nAccount Balance: {self.balance}"

    def deposit(self, d_amt):
        self.balance += d_amt
        print("Deposit accepted")
        
    def withdraw(self, w_amt):
        if self.balance >= w_amt:
            self.balance -= w_amt
            print("Withdrawal accepted")
        else:
            print("Funds unavailable")
            
acc1 = BankAccount("harry styles", 1010101101010)
acc2 = BankAccount("tom holland", 22929292929292)

print(acc1)
print(acc2)

print(acc1.owner)
print(acc2.balance)

acc1.withdraw(34567897634)
acc1.withdraw(123456789098765)


