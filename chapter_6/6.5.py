#BOARDCOVER

basicShape = [
[[1,1],
[1,0]],
[[1,1],
[0,1]],
[[1,0],
[1,1]],
[[0,1],
[1,1]]]

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

# fill the shape
def shapePlus(setting, i, j, index, select):
    if (select == 3):
        j=j-1
    setting[i][j]+=basicShape[select][0][0]
    setting[i][j+1]+=basicShape[select][0][1]
    setting[i+1][j]+=basicShape[select][1][0]
    setting[i+1][j+1]+=basicShape[select][1][1]
    if (setting[i+1][j] == 2 or setting[i][j+1] == 2 or setting[i+1][j+1] == 2):
        setting[i][j]-=basicShape[select][0][0]
        setting[i][j+1]-=basicShape[select][0][1]
        setting[i+1][j]-=basicShape[select][1][0]
        setting[i+1][j+1]-=basicShape[select][1][1]
        return False
    return True

def game(gamenum, setting, way):
    row = len(setting)
    col = len(setting[0])
    sum = row * col
    rsum = 0
    
    # divide with 3 => check
    for i in range(0,row):
        for j in range(0,col):
            sum = sum - setting[i][j]
    if (sum%3 != 0):
        return 0
    
    # fill the shape
    for i in range(0, row-1):
        for j in range(0, col-1):
            if (setting[i][j] == 0):
                for k in range(0,4):
                    shapePlus(setting, i, j, gamenum, k)
    
    # shape complete => return way
    for i in range(0,row):
        for j in range(0,col):
            rsum = rsum + setting[i][j]
    if (rsum == (row * col)):
        way = way + 1
    else:
        while True:
            if ():
                break
            else:
                game(gamenum, setting, way)
            break
        return way

setGame()
print(game(1, setting_1, 0))

setGame()
print(game(2, setting_2, 0))

setGame()
print(game(3, setting_3, 0))
