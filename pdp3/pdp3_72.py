def main():
	
	n=int(input())	
	if((n>=5) and (n<=6) or (n>=10)) :
		benar=True
	else:
		benar=False
	print("interval n>=5{}<=6 atau {}>=10 adalah {}\n".format(n,n,benar))

if __name__ == '__main__':
	main()