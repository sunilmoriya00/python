nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

my_list = [n for n in nums]
print my_list

# get square value of each number from list
my_list = [n * n for n in nums]
print 'square:', my_list

# get all the even numbers from given list
my_list = [n for n in range(1, 100) if n % 2 == 0]
print 'All even number till 100:', my_list
print 'Total number of even number till 100 are:', len(my_list)

# get all the odd numbers from given list
my_list = [n for n in range(1, 100) if n % 2 != 0]
print 'Total number of odd: {} and count is: {:02}'.format(my_list, len(my_list))
