def main():
	i=0
	j=0
	for i,j in zip(range(1,101,1),range(100,0,-1)):
		print("i - " + str(i) + " dan j - " +str(j))

if __name__ == '__main__':
	main()