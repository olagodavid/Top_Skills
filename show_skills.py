def show_notstudied_list():
	count = 1
	print("To Study")
	for d in notstudied_list:
		print("{0} - {1}".format(count, d))
		count += 1

def show_studied_list():
	count = 1
	print("Studied")
	for d in studied_list:
		print("{0} - {1}".format(count, d))
		count += 1
