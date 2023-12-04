def main():
	sumData=0
	lenData=0
	for x in range(1,21):
		print(x)
		sumData+=x
		lenData+=1
	print("Jumlah : {}".format(sumData))
	print("Jumlah : {}".format(lenData))
	print("Rerata : {}".format(sumData/lenData))
if __name__ == '__main__':
	main()