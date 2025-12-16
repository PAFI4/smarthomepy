import unittest
import mock.GPIO as GPIO
from unittest.mock import patch, PropertyMock
from unittest.mock import Mock

from mock.adafruit_bmp280 import Adafruit_BMP280_I2C
from src.smart_room import SmartRoom
from mock.senseair_s8 import SenseairS8


class TestSmartRoom(unittest.TestCase):

    @patch.object(GPIO, "input")
    def test_something(self, mock_object: Mock):
        # This is an example of test where I want to mock the GPIO.input() function
        pass



    @patch.object(GPIO, "input")
    def test_room_occupancy(self, smart_room: Mock):
        # This is an example of test where I want to mock the GPIO.input() function
        smart_room.return_value=True
        smart_room=SmartRoom()
        ans=smart_room.check_room_occupancy(self.INFRARED_PIN)
        self.assertTrue(ans)

    @patch.object(GPIO, "input")
    def enough_light(self, smart_room: Mock):
        smart_room.return_value = True
        smart_room = SmartRoom()
        ans = smart_room.check_enough_light(self.PHOTO_PIN)
        self.assertTrue(ans)




