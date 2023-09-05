print("-----------bank management system-----------------")
class bank:
    def __init__(self,name,total):
        
        self.name=name
        self.accountno=1001
        self.total=total
        self.minimbal=1000
    
    
    
    def creataccount(self):
        if self.total>=1000:
            print("acount created sucessfully and your acount no is=",self.accountno)
        else:
            self.total=0
            print("amount must be grater than 1000")
        
    def creditamount(self):
        acc=int(input("enter account number to verify="))
        if acc==self.accountno:
            amt=int(input("enter amount you want to add="))
            if amt>0:
                self.total=self.total+amt
                print("amount credit scessfully")
            else:
                print("invalid amount")
        else:
            print("can't credit amount")
    def debitamount(self):
        debit_amt=int(input("enter amount you want to debit="))
        new_amt=self.total-debit_amt
        if self.total>0 and new_amt>self.minimbal:
            self.total=self.total-debit_amt
            print("amount has be debited sucessfully")
        else:
            print("you cannot debit because invalid amount")

    def showbal(self):
        print("current bal=",self.total)
    
name=input("enter your name=")
total=int(input("eneter opening acount amount="))
b=bank(name,total) 

while True:
    print("1:creataccount/n2:creditamount/n3:debitamount/n4:showbal/n5:exit")

    ch=int(input("enter choice number"))
    if ch==1:
        b.creataccount()
    elif ch==2:
        b.creditamount()
    elif ch==3:
        b.debitamount()
    elif ch==4:
        b.showbal()
    elif ch==5:
        break
    else:
        print("wrong choice number")                    
