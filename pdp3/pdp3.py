from sys import argv
def main():
	data=list(map(int, argv[1].split(',')))
	print(min(data))
	print(max(data))
	print(sum(data)/len(data))
	print(len(data))

	

if __name__ == '__main__':
	main()