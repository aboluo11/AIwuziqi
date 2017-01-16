import pygame
from pygame import *
import numpy as np
import time


class Myerror(Exception):
    pass


pygame.init()

SCREEN_SIZE = (700, 700)
screen = pygame.display.set_mode(SCREEN_SIZE, 0, 32)
screen.fill((213, 184, 154))

x_list = []


for x in range(50, 651, 40):
    pygame.draw.line(screen, (0, 0, 0), (x, 50), (x, 650), 2)
    pygame.draw.line(screen, (0, 0, 0), (50, x), (650, x), 2)
    x_list.append(x)


def mmm(black, yu, aerfa, beta, count):
    l, l2 = [], []

    def lalala(temp, ai):
        c5, huo4, si4, huo3, si3, huo2, si2, huo1 = 0, 0, 0, 0, 0, 0, 0, 0
        eval = 0
        coo = {0:(-1,-1),1:(-1,-1),2:(-1,-1),3:(-1,-1)}
        for i in range(16):
            for j in range(16):
                if temp[i, j] == ai:
                    for t in range(4):
                        pd = 0
                        xia, zhe, kong = 0, 0, 0
                        wz = []
                        x, y = i, j
                        if t == 0:
                            if y >= 1:
                                if temp[x, y - 1] != ai:
                                    if temp[x, y - 1]:
                                        pd = 1
                                        zhe = 1
                                    else:
                                        if y >= 2:
                                            if temp[x,y - 2] != ai:
                                                pd = 1
                                        else:
                                            pd = 1
                            else:
                                pd,zhe = 1,1
                        elif t == 1:
                            if x >= 1:
                                if temp[x - 1, y] != ai:
                                    if temp[x - 1, y]:
                                        pd = 1
                                        zhe = 1
                                    else:
                                        if x >= 2:
                                            if temp[x - 2,y] != ai:
                                                pd = 1
                                        else:
                                            pd = 1
                            else:
                                pd,zhe = 1,1
                        elif t == 2:
                            if x >= 1 and y >= 1:
                                if temp[x - 1, y - 1] != ai:
                                    if temp[x - 1, y - 1]:
                                        pd = 1
                                        zhe = 1
                                    else:
                                        if y >= 2 and x >= 2:
                                            if temp[x - 2,y - 2] != ai:
                                                pd = 1
                                        else:
                                            pd = 1
                            else:
                                pd,zhe = 1,1
                        else:
                            if x <= 14 and y >= 1:
                                if temp[x + 1, y - 1] != ai:
                                    if temp[x + 1, y - 1]:
                                        pd = 1
                                        zhe = 1
                                    else:
                                        if y >= 2 and x <= 13:
                                            if temp[x + 2,y - 2] != ai:
                                                pd = 1
                                        else:
                                            pd = 1
                            else:
                                pd,zhe = 1,1
                        if pd:
                            n = 1
                            while 1:
                                a,s = x,y
                                if t == 0:
                                    y += 1
                                elif t == 1:
                                    x += 1
                                elif t == 2:
                                    x += 1
                                    y += 1
                                elif t == 3:
                                    x -= 1
                                    y += 1
                                n += 1
                                if n <= 5:                                    
                                    if x >= 0 and x <= 15 and y<= 15:
                                        if temp[x, y] == ai:
                                            xia += 1
                                        elif temp[x,y] == 0:
                                            kong += 1
                                            wz.append(n)
                                            xia += 1
                                        else:
                                            if temp[a,s]:
                                                zhe += 1
                                            break
                                    else:
                                        zhe += 1
                                        break
                                else:
                                    break
                        else:
                            continue
                        zhen_kong = kong
                        for each in range(5,0,-1):
                            if wz:
                                if each == wz[-1]:
                                    wz.pop()
                                    zhen_kong -= 1
                                else:
                                    break
                            else:
                                break
                        if xia - kong + 1 >= 5:
                            return 100000
                        if xia - kong + 1 == 4:
                            if zhen_kong:
                                if zhe != 2:
                                    si4 += 1
                            else:
                                if zhe == 0:
                                    huo4 += 1
                                elif zhe == 1:
                                    si4 += 1
                        if xia - kong + 1 == 3:
                            if zhen_kong > 1:
                                if zhe != 2:
                                    si3 += 1
                            else:
                                if zhe == 0:
                                    huo3 += 1
                                elif zhe == 1:
                                    si3 += 1
                        if xia - kong + 1 == 2:
                            if zhen_kong > 1:
                                if zhe != 2:
                                    si2 += 1
                            else:
                                if zhe == 0:
                                    huo2 += 1
                                elif zhe == 1:
                                    si2 += 1
                        '''if xia - kong + 1 == 1:
                            if zhe == 0:
                                huo1 += 1'''

        if si4 and huo3:
            return 10000 
        elif si4 >= 2:
            return 10000          
        else:
            eval += (10000 * huo4 + 1000 * si4 + 100 * huo3 +
                 10 * si3 + 1 * huo2 + 0.1 * si2)

        return eval

    def nnn(temp):
        hei = lalala(temp, 2)
        bai = lalala(temp, 1)
        if hei == 100000:
            return 100000
        elif bai == 100000:
            return -100000
        else:
            if black:
                return (hei - bai*10)
            else:
                return (hei*10 - bai)

    def youlinju(i, j, temp):
        for x in range(-1, 2):
            for y in range(-1, 2):
                try:
                    if temp[i + x, j + y]:
                        return 1
                except IndexError:
                    pass

    eval_list = []
    for x in range(16):
        for y in range(16):
            if yu[x][y] == 0:
                if youlinju(x, y, yu):
                    temp = np.array(yu)
                    if black:
                        temp[x,y] = 2
                    else:
                        temp[x,y] = 1
                    evaluate = nnn(temp)
                    eval_list.append(((x, y), evaluate, temp))

    for j in range(len(eval_list) - 1):
        for i in range(j, len(eval_list)):
            pd = 0
            if black:
                if eval_list[i][1] > eval_list[j][1]:
                    pd = 1
            else:
                if eval_list[i][1] < eval_list[j][1]:
                    pd = 1
            if pd:
                aaa = eval_list[j]
                eval_list[j] = eval_list[i]
                eval_list[i] = aaa

    for each in eval_list[:7]:
        '''print(each[0],each[1])'''
        (x, y) = each[0]
        evaluate = each[1]
        temp = each[2]
        if evaluate == 100000 or evaluate == -100000:
            return ((x, y), evaluate)
        elif count <= 3:
            a = mmm(not black, temp, aerfa, beta, count + 1)
            if a != None:
                if not black:
                    if a[1] < aerfa:
                        return None
                    else:
                        beta = a[1]
                else:
                    if a[1] > beta:
                        return None
                    else:
                        aerfa = a[1]
                l.append(((x, y), a[1]))
            else:
                continue
        else:
            l.append(((x, y), evaluate))

    for each in l:
        l2.append(each[1])
    for each in l:
        if black:
            if each[1] == max(l2):
                return each
        else:
            if each[1] == min(l2):
                return each


