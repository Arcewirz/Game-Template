from constants import *
from playerSprite import PlayerSprite
import arcade

class MenuView(arcade.View):

    def __init__(self):
        super(MenuView, self).__init__()
        self.music = None
        self.current_player = None

    def play_song(self):
        """Play the song. """
        self.music = arcade.Sound("sounds/menu music.wav", streaming=True)
        self.current_player = self.music.play(MUSIC_VOLUME)

    def on_show(self):
        """ This is run once when we switch to this view """
        # Reset the viewport, necessary if we have a scrolling game and we need
        # to reset the viewport back to the start so we can see what we draw.
        arcade.set_viewport(0, SCREEN_WIDTH - 1, 0, SCREEN_HEIGHT - 1)
        self.play_song()

    def on_draw(self):
        """ Draw this view """
        background = arcade.load_texture(":resources:images/backgrounds/abstract_1.jpg")
        arcade.draw_lrwh_rectangle_textured(0,0,SCREEN_WIDTH, SCREEN_HEIGHT, background)
        arcade.draw_text("JUMP KNIGHT", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 1.2,
                         arcade.color.WHITE, font_size=70, anchor_x="center", font_name='GARA')
        arcade.draw_text("PLAY [1]", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 1.6,
                         arcade.color.WHITE, font_size=40, anchor_x="center", font_name='GARA')
        arcade.draw_text("RULES [2]", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2.2,
                         arcade.color.WHITE, font_size=40, anchor_x="center", font_name='GARA')
        arcade.draw_text("ABOUT AUTHOR [3]", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 4,
                         arcade.color.WHITE, font_size=40, anchor_x="center", font_name='GARA')
        arcade.draw_text("EXIT [ESC]", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 20,
                         arcade.color.WHITE, font_size=40, anchor_x="center", font_name='GARA')
        arcade.draw_text("To choose, press the key given in square brackets.", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 1.35,
                         arcade.color.WHITE, font_size=20, anchor_x="center", font_name='GARA')



    def on_key_press(self, _key, _modifiers):
        """ If the user presses key, a given action will happen. """
        if _key == arcade.key.KEY_1 or _key == arcade.key.NUM_1:
            choose_view = GamemodeView()
            self.window.show_view(choose_view)
            self.music.stop(self.current_player)
        elif _key == arcade.key.KEY_2 or _key == arcade.key.NUM_2:
            rules_view = RulesView()
            self.window.show_view(rules_view)
            self.music.stop(self.current_player)
        elif _key == arcade.key.KEY_3 or _key == arcade.key.NUM_3:
            author_view = AuthorView()
            self.window.show_view(author_view)
            self.music.stop(self.current_player)
        elif _key == arcade.key.ESCAPE:
            self.window.close()

class RulesView(arcade.View):
    def on_show(self):
        """ This is run once when we switch to this view """
        # Reset the viewport, necessary if we have a scrolling game and we need
        # to reset the viewport back to the start so we can see what we draw.
        arcade.set_viewport(0, SCREEN_WIDTH - 1, 0, SCREEN_HEIGHT - 1)
    def on_draw(self):
        """ Draw this view """
        background = arcade.load_texture(":resources:images/backgrounds/abstract_1.jpg")
        arcade.draw_lrwh_rectangle_textured(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, background)
        arcade.draw_text("Apparently you have to just jump higher and try not to fall. \n"
                         "Collecting DRAGON COINS for better score is also nice.\n"
                         "To jump just press SPACE. The longer you hold the bigger the jump! \n"
                         "For walking and jump direction use arrows.", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 1.5,
                         arcade.color.WHITE, font_size=30, anchor_x="center", font_name='GARA')
        arcade.draw_text("BACK [ESC]", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 20,
                         arcade.color.WHITE, font_size=40, anchor_x="center", font_name='GARA')


    def on_key_press(self, _key, _modifiers):
        if _key == arcade.key.BACKSPACE or _key == arcade.key.ESCAPE:
            start_view = MenuView()
            self.window.show_view(start_view)

