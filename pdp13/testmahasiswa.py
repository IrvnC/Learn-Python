from mahasiswa import * 
 
def main():
	s1=mahasiswa()
	s2=mahasiswa('A11.1234','Budi','3.57')
	data=list()
	data.append(mahasiswa('A11.1235','Budi','3.57'))
	data.append(mahasiswa('A11.1111','Bagus','3.17'))
	data.append(mahasiswa('A11.1212','Alan','2.99'))
	tulisdata(s1)
	tulisdata(s2)
	print(getnim(s2))
	print(getnama(s2))
	print(getipk(s2))
	setnim(s2,'A11.9999')
	setnama(s2,'Agus Bijaksana')
	setipk(s2,'3.98')
	tulisdata(s2)
	tulisdata(data[0])
	# found=(m for m in data if m.nim=='A11-1111')
	tulisdata(searching1(data,'A11.1111'))
	tulisdata(searching1(data,'A11.111B'))
	print("index:{}".format(searching2(data,'A11.1111')))
	print("index:{}".format(searching2(data,'A11.111B')))
	sorting(data,0)
	printlist(data)
	print("Ta da ! ")
	
if __name__ == '__main__':
	main() 