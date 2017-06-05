import smbus
from utils import bytes_to_word

class I2C_Channel(object):

    def __init__(self, smbus, i2c_address, channel_address):
        self.bus = smbus
        self.i2c_address = i2c_address
        self.channel_address = channel_address

    def get_value(self):
        self.bus.write_byte_data(self.i2c_address, 0x6b, 0)
        high = self.bus.read_byte_data(self.i2c_address, self.channel_address)
        low = self.bus.read_byte_data(self.i2c_address, self.channel_address+1)
        return bytes_to_word(high, low)
