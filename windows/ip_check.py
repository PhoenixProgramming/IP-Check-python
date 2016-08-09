__DEBUG__ = 0

print("IP Checker V1.0, Created by Jhogece")
file = open("iplist.txt","r") #readlines()
if __DEBUG__ == 1:
	print(file)
list = file.read().splitlines()
if __DEBUG__ == 1:
	print(list)
chk = str(input("Enter an IP to check: "))
print("Entered IP:")
print(chk)
print()
if __DEBUG__ == 1:
	print(chk in list)
if chk in list: #== True:
	print("Phoenix Member")
else:
	print("Enemy")