def change(coo):
    return (x_list[coo[1]], x_list[coo[0]])

ju = np.zeros((16, 16), int)

a, b = 7, 8
pygame.draw.circle(screen, (0, 0, 0), change((a, b)), 6)

pygame.draw.rect(screen,(0,0,0),(660,300,30,30))
pygame.draw.rect(screen,(255,255,255),(660,400,30,30))
pygame.draw.rect(screen,(0,255,0),(660,660,30,30))
pygame.draw.rect(screen,(0,0,255),(660,600,30,30))

aixy = []
ij = []
renij = []
renxy = []
hei = 0
pd = 0
diyici = 1

while 1:
    x, y = pygame.mouse.get_pos()
    event = pygame.event.wait()
    if event.type == QUIT:
        pygame.quit()
    elif event.type == MOUSEBUTTONDOWN:
        if event.button == 1:
            if x<=660 and y<=660:
                isbreak = 0
                try:
                    i = 0
                    for each in x_list:
                        if abs(each - x) <= 20:
                            x = each
                            isbreak = 1
                            break
                        i += 1
                    if not isbreak:
                        raise Myerror
                    else:
                        isbreak = 0

                    j = 0
                    for each in x_list:
                        if abs(each - y) <= 20:
                            y = each
                            isbreak = 1
                            break
                        j += 1
                    if not isbreak:
                        raise Myerror
                except Myerror:
                    continue
                if not ju[j,i]:
                    if hei:
                        pygame.draw.circle(screen, (0, 0, 0), (x, y), 10) 
                    else:
                        pygame.draw.circle(screen, (255, 255, 255), (x, y), 10)
                    ju[j, i] = 1                                  
                    aixy.append((x,y))
                    ij.append((j,i))
                    pd = 1
                    hei = not hei
            elif x >=660 and x <= 690 and y >= 660 and y <= 690:
                try:
                    pygame.draw.circle(screen,(213,184,154),aixy[-1],10)
                    x, y = aixy[-1][0], aixy[-1][1]
                    pygame.draw.rect(screen,(213,184,154),(x-12,y-12,24,24),2)
                    pygame.draw.line(screen,(0,0,0),(x-13,y),(x+13,y),2)
                    pygame.draw.line(screen,(0,0,0),(x,y-13),(x,y+13),2)
                    ju[ij[-1]] = 0
                    renij.append(ij.pop())
                    renxy.append(aixy.pop())
                except IndexError:
                    pass
            elif x >= 660 and x <= 690 and y >= 600 and y <= 630:
                if hei:
                    try:
                        pygame.draw.circle(screen,(0,0,0),renxy[-1],10)
                        ju[renij[-1]] = 2
                        ij.append(renij.pop())
                        aixy.append(renxy.pop())
                    except IndexError:
                        pass
                else:
                    try:
                        pygame.draw.circle(screen,(255,255,255),renxy[-1],10)
                        ju[renij[-1]] = 1
                        ij.append(renij.pop())
                        aixy.append(renxy.pop())   
                    except IndexError:
                        pass 
            elif x >= 660 and x <= 690 and y >= 300 and y <= 330:
                if diyici:
                    pygame.draw.circle(screen,(0,0,0),change((7,8)),10)
                    ju[7,8] = 2
                    diyici = 0
            elif x >= 660 and x <=690 and y >= 400 and y <= 430:
                if diyici:
                    hei = not hei
                    diyici = 0
         


    elif event.type == MOUSEBUTTONUP:
        if pd:
            try:
                pygame.draw.rect(screen, (213, 184, 154), (p - 12, q - 12, 24, 24),2)
                pygame.draw.line(screen,(0,0,0),(p-13,q),(p-11,q),2)
                pygame.draw.line(screen,(0,0,0),(p,q-13),(p,q-11),2)
                pygame.draw.line(screen,(0,0,0),(p+13,q),(p+11,q),2)
                pygame.draw.line(screen,(0,0,0),(p,q+13),(p,q+11),2)                
            except:
                pass
            t1 = time.process_time()
            jieguo = mmm(1, ju, -1000000, 1000000, 1)
            coo = jieguo[0]
            '''print(coo)'''
            t2 = time.process_time()
            print(t2 - t1)
            x, y = change(coo)[0], change(coo)[1]
            if hei:
                pygame.draw.circle(screen, (0, 0, 0), (x, y), 10)   
            else:
                pygame.draw.circle(screen, (255, 255, 255), (x, y), 10)
            ju[coo] = 2        
            pygame.draw.rect(screen, (0, 255, 0), (x - 12, y - 12, 24, 24),2)
            aixy.append((x,y))
            p, q = x, y
            ij.append(coo)
            pd = 0
            hei = not hei

    pygame.display.update()
