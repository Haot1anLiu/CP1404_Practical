from kivy.app import App
from kivy.lang import Builder
from kivy.app import StringProperty

MILES_TO_KM = 1.61

class MilesConverterApp(App):
    message = StringProperty()
    """ MilesConverterApp is a Kivy App for converting miles to kilometres """
    def build(self):
        """Build the Kivy app form the kv file"""
        self.title = "Convert Miles to Kilometers"
        self.root = Builder.load_file('convert_miles_km.kv')
        self.message = '54.717'
        return self.root

    def handle_convert(self):
        value = self.check_valid_input()
        result = value * MILES_TO_KM
        self.message = str(result)

    def handle_increment(self, change):
        value = self.check_valid_input() + change
        self.root.ids.input_value.text = str(value)
        self.handle_convert()

    def check_valid_input(self):
        try:
            value = float(self.root.ids.input_value.text)
            return value
        except ValueError:
            return 0


MilesConverterApp().run()