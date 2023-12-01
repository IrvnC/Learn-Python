def main():
	
	n=int(input())	
	if((n<8) or (n>9) and (n<=15) or (n<=21) and (n>33)):
		benar=True
	else:
		benar=False
	print("interval {}<8 atau interval 9<{}<=15 atau interval 21<={}<33adalah {}\n".format(n,n,n,benar))
if __name__ == '__main__':
	main()