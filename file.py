num = open("numbers.text", 'r+')
#num.write('12343545454')
values = num.read()
print(values)
num.close()