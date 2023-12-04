def main():
	
	print("konversi nilai")
	nilai=int(input("masukkan nilai angka (bilangan bulat) : "))
	
	if nilai>80:
		nilaihuruf= 'A'
	elif nilai >=61 and nilai <=80:
		nilaihuruf= 'B'
	elif nilai >=41 and nilai <=60:
		nilaihuruf= 'C'
	elif nilai >=21 and nilai <=40:
		nilaihuruf= 'D'
	elif nilai >=0 and nilai <= 20:
		nilaihuruf= 'E'
	else:
		print("nilai tidak valid")

	print("Nilai Angka : {}, Nilai Huruf : {}".format(nilai,nilaihuruf))
if __name__ == '__main__':
	main()