goods = {1: ("тетрадь", 20), 2: ("ручка", 35)}
sales = [(1,3), (2,2), (1,5)]
total = 0
for code, quantity in sales:
    name, price = goods[code]
    if name == "тетрадь":
        total += quantity
print(total)
