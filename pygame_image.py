import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")
    bg_img2 = pg.image.load("fig/pg_bg.jpg")
    bg_img2 = pg.transform.flip(bg_img2,True, False)
    kk_img = pg.image.load("fig/3.png") #練習問題2 こうかとん画像読み込み
    kk_img = pg.transform.flip(kk_img, True, False) #引数(画像Surface,左右反転,上下反転)
    kk_rct = kk_img.get_rect() #練習問題8-1 SurfaceからRectを抽出する
    kk_rct.center = 300, 200 #練習問題8-2 初期座標を設定

    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        
        key_lst = pg.key.get_pressed() #練習問題8-3 key方向
        if key_lst[pg.K_UP]:
            kk_rct.move_ip((0,-1)) #(横方向速度, 縦方向速度)
        if key_lst[pg.K_DOWN]:
            kk_rct.move_ip((0,1))
        if key_lst[pg.K_LEFT]:
            kk_rct.move_ip((-1,0))
        if key_lst[pg.K_RIGHT]:
            kk_rct.move_ip((1,0))

        x = -(tmr%3200)
        screen.blit(bg_img, [x, 0])
        screen.blit(bg_img2,[x+1600, 0])
        screen.blit(bg_img, [x+3200, 0])#練習問題8-5 描画
        screen.blit(kk_img, kk_rct) #練習問題4 こうかとん描画
        
        pg.display.update()
        tmr += 1        
        clock.tick(200) #練習問題5 FPSを200に変更


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()