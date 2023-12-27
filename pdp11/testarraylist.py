from arraylist import*
data1=[2,42,32,12,22,39,15,8,4,20]
data2=[3.45,2.33,1.49,4.00,3.86,3.92,3.21,2.89,2.45,2.68]
data3=['A','G','U','S','-','W','A','H','Y','U']

def main():
	print("data1: ",end='');tulistabeldata(data1)
	print("data2: ",end='');tulistabeldata(data2)
	print("data3: ",end='');tulistabeldata(data3)
	print("Cari 22 : {}".format(carielm(data1,22)))
	print("Cari idx 22 : {}".format(cariidxdata(data1,22)))
	print("Cari Bool 22 : {}".format(caribol(data1,22)))
	print("Cari 3.86 : {}".format(carielm(data2,3.86)))
	print("Cari idx 3.86 : {}".format(cariidxdata(data2,3.86)))
	print("Cari Bool 3.86: {}".format(caribol(data2,3.86)))
	print("Cari 'W' : {}".format(carielm(data3,'W')))
	print("Cari idx 'W' : {}".format(cariidxdata(data3,'W')))
	print("Cari Bool 'W' : {}".format(caribol(data3,'W')))
	print("Ta da  berhasil!!")
if __name__ == '__main__':
	main()