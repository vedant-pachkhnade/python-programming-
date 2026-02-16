principal_amount = int(input("Enter principle amount: "))
n_years = int(input("Enter number number of years: "))

if n_years < 10:
    rate = 0.05
else:
    rate = 0.08

simple_interest = principal_amount * rate * n_years
print(round(simple_interest))
