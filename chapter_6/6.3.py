boggle = [['U','R','L','P','M'],['X','P','R','E','T'],['G','I','A','E','T'],['X','T','N','Z','Y'],['X','O','Q','R','S']]
dx = [-1,-1,-1,1,1,1,0,0,0]
dy = [-1,0,1,-1,0,1,-1,0,1]

def hasWord(y, x, strWord):
	word = list(strWord)
	if (y<0|y>=5|x<0|x>=5):
		return False
	elif (word[0] != boggle[y][x]):
		return False
	elif (len(word) == 1):
		return True
	else:
		for temp in range(0,7) :
			nextY = y + dy[temp]
			nextX = dx[temp]
			if(hasWord(nextY, nextX, word[-1])):
				print ("win")
				return True
	return False

hasWord(2,1,"IP")