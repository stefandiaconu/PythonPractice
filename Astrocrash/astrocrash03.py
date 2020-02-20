import math, random

    VELOCITY_STEP = .03

    sound = games.load_sound("thrust.wav")

        # apply thrust based on up arraow key
        if games.keyboard.is_pressed(games.K_UP):
            Ship.sound.play()

            # change velocity components based on ship's angle
            angle = self.angle * math.pi / 180 # convert to radians

            self.dx += Ship.VELOCITY_STEP * math.sin(angle)
            self.dy += Ship.VELOCITY_STEP * -math.cos(angle)

        # wrap the ship around the screen
        if self.top > games.screen.height:
            self.bottom = 0

        if self.bottom < 0:
            self.top = games.screen.height
        
        if self.left > games.screen.width:
            self.right = 0

        if self.right < 0:
            self.left = games.screen.width