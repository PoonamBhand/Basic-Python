# 9. Discount price with default discount=10%
discount = lambda price, disc=10: price - (price * disc / 100)
print("Final Price:", discount(1000))
