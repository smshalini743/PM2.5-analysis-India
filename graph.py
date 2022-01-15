import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

filename1 = "./files/sheet1.csv"
filename2 = "./files/sheet2.csv"
filename3 = "./files/sheet3.csv"
filename4 = "./files/sheet4.csv"

df1 = pd.read_csv(filename1)
df2 = pd.read_csv(filename2)
df3 = pd.read_csv(filename3)
df4 = pd.read_csv(filename4)

# morning_1_1 = []
# morning_1_2 = []
# day_1_1 = []
# day_1_2 = []
# night_1_1 = []
# night_1_2 = []

# morning_2_1 = []
# morning_2_2 = []
# day_2_1 = []
# day_2_2 = []
# night_2_1 = []
# night_2_2 = []

# morning_3_1 = []
# morning_3_2 = []
# day_3_1 = []
# day_3_2 = []
# night_3_1 = []
# night_3_2 = []

# morning_4_1 = []
# morning_4_2 = []
# day_4_1 = []
# day_4_2 = []
# night_4_1 = []
# night_4_2 = []

list1 = []
list2 = []

length1 = df1.shape[0]
length2 = df2.shape[0]
length3 = df3.shape[0]
length4 = df4.shape[0]

dictionary = {}

for k in range(3):
	list1 = []
	list2 = []
	colname1 = ""
	colname2 = ""
	for i in range(length1):
		dat = str(df1.iat[i, 0])
		point1 = dat.find(" ")
		point2 = dat.find(":")
		num = int(dat[point1+1:point2])

		if k == 0:
			colname1 = "Morning_1_1"
			colname2 = "Morning_1_2"
			if num >= 5 and num <= 9:
				list1.append(df1.iat[i, 1])
				list2.append(df1.iat[i, 2])

		if k == 1:
			colname1 = "Day_1_1"
			colname2 = "Day_1_2"
			if num >=10 and num <= 19:
				list1.append(df1.iat[i, 1])
				list2.append(df1.iat[i, 2])

		if k == 2:
			colname1 = "Night_1_1"
			colname2 = "Night_1_2"
			if num >= 20 and num <= 23:
				list1.append(df1.iat[i, 1])
				list2.append(df1.iat[i, 2])

			if num >= 0 and num <= 4:
				list1.append(df1.iat[i, 1])
				list2.append(df1.iat[i, 2])

	dictionary[colname1] = list1
	dictionary[colname2] = list2

for k in range(3):
	list1 = []
	list2 = []
	colname1 = ""
	colname2 = ""
	for i in range(length2):
		dat = str(df2.iat[i, 0])
		point1 = dat.find(" ")
		point2 = dat.find(":")
		num = int(dat[point1+1:point2])

		if k == 0:
			colname1 = "Morning_2_1"
			colname2 = "Morning_2_2"
			if num >= 5 and num <= 9:
				list1.append(df2.iat[i, 1])
				list2.append(df2.iat[i, 2])

		if k == 1:
			colname1 = "Day_2_1"
			colname2 = "Day_2_2"
			if num >=10 and num <= 19:
				list1.append(df2.iat[i, 1])
				list2.append(df2.iat[i, 2])

		if k == 2:
			colname1 = "Night_2_1"
			colname2 = "Night_2_2"
			if num >= 20 and num <= 23:
				list1.append(df2.iat[i, 1])
				list2.append(df2.iat[i, 2])

			if num >= 0 and num <= 4:
				list1.append(df2.iat[i, 1])
				list2.append(df2.iat[i, 2])

	dictionary[colname1] = list1
	dictionary[colname2] = list2

for k in range(3):
	list1 = []
	list2 = []
	colname1 = ""
	colname2 = ""
	for i in range(length3):
		dat = str(df3.iat[i, 0])
		point1 = dat.find(" ")
		point2 = dat.find(":")
		num = int(dat[point1+1:point2])

		if k == 0:
			colname1 = "Morning_3_1"
			colname2 = "Morning_3_2"
			if num >= 5 and num <= 9:
				list1.append(df3.iat[i, 1])
				list2.append(df3.iat[i, 2])

		if k == 1:
			colname1 = "Day_1_1"
			colname2 = "Day_1_2"
			if num >=10 and num <= 19:
				list1.append(df3.iat[i, 1])
				list2.append(df3.iat[i, 2])

		if k == 2:
			colname1 = "Night_1_1"
			colname2 = "Night_1_2"
			if num >= 20 and num <= 23:
				list1.append(df3.iat[i, 1])
				list2.append(df3.iat[i, 2])

			if num >= 0 and num <= 4:
				list1.append(df3.iat[i, 1])
				list2.append(df3.iat[i, 2])

	dictionary[colname1] = list1
	dictionary[colname2] = list2


for k in range(3):
	list1 = []
	list2 = []
	colname1 = ""
	colname2 = ""
	for i in range(length4):
		dat = str(df4.iat[i, 0])
		point1 = dat.find(" ")
		point2 = dat.find(":")
		num = int(dat[point1+1:point2])

		if k == 0:
			colname1 = "Morning_4_1"
			colname2 = "Morning_4_2"
			if num >= 5 and num <= 9:
				list1.append(df4.iat[i, 1])
				list2.append(df4.iat[i, 2])

		if k == 1:
			colname1 = "Day_4_1"
			colname2 = "Day_4_2"
			if num >=10 and num <= 19:
				list1.append(df4.iat[i, 1])
				list2.append(df4.iat[i, 2])

		if k == 2:
			colname1 = "Night_4_1"
			colname2 = "Night_4_2"
			if num >= 20 and num <= 23:
				list1.append(df4.iat[i, 1])
				list2.append(df4.iat[i, 2])

			if num >= 0 and num <= 4:
				list1.append(df4.iat[i, 1])
				list2.append(df4.iat[i, 2])

	dictionary[colname1] = list1
	dictionary[colname2] = list2


ke = list(dictionary)
print(ke)

for i in range(int(len(ke)/2)):
	x = np.array(dictionary[ke[2*i]])
	y = np.array(dictionary[ke[2*i + 1]])

	plt.scatter(x, y)
plt.show()