class AuthorView(arcade.View):
    def on_show(self):
        """ This is run once when we switch to this view """
        # Reset the viewport, necessary if we have a scrolling game and we need
        # to reset the viewport back to the start so we can see what we draw.
        arcade.set_viewport(0, SCREEN_WIDTH - 1, 0, SCREEN_HEIGHT - 1)

    def on_draw(self):
        """ Draw this view """
        background = arcade.load_texture(":resources:images/backgrounds/abstract_1.jpg")
        arcade.draw_lrwh_rectangle_textured(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, background)
        arcade.draw_text("I am just a normal boy studying maths and doing projects. \n"
                         "I love Jump King, thats why I came up with my own version.\n"
                         "I hope you will have fun!", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 1.5,
                         arcade.color.WHITE, font_size=30, anchor_x="center", font_name='GARA')
        arcade.draw_text("BACK [ESC]", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 20,
                         arcade.color.WHITE, font_size=40, anchor_x="center", font_name='GARA')

    def on_key_press(self, _key, _modifiers):
        if _key == arcade.key.BACKSPACE or _key == arcade.key.ESCAPE:
            start_view = MenuView()
            self.window.show_view(start_view)

class GamemodeView(arcade.View):
    def on_show(self):
        """ This is run once when we switch to this view """
        # Reset the viewport, necessary if we have a scrolling game and we need
        # to reset the viewport back to the start so we can see what we draw.
        arcade.set_viewport(0, SCREEN_WIDTH - 1, 0, SCREEN_HEIGHT - 1)

    def on_draw(self):
        """ Draw this view """
        background = arcade.load_texture(":resources:images/backgrounds/abstract_1.jpg")
        arcade.draw_lrwh_rectangle_textured(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, background)
        arcade.draw_text("CHOOSE A LEVEL", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 1.3,
                         arcade.color.WHITE, font_size=50, anchor_x="center", font_name='GARA')
        arcade.draw_text("TUTORIAL [1]", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 1.6,
                         arcade.color.WHITE, font_size=40, anchor_x="center", font_name='GARA')
        arcade.draw_text("JUMPING ROAD [2]", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2.2,
                         arcade.color.WHITE, font_size=40, anchor_x="center", font_name='GARA')
        arcade.draw_text("BACK [ESC]", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 20,
                         arcade.color.WHITE, font_size=40, anchor_x="center", font_name='GARA')

    def on_key_press(self, _key, _modifiers):
        if _key == arcade.key.BACKSPACE or _key == arcade.key.ESCAPE:
            start_view = MenuView()
            self.window.show_view(start_view)
        elif _key == arcade.key.KEY_2 or _key == arcade.key.NUM_2:
            game_view = GameView()
            game_view.setup()
            self.window.show_view(game_view)
            start_sound = arcade.load_sound("sounds/start game sound.wav")
            arcade.play_sound(start_sound, volume=0.5)
        elif _key == arcade.key.KEY_1 or _key == arcade.key.NUM_1:
            game_view = GameView()
            game_view.setup_tutorial()
            self.window.show_view(game_view)
class WinView(arcade.View):
    def on_show(self):
        """ This is run once when we switch to this view """
        # Reset the viewport, necessary if we have a scrolling game and we need
        # to reset the viewport back to the start so we can see what we draw.
        arcade.set_viewport(0, SCREEN_WIDTH - 1, 0, SCREEN_HEIGHT - 1)

    def on_draw(self):
        """ Draw this view """
        background = arcade.load_texture(":resources:images/backgrounds/abstract_1.jpg")
        arcade.draw_lrwh_rectangle_textured(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, background)
        arcade.draw_text("CONGRATULATIONS! YOU WON!", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 1.5,
                         arcade.color.WHITE, font_size=30, anchor_x="center", font_name='GARA')
        arcade.draw_text("ADVANCE [ENTER]", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 20,
                         arcade.color.WHITE, font_size=40, anchor_x="center", font_name='GARA')

    def on_key_press(self, _key, _modifiers):
        if _key == arcade.key.ENTER:
            start_view = MenuView()
            self.window.show_view(start_view)

