def main():
	
	n=int(input())	
	if((n>=3) and (n<=19) or (n>22) and (n<32)) :
		benar=True
	else:
		benar=False
	print("interval 3<={}<=19 atau 22>{}>32 adalah {}\n".format(n,n,benar))
if __name__ == '__main__':
	main()