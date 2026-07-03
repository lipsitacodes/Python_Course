# Write a program that takes a list of numbers and removes all duplicates using a set.
list = [12,124,44,21,2,1,44,2,1,42,43,12]
coset = set(list)
print(coset)
# Given a dictionary of products and their prices, find the product with the highest price.
def most_expensive_product(products):
    '''
    Find the product with the highest price.

    Parameters:
        products (dict): Dictionary of product: price pairs.

    Returns:
        tuple: (product_name, price) of the highest priced product.
    '''
    return max(products.items(), key=lambda x: x[1])
products = {
    "Laptop": 80000,
    "Phone": 60000,
    "Tablet": 35000,
    "Monitor": 15000
}

product, price = most_expensive_product(products)
print(f"The most expensive product is '{product}' with price {price}.")

# print(price.)
# Write a program that merges two dictionaries into one.
def merge_dicts(dict1, dict2):
    '''
    Merge two dictionaries into one.
    Parameters:
        dict1 (dict): First dictionary
        dict2 (dict): Second dictionary
    Returns:
        dict: A new dictionary with combined key-value pairs
    '''
    return {**dict1, **dict2}

d1 = {"a": 1, "b": 2}
d2 = {"c": 3, "d": 4}
merged = merge_dicts(d1, d2)
print(merged)  # {'a': 1, 'b': 2, 'c': 3, 'd': 4}
# Solution 2
d1 = {"a": 1, "b": 2}
d2 = {"c": 3, "d": 4}
d1.update(d2)
print(d1)  # {'a': 1, 'b': 2, 'c': 3, 'd': 4}
