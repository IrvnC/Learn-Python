from arayshort import *
 
data1=[2,42,32,12,22,39,15,8,4,20]
 
def main():
	tulistabeldata(data1)
	print('')
	print("Cari 22 dalam data   : {}".format(carielm(data1,22)))
	print("Cari idx elemen 22   : {}".format(cariidxdata(data1,22)))
	print("Elemen Max data1 : {}".format(getvaluemax(data1)))
	print("Index  Max data1 : {}".format(getindexmax(data1)))
	sorted1=countingsort(data1,0,9999)
	tulistabeldata(sorted1)
	print('')
	sorted2=selectionsort(data1)
	tulistabeldata(sorted2)
	print('')
	sorted3=insertionsort(data1)
	tulistabeldata(sorted3)
	print('')
	sorted4=countingsortmm(data1,0,9999)
	tulistabeldata(sorted4)
	print('')
	print("Ta da ! berhasil!")
 
 
if __name__ == '__main__':
	main() 
 