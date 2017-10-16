from tkinter import*
from random import*
from time import*
root = Tk()
size = 1000
a = 20
rooms = []
canvas = Canvas(root, width = size, height = size)
used = [[(0) for j in range(size // a + 1)] for i in range(size // a + 1)]
#///////////////////////////////////////////////////////////////////////////////
class trap(object):
    def __init__(self, x, y):
        self.trap = canvas.create_rectangle(x, y, x + 30, y + 30, fill="Grey")
        self.m = [0] * 6
        self.m[0] = canvas.create_polygon(x + 5, y + 5, x + 7.5, y, x + 10, y + 5, fill="white")
        self.m[1] = canvas.create_polygon(x + 5, y + 15, x + 7.5, y + 10, x + 10, y + 15, fill="white")
        self.m[2] = canvas.create_polygon(x + 5, y + 25, x + 7.5, y + 20, x + 10, y + 25, fill="white")
        self.m[3] = canvas.create_polygon(x + 20, y + 5, x + 22.5, y, x + 25, y + 5, fill="white")
        self.m[4] = canvas.create_polygon(x + 20, y + 15, x + 22.5, y + 10, x + 25, y + 15, fill="white")
        self.m[5] = canvas.create_polygon(x + 20, y + 25, x + 22.5, y + 20, x + 25, y + 25, fill="white")
    def check(self, q):
        a, b, c, d = canvas.coords(q.m[4])
        a1, b1, c1, d1 = canvas.coords(self.trap)
        if (a > a1 and a < c1 or (c > a1 and c < c1)) and (b > b1 and b < d1 or (d > b1 and d < b1)):
            q.damage(2)

def create_room():
    global rooms, used, door_out1, door_out2, traps
    fons = ['yellow4', "White", 'gold', 'pink', 'khaki']
    ind1 = randrange(0, 5)
    canvas.create_rectangle(0, 0, size, size, fill = fons[ind1])
    walls = []
    color = 'gray57'
    #creating of walls
    k = randrange(10, 12)
    for i in range(k):
        vector = randrange(5)
        len_ = randrange(5, 10)              #len - длина стены, которую мы сейчас генерируем                                #vector - направление стены(1 - верт, 2 - горизонт)
        x = randrange(4, size // a - 6)               #В зависимости от vector k1, k2, k3 или (y, x1, x2), или (x, y1, y2)
        y = randrange(0, size // a)            
        walls.append([len_, vector, x, y])       #walls - массив всех стен данной комнаты
    walls.append([(size // a) // 2 - 5, 3, 0, 0])
    walls.append([size // a - 1, 2, 0, 0])
    walls.append([(size // a) // 2 - 5, 3, (size // a), 0])
    walls.append([(size // a) // 2 - 5, 3, (size // a), (size // a) // 2 + 5])
    walls.append([size // a - 1, 4, size // a - 1, size // a - 1])
    walls.append([(size // a) // 2 - 5, 3, 0, (size // a) // 2 + 5])
    walls.append([(size // a) // 2 - 5, 3, size // a - 3, 0])
    walls.append([(size // a) // 2 - 5, 3, size // a - 3, (size // a) // 2 + 5])
    walls.append([4, 2, size // a - 3, (size // a) // 2 - 5])
    walls.append([4, 2, size // a - 3, (size // a) // 2 + 6])
    walls.append([(size // a) // 2 - 5, 3, size // a - 2, 0])
    walls.append([(size // a) // 2 - 5, 3, size // a - 1, 0])
    walls.append([(size // a) // 2 - 5, 3, size // a - 2, (size // a) // 2 + 5])
    walls.append([(size // a) // 2 - 5, 3, size // a - 1, (size // a) // 2 + 5])
    walls.append([(size // a) // 2 - 5, 3, size // a - 3, 0])
    walls.append([(size // a) // 2 - 5, 3, size // a - 4, 0])
    walls.append([(size // a) // 2 - 5, 3, size // a - 3, (size // a) // 2 + 5])
    walls.append([(size // a) // 2 - 5, 3, size // a - 4, (size // a) // 2 + 5])    
    rooms.append(walls)
    door_out1 = canvas.create_line((size // a - 1) * a, ((size // a) // 2 - 5) * a, (size // a - 1) * a, ((size // a) // 2 + 6) * a, width = 10, fill = 'brown')
    door_out2 = canvas.create_line((size // a) * a - 5, ((size // a) // 2 - 4) * a, (size // a) * a - 5, ((size // a) // 2 + 6) * a, width = 10, fill = 'brown')
    for i in range(len(walls)):
        len_ = walls[i][0]
        vector = walls[i][1]
        x = walls[i][2]
        y = walls[i][3]
        cenx = x
        ceny = y
        if vector == 1:
            for i in range(len_):
                if ceny > 1:
                    ceny = ceny - 1
                    canvas.create_rectangle(a * cenx, a * ceny, a * cenx + a, a * ceny + a, fill = color)
                    used[cenx][ceny] = 1
                    
        if vector == 2:
            for i in range(len_):
                if cenx < size // a - 1:
                    cenx = cenx + 1
                    canvas.create_rectangle(a * cenx, a * ceny, a * cenx + a, a * ceny + a, fill = color)
                    used[cenx][ceny] = 1
        if vector == 3:
            for i in range(len_):
                if ceny < size // a - 1:
                    ceny = ceny + 1
                    canvas.create_rectangle(a * cenx, a * ceny, a * cenx + a, a * ceny + a, fill = color)
                    used[cenx][ceny] = 1
        if vector == 4:
            for i in range(len_):
                if cenx > 1:
                    cenx = cenx - 1
                    canvas.create_rectangle(a * cenx, a * ceny, a * cenx + a, a * ceny + a, fill = color)
                    used[cenx][ceny] = 1
    x, y = randint(5, size - 40), randint(5, size - 40)
    traps = trap(x, y)
        


#/////////////////////////////////////
#/////////////////////////////////////
#/////////////////////////////////////

r = 4
      
class bullet(object):
    def __init__(self, r, speed, a, b, x, y, color):
        self.q = canvas.create_oval(a, b, a + r, b + r, fill=color)
        self.time = speed // 3
        if abs(a - x) > abs(b - y):
            if a - x < 0:
                w = 3
            else:
                w = -3
            t = (a - x) / w
            self.v = [w, (b - y) / t]
        else:
            if b - y < 0:
                w = 3
            else:
                w = -3
            t = (b - y) / w
            self.v = [(a - x) / t, w]
    def move(self):
        w = canvas.coords(self.q)
        w[0] += self.v[0]
        w[2] += self.v[0]
        w[1] += self.v[1]
        w[3] += self.v[1]
        canvas.coords(self.q, w)


class pistol(object):
    def __init__(self, r, cord):
        self.bullets = []
        self.speed = 20
        self.m = [0] * 5
        self.m[0] = canvas.create_polygon(cord[0] + 6 * r, cord[1] - 2 * r, cord[0] + 10 * r, cord[1] - 2 * r, cord[0] + 10 * r, cord[1], cord[0] + 7 * r, cord[1], cord[0] + 6 * r, cord[1] + r, cord[0] + 5 * r, cord[1] + r, fill="DimGray")
    def moveKiller(self, v):
        q = canvas.coords(self.m[0])
        for i in range(0, 11, 2):
            q[i] += v[0]
        for i in range(1, 12, 2):
            q[i] += v[1]
        canvas.coords(self.m[0], q)
    def turn(self, q, r):
        if q == 1:
            e = canvas.coords(self.m[0])
            e[0] -= 6 * r
            e[2] -= 14 * r
            e[4] -= 14 * r
            e[6] -= 8 * r
            e[8] -= 6 * r
            e[10] -= 4 * r
        elif q == 0:
            e = canvas.coords(self.m[0])
            e[0] += 6 * r
            e[2] += 14 * r
            e[4] += 14 * r
            e[6] += 8 * r
            e[8] += 6 * r
            e[10] += 4 * r
        canvas.coords(self.m[0], e)
    def bang(self, x, y):
        a, b = canvas.coords(self.m[0])[2], canvas.coords(self.m[0])[3]
        self.bullets.append(bullet(10, self.speed, a, b, x, y, "red"))
        


class Player(object):
    def __init__(self, killer, r, hp):
        self.dead = 1
        self.maxhp = canvas.create_rectangle(size - 70, 40, size - 10, 50, fill="White")
        self.hp = canvas.create_rectangle(size - 70, 40, hp, 50, fill="red")
        self.flag = 0
        self.m = [0] * 12
        self.m[0] = canvas.create_rectangle(3 * r, r, 12 * r, 3 * r, fill="brown")
        self.m[1] = canvas.create_rectangle(3 * r, 3 * r, 11 * r, 5 * r, fill="brown")
        self.m[2] = canvas.create_rectangle(r, 3 * r, 3 * r, 9 * r, fill="brown")
        self.m[3] = canvas.create_rectangle(3 * r, 5 * r, 11 * r, 13 * r, fill="SandyBrown")
        self.m[4] = canvas.create_rectangle(4 * r, 13 * r, 10 * r, 16 * r, fill="blue")
        self.m[5] = canvas.create_rectangle(5 * r, 16 * r, 6 * r, 17 * r, fill="yellow")
        self.m[6] = canvas.create_rectangle(8 * r, 16 * r, 9 * r, 17 * r, fill="yellow")
        self.m[7] = canvas.create_rectangle(5 * r, 7 * r, 7 * r, 9 * r, fill="white")
        self.m[8] = canvas.create_rectangle(9 * r, 7 * r, 11 * r, 9 * r, fill="white")
        self.m[9] = canvas.create_rectangle(6 * r, 7 * r, 7 * r, 9 * r, fill="black")
        self.m[10] = canvas.create_rectangle(10 * r, 7 * r, 11 * r, 9 * r, fill="black")
        self.m[11] = canvas.create_rectangle(6 * r, 11 * r, 8 * r, 12 * r, fill="red")
        self.killer = killer(r, [canvas.coords(self.m[4])[0], canvas.coords(self.m[4])[1]])
    def movePlayer(self, v):
        for i in range(12):
            a, b, c, d = canvas.coords(self.m[i])
            canvas.coords(self.m[i], a + v[0], b + v[1], c + v[0], d + v[1])
        self.killer.moveKiller(v)
    def bang(self, x, y):
        self.killer.bang(x, y)
    def damage(self, x):
        a, b, c, d = canvas.coords(self.hp)
        if c - x < a:
            canvas.create_text(size / 2, size / 2, text = "Game Over", font = "Verdana 50")
            self.dead = 0
        canvas.coords(self.hp, a, b, c - x, d)

def check_room():
    global rooms, player, door_out1, door_out2, used, orud, bullets
    coost = canvas.coords(player.m[4])
    x = (coost[2] + coost[0]) // 2
    y = coost[3]    
    if x > (size) - a * 2 and y > size // 2 - 5 * a and y < size // 2 + 6 * a:
        for i in range(100):
            coo1 = canvas.coords(door_out1)
            coo2 = canvas.coords(door_out2)
            canvas.coords(door_out1, coo1[0], coo1[1], coo1[2], coo1[3] - 2)
            canvas.coords(door_out2, coo2[0], coo2[1] + 2, coo2[2], coo2[3])
            canvas.update()
            sleep(0.005)
        #canvas.delete("all")
        for i in range(len(player.killer.bullets)):
            canvas.delete(player.killer.bullets[i].q)
        player.killer.bullets = []
        bullets = []
        canvas.update()
        canvas.create_text(400, 400, text = 'Next room', font = 'Verdana 40', justify = CENTER, fill = 'black')
        canvas.update()
        sleep(1)
        used = [[(0) for j in range(size // a + 1)] for i in range(size // a + 1)]
        create_room()
        player = Player(orud, r, canvas.coords(player.hp)[2])
        player.movePlayer([0, size//2])


def move():
    global player, v, step, k
    if player.dead != 0:
        check_room()
        coost = canvas.coords(player.m[4])
        #print(coost)
        x = (coost[2] + coost[0]) // 2
        y = coost[3]
        crash = 0
        for i in range(len(used)):
            for j in range(len(used[i])):
                if used[i][j] == 1:
                    x1 = i * a
                    y1 = j * a
                    x2 = i * a + a
                    y2 = j * a + a
                    #print(v)
                    #print('i, j = ', i, j, 'coords = ', x1, y1, x2, y2)
                    if x + v[0] > x1 and x + v[0] < x2 and y + v[1] > y1 and y + v[1] < y2:
                        #print('crash')
                        crash = 1
                        v = [0, 0]
                        break
        if crash == 0:
            player.movePlayer(v)
            player.movePlayer(v)
            if step == 0:
                v = [0, 0]
            else:
                step -= 1
        for i in range(len(player.killer.bullets)):
            for j in range(player.killer.bullets[i].time):
                player.killer.bullets[i].move()
                ####check of bullet
        traps.check(player)
        canvas.update()
        canvas.after(50, move)

def continuu():
    global fonn, textt
    canvas.delete(fonn)
    canvas.delete(textt)
    move()
    

def starting():
    global size, fonn, textt
    fonn = canvas.create_rectangle(0, 0, size, size, fill="Black")
    textt = canvas.create_text(size // 2, size // 2, text="Made by\n Ilia and Stepan", font="Verdana 50", fill = "White")
    canvas.update()


def up(event):
    global v, speed, step, k
    v[1] = -speed
    v[0] = 0
    step = k
def down(event):
    global v, speed, step, k
    v[1] = speed
    v[0] = 0
    step = k
def right(event):
    global v, speed, step, k
    v[0] = speed
    v[1] = 0
    step = k
def left(event):
    global v, speed, step, k
    v[0] = -speed
    v[1] = 0
    step = k

def right_up(event):
    global v, speed, step, k
    v[0] = speed
    v[1] = -speed
    step = k
def left_up(event):
    global v, speed, step, k
    v[0] = -speed
    v[1] = -speed
    step = k
def right_down(event):
    global v, speed, step, k
    v[0] = speed
    v[1] = speed
    step = k
def left_down(event):
    global v, speed, step, k
    v[0] = -speed
    v[1] = speed
    step = k
def stop(event):
    global v, speed, step, k
    v[0] = 0
    v[1] = 0
    step = k

def motion(event):
    global player, r
    q = canvas.coords(player.m[4])[0]
    if event.x < q and player.flag == 0:
        player.flag = 1
        a, b, c, d = canvas.coords(player.m[0])
        canvas.coords(player.m[0], a - r, b, c - r, d)
        a, b, c, d = canvas.coords(player.m[2])
        canvas.coords(player.m[2], a + 10 * r, b, c + 10 * r, d)
        a, b, c, d  = canvas.coords(player.m[7])
        canvas.coords(player.m[7], a - 2 * r, b, c - 2 * r, d)
        a, b, c, d  = canvas.coords(player.m[8])
        canvas.coords(player.m[8], a - 2 * r, b, c - 2 * r, d)
        a, b, c, d  = canvas.coords(player.m[9])
        canvas.coords(player.m[9], a - 3 * r, b, c - 3 * r, d)
        a, b, c, d  = canvas.coords(player.m[10])
        canvas.coords(player.m[10], a - 3 * r, b, c - 3 * r, d)
        player.killer.turn(1, r)
    elif event.x > q and player.flag == 1:
        player.flag = 0
        a, b, c, d = canvas.coords(player.m[0])
        canvas.coords(player.m[0], a + r, b, c + r, d)
        a, b, c, d = canvas.coords(player.m[2])
        canvas.coords(player.m[2], a - 10 * r, b, c - 10 * r, d)
        a, b, c, d  = canvas.coords(player.m[7])
        canvas.coords(player.m[7], a + 2 * r, b, c + 2 * r, d)
        a, b, c, d  = canvas.coords(player.m[8])
        canvas.coords(player.m[8], a + 2 * r, b, c + 2 * r, d)
        a, b, c, d  = canvas.coords(player.m[9])
        canvas.coords(player.m[9], a + 3 * r, b, c + 3 * r, d)
        a, b, c, d  = canvas.coords(player.m[10])
        canvas.coords(player.m[10], a + 3 * r, b, c + 3 * r, d)
        player.killer.turn(0, r)
def bang(event):
    player.bang(event.x, event.y)


create_room()
player = Player(pistol, r, size - 10)
orud = pistol
player.movePlayer([0, size//2])
speed = 5
v = [0, 0]
k = 8
step = k
starting()
canvas.after(2000, continuu)



root.bind("7", left_up)
root.bind("9", right_up)
root.bind("1", left_down)
root.bind("3", right_down)
root.bind("8", up)
root.bind("2", down)
root.bind("6", right)
root.bind("4", left)
root.bind("5", stop)
root.bind("<Motion>", motion)
root.bind("<Button-1>", bang)

#///////////////////////////////////////////////////////////////////////////////
canvas.pack()
canvas.update()
root.mainloop()
