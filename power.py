def power_of_two(x):
    # for example, 1 is a power of 2 since 2^0 = 1 and 0 is not a power of 2.
    #si x 
    return x != 0 & ((x &(x-1)) == 0)

print("test")
print("test2")


assert power_of_two(0) == False
assert power_of_two(1) == True
assert power_of_two(2) == True
assert power_of_two(5) == False
assert power_of_two(6) == False
assert power_of_two(4096) == True