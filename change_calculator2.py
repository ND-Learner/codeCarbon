from decimal import Decimal
from codecarbon import EmissionsTracker

tracker = EmissionsTracker()
tracker.start()

def change():
    
    paid = Decimal(input("Amount Paid: £"))
    change = Decimal(10) - Decimal(paid)

    print ("Change due: £", Decimal(change))
    print ("Hand the customer: ")

    denoms = map(Decimal, ('5.00', '2.00', '1.00', '0.50', '0.20', '0.10', '0.05', '0.02', '0.01'))

    remain = change

    for denom in denoms:

        thisdenom, remain = divmod(remain, denom)

        if thisdenom > 0:
             print ("{} x £ {}".format(thisdenom, denom))
            
change()

tracker.stop()
emissions: float = tracker.stop()
print(emissions)