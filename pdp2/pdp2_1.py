def main():
	#Number 1
	#multiple input
	print("mol,suhu,tekanan :", end="")
	# #end biar ga ada enternya
	mol,suhu,tekanan = [int(a) for a in input().split()]
	gas_ideal=8.314
	V=mol*gas_ideal*suhu/tekanan
	print("Vol gas : {}".format(V))

	#Vol gas : 12.471000
	# print("P=()")

	#Number 2
	print("Arus Listrik,Hambatan Listrik :", end="")
	I,R = [int(x) for x in input().split()]
	V=I*R
	print("Tegangan : {}".format(V))

	#Number3
	print("sisi sejajar,tinggi trapesium a b h :", end="")
	a,b,h = [int(a) for a in input().split()]
	L=1/2*h*(a+b)
	print("Luas Trapesium : {}".format(L))
  

if __name__ == "__main__":
    main()