"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""
class Employee:
    def __init__(self, name, contract, commission, hours, pay,monthlySal, contractNum, contractPay,bonusCommission):
        self.name = name
        self.contract = contract #hourly/salary
        self.commission = commission #none, bonus, contract
        self.hours = hours
        self.pay = pay
        self.monthlySal = monthlySal
        self.contractNum = contractNum
        self.contractPay = contractPay
        self.bonusCommission = bonusCommission
        

    def get_pay(self):
        initialPay =0
        if self.contract == "hourly":
            initialPay = self.hours * self.pay
        elif self.contract == "monthly":
            initialPay = self.monthlySal
        if self.commission == None:
            return initialPay
        elif self.commission == "bonus":
            return initialPay + self.bonusCommission
        else:
            return initialPay + self.contractNum * self.contractPay
        
            

    def __str__(self):
        string =   f"{self.name} works on a "
        if self.contract == "hourly":
            string += f"contract of {self.hours} hours at {self.pay}/hour"
        else:
            string += f"monthly salary of {self.monthlySal}"
        if self.commission == "contract":
            string += f" and receives a commission for {self.contractNum} contract(s) at {self.contractPay}/contract."
        elif self.commission == "bonus":
            string += f" and receives a bonus commission of {self.bonusCommission}."
        else:
            string +="."
        totalPay = self.get_pay()
        string+= f" Their total pay is {totalPay} "   
        return string
            

    


       
        


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie',"monthly", None, None, None,4000,None,None,None)


# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie',"hourly" , None, 100 , 25,None, None,None, None)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee', "monthly", "contract", None, None,3000,4,200,None)
print(renee.get_pay(),renee.__str__())
# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan',"hourly", "contract", 150,25,None,3,220,None)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie',"monthly", "bonus", None,None,2000,None,None,1500)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel',"hourly","bonus", 120,30,None,None,None,600)
