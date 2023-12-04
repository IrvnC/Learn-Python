def main():
	a=int(input("masukkan jumlah boneka : "))
	if a>50:
		harga=10
	elif a>=11:
		harga=20
	elif a>=2 :
		harga=25
	elif a==1:
		harga=30
	else :
		print("error,tidak boleh<=0 ")
		harga=0
	total=harga*a
	print(total)
	
 

if __name__ == '__main__':
	main()