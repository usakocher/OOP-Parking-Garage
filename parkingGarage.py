class ParkingGarage:
    def __init__(self, capacity, currentTicket = {}):
        self.capacity = capacity
        self.currentTicket = currentTicket
        temporary = list(range(1, capacity + 1))
        self.tickets = [str(n) for n in temporary]

    def checkTicket(self, ticket):
        if ticket in self.currentTicket.keys():
            return True
        else:
            return False

    def takeTicket(self):
        if self.tickets == []:
            print(f'Sorry no more spaces available.')
        else:
            self.tickets = sorted(self.tickets, key = int)
            ticket = self.tickets.pop(0)
            print(f'Your ticket number is {ticket}')
            self.currentTicket[ticket] = False

    def payForParking(self, ticket):
        while True:
            if self.checkTicket(ticket):
                if self.currentTicket[ticket] == True:
                    self.paying(ticket)
                    break
                else:
                    payQuest = input('Your payment is $10. Would you like to pay now? (y/n) ')
                    if payQuest.lower() == 'y':
                        paid = input('Enter anything to pay: ')
                        self.paying(ticket)
                        return True
                    elif payQuest.lower() == 'n':
                        return False
                    else:
                        print('That is not a valid input. Please try again')
                        return False
            else:
                print(f'{ticket} is not a valid ticket.')
                break

    def paying(self, ticket):
        self.currentTicket[ticket] = True
        print('Your ticket has been paid, you have 15 minutes to leave the garage')

    def leaveGarage(self, ticket):
        while True:
            if self.checkTicket(ticket):
                if self.currentTicket[ticket] == False:
                    if self.payForParking(ticket) == True:
                        del self.currentTicket[ticket]
                        self.tickets.append(ticket)
                        break
                    else:
                        break
                else:
                    print('Your ticket has already been paid.\nThank you, have a nice day!')
                    self.tickets.append(ticket)
                    del self.currentTicket[ticket]
                    break
            else:
                print(f'{ticket} is not a valid ticket.')
                break

    def run(self):
        while True:
            response = input('Do you want to park, pay or leave, or enter quit to end the program: ')
            if response.lower() == 'park':
                self.takeTicket()
            elif response.lower() == 'pay':
                ticket = input('What is your ticket number? ')
                self.payForParking(ticket)
            elif response.lower() == 'leave':
                ticket = input('What is your ticket number? ')
                self.leaveGarage(ticket)
            elif response.lower() == 'quit':
                break
            else:
                print('That is not a valid input, please select again.')    



garage = ParkingGarage(15)
garage.run()