#recursive function
#def factorial(n):
#	if n==1:
#		return 1
#	else:
#		return n* factorial(n-1)
		
#f=factorial(4)
#print(f)

fibonacci
list=[]
masukan=int(input("Masukan banyak bilanngan fibonacci: "))
n=range(1,masukan+1)

for index, data in enumerate(n):
	if data==1:
		list.append(data)
		list.append(data)
	else:
		hasil= list[index-1]+list[index]
		list.append(hasil)
print(list)

#fibonacci recursive
#list=[]
#masukan=int(input("Masukan banyak bilangan fibonacci: "))
#n=1,masukan
#def fibonacci(n):
#	if n==1:
#		list.append(n)
#		return n
#	else:
#		return n + fibonacci(n-1)
		
#f=fibonacci(3)
#print(n)