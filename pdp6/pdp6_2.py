import random
def main():
	y=0
	while True:
		x=random.randint(1,50)
		y=0
		while True:
			y+=1
			n=int(input("Tebakan ke {} , masukkan angka tebakan ? :".format(y)))
			if n>x:
				print("Angka anda lebih besar")
			elif n<x:
				print("Angka anda lebih kecil")
			elif n==x:
				print("Hebat angka {} berhasil anda tebak dalam {} kali".format(x,y))
				break
			if y==5:
				print("Anda tidak berhasil menebak, angka ajaib = {}".format(x))
				break
		nn=input("Apakah anda akan bermain lagi [Yy/Tt] : ").upper()
		if nn=="T":
			print("Selamat tinggal")
			break
		print("\n")


if __name__== '__main__':
	main()