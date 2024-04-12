import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QRadioButton, QPushButton
from gpiozero import LED

class LEDController(QWidget):
    def __init__(RGB):
        super().__init__()
        RGB.initUI()

    def initUI(RGB):
        RGB.setWindowTitle("LED Controller")

        # Define LED pins
        RGB.LED_pins = [18, 23, 24]

        # Setup LED objects
        RGB.leds = [LED(pin) for pin in RGB.LED_pins]

        # Create radio buttons for LEDs
        RGB.radio_buttons = []
        for led in RGB.leds:
            radio_button = QRadioButton(f"LED {led.pin}", RGB)
            radio_button.toggled.connect(lambda state, led=led: RGB.toggle_led(state, led))
            RGB.radio_buttons.append(radio_button)

        # Create exit button
        RGB.exit_button = QPushButton("Exit", RGB)
        RGB.exit_button.clicked.connect(RGB.close)

        # Layout setup
        layout = QVBoxLayout()
        for button in RGB.radio_buttons:
            layout.addWidget(button)
        layout.addWidget(RGB.exit_button)

        RGB.setLayout(layout)
        RGB.show()

    # Function to toggle LED state
    def toggle_led(RGB, state, led):
        if state:
            led.on()
        else:
            led.off()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = LEDController()
    sys.exit(app.exec_())
