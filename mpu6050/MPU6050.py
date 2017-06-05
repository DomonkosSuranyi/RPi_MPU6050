from smbus import SMBus
from I2C_Channel import I2C_Channel

class MPU6050(object):

    def __init__(self, i2c_addr,
        addr_gyro_x = 0x43, addr_gyro_y = 0x45, addr_gyro_z = 0x47,
    addr_accel_x = 0x3b, addr_accel_y = 0x3d, addr_accel_z = 0x3f
    ):
        bus = SMBus(1)
        self.sensors = {
            "GX" : I2C_Channel(bus, i2c_addr, addr_gyro_x),
            "GY" : I2C_Channel(bus, i2c_addr, addr_gyro_y),
            "GZ" : I2C_Channel(bus, i2c_addr, addr_gyro_z),
            "AX" : I2C_Channel(bus, i2c_addr, addr_accel_x),
            "AY" : I2C_Channel(bus, i2c_addr, addr_accel_y),
            "AZ" : I2C_Channel(bus, i2c_addr, addr_accel_z)
        }

    def read_data(self, key):
        return self.sensors.get(key).get_value()

