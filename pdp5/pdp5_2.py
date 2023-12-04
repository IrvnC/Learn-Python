def main():
	i=0
	for i in range(100,0,-2):
		if i>0 and i%2==0:
			print (i)
			continue
		else :
			break

if __name__ == '__main__':
	main()