main_dish = input("Enter name of dish you want to eat: ")
time_of_day = int(input("Enter time of arrivel: "))
has_voucher = input("Did you have voucher: ") == "True"
is_card_payment = input("Did you want to pay by card: ") == "True"

if main_dish == "paneer tikka":
    cost = 250
elif main_dish == "butter chicken":
    cost = 240
elif main_dish == "masala dosa":
    cost = 200
else:
    print("Invalid main dish")
    exit()

if time_of_day >= 12 and time_of_day <= 15:
    total_cost = cost * 0.85
else:
    total_cost = cost

if has_voucher:
    total_cost *= 0.9

if is_card_payment:
    service_charge = 0.05 * total_cost
    total_cost += service_charge

print(f"{total_cost:.2f}")