class GameView(arcade.View):
    """
    Main application class.
    """

    def __init__(self):

        # Call the parent class and set up the window
        super().__init__()

        self.is_tutorial = False

        self.window.set_mouse_visible(False)

        self.time_elapsed = None

        # These are 'lists' that keep track of our sprites. Each sprite schould
        # go into a list.
        self.coin_list = None
        self.wall_list = None
        self.player_list = None
        self.princess_list = None
        self.door_list = None

        # Separate variable that holds the player sprite
        self.player_list = None

        # Player sprite
        self.player_sprite: Optional[PlayerSprite] = None

        # Our physics engine
        self.physics_engine: Optional[arcade.PymunkPhysicsEngine]

        # Used to keep track of our scrolling
        self.view_bottom = None
        self.view_left = None

        # Keep track of the score
        self.score = None

        # Track the current state of what key is pressed
        self.left_pressed: bool = False
        self.right_pressed: bool = False
        self.space_pressed: bool = False
        self.player_jump_impulse = 0
        self.jump_timer = 0
        self.left_jump: bool = False
        self.right_jump: bool = False

        # Load sounds
        self.collect_coin_sound = arcade.load_sound(":resources:sounds/coin3.wav")
        self.jump_sound = arcade.load_sound(":resources:sounds/jump5.wav")

        arcade.set_background_color(arcade.csscolor.CORNFLOWER_BLUE)

    def setup(self):
        """ Set up the game here. Call this function to restart the game. """
        # Used to keep track of our scrolling
        self.view_bottom = 0
        self.view_left = 0
        self.time_elapsed = 0

        # Create the Sprite lists
        self.player_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList(use_spatial_hash=True)
        self.coin_list = arcade.SpriteList(use_spatial_hash=True)
        self.princess_list = arcade.SpriteList(use_spatial_hash=True)
        self.door_list = arcade.SpriteList(use_spatial_hash=True)

        # Set up the player, specifically placing it at these coordinates.
        self.player_sprite = PlayerSprite()
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 50
        self.player_list.append(self.player_sprite)

        self.score = 0

        self.view_bottom = 0
        self.view_left = 0

        # --- Load in a map from the tiled editor ---

        # Name of file to load
        map_name = "jumping_road.tmx"
        # Name of the layer in the file that has our platforms/walls
        platforms_layer_name = 'Platforms'
        # Name of the layer that has items for pick-up
        coins_layer_name = 'Coins'
        princess_layer_name = 'Princess'

        # Read in the tiled map
        my_map = arcade.tilemap.read_tmx(map_name)

        # -- Platforms
        self.wall_list = arcade.tilemap.process_layer(map_object=my_map,
                                                      layer_name=platforms_layer_name,
                                                      scaling=TILE_SCALING,
                                                      use_spatial_hash=True)

        # -- Coins
        self.coin_list = arcade.tilemap.process_layer(my_map, coins_layer_name, TILE_SCALING)
        # -- Princess
        image_source = "images/princess.png"
        princess = arcade.Sprite(image_source, PRINCESS_SCALING)
        princess.center_x = SCREEN_WIDTH / 8
        princess.center_y = 9472 / 4
        self.princess_list.append(princess)

        # -- Other stuff
        # Set the background color
        if my_map.background_color:
            arcade.set_background_color(my_map.background_color)

        # Create the 'physics engine'
        damping = DEFAULT_DAMPING
        gravity = (0, -GRAVITY)
        self.physics_engine = arcade.PymunkPhysicsEngine(damping=damping,
                                                         gravity=gravity)
        self.physics_engine.add_sprite(self.player_sprite,
                                       friction=PLAYER_FRICTION,
                                       mass=PLAYER_MASS,
                                       moment=arcade.PymunkPhysicsEngine.MOMENT_INF,
                                       collision_type="player",
                                       max_horizontal_velocity=PLAYER_MAX_HORIZONTAL_SPEED,
                                       max_vertical_velocity=PLAYER_MAX_VERTICAL_SPEED)
        self.physics_engine.add_sprite_list(self.wall_list,
                                            friction=WALL_FRICTION,
                                            collision_type="wall",
                                            body_type=arcade.PymunkPhysicsEngine.STATIC)

    def setup_tutorial(self):
        """ Set up the game here. Call this function to restart the game. """
        self.is_tutorial = True

        # Used to keep track of our scrolling
        self.view_bottom = 0
        self.view_left = 0
        self.time_elapsed = 0

        # Create the Sprite lists
        self.player_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList(use_spatial_hash=True)
        self.coin_list = arcade.SpriteList(use_spatial_hash=True)
        self.princess_list = arcade.SpriteList(use_spatial_hash=True)
        self.door_list = arcade.SpriteList(use_spatial_hash=True)

        # Set up the player, specifically placing it at these coordinates.
        self.player_sprite = PlayerSprite()
        self.player_sprite.center_x = 200
        self.player_sprite.center_y = 1700
        self.player_list.append(self.player_sprite)

        self.score = 0

        self.view_bottom = 0
        self.view_left = 0

        # --- Load in a map from the tiled editor ---

        # Name of file to load
        map_name = "tutorial_road.tmx"
        # Name of the layer in the file that has our platforms/walls
        platforms_layer_name = 'Platforms'
        # Name of the layer that has items for pick-up
        doors_layer_name = 'Doors'

        # Read in the tiled map
        my_map = arcade.tilemap.read_tmx(map_name)

        # -- Platforms
        self.wall_list = arcade.tilemap.process_layer(map_object=my_map,
                                                      layer_name=platforms_layer_name,
                                                      scaling=TILE_SCALING,
                                                      use_spatial_hash=True)
        # -- Doors
        self.door_list = arcade.tilemap.process_layer(map_object=my_map,
                                                      layer_name=doors_layer_name,
                                                      scaling=TILE_SCALING,
                                                      use_spatial_hash=True)


        # Create the 'physics engine'
        damping = DEFAULT_DAMPING
        gravity = (0, -GRAVITY)
        self.physics_engine = arcade.PymunkPhysicsEngine(damping=damping,
                                                         gravity=gravity)
        self.physics_engine.add_sprite(self.player_sprite,
                                       friction=PLAYER_FRICTION,
                                       mass=PLAYER_MASS,
                                       moment=arcade.PymunkPhysicsEngine.MOMENT_INF,
                                       collision_type="player",
                                       max_horizontal_velocity=PLAYER_MAX_HORIZONTAL_SPEED,
                                       max_vertical_velocity=PLAYER_MAX_VERTICAL_SPEED)
        self.physics_engine.add_sprite_list(self.wall_list,
                                            friction=WALL_FRICTION,
                                            collision_type="wall",
                                            body_type=arcade.PymunkPhysicsEngine.STATIC)

    def on_draw(self):
        """ Render the screen. """

        # Clear the screen to the background color
        arcade.start_render()

        background_texture = arcade.load_texture("images/BACKGROUND.png")
        arcade.draw_texture_rectangle((4480 / 2) / 4, (10240 / 2) / 4, 4480 / 4, 10240 / 4, background_texture)

        # Tutorial hints
        if self.is_tutorial:
            tutorial_text = "USE ARROWS TO MOVE. USE SPACE TO JUMP. \n THE LONGER YOU HOLD THE BIGGER THE JUMP."
            arcade.draw_text(tutorial_text, 50, 1700,
                             arcade.csscolor.WHITE, 40)

        # Draw our sprites
        self.coin_list.draw()
        self.player_list.draw()
        self.wall_list.draw()
        self.princess_list.draw()
        self.door_list.draw()

        # Draw our score on the screen, scrolling it with the viewport
        texture = arcade.load_texture("images/dragon coin.png")
        arcade.draw_scaled_texture_rectangle(self.view_left + SCREEN_WIDTH - 40,
                                             self.view_bottom + SCREEN_HEIGHT - 30, texture, scale=0.8)
        score_text = f"{self.score}"
        arcade.draw_text(score_text, self.view_left + SCREEN_WIDTH - 125, self.view_bottom + SCREEN_HEIGHT - 87,
                         arcade.csscolor.WHITE, 55)
        # Draw our speedrun timer
        speedrun_text = f"TIME: {self.time_elapsed:7.1f}"
        arcade.draw_text(speedrun_text, 10 + self.view_left, self.view_bottom + SCREEN_HEIGHT - 40,
                         arcade.csscolor.WHITE, 30)

    def on_key_press(self, key: int, modifiers: int):
        """Called whenever a key is pressed."""

        if key == arcade.key.LEFT:
            self.left_pressed = True
        elif key == arcade.key.RIGHT:
            self.right_pressed = True
        elif key == arcade.key.SPACE:
            self.space_pressed = True
            self.player_jump_impulse = 0
        elif key == arcade.key.ESCAPE:
            start_view = MenuView()
            self.window.show_view(start_view)
            start_view.play_song()

    def on_key_release(self, key: int, modifiers: int):
        """Called when the user releases a key."""

        if key == arcade.key.LEFT:
            self.left_pressed = False
        elif key == arcade.key.RIGHT:
            self.right_pressed = False
        elif key == arcade.key.SPACE:
            if self.right_pressed:
                self.right_jump = True
            elif self.left_pressed:
                self.left_jump = True
            self.space_pressed = False

    def on_update(self, delta_time: float):
        """Movement and game logic."""

        # Process left/right and jumping
        if self.space_pressed and self.physics_engine.is_on_ground(self.player_sprite):
            # Change texture when loading jump DOES NOT WORK
            self.player_sprite.texture = self.player_sprite.pre_jump_texture_pair[
                self.player_sprite.character_face_direction]
            if self.player_jump_impulse < MAX_JUMP_IMPULSE:
                self.player_jump_impulse += 60
            else:
                self.space_pressed = False
            self.player_sprite.change_x = 0
        elif self.player_jump_impulse > 320 and self.physics_engine.is_on_ground(self.player_sprite):
            impulse = (0, self.player_jump_impulse)
            self.physics_engine.apply_impulse(self.player_sprite, impulse)
            arcade.play_sound(self.jump_sound, volume=0.1)
            if self.right_pressed and not self.left_pressed:
                force = (PLAYER_MOVE_FORCE_IN_AIR, 0)
                self.physics_engine.apply_force(self.player_sprite, force)
            elif self.left_pressed and not self.right_pressed:
                force = (-PLAYER_MOVE_FORCE_IN_AIR, 0)
                self.physics_engine.apply_force(self.player_sprite, force)
        elif self.right_pressed and not self.left_pressed and self.physics_engine.is_on_ground(self.player_sprite):
            if self.jump_timer == 0:
                force = (PLAYER_MOVE_FORCE_ON_GROUND, 0)
                self.physics_engine.apply_force(self.player_sprite, force)
        elif self.left_pressed and not self.right_pressed and self.physics_engine.is_on_ground(self.player_sprite):
            if self.jump_timer == 0:
                force = (-PLAYER_MOVE_FORCE_ON_GROUND, 0)
                self.physics_engine.apply_force(self.player_sprite, force)
        elif self.physics_engine.is_on_ground(self.player_sprite):
            self.player_sprite.change_x = 0

        if self.physics_engine.is_on_ground(self.player_sprite):
            self.jump_timer = 0
        else:
            self.player_jump_impulse = 0
            self.jump_timer += 1

        # Move the player with the physics engine
        self.physics_engine.step()

        # See if we hit any coins, doors or princesses
        coin_hit_list = arcade.check_for_collision_with_list(self.player_sprite,
                                                             self.coin_list)
        princess_hit = arcade.check_for_collision_with_list(self.player_sprite,
                                                            self.princess_list)
        doors_hit = arcade.check_for_collision_with_list(self.player_sprite,
                                                         self.door_list)
        if princess_hit or doors_hit:
            win_view = WinView()
            self.window.show_view(win_view)

        # Loop through each coin we hit (if any) and remove it
        for coin in coin_hit_list:
            # Remove the coin
            coin.remove_from_sprite_lists()
            # Play sound
            arcade.play_sound(self.collect_coin_sound, volume=0.3)
            # Add one to the score
            self.score += 1

        # --- Manage Scrolling ---

        # Track if we need to change the viewport

        changed = False

        # Scroll up
        top_boundary = self.view_bottom + SCREEN_HEIGHT - TOP_VIEWPORT_MARGIN
        if self.player_sprite.top > top_boundary:
            self.view_bottom += self.player_sprite.top - top_boundary
            changed = True

        # Scroll down
        bottom_boundary = self.view_bottom + BOTTOM_VIEWPORT_MARGIN
        if self.player_sprite.bottom < bottom_boundary:
            self.view_bottom -= bottom_boundary - self.player_sprite.bottom
            changed = True

        if changed:
            # Only scroll to integers. Otherwise we end up with pixels that
            # don't line up on the screen
            self.view_bottom = int(self.view_bottom)
            self.view_left = int(self.view_left)

            # Do the scrolling
            arcade.set_viewport(self.view_left,
                                SCREEN_WIDTH + self.view_left,
                                self.view_bottom,
                                SCREEN_HEIGHT + self.view_bottom)
        # Managing speedrun timer
        self.time_elapsed += delta_time