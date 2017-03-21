import csv

csvfile = open('source.csv', 'rb') # 1
CSVlist = []
DayList = []
DayHourList=[]
Temlist = []
ResultDayList = []

for row in csv.reader(csvfile, delimiter=','): # 2
    CSVlist.append(row)
for i in range(len(CSVlist)):
    Temlist.append(CSVlist[i])
    if (int(i)+1)%4==0:
      DayList.append(Temlist)
      Temlist = []
#print 0,DayList[0]
print len(DayList)


DayIndex = 60
for DayIndex in range(61):
	DayHourList = []
	for HourIndex in range(len(DayList[0][0])):
		for i in DayList[DayIndex]:
			Temlist.append(i[HourIndex])
		DayHourList.append(Temlist)
		Temlist=[]
	Date = DayHourList[0][0]
	time = 0
	for i in range(len(DayHourList)):
   		if i <2:
			pass
   		else:
	
			Temlist.append(Date)
			Temlist.append(str(time)+":00")
			for q in DayHourList[i]:
				Temlist.append(q)
			ResultDayList.append(Temlist)   
			Temlist=[]

			#print Date 
			#print time
			#print DayHourList[i]
			time +=1
for i in ResultDayList:
	print i,"\n"
#print ResultDayList
#print len(ResultDayList)



with open("result.csv", "wb") as f:
    writer = csv.writer(f)
    writer.writerows(ResultDayList)
	

