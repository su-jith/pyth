class bank:
    def __init__ (self,acc_name="empty",acc_no="empty",acc_type="empty",acc_balance="0"):
        self.acc_name=acc_name
        self.acc_no=acc_no
        self.acc_type=acc_type
        self.acc_balnce=acc_balance

    def deposite(self,acc_balance=0):
        self.acc_balnace=self.acc_balance+acc_balance
    def withdraw(self,):
        if not self.acc_balance:
            print("\n zero balnce")
        else:
            acc_balance=int(input("enter amount"))
            if(self.acc_balance)<0:
                print("no sufficient balanace")
            else:
                self.acc=self.acc_balnce-acc_balance
    def show_Details(self):
        print("acc name:",self.acc_name)
        print("acc no:",self.acc_number)
        print("acc type:",self.acc_number)
        print("acc balance:",self.acc_balance)


        name=input("enter name")
        number=input("enter no")
        type=input("enter type")

        b=bank(number,name,acctype)
        b.show_Details()
        while(true):
            
            print("1.deposite\n 2.withdrw\n 3.deatils\n 4.exit\n")
            n=int(input("entr choice"))
            if n==1:
                      n=int(input("enter amount"))
                      b.deposite(n)
            elif n==2:
                      b.withdraw()
            elif n==3:
                      b.showdetails()
            else:
                      print("exit")
                      break;
                      

        
