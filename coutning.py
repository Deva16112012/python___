x=input("Enter string:")
wordcount=1
charectercount=0
for i in x:
	charectercount=charectercount+1
	if (i== ' '):
		wordcount=wordcount+1

print("Charecter count is")
print(charectercount)
print("Word count is")
print(wordcount)