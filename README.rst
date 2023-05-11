Reading information from Dymo USB scale.


=======
Install
=======

.. code-block:: bash

    # sudo apt-get install python libusb-1.0-0
    # touch /etc/udev/rules.d/99-garmin.rules
    # echo 'SUBSYSTEM=="usb", ATTR{idVendor}=="0922", ATTR{idProduct}=="8003", MODE="666"' > /etc/udev/rules.d/99-garmin.rules

.. code-block:: bash

    pip install dymo-scale

=======
Example
=======

.. code-block:: python

  from dymo import scale

  usb = scale.USB(vendor_id=0x0922, product_id=0x8003)
  print usb.get_weight()


=======
Donation
=======

.. image:: https://img.shields.io/badge/Donate-PayPal-green.svg
  :target: https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=YYZQ6ZRZ3EW5C
