

numbers = [1,2,3,4]
def find_average(numbers):
    if len(numbers) == 0:
        return 0
    total = sum(numbers)
    average = int(total / len(numbers))
    return average
    
