import math
import arcade
WINDOW_WIDTH = 1920
WINDOW_HEIGHT = 1080
Width = 1860
Height = 1000
WINDOW_TITLE = "chaser and runner"
speed1 = 10
speed2 = 6
obrad = 40
class GameView(arcade.Window):
    def __init__(self):
        super().__init__(WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_TITLE)
        self.player_sprite1 = None
        self.player_sprite2 = None
        self.game_over = False
        self.single_player = False
    def keep_in_rectangle(self, sprite,):
        dx = Width
        dy = Height
        if sprite.center_x > dx:
            sprite.center_x = dx
        elif sprite.center_y > dy:
            sprite.center_y = dy
        elif sprite.center_x < 60:
            sprite.center_x = 60
        elif sprite.center_y < 130:
            sprite.center_y = 130
    def ai_control(self, ai_sprite, target_sprite, speed = 7):
        if target_sprite.center_x > ai_sprite.center_x:
            ai_sprite.change_x = speed
        elif target_sprite.center_x < ai_sprite.center_x:
            ai_sprite.change_x = -speed
        else:
            ai_sprite.change_x = 0
        if target_sprite.center_y > ai_sprite.center_y:
            ai_sprite.change_y = speed
        elif target_sprite.center_y < ai_sprite.center_y:
            ai_sprite.change_y = -speed
        else:
            ai_sprite.change_y = 0
    def on_update(self, delta_time):
        self.physics_player1.update()
        self.engine2.update()
        if arcade.check_for_collision(self.player_sprite1, self.player_sprite2):
            self.game_over = True
        
        if self.single_player:
            self.ai_control(self.player_sprite2, self.player_sprite1)
        self.keep_in_rectangle(self.player_sprite1)
        self.keep_in_rectangle(self.player_sprite2)
        return super().on_update(delta_time)
    def setup(self):
        self.background_color = arcade.csscolor.BLACK
        self.player_texture1 = arcade.load_texture(":resources:images/animated_characters/male_adventurer/maleAdventurer_idle.png")
        self.player_texture2 = arcade.load_texture(":resources:images/animated_characters/female_adventurer/femaleAdventurer_idle.png")
        self.player_sprite1 = arcade.Sprite(self.player_texture1)
        self.player_sprite1.center_x = WINDOW_WIDTH/2
        self.player_sprite1.center_y = WINDOW_HEIGHT/1.35
        self.player_sprite2 = arcade.Sprite(self.player_texture2)
        self.player_sprite2.center_x = WINDOW_WIDTH/2
        self.player_sprite2.center_y = WINDOW_HEIGHT/2.95
        self.obstacles = arcade.SpriteList()
        square1 = arcade.SpriteCircle(obrad,arcade.color.RED,False,300,250)
        self.obstacles.append(square1)
        square2 = arcade.SpriteCircle(obrad,arcade.color.BLUE,False,960,200)
        self.obstacles.append(square2)
        square3 = arcade.SpriteCircle(obrad,arcade.color.GREEN,False,1600,250)
        self.obstacles.append(square3)
        square4 = arcade.SpriteCircle(obrad,arcade.color.YELLOW,False,300,750)
        self.obstacles.append(square4)
        square5 = arcade.SpriteCircle(obrad,arcade.color.PURPLE,False,960,900)
        self.obstacles.append(square5)
        square6 = arcade.SpriteCircle(obrad,arcade.color.MAGENTA,False,1600,750)
        self.obstacles.append(square6)
        square7 = arcade.SpriteCircle(40,arcade.color.ORANGE,False,WINDOW_WIDTH/2,WINDOW_HEIGHT/2)
        self.obstacles.append(square7)
        self.engine2 = arcade.PhysicsEngineSimple(self.player_sprite2)
        self.physics_player1 = arcade.PhysicsEngineSimple(self.player_sprite1, self.obstacles)
    def on_draw(self):
        self.clear()
        arcade.draw_lbwh_rectangle_outline(20,60,Width,Height,arcade.color.RED,border_width=10)
        if self.game_over:
            arcade.draw_text("GAME OVER",WINDOW_WIDTH / 2,WINDOW_HEIGHT / 2,arcade.color.WHITE,font_size=80,anchor_x="center",anchor_y="center")
            return
        arcade.draw_sprite(self.player_sprite1)
        arcade.draw_sprite(self.player_sprite2)
        self.obstacles.draw()
    def on_key_press(self, symbol, modifiers):
        if symbol == arcade.key.UP:
            self.player_sprite1.change_y= speed1
        elif symbol == arcade.key.DOWN:
            self.player_sprite1.change_y = -speed1
        elif symbol == arcade.key.LEFT:
            self.player_sprite1.change_x = -speed1
        elif symbol == arcade.key.RIGHT:
            self.player_sprite1.change_x = speed1
        elif symbol == arcade.key.W:
            self.player_sprite2.change_y= speed2
        elif symbol == arcade.key.S:
            self.player_sprite2.change_y = -speed2
        elif symbol == arcade.key.A:
            self.player_sprite2.change_x = -speed2
        elif symbol == arcade.key.D:
            self.player_sprite2.change_x = speed2
        elif symbol == arcade.key.ESCAPE:
            self.setup()
            self.game_over = False
        return super().on_key_press(symbol, modifiers)
    def on_key_release(self, symbol, modifiers):
        if symbol == arcade.key.UP:
            self.player_sprite1.change_y= 0
        elif symbol == arcade.key.DOWN:
            self.player_sprite1.change_y = 0
        elif symbol == arcade.key.LEFT:
            self.player_sprite1.change_x = 0
        elif symbol == arcade.key.RIGHT:
            self.player_sprite1.change_x = 0
        elif symbol == arcade.key.W:
            self.player_sprite2.change_y= 0
        elif symbol == arcade.key.S:
            self.player_sprite2.change_y = 0
        elif symbol == arcade.key.A:
            self.player_sprite2.change_x = 0
        elif symbol == arcade.key.D:
            self.player_sprite2.change_x = 0
        return super().on_key_release(symbol, modifiers)
def main():
    window = GameView()
    window.setup()
    arcade.run()
if __name__ == "__main__":
    main()
