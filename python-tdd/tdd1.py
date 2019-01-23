def even_number_of_evens(numbers):
    if numbers == []:
        return False
    else:           #initialise variable to say currently evens = 0
        evens = 0
        
    for n in numbers:
        if n % 2 == 0:
            evens += 1
            
    if evens == 0:
        return False
    else:        
        return evens %2 == 0        #rtn true if number of evens is even. false if not


assert even_number_of_evens([]) == False, "No numbers"
assert even_number_of_evens([2]) == False, "One even number"
assert even_number_of_evens([2, 4]) == True, "Two even numbers"
assert even_number_of_evens([2, 3]) == False, "Two numbers, only one even"
assert even_number_of_evens([2,3,9,10,13,7,8]) == False, "3 even"
assert even_number_of_evens([2,3,9,10,13,7,8,5,12]) == True, "4 even numbers"
assert even_number_of_evens([1,3,9]) == False, "No even numbers"

print("All tests passed!!")