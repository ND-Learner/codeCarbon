from decimal import Decimal
from codecarbon import EmissionsTracker

tracker = EmissionsTracker()
tracker.start()

def change():
    
    paid = Decimal(input("Amount Paid: £"))
    change = Decimal(10) - Decimal(paid)

    print ("Change due: £", change)
    print ("Hand the customer: ")

    denoms = map(Decimal, ('5.00', '2.00', '1.00', '0.50', '0.20', '0.10', '0.05', '0.02', '0.01'))


    for denom in denoms:

        thisdenom, change = divmod(change, denom)
        if thisdenom > 0:
            print (str(thisdenom) + " x £ " + str(denom))    

            
change()

tracker.stop()
emissions: float = tracker.stop()
print(emissions)
