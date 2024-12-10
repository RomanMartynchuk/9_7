def is_prime(summ):
    def wrapper(*args):
        sum_numbers_three = summ(*args)
        result = [x for x in range(1,sum_numbers_three+1) if sum_numbers_three % x == 0]
        if len(result) == 2:
            print("Простое")
        else:
            print("Составное")
        return sum_numbers_three
    return wrapper

@is_prime
def sum_three(*args):
    sum_numbers = sum(args)
    return sum_numbers

result = sum_three(2, 3, 6)
print(result)