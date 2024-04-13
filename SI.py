#WAP to display Simple Interest after accepting Principal, rate and time.

p = int(input("Enter the principal: "))
r = float(input("Enter the rate: "))
t = float(input("Enter the time: "))

si = (p*r*t)/100

print("Simple Intrest: ", si)