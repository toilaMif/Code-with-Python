import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((300,400))
pygame.display.set_caption('Game Trung code')

NEN = (0,195, 180)
DUONG_KE = (0, 166, 153)
MAU_X = (84, 84, 84)
MAU_O = (239, 238, 205)

circles = []
line = []
win_x= []
win_o= []
ban_co = [0,1,2,3,4,5,6,7,8]
bat_dau = 'o'
kieu_thang_x= False
kieu_thang_o=False
running = True
thang = False
hoa=False
ket_thuc=False

def thay_phien (bat_dau):
        if bat_dau == 'o':
            return 'x'
        return 'o'

def ktra_thang(XorO,a,b,c):
    if ban_co[a] == XorO and ban_co[b] == XorO and ban_co[c] == XorO:
        return True
    return False

def ktra_thang_all(XorO):
        #Hàng ngang
    if ktra_thang(XorO,0,1,2)==True:
        return XorO
    if ktra_thang(XorO,3,4,5)==True:
        return XorO
    if ktra_thang(XorO,6,7,8)==True:
        return XorO
    #Hàng dọc
    if ktra_thang(XorO,0,3,6)==True:
        return XorO
    if ktra_thang(XorO,1,4,7)==True:
        return XorO
    if ktra_thang(XorO,2,5,8)==True:
        return XorO
    #Đường chéo
    if ktra_thang(XorO,0,4,8)==True:
        return XorO
    if ktra_thang(XorO,2,4,6)==True:
        return XorO
    return False

def ktra_kieu_thang(XorO):
        #Hàng ngang
    if ktra_thang(XorO,0,1,2)==True:
        return 1
    if ktra_thang(XorO,3,4,5)==True:
        return 2
    if ktra_thang(XorO,6,7,8)==True:
        return 3
    #Hàng dọc
    if ktra_thang(XorO,0,3,6)==True:
        return 4
    if ktra_thang(XorO,1,4,7)==True:
        return 5
    if ktra_thang(XorO,2,5,8)==True:
        return 6
    #Đường chéo
    if ktra_thang(XorO,0,4,8)==True:
        return 7
    if ktra_thang(XorO,2,4,6)==True:
        return 8
    return False

def ktra_danh_full_chua():
        if  (ban_co[0]=='x' or ban_co[0]=='o') and (ban_co[1]=='x' or ban_co[1]=='o') and (ban_co[2]=='x' or ban_co[2]=='o') and (ban_co[3]=='x' or ban_co[3]=='o') and (ban_co[4]=='x' or ban_co[4]=='o') and (ban_co[5]=='x' or ban_co[5]=='o') and (ban_co[6]=='x' or ban_co[6]=='o') and (ban_co[7]=='x' or ban_co[7]=='o') and (ban_co[8]=='x' or ban_co[8]=='o'): 
            return True

def ve_ban_co():#vẽ bàn cờ
    pygame.draw.line(screen, DUONG_KE, (75, 100), (225, 100), 5)
    pygame.draw.line(screen, DUONG_KE, (75, 150), (225, 150), 5)
    pygame.draw.line(screen, DUONG_KE, (125, 50), (125, 200), 5)
    pygame.draw.line(screen, DUONG_KE, (175, 50), (175, 200), 5)

def thoat ():
    sys.exit()
        
font = pygame.font.SysFont('Times New Roman', 30)
font1 = pygame.font.SysFont('Times New Roman', 10)

