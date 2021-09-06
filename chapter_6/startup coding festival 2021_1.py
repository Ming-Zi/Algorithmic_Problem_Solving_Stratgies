N = int(input())
time = [[0 for col in range(N+1)] for row in range(4)]
start = []
end = []
temp = []
maxstart = 0
minend = 99999
for i in range(N):
	temp = input()
	time[i][0] = int(temp[:2])
	time[i][1] = int(temp[3:5])
	time[i][2] = int(temp[8:10])
	time[i][3] = int(temp[11:])
	start.append(time[i][0]*60 + time[i][1])
	end.append(time[i][2]*60 + time[i][3])
	if (maxstart <= start[i]):
		maxstart = start[i]
		temp1 = i
	if (minend >= end[i]):
		minend = end[i]
		temp2 = i

if (maxstart >= minend):
	print(-1)
else:
	print("{:02d}:{:02d} ~ {:02d}:{:02d}".format(time[temp1][0],time[temp1][1],time[temp2][2],time[temp2][3]))
	
	