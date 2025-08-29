# 6. Calculate interest with default rate=5, time=1
interest = lambda p, r=5, t=1: (p * r * t) / 100
print("Interest:", interest(1000))
