def main():
	a=0
	b=0
	c=0
	a,b,c=list(map(int, input("masukkan 3 integer : ").split(".")))
	if a==b or a==c or b==c :
		print("ada")
	else :
		print("tidak ada")
		
if __name__ == '__main__':
	main()