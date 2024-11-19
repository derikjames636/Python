inventory=[
    ('Laptop',5,30000),
    ('Headphone',4,500),
    ('Mouse',58,150),
    ('Keyboard',10,200),
    ('Moniter',10,3000)

]
highest_stock_value=0
item_with_highest_stoke_value=None
for item in inventory:
    item_name,quantity,prize=item
    stoke_value = quantity * prize
    print('Item name', item_name, "the total value is:", stoke_value)
    if stoke_value>highest_stock_value:
        highest_stock_value=stoke_value
        item_with_highest_stock_value=item_name
print('The item price with highest stock value is ',highest_stock_value)
print('The item name with highest stock value is ',item_with_highest_stock_value)