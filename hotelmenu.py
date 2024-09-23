menu = {
    'pizza': 40,
    'pasta': 50,
    'burger': 30,
    'salad': 20,
    'fries': 15,
    'soup': 25,
    'steak': 60,
    'sandwich': 35,
    'tacos': 45,
    'sushi': 70
}


print('welcome to our python Restaurant')

order_total=0
item_1=input('enter the name of item you want to order =')

if item_1 in menu:
    order_total+=menu[item_1]
    print(f'your item {item_1} has been order')
else:
    print(f'Order item is {item_1} not available yet!')

another_order=input('do u want to add another order ')

if another_order== 'yes':
    item_2 =input('enter the second item:')
    if item_2 in menu:
        order_total+=menu[item_2]
        print(f'your {item_2} has been order')
    else:
        print(f'{item_2} is not available')

print(f'the total amount of item to pay is {order_total}')

