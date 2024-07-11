import json, random

class RegularUser:
    def __init__(self,user_id,username,password,email,remaining_time=int,paytopay_cash_balance=0,epay_balance=0,isClient="Regular"):
        self.user_id=user_id
        self.username=username
        self.__password=password
        self.email=email
        self.remaining_time=remaining_time
        self.paytopay_cash_balance=paytopay_cash_balance
        self.epay_balance=epay_balance
        self.isClient=isClient

    def __str__(self):
        return f"================================\nUser Id: {self.user_id}\nUsername: {self.username}\nPassword: {self.getUserPassword()}\nEmail: {self.email}\nRemaining Time: {self.remaining_time} hours\nPay-to-Pay Cash Balance: {self.paytopay_cash_balance}\nE-pay Balance: {self.epay_balance}\nClient Type: {self.isClient}\n"

    def display_details(self):
        return f"\nClient Type: {self.isClient}\n\nUser Id: {self.user_id}\nUsername: {self.username}\nEmail: {self.email}\nRemaining Time: {self.remaining_time} hours\nPay-to-Pay Cash Balance: {self.paytopay_cash_balance}\nE-pay Balance: {self.epay_balance}\n\n"

    def getUserPassword(self):
        return self.__password   

    def setNewUserPassword(self, j):    
        self.__password = j
        
class Member(RegularUser):
    def __init__(self, user_id, username, password, email, remaining_time, membership_expiration_in_hours = int, paytopay_cash_balance=0, epay_balance=0, isClient= "Member"):
        super().__init__(user_id, username, password, email, remaining_time, paytopay_cash_balance, epay_balance, isClient)
        self.membership_expiration_in_hours=membership_expiration_in_hours
        
    def __str__(self):
        return f"================================\nUser Id: {self.user_id}\nUsername: {self.username}\nPassword: {self.getUserPassword()}\nEmail: {self.email}\nRemaining Time: {self.remaining_time} hours\nMembership Expiration (in hours): {self.membership_expiration_in_hours}\nPay-to-Pay Cash Balance: {self.paytopay_cash_balance}\nE-pay Balance: {self.epay_balance}\nClient Type: {self.isClient}\n"
    
    def display_details(self):
        return f"\nClient Type: {self.isClient}\n\nUser Id: {self.user_id}\nUsername: {self.username}\nEmail: {self.email}\nRemaining Time: {self.remaining_time} hours\nMembership Expiration (in hours): {self.membership_expiration_in_hours}\nPay-to-Pay Cash Balance: {self.paytopay_cash_balance}\nE-pay Balance: {self.epay_balance}\n\n"
    
    def getUserPassword(self):
        return super().getUserPassword()
    
    def setNewUserPassword(self, j):
        return super().setNewUserPassword(j)
        pass    
    
class VIP_Member(RegularUser):
    def __init__(self, user_id, username, password, email, remaining_time, membership_expiration_in_hours = int, paytopay_cash_balance=0, epay_balance=0, isClient= "VIP"):
        super().__init__(user_id, username, password, email, remaining_time, paytopay_cash_balance, epay_balance, isClient)
        self.membership_expiration_in_hours=membership_expiration_in_hours
        
    def __str__(self):
        return f"================================\nUser Id: {self.user_id}\nUsername: {self.username}\nPassword: {self.getUserPassword()}\nEmail: {self.email}\nRemaining Time: {self.remaining_time} hours\nMembership Expiration (in hours): {self.membership_expiration_in_hours}\nPay-to-Pay Cash Balance: {self.paytopay_cash_balance}\nE-pay Balance: {self.epay_balance}\nClient Type: {self.isClient}\n"
    
    def setCashback_P2P(self,price):
        #10% Cash Back for VIP Clients
        returnCashback=(((price*10)/100))
        self.paytopay_cash_balance += returnCashback
        return f"\n\n\tSince the Client is VIP, there will be a 10% Cashback (Value:{returnCashback}) based on the price of the purchased computer\n\tNew Pay-to_Pay Balance: {self.paytopay_cash_balance}"
    
    def setCashback_EPay(self,price):
        #10% Cash Back for VIP Clients
        returnCashback=(((price*10)/100))
        self.epay_balance += returnCashback
        return f"\n\n\tSince the Client is VIP, there will be a 10% Cashback (Value:{returnCashback}) based on the price of the purchased computer\n\tNew Pay-to_Pay Balance: {self.epay_balance}"
    
    def getUserPassword(self):
        return super().getUserPassword()
    
    def setNewUserPassword(self, j):
        return super().setNewUserPassword(j)
    
    def display_details(self):
        return f"\nClient Type: {self.isClient}\n\nUser Id: {self.user_id}\nUsername: {self.username}\nEmail: {self.email}\nRemaining Time: {self.remaining_time} hours\nMembership Expiration (in hours): {self.membership_expiration_in_hours}\nPay-to-Pay Cash Balance: {self.paytopay_cash_balance}\nE-pay Balance: {self.epay_balance}\n\n"
        
