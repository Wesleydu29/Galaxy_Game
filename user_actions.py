from kivy.uix.relativelayout import RelativeLayout

def keyboard_closed(self):
        self._keyboard.unbind(on_key_down=self._on_keyboard_down)
        self._keyboard.unbind(on_key_up=self._on_keyboard_up)
        self._keyboard = None


def on_keyboard_down(self, keyboard, keycode, text, modifiers):
        if keycode[1] == 'left':
            self.current_speed_x = self.speed_x
        elif keycode[1] == 'right':
            self.current_speed_x = -self.speed_x
        return True

    
def on_keyboard_up(self, keyboard, keycode):
    self.current_speed_x = 0
        
    
def on_touch_down(self, touch): # to mobile phone
    if not self.state_game_over and self.state_game_started:
        if touch.x < self.width/2: # slide to the left
            self.current_speed_x = self.speed_x
        else:
            self.current_speed_x = -self.speed_x # slide to the right
    return super(RelativeLayout, self).on_touch_down(touch) #parent class
    
def on_touch_up(self, touch): 
    self.current_speed_x = 0