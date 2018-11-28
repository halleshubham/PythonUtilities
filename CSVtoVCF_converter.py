import sys

fileName= sys.argv[1]
vcfFile = open(fileName + ".vcf", "w")
try:
	prefix = sys.argv[2]
except Exception as e:
	prefix = "AbhivyaktiOnline"

def addContact(contactSting):
	contactA = contactSting.split(',')
	if(contactA[1] == ""):
		return
	
	contact = ''
	
	for index in range(len(contactA)):
		a = contactA[index]
		
		if(index == 0):
			name = "FN:" + prefix + " " + contactA[index]
			vcfFile.write("BEGIN:VCARD\nVERSION:2.1\n" + name)
		else:	
			try :
				a = int(a)
			except:
				print("#" + a + "#")
				break 	

			contact = "\nTEL;CELL:" + str(a)
			vcfFile.write(contact)
	
	vcfFile.write("\nEND:VCARD\n")				

with open(sys.argv[1]) as lsyFileObject:
	temp=0
	count=0
	for line in lsyFileObject:
		addContact(line)
		count=count+1
		if(count==100):
			count=0
			temp=temp+1
			print(temp)
			vcfFile.close()
			vcfFile = open(fileName+"_"+ str(temp) + ".vcf", "w")

	
