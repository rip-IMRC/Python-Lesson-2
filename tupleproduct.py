def product_of_tuple(input_tuple):
    product = 1
    for number in input_tuple:
        product *= number
    return product
my_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
result = product_of_tuple(my_tuple)
print(f"The product of the tuple {my_tuple} is: {result}")