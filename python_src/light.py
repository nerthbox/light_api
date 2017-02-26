import RPi.GPIO as GPIO

class Light(object):

    def __init__(self, channel, direction):
        self.channel = channel
        self.direction = direction
        self.input_value = None
        if(self.direction == "output"):
            self._init_output()
        elif(self.direction == "input"):
            self._init_input()
        else:
            print "direction must be 'input' or 'output'"
            exit(1)

        GPIO.setmode(GPIO.BOARD)
        GPIO.setwarnings(False)

    def _init_output(self):
        GPIO.setup(self.channel, GPIO.OUT, initial=GPIO.LOW)

    def _init_input(self):
        GPIO.setup(self.channel, GPIO.IN)

    def high(self):
        GPIO.output(self.channel, GPIO.HIGH)

    def low(self):
        self.input_value = GPIO.input(self.channel)

