fruits = [
    {
        'name': 'Apple',
        'price': 3.99,
        'stock': 2001
    },
    {
        'name': 'Banana',
        'price': 4.99,
        'stock': 2002
    },
    {
        'name': 'Cherry',
        'price': 2.99,
        'stock': 2003
    },
    {
        'name': 'Durian',
        'price': 4.99,
        'stock': 2004
    },
    {
        'name': 'Elderberry',
        'price': 3.99,
        'stock': 2005
    },
    {
        'name': 'Fig',
        'price': 2.99,
        'stock': 2001
    },
    {
        'name': 'Grape',
        'price': 3.99,
        'stock': 2002
    },
    {
        'name': 'Honeyberry',
        'price': 4.99,
        'stock': 2003
    },
    {
        'name': 'Incaberry',
        'price': 2.99,
        'stock': 2004
    },
    {
        'name': 'Jackfruit',
        'price': 4.99,
        'stock': 2005
    },
    {
        'name': 'Kiwifruit',
        'price': 3.99,
        'stock': 2001
    },
    {
        'name': 'Lemon',
        'price': 2.99,
        'stock': 2002
    },
    {
        'name': 'Mango',
        'price': 4.99,
        'stock': 2003
    },
    {
        'name': 'Nectarine',
        'price': 3.99,
        'stock': 2004
    },
    {
        'name': 'Orange',
        'price': 2.99,
        'stock': 2005
    },
    {
        'name': 'Papaya',
        'price': 3.99,
        'stock': 2001
    },
    {
        'name': 'Quince',
        'price': 4.99,
        'stock': 2002
    },
    {
        'name': 'Raspberry',
        'price': 2.99,
        'stock': 2003
    },
    {
        'name': 'Strawberry',
        'price': 4.99,
        'stock': 2004
    },
    {
        'name': 'Tamarind',
        'price': 3.99,
        'stock': 2005
    },
    {
        'name': 'Watermelon',
        'price': 2.99,
        'stock': 2001
    }
]


def valid_fruit_object(fruit_object):
    if "name" in fruit_object and "price" in fruit_object and "stock" in fruit_object:
        return True
    else:
        return False


valid_object = {
    'name': 'Avocado',
    'price': 3.99,
    'stock': 2001
}

missing_name = {
    'price': 3.99,
    'stock': 2001
}

missing_price = {
    'name': 'Avocado',
    'stock': 2001
}

missing_stock = {
    'name': 'Avocado',
    'price': 3.99,
}
