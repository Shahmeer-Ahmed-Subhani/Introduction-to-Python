
def raise_to_power(base_num, pow_num):
    result = 1
    # it will loop through the for loop as many times as the pownum. Basenum * Basenum 
    # it goes to the pow num but if it is 3, it will go to 2. 1 Less
    for index in range(pow_num):
        #The first time. Base num x 1. Result is now Base num. Second time, square. Third time, cube
        result = result * base_num
        # can also be return result
        print(result)

print(raise_to_power(3, 3))

