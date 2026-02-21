
# Entrada 4 
# TK101 => P1 => 55
# TK102 => P2 => 200
# TK103 => P3 => 1200
# TK104 => P1 => 61

time_per_priority = {
    'P1':60,
    'P2':240,
    'P3':1440
}

class SLA:
    # Data
    ticket_no : int
    priority : str
    time_spent : int
    time_sla : int
    violation : bool
    at_risk : bool

    def violationCheck(self):
        if self.time_sla < self.time_spent :
            return True

    def riskCheck(self):
        if self.time_spent >= self.time_sla*0.8 :
            return True

    def issueStatement(self):
        if self.violation:
            print(f"Warning, Ticket satus : {self.priority} Violation : {self.violation} Time exceeded : {self.time_spent-self.time_sla} min")            
        elif self.at_risk:
            print(f"Warning, Ticket satus : {self.priority} At risk : {self.atrisk} Time left : {self.time_sla-self.time_spent} min")            
        else :
            print(f"Ticket satus for TK{self.ticket_no} : {self.priority} At risk : {self.atrisk} Time left : {self.time_sla-self.time_spent} min")            

    # Fix into method
    # Get element
    def get_int(possibleNumber, errString, inputString):
        possibleNumber = input(inputString)
        while True:
            try:
                if not int(possibleNumber):
                    exit
                else:
                    return possibleNumber
            except ValueError:
                print(errString)
                possibleNumber = input(inputString)

    def __init__(self, ticket_no, priority, time_spent):
        self.ticket_no = self.get_int(ticket_no, "Enter a number\n Check again", "Ticket Number : ")
        self.priority = priority
        self.time_spent = self.get_int(time_spent)
        self.time_sla = time_per_priority.get(self.priority,'Prioridad no registrada')
        self.violation = self.violationCheck()
        self.at_risk = self.riskCheck()

def main():
    n = 0
    tickets = []
    print("Enter the number of tickets :")

    numberOfTickets = input()
    numberOfTickets = int(isNumber(numberOfTickets,"It's not a number", "Enter a number : "))

    print("\nEnter ticket information :")

    while(n < numberOfTickets) :
         ticket_number = input("Ticket Number : ")

         priority_entered = input("Priority : ")
         while not time_per_priority.get(priority_entered):
            print("Priority entered doesn't exist\n Check again")
            priority_entered = input("Priority : ")

         time_entered = input("Time spent online : ")
         time_entered = int(isNumber(time_entered, "It's not a number", "Enter a number : "))
         tickets.append(sla(ticket_number,priority_entered,int(time_entered)))
         n = n+1
    
    for tick in tickets :
        tick.issueStatement()

if __name__ == '__main__':
    main()