def main():
	
	n=int(input())	
	if((n<5) or (n>17)) :
		benar=True
	else:
		benar=False
	print("interval 5<{} atau 17>{} adalah {}\n".format(n,n,benar))
if __name__ == '__main__':
	main()