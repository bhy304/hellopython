fruits={'orange':200, 'apple':300, 'banana':500}
cart = {'orange':3, 'apple':2, 'banana': 2}

#방법1
sum = 0
for key in cart:
    # print(key)
    sum += fruits[key] + cart[key]
print(sum)

#방법2
# print(cart.items())
sum = 0
for key, value in cart.items():
    sum += fruits[key] * value
print(sum)