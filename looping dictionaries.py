phone_numbers = {"John Smith": "+37682929928", "Marry Simpons": "+423998200919"}
for pair in phone_numbers.items():
    print("{} has a phone number {}".format(pair[0],format(pair[1])))