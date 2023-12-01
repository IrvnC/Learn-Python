def main():

	n=int(input())	
	if((n>=5) and (n<=6)) :
		benar=True
	else:
		benar=False
	print("interval 5<={}<=6 adalah {}\n".format(n,benar))

if __name__ == '__main__':
	main()