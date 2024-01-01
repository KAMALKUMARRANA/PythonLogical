class prime:
	def cal(self,n1,n2):
		self.n1=n1
		self.n2=n2
		for i in range(n1,n2+1):
			if i>1:
				for j in range(2,int(i/2)+1):
					if i%j==0:
						break
				else:
					print(i)
					
		
					


p1=prime()
p1.cal(1,20)