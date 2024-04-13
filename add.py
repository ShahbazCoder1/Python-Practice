#Question:
#WAP to accept 4 numbers and display the sum and average.

a = int(input("Enter the number: "))
b = int(input("Enter the number: "))
c = int(input("Enter the number: "))
d = int(input("Enter the number: "))

s = a + b + c + d
avg = float(s/4)
print("sum: ", s , "\nAverage: ", avg)
