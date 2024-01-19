
class ParkingGarage():
    def __init__(self, total_tickets_available, parking_spaces_available):
        self.total_tickets_available = total_tickets_available
        self.parking_spaces_available = parking_spaces_available
        self.current_ticket = {}



    def take_ticket(self):
        # self.total_tickets_available = self.parking_spaces_available  ?
        while True:
            if self.parking_spaces_available >= 1:
                print("Welcome to our Garage!")
                user_response = input("Lucky for you, we currently have space available. Would you like a ticket? Yes or No").title()
                if user_response == "Yes":
                    print("Okay that'll be $20.00")
                elif user_response == "No":
                    print("Okay have a nice day.")
                else:
                    print("Sorry that is an invalid option.")



            else:
                print("Sorry we're currently full. Please come back later.")
                break

    def pay_for_parking(self):



    def leave_garage(self):