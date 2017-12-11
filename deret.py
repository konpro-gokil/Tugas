fibs=[1,1]
num= input("Masukan jumlah deret fibonacci: ")
num= int(num)
if (num<3):
	print("Mnimal 3 deret")
else:
	for i in range (num-2):
		fibs.append (fibs[-2]+fibs [-1])
		print(fibs)