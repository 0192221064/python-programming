def calculate_bread_cost(fresh_loaves, day_old_loaves):
    regular_price = 185
    discount_rate = 0.60
    
    if fresh_loaves < 0:
        return "Number of fresh loaves cannot be negative."
    if day_old_loaves < 0:
        return "Number of day old loaves cannot be negative."
    
    fresh_loaves_cost = fresh_loaves * regular_price
    day_old_loaves_cost = day_old_loaves * regular_price * (1 - discount_rate)
    
    total_cost = fresh_loaves_cost + day_old_loaves_cost
    
    return (
        f"Regular price: Rs.{regular_price:.2f}\n"
        f"Amount of new loaves: Rs.{fresh_loaves_cost:.2f}\n"
        f"Amount of day old loaves: Rs.{day_old_loaves_cost:.2f}\n"
        f"Total amount: Rs.{total_cost:.2f}"
    )

# Test cases
print(calculate_bread_cost(5, 3))
print(calculate_bread_cost(4, 6))
print(calculate_bread_cost(-1, 5))
print(calculate_bread_cost(0, 6))
print(calculate_bread_cost(7, 8))
