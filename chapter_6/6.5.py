#BOARDCOVER
def setGame():
    global setting_1
    global setting_2
    global setting_3
    setting_1 = [
        [1,0,0,0,0,0,1],
        [1,0,0,0,0,0,1],
        [1,1,0,0,0,1,1]
    ]

    setting_2 = [
        [1,0,0,0,0,0,1],
        [1,0,0,0,0,0,1],
        [1,1,0,0,1,1,1]
    ]

    setting_3 = [
        [1,1,1,1,1,1,1,1,1,1],
        [1,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,1],
        [1,1,1,1,1,1,1,1,1,1]
    ]

basicShape = [
[[1,1],
[1,0]],
[[1,1],
[0,1]],
[[1,0],
[1,1]],
[[0,1],
[1,1]]]


def game(setting):
    sum = 0
    row = len(setting)
    col = len(setting[0])
    for i in range(0,row):
        for j in range(0,col):
            sum = sum + setting[i][j]
    if (sum%3 != 0):
        return False
    for i in range(0, row-1):
        for j in range(0, col-1):
            if (setting[i][j] == 1):
                setting[i][j] = setting[i][j] + basicShape[3]
                if (setting[i][j+1])


set()
game(setting_1)
set()
game(setting_2)
set()
game(setting_3)
