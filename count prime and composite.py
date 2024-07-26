numbers = []
print("Enter the numbers")
while True:
    try:
        number = input()
        if number:
            numbers.append(number)
        else:
            break
    except EOFError:
        break

prime_count = 0
composite_count = 0

for number in numbers:
    num = int(number)
    if num > 1:
        is_prime = True
        if num == 2:
            is_prime = True
        elif num % 2 == 0:
            is_prime = False
        else:
            for i in range(3, int(num**0.5) + 1, 2):
                if num % i == 0:
                    is_prime = False
                    break
        if is_prime:
            prime_count += 1
        else:
            composite_count += 1

print(f"Composite number:{composite_count} Prime number:{prime_count}")
