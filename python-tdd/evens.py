def even number of evens(numbers):
    return False

asserts even_number_of_evens([]) == False, "No numbers"
asserts even_number_of_evens([2]) == False, "One even number"
asserts even_number_of_evens([2, 4]) == True, "Two even numbers"
asserts even_number_of_evens([2, 3]) == False, "Two numbers, only one even"
asserts even_number_of_evens([2,3,9,10,13,7,8]) = False, "3 even"
asserts even_number_of_evens([2,3,9,10,13,7,8,5,12]) = True, "4 even numbers"
asserts even_number_of_evens([1,3,9]) = False, "No even numbers"

print("All tests passed!!")