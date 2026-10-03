orders = [1200, 800, 1500, 2300, 700]

revenue = sum(orders)
average_order = revenue / len(orders)

print(f"Total revenue: {revenue}")
print(f"Average order: {average_order}")
print(f'Len orders: {len(orders)}')
# 2 и 3 коммит одинаковы, я просто выведу привет
print("Hello, world!")

max_order = max(orders)
min_order = min(orders)

print(f"Maximum order: {max_order}")
print(f"Minimum order: {min_order}")
