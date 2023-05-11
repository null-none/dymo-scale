import usb.core
import usb.util

import math

DATA_MODE_GRAMS = 2
DATA_MODE_OUNCES = 11

VENDOR_ID  = 0x0922
PRODUCT_ID = 0x8003

class USB(object):

    def __init__(self, vendor_id=VENDOR_ID, product_id=PRODUCT_ID):

        self.device = usb.core.find(idVendor=vendor_id,
                                    idProduct=product_id)

        if self.device.is_kernel_driver_active(0):
            self.device.detach_kernel_driver(0)

        self.device.set_configuration()
        self.endpoint = self.device[0][(0,0)][0]
    
    def __del__(self):
        self.device.reset()

    def get_weight(self):
        attempts = 10
        data = None
        grams = 0
        while data is None and attempts > 0:
            try:
                data = self.device.read(self.endpoint.bEndpointAddress,
                                        self.endpoint.wMaxPacketSize)
            except usb.core.USBError as e:
                data = None
                if e.args == ('Operation timed out',):
                    attempts -= 1
                    continue

        weight = None
        raw_weight = data[4] + data[5] * 256

        if data[2] == DATA_MODE_OUNCES:
            scaling_factor = math.pow(10, (data[3] - 256))
            ounces = raw_weight * scaling_factor
            weight = ounces
        elif data[2] == DATA_MODE_GRAMS:
            grams = raw_weight
            weight = grams

        if data[1] == 5:
            weight = weight * -1

        return weight, data[2]
