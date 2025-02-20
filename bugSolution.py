def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list to prevent ZeroDivisionError
    return sum(numbers) / len(numbers)

my_numbers = [10, 20, 30, 40, 50]
average = calculate_average(my_numbers)
print(f"The average is: {average}")

my_empty_list = []
average_empty = calculate_average(my_empty_list)
print(f"The average of an empty list is: {average_empty}")

#Additional handling for non-numeric input
def calculate_average_robust(numbers):
    numeric_numbers = [num for num in numbers if isinstance(num, (int, float))]
    if not numeric_numbers:
        return 0
    return sum(numeric_numbers) / len(numeric_numbers)

my_mixed_list = [10, 20, 'a', 30, 40, 50]
average_mixed = calculate_average_robust(my_mixed_list) 
print(f"The average of a mixed list is: {average_mixed}") 