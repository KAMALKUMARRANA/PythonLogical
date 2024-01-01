def check_vowel(str):
	str=str.lower()
	char=set("aeiou")
	for i in str:
		if i in char:
			char.remove(i)
	if len(char)==0:
		print("Accepted")
	else:
		print("Not")
			


n=input("Enter the string: ")
check_vowel(n)