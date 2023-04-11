import random
import arcade
from config import *


class MenuView(arcade.View):
    """ Class that manages the 'menu' view. """

    def on_show_view(self):
        """ Called when switching to this view"""
        arcade.set_background_color(arcade.color.WHITE)

    def on_draw(self):
        """ Draw the menu """
        self.clear()
        arcade.draw_text("Reciclaje por Juan y Teodoro", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2,
                         arcade.color.BLACK, font_size=30, anchor_x="center")

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        """ Use a mouse press to advance to the 'game' view. """
        game_view = MyGame()
        game_view.setup()
        self.window.show_view(game_view)


class GameOverView(arcade.View):
    """ Class that manages the 'menu' view. """

    def __init__(self):
        super().__init__()
        self.final_score = 0

    def on_show_view(self):
        """ Called when switching to this view"""
        arcade.set_background_color(arcade.color.WHITE)

    def on_draw(self):
        """ Draw the menu """
        self.clear()
        arcade.draw_text(f"Game Over    Your Final Score: {int(self.final_score)}", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2,
                         arcade.color.BLACK, font_size=30, anchor_x="center")

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        """ Use a mouse press to advance to the 'game' view. """
        arcade.exit()


class MyGame(arcade.View):
    """ Our custom Window Class"""

    def __init__(self):
        """ Initializer """
        # Call the parent class initializer
        super().__init__()

        # Variables that will hold sprite lists
        self.waste_list = None

        # Set up the game info
        self.waste_sprite = None
        self.score = 0
        self.lives = 0
        self.multi = 0.0
        self.waste_name = None
        self.background = None

        # Don't show the mouse cursor
        self.window.set_mouse_visible(False)

        arcade.set_background_color(arcade.color.AMAZON)

    def setup(self):
        """ Set up the game and initialize the variables. """

        # Sprite lists
        self.waste_list = arcade.SpriteList()

        # Score
        self.score = 0
        self.multi = 1.0

        # Set up the waste
        # Images of waste are drawn by JuanVaz2002
        self.waste_name = random.choice(random_waste_list)
        random_waste_list.remove(self.waste_name)
        img = f"assets/{self.waste_name}"
        self.waste_sprite = arcade.Sprite(img, SPRITE_SCALING_WASTE)
        self.waste_sprite.center_x = self.window.width / 2
        self.waste_sprite.center_y = self.window.height / 2
        self.waste_list.append(self.waste_sprite)
        self.lives = 5

        # Set up the background
        self.background = arcade.load_texture(f"assets/{MAP_NAME}")

    def on_draw(self):
        """ Draw everything """
        self.clear()
        # Draw the background texture
        arcade.draw_lrwh_rectangle_textured(0, 0, self.window.width, self.window.height, self.background)
        self.waste_list.draw()

        # Put the text on the screen.
        output = f"Score: {int(self.score)}  Lives: {int(self.lives)}"
        arcade.draw_text(text=output, start_x=10, start_y=20,
                         color=arcade.color.WHITE, font_size=14)

    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):
        if button == arcade.MOUSE_BUTTON_LEFT or button == arcade.MOUSE_BUTTON_RIGHT:
            if 95 < x < 275 and 350 < y < 485:  # Orgánico
                if self.waste_name in organic_waste_list:
                    self.gain_point()
                else:
                    self.lose_point_and_life()

            if 310 < x < 480 and 350 < y < 485:  # Desechos Peligrosos
                if self.waste_name in danger_waste_list:
                    self.gain_point()
                else:
                    self.lose_point_and_life()

            if 500 < x < 680 and 350 < y < 485:  # Vidrio
                if self.waste_name in glass_waste_list:
                    self.gain_point()
                else:
                    self.lose_point_and_life()

            if 95 < x < 275 and 60 < y < 340:  # Papel
                if self.waste_name in paper_waste_list:
                    self.gain_point()
                else:
                    self.lose_point_and_life()

            if 310 < x < 480 and 60 < y < 340:  # Desechos en General
                if self.waste_name in general_waste_list:
                    self.gain_point()
                else:
                    self.lose_point_and_life()

            if 500 < x < 680 and 60 < y < 340:  # Plásticos y envases metálicos
                if self.waste_name in plastic_metal_waste_list:
                    self.gain_point()
                else:
                    self.lose_point_and_life()

            self.change_waste()

    def on_mouse_release(self, x: int, y: int, button: int, modifiers: int):
        pass

    def on_mouse_motion(self, x, y, dx, dy):
        """ Handle Mouse Motion """

        # Move the center of the player sprite to match the mouse x, y
        self.waste_sprite.center_x = x
        self.waste_sprite.center_y = y

    def on_update(self, delta_time):
        if len(random_waste_list) == 0 or self.lives == 0:
            game_over_view = GameOverView()
            game_over_view.final_score = self.score
            self.window.set_mouse_visible(True)
            self.window.show_view(game_over_view)

    def change_waste(self):
        self.waste_list.pop(0)
        self.waste_name = random.choice(random_waste_list)
        random_waste_list.remove(self.waste_name)
        img = f"assets/{self.waste_name}"
        self.waste_sprite = arcade.Sprite(img, SPRITE_SCALING_WASTE)
        self.waste_sprite.center_x = self.window.width / 2
        self.waste_sprite.center_y = self.window.height / 2
        self.waste_list.append(self.waste_sprite)

    def gain_point(self):
        self.score += (150 * self.multi)
        if self.multi < 1.5:
            self.multi += 0.1

    def lose_point_and_life(self):
        if self.score - 100 < 0:
            self.score = 0
        else:
            self.score -= 100

        self.lives -= 1
        self.multi = 1.0


def main():
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    menu_view = MenuView()
    window.show_view(menu_view)
    arcade.run()


if __name__ == "__main__":
    main()
