def main():
	n=int(input("jumlah analisis"))
	y=0
	for i in range(1,n+1):
		lagi=0
		print("{} + {} = ? ".format(i,i), end='')
		jawab=int(input())
		if jawab==i+i:
			print("benar")
		else:
			print("salah")
			print("coba lagi")
			y+=1
			benar=False
			while lagi in range (1,4) and benar:
				print("{} + {} = ? ".format(i,i))
				jawab=int(input())
				if jawab == i+i:
					print("Benar!")
					benar=True
			lagi+=1

			if not benar:
				print("Jawabannya adalah {}".format(i+i))
				
	print("analisa , jumlah analisa {} , analisa benar {} , analisa salah{}".format(n,n-y,y))

if __name__== '__main__':
	main()