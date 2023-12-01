def main():
	
	n=int(input())	
	if((n>3) and (n<=15)) :
		benar=True
	else:
		benar=False
	print("interval 3<{}<=15 adalah {}\n".format(n,benar))

if __name__ == '__main__':
	main()