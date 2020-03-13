def s(a,b):
	a = bin(a)[2:]
	b = bin(b)[2:]
	c_in = 0
	value = ''
	if not len(a) == len(b):
		to_fill = abs(len(a) - len(b))
		
		if len(a) > len(b):
			b = b.zfill(len(a))
		else:
			a = a.zfill(len(b))

	for i,j in zip(reversed(a),reversed(b)):
		i_xor_j = int(i) ^ int(j)
		i_and_j = int(i) and int(j)
		s = int(c_in) ^ int(i_xor_j)
		c_in_and_i_xor_j = int(c_in) and int(i_xor_j)
		c_in = int(i_and_j) or int(c_in_and_i_xor_j)
		value += str(int(s))
	value += str(int(c_in))

	return int(value[::-1],2)
	
print(s(5,9))

