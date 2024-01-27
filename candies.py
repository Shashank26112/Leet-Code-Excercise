def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**5) + 1):
        if n % i == 0:
            return False
    return True

candies_in_stock = 100
cost_of_each_candy = 5
max_candies_chaitra_can_buy = 0

for i in range(candies_in_stock, 0, -1):
    current_cost = i * cost_of_each_candy
    if current_cost > max_candies_chaitra_can_buy:
        max_candies_chaitra_can_buy = current_cost
        if is_prime(i):
            cost_of_each_candy = 4

print("The cost of each candy is:", cost_of_each_candy)