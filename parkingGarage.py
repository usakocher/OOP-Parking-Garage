class ParkingGarage:
    def __init__(self, tickets = ['1', '2', '3'],
        currentTicket = 
            {
            '1': False,
            '2': False,
            '3': False
            }):
        self.tickets = tickets
        self.currentTicket = currentTicket

    def takeTicket(self):
        if self.tickets == []:
            print(f'Sorry no more spaces available.')
        else:
            ticket = self.tickets.pop(0)
            print(f'Your ticket number is {ticket}')
            self.currentTicket[ticket] = False

    def payForParking(self, ticket):
        while True:
            paying = input('Your payment is $10. Would you like to pay now? (y/n) ')
            if paying.lower() == 'y':
                if self.currentTicket[ticket] == True:
                    print('Your ticket has been paid, you have 15 minutes to leave the garage')
                else:
                    paid = input('Enter anything to pay ')
                    self.currentTicket[ticket] = True
                    print('Your ticket has been paid, you have 15 minutes to leave the garage')
            elif paying.lower() == 'n':
                break
            else:
                print('That is not a valid input. Please try again.')

    def leaveGarage(self, ticket):
        if self.currentTicket[ticket] == False:
            self.payForParking(ticket)
        else:
            print('Your ticket has already been paid.\nThank you, have a nice day!')
            self.tickets.append(ticket)



garage = ParkingGarage()
while True:
    response = input('Do you want to park, pay or leave, or enter quit to end the program: ')
    if response.lower() == 'park':
        garage.takeTicket()
    elif response.lower() == 'pay':
        ticket = input('What is your ticket number? ')
        garage.payForParking(ticket)
    elif response.lower() == 'leave':
        ticket = input('What is your ticket number? ')
        garage.leaveGarage(ticket)
    elif response.lower() == 'quit':
        break
    else:
        print('That is not a valid input, please select again.')