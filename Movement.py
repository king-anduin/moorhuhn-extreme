class Player():

    def __init__(self):
        self.image = pg.Surface((50, 50)) 
        self.image.fill(GREEN)
        self.rect = self.image.get_rect() 
        self.vx, self.vy = 0, 0
        self.ax, self.ay = 0, 0
        self.x, self.y = (WIDTH / 2, HEIGHT / 2)

    def update(self):
        self.move_4way()
        # equations of motion
        self.ax += self.vx * PLAYER_FRICTION 
        self.ay += self.vy * PLAYER_FRICTION 
        self.vx += self.ax
        self.vy += self.ay
        self.x += self.vx + 0.5 * self.ax 
        self.y += self.vy + 0.5 * self.ay 
        self.rect.x = self.x
        self.rect.y = self.y

    def render(self, screen): 
        screen.blit(self.image, self.rect)

    def move_4way(self):
        self.ax = 0
        self.ay = 0
        keystate = pg.key.get_pressed() 
        if keystate[pg.K_UP]:
            self.ay = -PLAYER_ACC 
        if keystate[pg.K_DOWN]:
            self.ay = PLAYER_ACC 
        if keystate[pg.K_LEFT]: 
            self.ax = -PLAYER_ACC
        if keystate[pg.K_RIGHT]: 
            self.ax = PLAYER_ACC
        if self.ax != 0 and self.ay != 0: 
            self.ax *= 0.7071
            self.ay *= 0.7071

 # Schläger mit Maus steuern
class crosshair(Sprite):
    def events(self, mousex):
        self.x = mousex
        self.x = min(self.x, (WIDTH - (self._rect.width * 0.5)))
        self.x = max(self.x, self._rect.width * 0.5)
    def update(self, dt):
        self._rect.center = (self.x, self.y)