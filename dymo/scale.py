import usb.core
import usb.util

class USB(object):

    def __init__(self):
        VENDOR_ID  = 0x0922
        PRODUCT_ID = 0x8003

        self.device = usb.core.find(idVendor=VENDOR_ID,
                                    idProduct=PRODUCT_ID)

        if self.device.is_kernel_driver_active(0):
            self.device.detach_kernel_driver(0)

        self.device.set_configuration()
        self.endpoint = device[0][(0,0)][0]


    def get_weight_grams(self):
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

        grams = data[4] + (256 * data[5])
        return grams
