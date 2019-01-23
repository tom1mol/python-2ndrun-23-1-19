def count_upper_case(message):
    count = 0                           
    for c in message:                   #walks through the message
        if c.isupper():                  #if character is upper case
            count += 1                  #increment counter
    return count                        #total count is returned
    
assert count_upper_case("") == 0, "Empty string"        #print(count_upper_case("Hello World"))  gives ans 2(H+W)
assert count_upper_case("A") == 1, "One upper case"
assert count_upper_case("a") == 0, "One lower case"
assert count_upper_case("$%^&") == 0, "Special characters"

print ("All tests passed")


#(from assertions video)
# x = 3
# y = 2

# assert x < y, "{0} should be less than {1}".format(x, y)

# print(x + y)
