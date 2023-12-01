def main():
	
	n=int(input())	
	if((n>2) and (n<=5) or (n>=15) and (n<27)) :
		benar=True
	else:
		benar=False
	print("interval 2<{}<=5 atau 15>={}>27 adalah {}\n".format(n,n,benar))
if __name__ == '__main__':
	main()