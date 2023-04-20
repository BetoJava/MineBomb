from random import randint

def map_alea(x, y):
    Map = []
    for i in range(y):
        Map.append([])
        for j in range(x):
            num = randint(0,6)
            if num in [4,5,6]:
                num = 0
            chance = randint(1,100)
            if chance == 100:
                num = 7
            chance = randint(1,1000)
            if chance == 1564:
                num = 8
            elif chance == 1658:
                num = 9
            elif chance == 7777:
                num = 10
            elif chance == 9852:
                num = 11
                
            Map[i].append(num)
    Map[0][0] = 0
    return Map

def up(pos, Map):
    x = pos[0]
    y = pos[1]
    if y != 0:
        if Map[y-1][x] in [-1,-2,-3,-4,0,3,7,8,9,10,11]:
            pos[1] -= 1
    return pos
    
def down(pos, Map):
    x = pos[0]
    y = pos[1]
    if y != len(Map)-1:
        if Map[y+1][x] in [-1,-2,-3,-4,0,3,7,8,9,10,11]:
            pos[1] += 1
    return pos

def right(pos, Map):
    x = pos[0]
    y = pos[1]
    if x != len(Map[0])-1:
        if Map[y][x+1] in [-1,-2,-3,-4,0,3,7,8,9,10,11]:
            pos[0] += 1
    return pos
        
def left(pos, Map):
    x = pos[0]
    y = pos[1]
    if  x != 0:
        if Map[y][x-1] in [-1,-2,-3,-4,0,3,7,8,9,10,11]:
            pos[0] -= 1
    return pos

def chance(b_max, val_vic, val_def):
    chance = randint(1,b_max)
    if chance == b_max//2:
        return val_vic
    else:
        return val_def
        
def destroyed_block():
    '''When a block is destroyed, this return a number corresponding to 
    a coin, a music coin, a relic, or nothing'''
    ale = randint(1,3)
    if ale == 1:
        num = chance(2, 1, 0)
        if num == 1:
            num = randint(8,11)
    elif ale == 2:
        num = chance(5, 7, 0)
    else:
        num = 3
    return num

def destroy(pos, Map):
    '''Destroy blocks following the hero'''
    x = pos[0]
    y = pos[1]
    if x != 0:
        if Map[y][x-1] == 2:
            num = destroyed_block()
            Map[y][x-1] = num
            
    if x != len(Map[0])-1:
        if Map[y][x+1] == 2:
            num = destroyed_block()
            Map[y][x+1] = num
            
    if y != len(Map)-1:
        if Map[y+1][x] == 2:
            num = destroyed_block()
            Map[y+1][x] = num
            
    if y != 0: 
        if Map[y-1][x] == 2:
            num = destroyed_block()
            Map[y-1][x] = num
    return Map
          
def destroy_all(score, Map):
    '''Destroy all blocks on the Map'''
    for i in range(len(Map)-1):
        for j in range(len(Map[i])-1):
            if Map[i][j] == 2:
                num = destroyed_block()
                Map[i][j] = num
                score[3] += 1
    return Map, score



print(' -  M  i  n  e  B  o  m  b  - ')

choice = '4'
while choice not in ['1', '2', '3']:
    choice = str(input('New Game / Continue / Scores (1/2/3) : '))
    
if choice == '2':
    name = []
    inventory = []
    score = []
    pos = []
    Map = []
    
    f = open('data/game.txt','r', encoding='utf-8')
    a = f.readline()
    name.append(a[:-1])
    for i in range(3):
        a = f.readline()
        inventory.append(int(a[:-1]))
    for i in [3,4,5,6,7]:
        a = f.readline()
        inventory.append(a[:-1])
    for i in range(5):
        a = f.readline()
        score.append(int(a[:-1]))
    for i in range(2):
        a = f.readline()
        pos.append(int(a[:-1]))
    f.close()
    
    f = open('data/map.txt','r', encoding='utf-8')
    y = f.readline()
    x = f.readline()
    for i in range(int(y[:-1])):
        Map.append([])
        for j in range(int(x[:-1])):            
            a = f.readline()
            Map[i].append(int(a[:-1]))
    f.close()
    
elif choice == '1':
    name = ['']
    name[0] = str(input('Your name : '))
    x,y = randint(5,30), randint(5,30)
    Map = map_alea(x,y) 
    pos = [0,0] # X,Y
    inventory = [0, 0, 0, ' ☺ ', ' ', ' ', ' ', ' ']   # coins, bombs, Megabombs, skin, '♣', '♦', '♥', '♠'
    score = [0,0,0,0,1]  

if choice in ['1', '2']:    
    print('Rules :')
    print("  - tap 'z','s','q','d' to move")
    print("  - tap 'next' to change the Map")
    print("  - tap 'shop' to go to the shop")
    print("  - tap the 'space bar' to use bombs")
    print("  - tap the 'b' to use Megabombs")
    print("  - collect the fourth : '♣' '♦' '♥' '♠' to access to")
    print("    the final Map by tapping 'final'")
    print("  - tap 'end' to quit and save")
    print('')
    shop = False
    end = True

if choice == '3':
        end = False
        f = open('data/score.txt','r', encoding='utf-8')
        print(f.read())
        f.close()
        save = False

