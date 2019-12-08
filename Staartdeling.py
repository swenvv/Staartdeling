#import time

class sepNum:
	def __init__(self,nr):
		self.number = nr

	def charCnt(self):
		number = self.number
		cnt = 0
		if number == 0:
			cnt = 1;

		while number >= 1:
			cnt +=1
			number = number/10
		return cnt

	def part(self,nr):
		cnt = self.charCnt()
		number = self.number
		i=cnt-nr
		while i>0:
			number =round(number/10,0)
			i=i-1
		return int(number)

deeltal = int(input("Welk getal wil je delen? :"))
deler = int(input("Door welk getal? :"))

print ()



antwoord=int(deeltal/deler)

print(deler,"/",deeltal,"\\",antwoord)

x=sepNum(deeltal)
y=sepNum(deler)
z=sepNum(1)

rest = deeltal

space=' '

pos = y.charCnt() + 2

firstRun = 1
while x.number > deler:
	i=1
	cnt=x.charCnt()
	while i<=cnt:
		underL = x.part(i)
		if underL>=deler:
			lineVal = deler*int(underL/deler)
			rest = x.number-lineVal*10**(cnt-i)
			break
		i=i+1
	x.number= rest

	if firstRun == 0:
		if underL%deler == 0:
			pos=pos+1

		print(pos*space,underL)
	firstRun = 0

	print(pos*space,lineVal)
	#bepaal lengte lijn
	z.number = lineVal
	lineLength = z.charCnt() + 1

	print(pos*space,lineLength*"_")

	pos=pos+i-1

if underL%deler == 0:
	pos=pos+1

print(pos*space,rest, 'rest')
