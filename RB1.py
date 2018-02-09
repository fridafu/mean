msg = "\nU cannot do it with the zero under there!!!"

def mean(num_list):
	if len(num_list)== 0:
		raise Exception(msg)
	else:
		return sum(num_list)/len(num_list) +1


def mean2(num_list):
	try:
		return sum(num_list)/len(num_list)
	except ZeroDivisionError as detail:
		raise ZeroDivisionError(detail.__str__() + msg)
	except TypeError as detail:
		msg2 = "\n use numbers "
		raise TypeError(detail.__str__() + msg2)
