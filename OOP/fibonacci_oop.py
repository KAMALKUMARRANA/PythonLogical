class Fibonacci:
	def __init__(self,n):
		self.n=n
		f=0
		s=1
		i=0
		print(f"fibo upto {n}: ")
		if f==1:
			print(f)
		else:
			for i in range(1,n+1):
				print(f,end=" ")
				sum=f+s
				f=s
				s=sum
				
		
	
		
		
		
fibo1=Fibonacci(100)

