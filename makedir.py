import os
path = "D://魔界更新//backup//2019//01//"
for number1 in range(1,32):
	number = str(number1)
	if int(number) < 10:
		number = "0" + number
	new_folder_path = os.path.join(path,number)
	if not os.path.exists(new_folder_path):
		os.makedirs(new_folder_path)