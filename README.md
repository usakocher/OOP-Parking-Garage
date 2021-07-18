# OOP-Parking-Garage

## Team Members
Adam Kocher<br/>
Gilberto Cotzajay

## Project Aims
Our task was to create a parking garage class to get more familiar with Object Oriented Programming(OOP).
Our program was to issue a parking ticket, and provide functions for paying that ticket, as well as 
leaving the garage.

## Assumptions
For this project, we assume the garage has a finite amount of parking spaces. We also assume that
the customer of this project, would be the person wanting to park the vehicle. We designed the program
so that the ticket number correlated with the number on the parking space, starting with Ticket #1 as
the closest to the exit. We also assumed there were payment machines at each floor, not just at the
exit. This is common in modern parking garages.

## Program
Our program askes the customer if they want to park, pay, leave or quit the program. From there, the program
starts the associating function.

Special cases: Program accounts for bad inputs.
#### Park
The program issues a ticket according to availability:

Special cases: Program accounts for bad inputs. Also issues tickets as most convenient, or closest to the exit.
#### Pay
Allows a customer to pay for a ticket anywhere in the facility.

Special cases: Program verifies ticket validity and wether it has been paid alreadyh. Program accounts for bad inputs.
#### Leave
Prompts the customer for their ticket and then allows them to leave the facility. Opens space up for another customer.

Special cases: Program verifies ticket validity and wether it has been paid alreadyh. Program accounts for bad inputs.
#### Quit
Allows the customer to quit the program.

## Contributions
Gilberto wrote the main backbone of the program. He constructed the main if/else tree and the core functions.
Adam wrote the code that account for errors or edge cases.

## Lessons Learned
This project provided a great example of OOP, mainly the ability to build part of a program and test it, before moving on
to the next part. But this requires a better planning stage, so that the designer can account for areas of the code
that haven't been coded yet.

We also learned that testing the program is key to determining all the edge cases and how the program handles them. We probably
ran 50 test cases on the program after it was complete, making several small changes along the way.
