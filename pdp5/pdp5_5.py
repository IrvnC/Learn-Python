def main():
	n=0
	while True:
		n=input("masukkan nilai : ")
		if n =='-99':
			print ("selesai anda, code: {}".format(n))
			break
		else:
			print(n)
if __name__ == '__main__':
	main()