#WAP to accept cost price and profit percentage and display the Selling price.

cp = int(input("Enter the Cost Price: "))
p = float(input("Enter the cost percentage: "))

sp = ((100 + p)/100)*cp

print("Selling Price: ", sp)