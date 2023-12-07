def main():

	f=0
	text=""
	print("C--->F")
	for x in range (-40,101):
		f=(x*(9/5))+32
		if x>=100:
			text="Air mendidih"
		elif x>=40:
			text="Air mandi panas"
		elif x>=37:
			text="Temperatur tubuh"
		elif x>=30:
			text="Cuaca pantai"
		elif x>=21:
			text="Temperatur ruangan"
		elif x>=10:
			text="Hari yang dingin"
		elif x>=0:
			text="Titik beku air"
		elif x>=-18:
			text="Cuaca dingin bersalju"
		elif x>=-40:
			text="Cuaca sangat dingin bersalju"
		print("{:.0f} ---> {:.2f} {}".format(x,f,text))
		text=""


if __name__ == '__main__':
	main()