class Computer:
    def __init__(self,number,computer_id,is_Available,purchasable,specs,price,stock=1,user_logged_in="None",isType="Low End"):
        self.number=number
        self.computer_id=computer_id
        self.is_Available=is_Available
        self.user_logged_in=user_logged_in
        self.purchasable=purchasable
        self.isType=isType
        self.specs=specs
        self.price=price
        self.stock=stock
        
    def __str__(self):
        return f"================================\nComputer Number: {self.number}\n\nComputer Id: {self.computer_id}\nAvailable: {self.is_Available}\nPurchasable: {self.purchasable}\nSpecs: {self.specs}\nPrice: {self.price}\nStock(s): {self.stock}\nUser Logged In: {self.user_logged_in}\nType of Computer: {self.isType}\n"
    
    def display_details(self):
        return f"\nType of Computer: {self.isType}\n\nComputer Number: #{self.number}\n\nComputer Id: {self.computer_id}\nAvailable: {self.is_Available}\nPurchasable: {self.purchasable}\nSpecs: {self.specs}\nPrice: {self.price}\nStock(s): {self.stock}\nUser Logged In: {self.user_logged_in}\n\n"
    
class GamingVIP_Computer(Computer):
    def __init__(self, number, computer_id, is_Available, purchasable, specs, price, stock=1, user_logged_in="None", isType="High End"):
        super().__init__(number, computer_id, is_Available, purchasable, specs, price, stock, user_logged_in, isType)
        
    def __str__(self):
        return f"================================\nComputer Number: {self.number}\n\nComputer Id: {self.computer_id}\nAvailable: {self.is_Available}\nPurchasable: {self.purchasable}\nSpecs: {self.specs}\nPrice: {self.price}\nStock(s): {self.stock}\nUser Logged In: {self.user_logged_in}\nType of Computer: {self.isType}\n"
    
    def display_details(self):
        return f"\nType of Computer: {self.isType}\n\nComputer Number: #{self.number}\n\nComputer Id: {self.computer_id}\nAvailable: {self.is_Available}\nPurchasable: {self.purchasable}\nSpecs: {self.specs}\nPrice: {self.price}\nStock(s): {self.stock}\nUser Logged In: {self.user_logged_in}\n\n"
    
