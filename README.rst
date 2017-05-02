Reading information from Dymo USB scale.


=======
Install
=======

.. code-block:: bash

    sudo apt-get install python libusb-1.0-0
    # Create text file /etc/udev/rules.d/99-garmin.rules with contents:
    # SUBSYSTEM=="usb", ATTR{idVendor}=="0922", ATTR{idProduct}=="8003", MODE="666" 

.. code-block:: bash

    pip install python-dymo-scale

=======
Example
=======

.. code-block:: python

  from dymo import scale

  usb = scale.USB()
  print usb.get_weight_grams()


=======
Donation
=======

.. image:: https://img.shields.io/badge/Donate-PayPal-green.svg
  :target: https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=YYZQ6ZRZ3EW5C
