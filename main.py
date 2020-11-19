from kivy.app import App
from kivy.uix.widget import Widget
import kivy
from kivy import properties
from kivy.vector import Vector
from kivy.clock import Clock
import random

class paddle(Widget):
    def collision(self, ball):
        if self.collide_widget(ball):
            ball.velocity = Vector(10, 0).rotate(random.randint(45, 145))
            ball.velocity_x *= -1.01 
            
class ball(Widget):
    kivy.lang.Builder.load_file("/home/mmohdbilal/KIVY /KIVY-2/style.kv")
    velocity_x = properties.NumericProperty(0)
    velocity_y = properties.NumericProperty(0)
    velocity = properties.ReferenceListProperty(velocity_x, velocity_y)
    
    def move(self):
        self.pos = Vector(*self.velocity) + self.pos
        
        
class app(Widget):
    
    pongball = properties.ObjectProperty(None)
    player = properties.ObjectProperty(None)
    opponent =  properties.ObjectProperty(None)
    score = properties.NumericProperty(0)
    game = properties.ObjectProperty(None)

    def serve(self):
        self.game = "off"
        
    def on_touch_down(self, touch):
        if touch.x <= self.width and self.game == "off":
            self.pongball.velocity = Vector(0, 0)
                
    def on_touch_up(self, touch):
        if touch.x <= self.width and self.game == "off":
            self.pongball.velocity = Vector(10, 0).rotate(random.randint(60, 300))
            self.game = "on"
    
           
    def update(self, dt):
        self.pongball.move()
        if (self.pongball.y <= 30) or (self.pongball.y >= self.height-45):
            self.pongball.velocity_y *= -1
            
        if (self.pongball.x <= 0) or (self.pongball.x >= self.width-25):
            self.score += 1
            self.pongball.velocity_x *= -1
        
        if (self.player.y <= 0) :
            self.player.y +=20
        if (self.player.y >= self.height-125):
             self.player.y -=20
             
        if (self.opponent.y <= 0) :
            self.opponent.y +=20
        if (self.opponent.y >= self.height-125):
             self.opponent.y -=20
             
             
        self.player.collision(self.pongball)
        self.opponent.collision(self.pongball)
        
    
    def on_touch_move(self, touch):
        if touch.x <= self.width/4:
            self.player.center_y = touch.y
            
        if touch.x >= self.width - self.width/4:
            self.opponent.center_y = touch.y
        
        

class MyApp(App):
    def build(self):
        game = app()
        game.serve()
        Clock.schedule_interval(game.update, 1.00/60.00)
        return game
    
MyApp().run()