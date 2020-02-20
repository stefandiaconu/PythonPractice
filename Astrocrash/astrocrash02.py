class Ship(games.Sprite):
    """ The player's ship. """
    image = games.load_image("ship.bmp")
    ROTATION_STEP = 3
    MISSILE_DELAY = 25

    def __init__(self, x, y):
        """Initialize ship sprite. """
        super(Ship, self).__init__(image = Ship.image, x = x, y = y)
        self.missile_wait = 0

    def update(self):
        """ Rotate based on keys pressed. """
        if games.keyboard.is_pressed(games.K_LEFT):
            self.angle -= Ship.ROTATION_STEP
        if games.keyboard.is_pressed(games.K_RIGHT):
            self.angle += Ship.ROTATION_STEP

        # fire missile if spacebar pressed
        if games.keyboard.is_pressed(games.K_SPACE):
            games.screen.add(new_missile)

        # if waiting until the ship can fire next, decrease wait
        if self.missile_wait > 0:
            self.missile_wait -= 1

        # fire missile if space bar pressed and missile wait is over
        if games.keyboard.is_pressed(games.K_SPACE) and self.missile_wait == 0:
            new_missile = Missile(self.x, self.y, self.angle)
            games.screen.add(new_missile)
            self.missile_wait = Ship.MISSILE_DELAY

        # check if ship overlaps any other object
        if self.overlapping_sprites:
            for sprite in self.overlapping_sprites:
                sprite.die()
            self.die()

    def die(self):
        """ Destroy ship. """
        self.destroy()

    # create the ship
    the_ship = Ship(image = Ship.image,
                    x = games.screen.width/2,
                    y = games.screen.height/2)
    games.screen.add(the_ship)