def NULL_not_found(object: any) -> int:
	if object is None :
		print(f"Nothing: {object} {type(object)}")
	elif type(object) == int and object == 0 :
		print(f"Zero: {object} {type(object)}")
	elif type(object) == str and object == "" :
		print(f"Empty:{object} {type(object)}")
	elif type(object) == bool and object == False :
		print(f"Fake: {object} {type(object)}")
	elif type(object) == float and object != object :
		print(f"Cheese: {object} {type(object)}")
	else :
		print("Type not Found")
		return 1
	return 0