while end :

    if Map[pos[1]][pos[0]] == 3:
        inventory[0] += 1
        score[0] += 1
        Map[pos[1]][pos[0]] = 0
        
    elif Map[pos[1]][pos[0]] == 7:
        inventory[0] += 25
        score[0] += 25
        Map[pos[1]][pos[0]] = 0
        
    elif Map[pos[1]][pos[0]] == 8:
        inventory[4] = '♣'
        Map[pos[1]][pos[0]] = 0
        
    elif Map[pos[1]][pos[0]] == 9:
        inventory[5] = '♦'
        Map[pos[1]][pos[0]] = 0
        
    elif Map[pos[1]][pos[0]] == 10:
        inventory[6] = '♥'
        Map[pos[1]][pos[0]] = 0
        
    elif Map[pos[1]][pos[0]] == 11:
        inventory[7] = '♠'
        Map[pos[1]][pos[0]] = 0
        
    elif Map[pos[1]][pos[0]] == -1:
        if inventory[0] >= 7:
            inventory[0] -= 7
            inventory[1] += 1
            
    elif Map[pos[1]][pos[0]] == -2:
        if inventory[0] >= 70:
            inventory[0] -= 70
            inventory[1] += 15
            
    elif Map[pos[1]][pos[0]] == -3:
        if inventory[0] >= 400:
            inventory[0] -= 400
            inventory[3] = ' ☻ '
            
    elif Map[pos[1]][pos[0]] == -4:
        if inventory[0] >= 500:
            inventory[0] -= 500
            inventory[2] += 1
        
        
    print('{} © | {}*Bomb | {}*Megabomb |{}|{}|{}|{}|'.format(inventory[0], inventory[1], inventory[2], inventory[4], inventory[5], inventory[6], inventory[7]))
    
    print('-'*3*len(Map[0])+'-'*2)
    for i in range(len(Map)):
        c = '|'
        for x in range(len(Map[i])):
            if pos[0] == x and pos[1] == i:
                c += inventory[3]
            else:
                if Map[i][x] == 0:
                    c += '   '
                elif Map[i][x] == 1:
                    c += ' x '
                elif Map[i][x] == 2:
                    c += ' o '
                elif Map[i][x] == 3:
                    c += ' © '    
                elif Map[i][x] == 7:
                    c += ' ♫ '  
                elif Map[i][x] == 8:
                    c += ' ♣ ' 
                elif Map[i][x] == 9:
                    c += ' ♦ '  
                elif Map[i][x] == 10:
                    c += ' ♥ '  
                elif Map[i][x] == 11:
                    c += ' ♠ '  
                elif Map[i][x] == -1:
                    c += ' 1 ' 
                elif Map[i][x] == -2:
                    c += ' 2 ' 
                elif Map[i][x] == -3:
                    c += ' 3 ' 
                elif Map[i][x] == -4:
                    c += ' 4 ' 
                
        c += '|'
        print(c)
    print('-'*3*len(Map[0])+'-'*2)
    
    if shop:
        print('1: 7 © 1*bomb | 2: 70 © 15*bomb | 3: 400 © skin ☻ | 4: 500 © 1*Megabomb')
    #184 ©☺☻♥♪♫

    call = input()
    if call == 'z':
        pos = up(pos, Map)
    elif call == 's':
        pos = down(pos, Map)
    elif call == 'd':
        pos = right(pos, Map)
    elif call == 'q':
        pos = left(pos, Map)
    elif call == ' ':
        if inventory[1] >= 1:
            inventory[1] -= 1
            score[1] += 1
            score[3] += 1
            Map = destroy(pos, Map)
    elif call == 'b':
        if inventory[2] >= 1:
            inventory[2] -= 1
            score[2] += 1
            (Map, score) = destroy_all(score, Map)
        
    elif call == 'end':
        save = True
        end = False
        
    elif call == 'next':
        pos = [0,0]
        x,y = randint(5,30), randint(5,30)
        Map = map_alea(x,y) 
        shop = False
        score[4] += 1
        
    elif call == 'shop':
        pos = [4,4]
        shop = True
        Map = [[1,1,0,0,0,0,1,1],
               [1,0,0,0,0,0,0,1],
               [0,0,-1,-2,-3,-4,0,0],
               [0,1,0,0,0,0,1,0],
               [0,0,0,0,0,0,0,0],] 
        
    elif call == 'final':
        if inventory[4] == '♣' and inventory[5] == '♦' and inventory[6] == '♥' and inventory[7] == '♠':
        
            print('')
            print(' -  V  I  C  T  O  R  Y  - ')
            print('')
            print('            {}'.format(inventory[3]))
            print('')
            print('')
            print('Total coins collected : {}'.format(score[0]))
            print('Total bombs used      : {}'.format(score[1]))
            print('Total Megaboms used   : {}'.format(score[2]))
            print('Total block destroyed : {}'.format(score[3]))
            print('Total Maps discovered : {}'.format(score[4]))
            print('')
            total_score = (score[0]*2+score[1]*10+score[2]*20+score[4]*8)
            if inventory[3] == ' ☻ ':
                total_score = int(total_score*1.25)
            print('Score : {}'.format(total_score))
            
            f = open('score.txt','a', encoding='utf-8')
            c = name[0] + ' : '
            f.write(str(c))
            f.write(str(total_score))
            f.write('\n')
            f.close()
            save = True
            end = False

    
if save:
    f = open('data/game.txt','w', encoding='utf-8')
    f.write(name[0])
    f.write('\n')
    for i in inventory:
        f.write(str(i))
        f.write('\n')
    for i in score:
        f.write(str(i))
        f.write('\n')
    for i in pos:
        f.write(str(i))
        f.write('\n')
    f.close()
    
    f = open('data/map.txt','w', encoding='utf-8')
    f.write(str(len(Map)))
    f.write('\n')
    f.write(str(len(Map[0])))
    f.write('\n')
    for i in range(len(Map)):
        for j in range(len(Map[i])):
            f.write(str(Map[i][j]))
            f.write('\n')
    f.close()
    
wait_before_ending = input('Tap anything to get out...')