def choi (circles, line, win_o, win_x, ban_co, bat_dau, kieu_thang_x, kieu_thang_o, running, thang, hoa, ket_thuc):
    while running: 
        screen.fill(NEN)
        image = pygame.image.load('D:\\Education\\Code\\Python\\Py1\Caro\\th-removebg-preview.png')
        
        mouse_x, mouse_y = pygame.mouse.get_pos()
        # print("Vi tri x:", mouse_x)
        # print("Vi tri y:", mouse_y)

        ve_ban_co()
        for event in pygame.event.get():
            if thang != False:
                if thang == 'x':
                    bat_dau='o'
                if thang == 'o':
                    bat_dau='x'
            if event.type == pygame.QUIT:
                running = False
                thoat()
            if event.type == pygame.MOUSEBUTTONDOWN: #chuột trái để chơi
                        if event.button == 1:
                            if (140 < mouse_x < 160) and (20 < mouse_y < 40):
                                for i in range(9):
                                    ban_co[i]=i
                                choi([], [], [], [], ban_co, bat_dau, False, False, True, False, False, False)
                            if (75 < mouse_x < 125) and (50 < mouse_y < 100): #Ô1
                                if thay_phien(bat_dau)=='x':
                                    if ban_co[0] == 'x' or ban_co[0] == 'o' or thang != False:
                                        break
                                    else:
                                        pos1=(85,60)
                                        pos2=(115,90)
                                        pos3=(115,60)
                                        pos4=(85,90)
                                        all=(pos1,pos2,pos3,pos4)
                                        line.append(all)
                                        bat_dau='x'
                                        ban_co[0]='x'
                                if thay_phien(bat_dau)=='o':
                                    if ban_co[0] == 'x' or ban_co[0] == 'o' or thang != False:
                                        break
                                    else:
                                        pos=(100,75)
                                        circles.append(pos)
                                        bat_dau='o'
                                        ban_co[0]='o'
                                thay_phien(bat_dau)
                                                            
                            if (125 < mouse_x < 175) and (50 < mouse_y < 100): #Ô2
                                if thay_phien(bat_dau)=='x':
                                    if ban_co[1] == 'x' or ban_co[1] == 'o' or thang != False:
                                        break
                                    else:
                                        pos1=(135,60)
                                        pos2=(165,90)
                                        pos3=(165,60)
                                        pos4=(135,90)
                                        all=(pos1,pos2,pos3,pos4)
                                        line.append(all)
                                        bat_dau='x'
                                        ban_co[1]='x'
                                if thay_phien(bat_dau)=='o':
                                    if ban_co[1] == 'x' or ban_co[1] == 'o' or thang != False:
                                        break
                                    else:
                                        pos=(150,75)
                                        circles.append(pos)
                                        bat_dau='o'
                                        ban_co[1]='o'
                                thay_phien(bat_dau)

                            if (175 < mouse_x < 225) and (50 < mouse_y < 100): #Ô3
                                if thay_phien(bat_dau)=='x':
                                    if ban_co[2] == 'x' or ban_co[2] == 'o' or thang != False:
                                        break
                                    else:
                                        pos1=(185,60)
                                        pos2=(215,90)
                                        pos3=(215,60)
                                        pos4=(185,90)
                                        all=(pos1,pos2,pos3,pos4)
                                        line.append(all)
                                        bat_dau='x'
                                        ban_co[2]='x'
                                if thay_phien(bat_dau)=='o':
                                    if ban_co[2] == 'x' or ban_co[2] == 'o' or thang != False:
                                        break
                                    else:
                                        pos=(200,75)
                                        circles.append(pos)
                                        bat_dau='o'
                                        ban_co[2]='o'
                                thay_phien(bat_dau)

                            if (75 < mouse_x < 125) and (100 < mouse_y < 150): #Ô4
                                if thay_phien(bat_dau)=='x':
                                    if ban_co[3] == 'x' or ban_co[3] == 'o' or thang != False:
                                        break
                                    else:
                                        pos1=(85,110)
                                        pos2=(115,140)
                                        pos3=(115,110)
                                        pos4=(85,140)
                                        all=(pos1,pos2,pos3,pos4)
                                        line.append(all)
                                        bat_dau='x'
                                        ban_co[3]='x'
                                if thay_phien(bat_dau)=='o':
                                    if ban_co[3] == 'x' or ban_co[3] == 'o' or thang != False:
                                        break
                                    else:
                                        pos=(100,125)
                                        circles.append(pos)
                                        bat_dau='o'
                                        ban_co[3]='o'
                                thay_phien(bat_dau)
                                                               
                            if (125 < mouse_x < 175) and (100 < mouse_y < 150): #Ô5
                                if thay_phien(bat_dau)=='x':
                                    if ban_co[4] == 'x' or ban_co[4] == 'o' or thang != False:
                                        break
                                    else:
                                        pos1=(135,110)
                                        pos2=(165,140)
                                        pos3=(165,110)
                                        pos4=(135,140)
                                        all=(pos1,pos2,pos3,pos4)
                                        line.append(all)
                                        bat_dau='x'
                                        ban_co[4]='x'
                                if thay_phien(bat_dau)=='o':
                                    if ban_co[4] == 'x' or ban_co[4] == 'o' or thang != False:
                                        break
                                    else:
                                        pos=(150,125)
                                        circles.append(pos)
                                        bat_dau='o'
                                        ban_co[4]='o'
                                thay_phien(bat_dau)

                            if (175 < mouse_x < 225) and (100 < mouse_y < 150): #Ô6
                                if thay_phien(bat_dau)=='x':
                                    if ban_co[5] == 'x' or ban_co[5] == 'o' or thang != False:
                                        break
                                    else:
                                        pos1=(185,110)
                                        pos2=(215,140)
                                        pos3=(215,110)
                                        pos4=(185,140)
                                        all=(pos1,pos2,pos3,pos4)
                                        line.append(all)
                                        bat_dau='x'
                                        ban_co[5]='x'
                                if thay_phien(bat_dau)=='o':
                                    if ban_co[5] == 'x' or ban_co[5] == 'o' or thang != False:
                                        break
                                    else:
                                        pos=(200,125)
                                        circles.append(pos)
                                        bat_dau='o'
                                        ban_co[5]='o'
                                thay_phien(bat_dau)

                            if (75 < mouse_x < 125) and (150 < mouse_y < 200): #Ô7
                                if thay_phien(bat_dau)=='x':
                                    if ban_co[6] == 'x' or ban_co[6] == 'o' or thang != False:
                                        break
                                    else:
                                        pos1=(85,160)
                                        pos2=(115,190)
                                        pos3=(115,160)
                                        pos4=(85,190)
                                        all=(pos1,pos2,pos3,pos4)
                                        line.append(all)
                                        bat_dau='x'
                                        ban_co[6]='x'
                                if thay_phien(bat_dau)=='o':
                                    if ban_co[6] == 'x' or ban_co[6] == 'o' or thang != False:
                                        break
                                    else:
                                        pos=(100,175)
                                        circles.append(pos)
                                        bat_dau='o'
                                        ban_co[6]='o'
                                thay_phien(bat_dau)

                            if (125 < mouse_x < 175) and (150 < mouse_y < 200): #Ô8
                                if thay_phien(bat_dau)=='x':
                                    if ban_co[7] == 'x' or ban_co[7] == 'o' or thang != False:
                                        break
                                    else:
                                        pos1=(135,160)
                                        pos2=(165,190)
                                        pos3=(165,160)
                                        pos4=(135,190)
                                        all=(pos1,pos2,pos3,pos4)
                                        line.append(all)
                                        bat_dau='x'
                                        ban_co[7]='x'
                                if thay_phien(bat_dau)=='o':
                                    if ban_co[7] == 'x' or ban_co[7] == 'o' or thang != False:
                                        break
                                    else:
                                        pos=(150,175)
                                        circles.append(pos)
                                        bat_dau='o'
                                        ban_co[7]='o'
                                thay_phien(bat_dau)

                            if (175 < mouse_x < 225) and (150 < mouse_y < 200): #Ô9
                                if thay_phien(bat_dau)=='x':
                                    if ban_co[8] == 'x' or ban_co[8] == 'o' or thang != False:
                                        break
                                    else:
                                        pos1=(185,160)
                                        pos2=(215,190)
                                        pos3=(215,160)
                                        pos4=(185,190)
                                        all=(pos1,pos2,pos3,pos4)
                                        line.append(all)
                                        bat_dau='x'
                                        ban_co[8]='x'
                                if thay_phien(bat_dau)=='o':
                                    if ban_co[8] == 'x' or ban_co[8] == 'o' or thang != False:
                                        break
                                    else:
                                        pos=(200,175)
                                        circles.append(pos)
                                        bat_dau='o'
                                        ban_co[8]='o'
                                thay_phien(bat_dau)
                                        
            kieu_thang_x=ktra_kieu_thang('x')
            kieu_thang_o=ktra_kieu_thang('o')

            if ktra_thang_all('x') == 'x':
                thang = ktra_thang_all('x')
           
            if ktra_thang_all('o') == 'o':
                thang = ktra_thang_all('o')
                                                       
            if ktra_danh_full_chua() == True and thang == False:
                hoa=True 
                    
        if thay_phien(bat_dau)!=' ' and ket_thuc== False:
            # Tạo chữ từ font đã thiết lập
            text = font1.render("LƯỢT CỦA" + ' ' + str(thay_phien(bat_dau)), True, MAU_X)
            # Hiển thị chữ lên cửa sổ
            screen.blit(text, (120, 235))
        
        if thang == 'x':
            if kieu_thang_x == 1 :
                pos1=(75,75)
                pos2=(225,75)
                pos_win_x=(pos1,pos2)
                win_x.append(pos_win_x)
            if kieu_thang_x == 2 :
                pos1=(75,125)
                pos2=(225,125)
                pos_win_x=(pos1,pos2)
                win_x.append(pos_win_x)
            if kieu_thang_x == 3 :
                # pygame.draw.line(screen, MAU_X, (75, 150), (225, 150), 5)
                pos1=(75,175)
                pos2=(225,175)
                pos_win_x=(pos1,pos2)
                win_x.append(pos_win_x)
            if kieu_thang_x == 4 :
                # pygame.draw.line(screen, MAU_X, (100, 50), (100, 200), 5)
                pos1=(100,50)
                pos2=(100,200)
                pos_win_x=(pos1,pos2)
                win_x.append(pos_win_x)
            if kieu_thang_x == 5 :
                # pygame.draw.line(screen, MAU_X, (150, 50), (150, 200), 5)
                pos1=(150,50)
                pos2=(150,200)
                pos_win_x=(pos1,pos2)
                win_x.append(pos_win_x)
            if kieu_thang_x == 6 :
                # pygame.draw.line(screen, MAU_X,  (200, 50), (200, 200), 5)
                pos1=(200,50)
                pos2=(200,200)
                pos_win_x=(pos1,pos2)
                win_x.append(pos_win_x)
            if kieu_thang_x == 7 :
                # pygame.draw.line(screen, MAU_X, (80,55), (220,195), 5)
                pos1=(80,55)
                pos2=(220,195)
                pos_win_x=(pos1,pos2)
                win_x.append(pos_win_x)
            if kieu_thang_x == 8 :
                # pygame.draw.line(screen, MAU_X, (220,55), (80,195), 5)
                pos1=(220,55)
                pos2=(80,195)
                pos_win_x=(pos1,pos2)
                win_x.append(pos_win_x)

            #in thong bao win
            text = font.render("CHIẾN THẮNG", True, MAU_X)
            screen.blit(text, (50, 310)) 

            #in x win
            pos1=(135,270)
            pos2=(165,300)
            pos3=(165,270)
            pos4=(135,300)
            all=(pos1,pos2,pos3,pos4)
            line.append(all)
            ket_thuc=True

        if thang == 'o':
            if kieu_thang_o == 1 :
                pos1=(75,75)
                pos2=(225,75)
                pos_win_o=(pos1,pos2)
                win_o.append(pos_win_o)
            if kieu_thang_o == 2 :
                pos1=(75,125)
                pos2=(225,125)
                pos_win_o=(pos1,pos2)
                win_o.append(pos_win_o)
            if kieu_thang_o == 3 :
                # pygame.draw.line(screen, MAU_X, (75, 150), (225, 150), 5)
                pos1=(75,175)
                pos2=(225,175)
                pos_win_o=(pos1,pos2)
                win_o.append(pos_win_o)
            if kieu_thang_o == 4 :
                # pygame.draw.line(screen, MAU_X, (100, 50), (100, 200), 5)
                pos1=(100,50)
                pos2=(100,200)
                pos_win_o=(pos1,pos2)
                win_o.append(pos_win_o)
            if kieu_thang_o == 5 :
                # pygame.draw.line(screen, MAU_X, (150, 50), (150, 200), 5)
                pos1=(150,50)
                pos2=(150,200)
                pos_win_o=(pos1,pos2)
                win_o.append(pos_win_o)
            if kieu_thang_o == 6 :
                # pygame.draw.line(screen, MAU_X,  (200, 50), (200, 200), 5)
                pos1=(200,50)
                pos2=(200,200)
                pos_win_o=(pos1,pos2)
                win_o.append(pos_win_o)
            if kieu_thang_o == 7 :
                # pygame.draw.line(screen, MAU_X, (80,55), (220,195), 5)
                pos1=(80,55)
                pos2=(220,195)
                pos_win_o=(pos1,pos2)
                win_o.append(pos_win_o)
            if kieu_thang_o == 8 :
                # pygame.draw.line(screen, MAU_X, (220,55), (80,195), 5)
                pos1=(220,55)
                pos2=(80,195)
                pos_win_o=(pos1,pos2)
                win_o.append(pos_win_o)

            #in thong bao win
            text = font.render("CHIẾN THẮNG", True, MAU_O)           
            screen.blit(text, (50, 310))

            #in o win  
            pos=(150,285)
            circles.append(pos)
            ket_thuc=True

        if hoa==True:
            text = font.render("HÒA", True, MAU_X)
            # Hiển thị chữ lên cửa sổ
            screen.blit(text, (120, 310)) 
            ket_thuc=True

            pos1=(110,270)
            pos2=(140,300)
            pos3=(140,270)
            pos4=(110,300)
            all=(pos1,pos2,pos3,pos4)
            line.append(all)

            pos=(175,285)
            circles.append(pos)
               
        for pos in circles:
            pygame.draw.circle(screen, MAU_O, pos, 20, width=5)

        for all in line:
            pos1, pos2, pos3, pos4 = all 
            pygame.draw.line(screen, MAU_X, pos1, pos2, 5)
            pygame.draw.line(screen, MAU_X, pos3, pos4, 5)
        
        for pos_win_x in win_x:
            posa, posb = pos_win_x
            pygame.draw.line(screen, MAU_X, posa, posb, 5)

        for pos_win_o in win_o:
            posa, posb = pos_win_o
            pygame.draw.line(screen, MAU_O, posa, posb, 5)

        if ket_thuc == True:
            #in tro choi end
            text = font1.render("TRÒ CHƠI KẾT THÚC", True, MAU_X)
            screen.blit(text, (100, 235))

            # Tạo ra nút reset
            image = pygame.transform.scale(image, (20, 20))
            screen.blit(image, (140,20))

        pygame.display.flip()      
choi(circles, line, win_o, win_x, ban_co, bat_dau,  kieu_thang_x, kieu_thang_o, running, thang, hoa, ket_thuc)

pygame.QUIT()