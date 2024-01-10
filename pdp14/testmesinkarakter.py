from mesinkarakter import *
from Global import *
def main():
	global CC
	print("Mulai Awal Pita...")
	CC=START()
	print("{}".format(CC),end='')
	while( not EOP()):
		CC=ADV()
		print("{}".format(CC),end='')
	print("\nAkhir Pembacaan pita..\n")
	print("\nTest fungsi-fungsi..\n")
	print('Panjang File : {}'.format(panjang()))
	print("Huruf Char not blank : {} ".format(hitungCH()))
	l,u,o=hitunghuruf()
	print("low : {}, upper : {}, other : {} ".format(l,u,o))
	print('Count A : {}'.format(hitung_a()))
	print("Vokal : {} ".format(hitungvokal()))
	print("AN : {} ".format(hitungAN()))
	print("Blank : {} ".format(hitungblank()))
	print('TA-DA!')
if __name__ == '__main__':
	main()