
class ParkingGarage():
    def __init__(self, total_tickets_available, parking_spaces_available):
        self.total_tickets_available = total_tickets_available
        self.parking_spaces_available = parking_spaces_available
        self.current_ticket = {}
        self.user_response = None  # Assuming user_response is a class attribute


    # Justin
    def take_ticket(self):
        # self.total_tickets_available = self.parking_spaces_available  ?
        while True:
            if self.parking_spaces_available >= 1:
                print("Welcome to our Garage!")
                self.user_response = input("Lucky for you, we currently have space available. Would you like a ticket? Yes or No").title()
                if self.user_response == "Yes":
                    print("Okay that'll be $20.00")
                elif self.user_response == "No":
                    print("Okay have a nice day.")
                else:
                    print("Sorry that is an invalid option.")

            else:
                print("Sorry we're currently full. Please come back later.")
                break


    # Razvan
    def pay_for_parking(self):
        if self.user_response == "Yes"
           self.current_ticket = +1




    
    
    
    
    
    
    
    
    
    
    
    
    
    
    # william
    def leave_garage(self):