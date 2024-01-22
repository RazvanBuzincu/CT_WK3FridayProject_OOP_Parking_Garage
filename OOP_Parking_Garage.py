class ParkingGarage():
    def __init__(self, parking_spaces_available):
        self.total_tickets_available = 100
        self.parking_spaces_available = parking_spaces_available
        self.current_ticket = {}
        self.user_response = None
    def take_ticket(self):
        while True:
            if  self.parking_spaces_available >= 1:
                print("Hello and welcome to our Garage!")
                self.user_response = input("Lucky for you, we currently have space available. Would you like a ticket? Yes or No? ").title()
                if self.user_response == "Yes":
                    print("Okay, here's your ticket")
                    self.total_tickets_available -= 1
                    print(f"There are {self.total_tickets_available} tickets left.")
                    self.current_ticket["Ticket Paid"] = False
                    print(self.current_ticket)
                    break
                elif self.user_response == "No":
                    print("Okay have a nice day.")
                else:
                    print("Sorry that is an invalid option.")
            else:
                print("Sorry we're currently full. Please come back later.")
                break
    def pay_for_parking(self):
        print("Thank you for choosing our parking garage today. Your total will be $20.00")
        self.user_response = input("Please select a PAYMENT METHOD. Press 1 for CASH or 2 for CARD. ")
        while True:
            if self.user_response == '1':
                print("Please insert your CASH.")
                print("Thank you for your payment, your ticket has now been paid. You have 15 minutes to leave the garage.")
                self.current_ticket["Ticket Paid"] = True
                print(self.current_ticket)
                break
            elif self.user_response == '2':
                print("Please swipe your CARD.")
                print("Thank you for your payment. Your card has successfully gone through and your ticket has now been paid. You have 15 minutes to leave the garage.")
                self.current_ticket["Ticket Paid"] = True
                print(self.current_ticket)
                break
            else:
                print("Sorry that is not a valid option. Please select CASH (1) or CARD (2).")


    def leave_garage(self):
        if self.current_ticket["Ticket Paid"] == True:
            print("Thank you again and we hope you enjoy the rest of your day.")
            self.total_tickets_available += 1
            print(f"There are now {self.total_tickets_available} tickets available.")
        else:
            print("Please proceed with your payment.")
parkinggarage = ParkingGarage(0)
parkinggarage.take_ticket()
parkinggarage.pay_for_parking()
parkinggarage.leave_garage()