given_series = #random series 

def maybe_fib(series):
	#solve the fib
	throw error if wrong



def rule_add_iterating_numbers(series):
	diff_between_first_set = sub_numbers(get_first_n_number(series,2)[::-1])


def get_first_n_number(series, n, reversed=0):
	if reversed == 0:
		return series[0:n]
	return series[0:n][::-1]

def sum_numbers(list_of_num_to_sum):
	x = list_of_num_to_sum.pop(0)
	for each in list_of_num_to_sum:
		x += each
	return x
	
def sub_numbers(list_of_num_to_sum):
	x = list_of_num_to_sum.pop(0)
	for each in list_of_num_to_sum:
		x -= each
	return x
.
.
.
.
.


list_of_possible_match = [maybe_fib, add_iterating_numbers, . . . ,  #list like fib, adding prime, taking the first 3 numbers and doing somethign with it]

for each_method in list_of_possible_match:
	try:
		each_method(given_series)
	catch error:
		print("didn't work out try another one")

if all_fail:
	#teach me new function/method?