class ComputerShop:
    def __init__(self, filename = "ComputerShop_data.json"):
        self.filename=filename
        self.allclientlist=[]
        self.RegularClientList=[]
        self.MemberClientList=[]
        self.VipClientList=[]
        self.allComputer_list=[]
        self.RegComputerList=[]
        self.VIPComputerList=[]
        self.LogHistory=[]
        self.PurchaseHistory_list=[]
    
    def add_client(self):
        newUsername=input("What would be the username?: ")
        newPassword=input("What would be the password?: ")
        newEmail=input("Please input the Email: ")
        newRemainingTime=int(input("What would be the remaining time?: "))
        newPaytoPayCashBalance=float(input('What is the "Pay to Pay" balance of the client?: '))
        newEpayBalance=float(input('What is the "E-pay" balance of the client?: '))
        newUserid=("2213"+f"{len(self.allclientlist)+1}")
        clientChoice=int(input("Is the client want to be a:\n1. Regular Client\n2. Member\n3. VIP Member\nWhat's the Choice: "))
        if clientChoice == 1:
            newRegularUser=RegularUser(newUserid,newUsername,newPassword,newEmail,newRemainingTime,newPaytoPayCashBalance,newEpayBalance)
            self.allclientlist.append(newRegularUser)
            self.RegularClientList.append(newRegularUser)
            print(f"{newRegularUser}================================\nAdded successfully!!")
            
        elif clientChoice == 2:
            newMemExpire=int(input("In hours, when will the membership expire?: "))
            newMember=Member(newUserid,newUsername,newPassword,newEmail,newRemainingTime,newMemExpire,newPaytoPayCashBalance,newEpayBalance)
            self.allclientlist.append(newMember)
            self.MemberClientList.append(newMember)
            print(f"{newMember}================================\nAdded successfully!!")
            
        elif clientChoice == 3:
            newVIPMemExpire=int(input("In hours, when will the VIP membership expire?: "))
            newVIPMember=VIP_Member(newUserid,newUsername,newPassword,newEmail,newRemainingTime,newVIPMemExpire,newPaytoPayCashBalance,newEpayBalance)
            self.allclientlist.append(newVIPMember)
            self.VipClientList.append(newVIPMember)
            print(f"{newVIPMember}================================\nAdded successfully!!")
        else:
            print("Pick only from the Given Choices (wrong input)")
            
        
    def edit_client_data(self):
        print("Give the Client ID and Username")
        clientask=(input("What is the client's ID?: "))
        clientask1=(input("What is the client's Username?: "))
        for a in self.allclientlist:
            if a.user_id == clientask and a.username == clientask1:
                print(f"Account found by the Username of {a.username}")
                clientask2=(input("Are you certain to edit the data? (Yes/No):  "))
                if clientask2 == "Yes":
                    newUsername1=input("What would be the username?: ")
                    newPassword1=input("What would be the password?: ")
                    newEmail1=input("Please input the Email: ")
                    newRemainingTime1=int(input("What would be the remaining time?: "))
                    newPaytoPayCashBalance1=float(input('What is the "Pay to Pay" balance of the client?: '))
                    newEpayBalance1=float(input('What is the "E-pay" balance of the client?: '))
                    a.username = newUsername1
                    a.setNewUserPassword(newPassword1)
                    a.email = newEmail1
                    a.remaining_time = newRemainingTime1
                    a.paytopay_cash_balance = newPaytoPayCashBalance1
                    a.epay_balance = newEpayBalance1
                    print(f"{a}\n================================\nSuccessfully Edited.")
                    break
                elif clientask2 == "No":
                    print("Going Back to Menu...")
                    break
                else:
                    print("Pick only from the Given Choices (wrong input)")
        else:
            print("User not Found")
                
    def delete_client_data(self):
        print("Give the Client ID and Username")
        clientask2=(input("What is the client's ID?: "))
        clientask2=(input("What is the client's Username?: "))
        for a in self.allclientlist:
            if a.user_id == clientask2 or a.username == clientask2:
                print(f"\n================================\n\nAccount found:{a.display_details()}")
                clientask2=str(input("Are you certain to delete the data? (Yes/No): "))
                if clientask2 == "Yes":
                    print("\nDeleting...")
                    self.allclientlist.remove(a)
                    print("\n================================\nClient data has been deleted.")
                    break
                elif clientask2 == "No":
                    print("Going Back to Menu...")
                    break
                else:
                    print("Pick only from the Given Choices (wrong input)")
        else:
            print("User not Found")
    
    def list_all_clients(self):
        print("================================\nCLIENT LIST:\n\n")
        for a in self.allclientlist:
            print(a.display_details())
            
    def assign_client2computer(self):
        print("Give the Client ID and Username")
        clientask6=(input("What is the client's ID?: "))
        clientask7=(input("What is the client's Username?: "))
        for g in self.allclientlist:
            #If regular user or member 
            if g.user_id == clientask6 or g.username == clientask7:
                print(f"\n================================\n\nAccount found:{g.display_details()}================================\n")
                print(f"================================\nThese are all the Computers:")
                for h in self.allComputer_list:
                    print(f"\n\n{h.display_details()}")
                if g.remaining_time == 0:
                    print("Client has no remaining time, please top up")
                else:
                    b=True
                    while b==True:
                        clientask8=int(input("Enter the computer's number\nTo which computer does the client want to use?: "))
                        for i in self.allComputer_list:
                            if i.number == clientask8:
                                if i.is_Available == "No":
                                    print("\nComputer is not currently available to use\n")
                                    continue                                     
                                if g.isClient == "Regular" and i.isType == "High End":
                                    print("\nOnly Members and VIP Members could access High End Computers\n")
                                    continue
                                generateTimeUsed=random.randint(0, g.remaining_time)
                                time=int(generateTimeUsed)
                                newLog=(f"client {g.user_id} ({g.username}) logged into computer number {i.number} for {time} hours")
                                print(newLog)
                                self.LogHistory.append(newLog)
                                g.remaining_time -= int(time)
                                print("================================\nClient Logged Successfully")  
                                b=False
        else:
            pass


    def view_log_history(self):
        print("================================\nLOG HISTORY LIST:\n\n")
        for l in self.LogHistory:
            print(l)

    def client_topup(self):
        print("Give the Client ID and Username")
        clientask4=(input("What is the client's ID?: "))
        clientask5=(input("What is the client's Username?: "))
        for g in self.allclientlist:
            if g.user_id == clientask4 or g.username == clientask5:
                print(f"\n================================\n\nAccount found:{g.display_details()}")
                clientask2=int(input("How much time to top up? (in hours): "))
                print(f"Adding {clientask2} hours to the remaining time...")
                g.remaining_time += clientask2
                print(f"\n================================\nSuccess!! New remaining time balance: {g.remaining_time} hours")
                break
        else:
            print("User not Found")
                
    def mem_vip_topup(self):
        print("Give the Client ID and Username")
        clientask4=(input("What is the client's ID?: "))
        clientask5=(input("What is the client's Username?: "))
        for m in self.allclientlist:
            if (m.user_id == clientask4 or m.username == clientask5) and (m.isClient == "Member" or m.isClient == "VIP"):
                print(f"\n================================\n\nAccount found:{m.display_details()}")
                clientask10=int(input("How much time to top up? (in hours): "))
                print(f"Adding {clientask10} hours to the Membership ...")
                m.membership_expiration_in_hours += clientask10
                print(f"\n================================\nSuccess!! New remaining time balance: {m.membership_expiration_in_hours} hours")
                break
        else:
            print("User not Found")

    def client_buy_computer(self):
        print("Give the Client ID and Username")
        clientask12=(input("What is the client's ID?: "))
        clientask13=(input("What is the client's Username?: "))
        for o in self.allclientlist:
        #If regular user or member 
            if o.user_id == clientask12 or o.username == clientask13:
                print(f"\n================================\n\nAccount found:{o.display_details()}================================\n")
                print(f"================================\nThese are all the Computers:")
                for p in self.allComputer_list:
                    print(f"\n\n{p.display_details()}")
                a=True
                while a == True:
                    clientask15 = int(input("What computer number does the client want to purchase?: "))                  
                    for p in self.allComputer_list:                             
                        if p.number == clientask15:
                            if p.purchasable == "Yes":
                                if p.stock != 0:
                                    clientask16=str(input(f"For the price of {p.price} is this the computer that will be purchased by client {o.username}? (Yes/No): "))
                                    if clientask16 == "Yes":
                                        clientask17=int(input("What kind of payement will be used? the Client's:\n 1. Pay-to-Pay Balance\n 2. E-pay Balance\nPick Your Choice: "))
                                        if clientask17 == 1:
                                            print("Purchasing...Wait for a Moment")
                                            if p.price <= o.paytopay_cash_balance:
                                                o.paytopay_cash_balance -= p.price
                                                print(f"\n================================\nSuccessfully purchased the computer, your new Pay-to-Pay Balance would be: {o.paytopay_cash_balance}")
                                                newPurchLog=(f"client {o.user_id} ({o.username}) purchased a {p.isType} computer with an ID of {p.computer_id} for a price of {p.price}")
                                                if o.isClient == "VIP":
                                                    print(self.setCashback_P2P(p.price))
                                                self.PurchaseHistory_list.append(newPurchLog)
                                                p.stock -= 1
                                                a=False
                                            elif p.price > o.paytopay_cash_balance:
                                                print("\n================================\nUnsuccessful, not sufficient amount balance")
                                                a=False
                                        elif clientask17 == 2:
                                            if p.price <= o.epay_balance:
                                                o.epay_balance -= p.price
                                                print(f"\n================================\nSuccessfully purchased the computer, your new E-pay Balance would be: {o.epay_balance}")
                                                newPurchLog=(f"client {o.user_id} ({o.username}) purchased a {p.isType} computer with an ID of {p.computer_id} for a price of {p.price}")
                                                if o.isClient == "VIP":
                                                    print(self.setCashback_P2P(p.price))
                                                self.PurchaseHistory_list.append(newPurchLog)
                                                p.stock -= 1
                                                a=False
                                            elif p.price > o.paytopay_cash_balance:
                                                print("\n================================\nUnsuccessful, not sufficient amount balance")
                                                a=False
                                else:
                                    print("\nComputer has no stock\n")    
                                    break            
                            else:
                                print("Computer is not currently purchasable")
                                break                
            else:
                pass            

                
                        
    def add_computer(self):
        newComID=input("What would be the computer's id?: ")
        newIsAvailb=input("Availability? (Yes/No): ")
        ask=input("Any Clients Logged in?\n 1. Yes\n 2. No\nPick: ")
        if ask == "1":
            newUserLog=input("What is the username?: ")
        if ask == "2":
            newUserLog=""
        newPurch=input("Purchasable? (Yes/No): ")
        newSpecs=input('Format:["Processor","Graphics Card","Storage Drive"]\nSpecs: ')
        newPrice=int(input("What would be the price?: "))
        newStock=int(input("How many would be the stock?: "))
        newNum=(f"{len(self.allComputer_list)+1}")
        ComChoice=int(input("Is the Computer:\n1. Regular Computer (Low End)\n2. Gaming Computer (High End)\nWhat's the Choice: "))
        if ComChoice == 1:
            newRegCom=Computer(newNum,newComID,newIsAvailb,newPurch,newSpecs,newPrice,newStock,newUserLog)
            self.allComputer_list.append(newRegCom)
            self.RegComputerList.append(newRegCom)
            print(f"{newRegCom}================================\nAdded successfully!!")
        elif ComChoice == 2:
            newVIPCom=GamingVIP_Computer(newNum,newComID,newIsAvailb,newPurch,newSpecs,newPrice,newStock,newUserLog)
            self.allComputer_list.append(newVIPCom)
            self.VIPComputerList.append(newVIPCom)
            print(f"{newVIPCom}================================\nAdded successfully!!")

    def edit_computer_data(self):
        askComID1=input("What would be the computer's id?: ")
        for n in self.allComputer_list:
            if n.computer_id == askComID1:
                print(f"\n================================\nComputer found:{n.display_details()}")
                clientask11=str(input("Are you certain to edit the data? (Yes/No): "))
                if clientask11 == "Yes":
                    newComID1=input("What would be the computer's id?: ")
                    newIsAvailb1=input("Availability? (Yes/No): ")
                    newUserLog1=input("Any Clients Logged in?(leave blank if none): ")
                    if newUserLog1 == "":
                        newUserLog1=""
                        return
                    newPurch1=input("Purchasable? (Yes/No): ")
                    newSpec1s=input("Specs: ")
                    newPrice1=int(input("What would be the price?: "))
                    newStock1=int(input("How many would be the stock?: "))
                    n.computer_id = newComID1
                    n.is_Available = newIsAvailb1
                    n.purchasable = newPurch1
                    n.specs = newSpec1s
                    n.price = newPrice1
                    n.stock = newStock1
                    n.user_logged_in = newUserLog1
                    print(f"{n}\n================================\nSuccessfully Done.")
                    break
                elif clientask11 == "No":
                    print("Going Back to Menu...")
                    break
                else:
                    print("Pick only from the Given Choices (wrong input)")
                    break
        else:
            print("User not Found")
                    
    def delete_computer_data(self):
        askComID=input("What would be the computer's id?: ")
        for f in self.allComputer_list:
            if f.computer_id == askComID:
                print(f"\n================================\n\nAccount found:{f.display_details()}")
                clientask3=str(input("Are you certain to delete the data? (Yes/No): "))
                if clientask3 == "Yes":
                    print("Deleting...")
                    self.allComputer_list.remove(f)
                    print("\n================================\nComputer data has been deleted.\n")
                    break
                elif clientask3 == "No":
                    print("Going Back to Menu...")
                    break
                else:
                    print("Pick only from the Given Choices (wrong input)")
                    break
            else:
                print("Computer not Found")
                
    def list_all_computers(self):
        print("================================\nCOMPUTER LIST:\n\n")
        for e in self.allComputer_list:
            print(e.display_details())

    def view_purchase_history(self):
        print("================================\nPURCHASE HISTORY LIST:\n\n")
        for l in self.PurchaseHistory_list:
            print(l)

    def save_to_json(self):
        reg_client_data = [{'User Id': a.user_id, 'Username': a.username, 'Password': a.getUserPassword(), 'Email': a.email, 'Remaining Time': a.remaining_time, 'Pay-to-Pay Cash Balance': a.paytopay_cash_balance, 'E-pay Balance': a.epay_balance, 'Client Type': a.isClient} for a in self.RegularClientList]
        mem_client_data = [{'User Id': b.user_id, 'Username': b.username, 'Password': b.getUserPassword(), 'Email': b.email, 'Remaining Time': b.remaining_time, 'Membership Expiration in Hours': b.membership_expiration_in_hours, 'Pay-to-Pay Cash Balance': b.paytopay_cash_balance, 'E-pay Balance': b.epay_balance, 'Client Type': b.isClient} for b in self.MemberClientList]
        vip_client_data = [{'User Id': c.user_id, 'Username': c.username, 'Password': c.getUserPassword(), 'Email': c.email, 'Remaining Time': c.remaining_time, 'Membership Expiration in Hours': c.membership_expiration_in_hours, 'Pay-to-Pay Cash Balance': c.paytopay_cash_balance, 'E-pay Balance': c.epay_balance, 'Client Type': c.isClient} for c in self.VipClientList]
        RegComputer_data = [{'Number': d.number, 'Computer ID': d.computer_id, 'Availablility': d.is_Available, 'Any Users Logged In': d.user_logged_in, 'Purchasable': d.purchasable, 'Type of Computer': d.isType, 'Specifications': d.specs, 'Price': d.price, 'Stock': d.stock} for d in self.RegComputerList]
        VIPComputer_data = [{'Number': e.number, 'Computer ID': e.computer_id, 'Availablility': e.is_Available, 'Any Users Logged In': e.user_logged_in, 'Purchasable': e.purchasable, 'Type of Computer': e.isType, 'Specifications': e.specs, 'Price': e.price, 'Stock': e.stock} for e in self.VIPComputerList]
        with open(self.filename, 'w') as json_file:
            json.dump({'Regular Client Accounts': reg_client_data, 'Member Accounts': mem_client_data, 'VIP Accounts': vip_client_data, 'Regular Computers': RegComputer_data, 'VIP Gaming Computers': VIPComputer_data, 'Log History': self.LogHistory, 'Purchase History': self.PurchaseHistory_list}, json_file, indent=2)
            print(f"Computer Shop data were saved to {self.filename}")

    def load_from_json(self):
        try:
            with open(self.filename, 'r') as json_file:
                data = json.load(json_file)
            self.RegularClientList = [RegularUser(a['User Id'], a['Username'], a.get('Password'), a['Email'], a['Remaining Time'], a['Pay-to-Pay Cash Balance'], a['E-pay Balance'], a['Client Type']) for a in data.get('Regular Client Accounts',[])]
            self.MemberClientList = [Member(b['User Id'], b['Username'], b.get('Password'), b['Email'], b['Remaining Time'], b['Membership Expiration in Hours'], b['Pay-to-Pay Cash Balance'], b['E-pay Balance'], b['Client Type']) for b in data.get('Member Accounts',[])]
            self.VipClientList = [VIP_Member(c['User Id'], c['Username'], c.get('Password'), c['Email'], c['Remaining Time'], c['Membership Expiration in Hours'], c['Pay-to-Pay Cash Balance'], c['E-pay Balance'], c['Client Type']) for c in data.get('VIP Accounts',[])]
            self.RegComputerList = [Computer(d['Number'], d['Computer ID'], d['Availablility'], d['Any Users Logged In'], d['Purchasable'], d['Type of Computer'], d['Specifications'], d['Price'], d['Stock']) for d in data.get('Regular Computers',[])]
            self.VIPComputerList = [GamingVIP_Computer(e['Number'], e['Computer ID'], e['Availablility'], e['Any Users Logged In'], e['Purchasable'], e['Type of Computer'], e['Specifications'], e['Price'], e['Stock']) for e in data.get('VIP Gaming Computers',[])]
            self.LogHistory = data.get('Log History',[])
            self.PurchaseHistory_list = data.get('Purchase History',[])
            for a in self.RegularClientList:
                self.allclientlist.append(a)
            for b in self.MemberClientList:
                self.allclientlist.append(b)
            for c in self.VipClientList:
                self.allclientlist.append(c)
            for d in self.RegComputerList:
                self.allComputer_list.append(d)
            for e in self.VIPComputerList:
                self.allComputer_list.append(e)

            print("Loaded to JSON successfully")
        except FileNotFoundError:
            print(f"File {self.filename} not found. Starting with an empty customer and account list.")
        except json.JSONDecodeError:
            print(f"Error decoding JSON data from {self.filename}. Starting with an empty customer and account list.")


    
    def generate_instances(self):
        reguser1 = RegularUser("22131", "Jay", "Pass#1234", "Jay@yahoo.com", 100, 50000, 2000)
        reguser2 = RegularUser("22132", "CoolUser567", "Cool#5678", "Mary@yahoo.com", 200, 60, 30)
        reguser3 = RegularUser("22133", "StarUser910", "Star#1121", "John@yahoo.com", 300, 70, 40)
        reguser4 = RegularUser("22134", "SuperUser1314", "Super#1516", "Patricia@yahoo.com", 400, 80, 50)
        reguser5 = RegularUser("22135", "MegaUser1718", "Mega#1920", "Robert@yahoo.com", 500, 90, 60)
        reguser6 = RegularUser("22136", "UltraUser2122", "Ultra#2324", "Jennifer@yahoo.com", 600, 100, 70)
        reguser7 = RegularUser("22137", "PowerUser2526", " Power#2728", "Michael@yahoo.com", 700, 110, 80)
        reguser8 = RegularUser("22138", "MasterUser2930", "Master#3132", "Linda@yahoo.com", 800, 120, 90)
        reguser9 = RegularUser("22139", "ProUser3334", "Pro#3536", "William@yahoo.com", 900, 130, 100)
        reguser10 = RegularUser("221310", "useEliteUser3738r10", "Elite#3940", "Elizabeth@yahoo.com", 1000, 140, 110)

        member1 = Member("221311", "Bob", "Milky#Way2000024", "Bob@gmail.com", 12000, 24, 1000000, 20000)
        member2 = Member("221312", "MoonWalker", "Lunar#Landing1969", "Johnson@gmail.com", 11000, 24, 900, 10000)
        member3 = Member("221313", "SunDancer", "Solar#Flare5678", "Smith@gmail.com", 1000000, 24, 8000, 1800)
        member4 = Member("221314", "CometChaser", "Halley#Comet1986", "Sophia@gmail.com", 9000, 24, 7000, 17000)
        member5 = Member("221315", "GalaxyRider", "Andromeda#Galaxy123", "Williams@gmail.com", 8000, 24, 60000, 1600)
        member6 = Member("221316", "PlanetHopper", "Mars#Rover2000020000", "Ethan@gmail.com", 7000, 24, 500, 15000)
        member7 = Member("221317", "AstroNomad", "Space#Travel7890000", "Olivia@gmail.com", 6000, 24, 4000, 14000)
        member8 = Member("221318", "NebulaNavigator", "Orion#Nebula8900001", "Davis@gmail.com", 50000, 24, 3000, 1300)
        member9 = Member("221319", "CosmicVoyager", "Voyager#1977", "Noah@gmail.com", 40000, 24, 2000, 12000)
        member10 = Member("2213120", "SpaceWhisperer", "Black#Hole0000123", "Miller@gmail.com", 3000, 24, 1000, 11000)

        vip_member1 = VIP_Member("2213121", "Cedrick", "P@ssw000rd#123", "Ava@gmail.com", 12000, 24, 1000000000, 5000000)
        vip_member2 = VIP_Member("2213122", "Starlight789", "St@rl!ght#789", "Wilson@gmail.com", 11000, 24, 2000000000, 6000000)
        vip_member3 = VIP_Member("2213123", "QuantumWave456", "Qu@ntum#456", "Liam@gmail.com", 13000, 24, 15000000, 7000000)
        vip_member4 = VIP_Member("2213124", "CosmicRay89000", "C000sm!cR@y#89000", "Moore@gmail.com", 14000, 24, 16000000, 8000000)
        vip_member5 = VIP_Member("2213125", "LunarEclipse567", "Lun@r#567", "Mia@gmail.com", 15000, 24, 17000000, 9000000)
        vip_member6 = VIP_Member("2213126", "SolarFlare321", "S000l@rFl@re#321", "Taylor@gmail.com", 16000, 24, 18000000, 1000000000)
        vip_member7 = VIP_Member("2213127", "NebulaCloud234", "N3bul@Cl000ud#234", "Jacob@gmail.com", 17000, 24, 19000000, 11000000)
        vip_member8 = VIP_Member("2213128", "GalacticWind789", "G@l@cticW!nd#789", "Anderson@gmail.com", 18000, 24, 2000000000, 12000000)
        vip_member9 = VIP_Member("2213129", "QuantumField345", "Qu@ntumF!3ld#345", "Bryan@gmail.com", 19000, 24, 21000000, 13000000)
        vip_member10 = VIP_Member("2213130", "StellarNova678", "St3ll@rN000v@#678", "Rick@gmail.com", 2000000, 24, 22000000, 14000000)
        
        clientList=[reguser1, reguser2, reguser3, reguser4, reguser5,reguser6, reguser7, reguser8, reguser9, reguser10,member1, member2, member3, member4, member5,member6, member7, member8, member9, member10,vip_member1, vip_member2, vip_member3, vip_member4, vip_member5,vip_member6, vip_member7, vip_member8, vip_member9, vip_member10]
        for q in clientList:
            self.allclientlist.append(q)
        for w in clientList:
            if w.isClient=="Regular":
                self.RegularClientList.append(w)
            elif w.isClient== "Member":
                self.MemberClientList.append(w)
            elif w.isClient== "VIP":
                self.VipClientList.append(w)

        #===================================

        com1=Computer(1,"I1OXE","No","Yes",["AMD Ryzen 5 5600","GIGABYTE GeForce RTX 3060 Gaming OC 12G (REV2.0)","Western Digital Blue 1TB HDD"],25000)
        com2=Computer(2,"HYDG8","Yes","Yes",["Intel Core i3-13100F","XFX Speedster MERC310 AMD Radeon RX 7900XTX Black","Seagate BarraCuda 1TB HDD"],35000)
        com3=Computer(3,"WBYQ2","Yes","Yes",["Intel Core i3-12100F","AMD Radeon RX 7600","Toshiba P300 1TB HDD"],45000)
        com4=Computer(4,"QHRGN","Yes","Yes",["Intel Core i3-10100F","NVIDIA GT 1030","Hitachi Ultrastar 1TB HDD"],40000)
        com5=Computer(5,"PH3NU","No","No",["AMD Athlon 200GE","ZOTAC GeForce GTX 1650 OC","Western Digital Black 500GB HDD"],20000)
        com6=Computer(6,"H4DCQ","Yes","Yes",["AMD Ryzen 7 5800X","MSI Gaming GeForce GT 710","Seagate FireCuda 1TB HDD"],37000)
        com7=Computer(9,"ASLFR","Yes","Yes",["Intel Core i7-13700K","EVGA GeForce GT 730","Western Digital Red 1TB HDD"],36000)
        com8=Computer(8,"793AM","Yes","Yes",["Intel Core i5-12400","Gigabyte Geforce GTX 1050 Ti OC","Toshiba X300 2TB HDD"],20000)
        com9=Computer(9,"JKTAP","Yes","Yes",["Intel Core i7-13700K","EVGA GeForce GT 730","Seagate IronWolf 1TB HDD"],37000)
        com10=Computer(10,"ENTIX","Yes","No",["Intel Core i7-14700K","MSI GeForce GTX 1650 Super Ventus XS OC","Hitachi Deskstar 1TB HDD"],39000)

        vipCom1=GamingVIP_Computer(11,"A1ZWV","No","Yes",["Intel Core i7-14700K","Nvidia's RTX 4090","Samsung 970 EVO Plus SDD"],60000)
        vipCom2=GamingVIP_Computer(12,"0YI07","Yes","Yes",["AMD Ryzen 5 7600X","Nvidia RTX 4080 Super","Western Digital Black SN750 NVMe SDD"],65000)
        vipCom3=GamingVIP_Computer(13,"A2A9O","Yes","Yes",["Intel Core i9-14900K","Nvidia RTX 4070 Ti Super","Crucial MX500 SDD"],70000)
        vipCom4=GamingVIP_Computer(14,"MMFR6","Yes","Yes",["AMD Ryzen 7 7800X3D","Nvidia RTX 4070 Super","Kingston A2000 NVMe PCIe M.2 1TB SDD"],75000)
        vipCom5=GamingVIP_Computer(15,"UBWC5","No","No",["AMD Ryzen 7 5800X3D","AMD Radeon RX 7900 XTX","Seagate FireCuda 520 PCIe Gen4 x4 NVMe 1TB SDD"],73000)
        vipCom6=GamingVIP_Computer(16,"5LF9R","Yes","Yes",["Intel Core i5-11600K","AMD Radeon RX 7800 XT","Samsung 860 PRO SDD"],80000)
        vipCom7=GamingVIP_Computer(17,"X02WR","Yes","Yes",["AMD Ryzen 9 7950X3D","Nvidia GeForce RTX 4060","Intel Optane 905P SDD"],65000)
        vipCom8=GamingVIP_Computer(18,"ANRO9","Yes","Yes",["Intel Core i9-13900K","AMD Radeon RX 7900 XT","Corsair Force Series MP600 SDD"],100000)
        vipCom9=GamingVIP_Computer(19,"U90WJ","Yes","Yes",["AMD Ryzen 7 5700X","Intel Arc A750","ADATA XPG SX8200 Pro SDD"],60000)
        vipCom10=GamingVIP_Computer(20,"9BK89","Yes","No",["Intel Core i5-14600K","AMD Radeon RX 7600 XT","Sabrent Rocket Q4 NVMe PCIe 4.0 M.2 2TB SDD"],60000)

        comList=[com1,com2,com3,com4,com5,com6,com7,com8,com9,com10,vipCom1,vipCom2,vipCom3,vipCom4,vipCom5,vipCom6,vipCom7,vipCom8,vipCom9,vipCom10]
        for r in comList:
            self.allComputer_list.append(r)
        for x in comList:
            if x.isType=="Low End":
                self.RegComputerList.append(x)

            elif x.isType=="High End":
                self.VIPComputerList.append(x)
 
        print("\n================================\nGenerated Successfully!")
        
    def clear_data(self):
        self.allclientlist.clear()
        self.allComputer_list.clear()
        self.LogHistory.clear()
        self.PurchaseHistory_list.clear()
        print("\n================================\nData Cleared Successfully!")
    def menu1(self):
        try:
            while True:
                print("================================\nWelcome Back Admin!\n")
                print(" 1. Create Client Account\n \
2. Edit Client Data\n \
3. Delete Client Data\n \
4. Time Top Up for Client\n \
5. See all Client Accounts\n \
6. See all Computers\n \
7. Log Client into a Computer\n \
8. Add Hours into Client's Membership Duration\n \
9. Show Log History\n \
10. Save Data to JSON\n \
11. Load Data from JSON\n \
\n \
\n \
888. Clear all Data (for test purposes)\n \
999. Generate instances of Clients and Computers (for test purposes)\n \
0. Back ")
                c=int(input("Pick Your Choice: "))
                if c == 1:
                    self.add_client()
                elif c == 2:
                    self.edit_client_data()
                elif c == 3:
                    self.delete_client_data()
                elif c == 4:
                    self.client_topup()                                   
                elif c == 5:
                    self.list_all_clients()
                elif c == 6:
                    self.list_all_computers()
                elif c == 7:
                    self.assign_client2computer()
                elif c == 8:
                    self.mem_vip_topup()
                elif c == 9:
                    self.view_log_history()
                elif c == 10:
                    self.save_to_json()
                elif c == 11:
                    self.load_from_json()
                    
                elif c == 888:
                    self.clear_data()                       
                elif c == 999:
                    self.generate_instances()                  
                elif c == 0:
                    print("================================\n")
                    False
                    introduction()
                else:
                    print("Pick only from the Given Choices (wrong input)\n")
                    return admin.menu1()
        except ValueError:
            print("Pick only from the Given Choices (wrong input)\n")
            return admin.menu1()
        except KeyboardInterrupt:
            print("Program stopped")        
        
    def menu2(self):
        try:
            while True:
                print("================================\nWelcome Back Admin!\n")
                print(" 1. Create Client Account\n \
2. Edit Client Data\n \
3. Delete Client Data\n \
4. See all Computers\n \
5. Add a Computer\n \
6. Edit Computer's Details\n \
7. Remove a Computer\n \
8. [Client Make Purchase] Buy a Computer\n \
9. View Purchase History\n \
10. Save Data to JSON\n \
11. Load Data from JSON\n \
\n \
\n \
888. Clear all Data (for test purposes)\n \
999. Generate instances of Clients and Computers (for test purposes)\n \
0. Back ")
                
                d=int(input("Pick Your Choice: "))
                if d == 1:
                    self.add_client()
                elif d == 2:
                    self.edit_client_data()
                elif d == 3:
                    self.delete_client_data()
                elif d == 4:
                    self.list_all_computers()
                elif d == 5:
                    self.add_computer()
                elif d == 6:
                    self.edit_computer_data()
                elif d == 7:
                    self.delete_computer_data()
                elif d == 8:
                    self.client_buy_computer()
                elif d == 9:
                    self.view_purchase_history()
                elif d == 10:
                    self.save_to_json()
                elif d == 11:
                    self.load_from_json()
                    
                elif d == 888:
                    self.clear_data()         
                elif d == 999:
                    self.generate_instances()    
                elif d == 0:
                    print("================================\n")
                    False
                    introduction()
                else:
                    print("Pick only from the Given Choices (wrong input)\n")
                    return admin.menu2()
        except ValueError:
            print("Pick only from the Given Choices (wrong input)\n")
            return admin.menu2()
        except KeyboardInterrupt:
            print("Program stopped")
    
admin=ComputerShop()

#====================================================================================================================================

def introduction():
    try:
        while True:
            print("✨✨✨✨✨✨✨💻🧑‍💻✨✨✨✨✨✨✨\n      Cedrick's Computer Shop")
            print("\nWould you like to:\n  1. Manage Client to Computer (Internet Cafe)\n  2. Manage Computers and Selling\n  0. Exit")
            a=int(input("Pick Your Choice: "))
            # Use Computer Route
            if a == 1:
                admin.menu1()
            # Buy Computer Route
            elif a == 2:
                admin.menu2()
            elif a == 0:
                print("Exiting...Have a Good Day!")
                False
                break
            else:
                print("Pick only from the Given Choices (wrong input)\n")
                return introduction()
    except ValueError:
        print("Pick only from the Given Choices (wrong input)\n")
        return introduction()
    except KeyboardInterrupt:
        print("Program stopped")

#====================================================================================================================================

if __name__ == "__main__":
    introduction()
