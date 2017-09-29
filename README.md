# Raspberry Pi ADS1299 Driver

<p align="center">
  <img alt="banner" src="/images/banner.jpg/" width="600">
</p>
<p align="center" href="">
  A High Level Driver for ADS1299 Control with Raspberry Pi
</p>

## Install

### Using PyPI

```
pip install RaspberryPiADS1299
```

Anaconda is not currently supported, if you want to use anaconda, you need to create a virtual environment in anaconda, activate it and use the above command to install it.

### From sources

For the latest version, you can install the package from the sources using the setup.py script

```
python setup.py install
```

or in developer mode to be able to modify the sources.

```
python setup.py develop
```

## Hardware Configuration

The Raspberry Pi 3 is used as a reference

|Signal  |  RPi Pin  |  ADS Pin|
|--------|:---------:|----------:|
|MOSI    |     19    |    DIN|
|MISO    |     21    |    DOUT|
|SCLK    |     23    |    SCLK|
|CS      |     24    |    CS|
|START   |     15    |    START|
|RESET   |     16    |    nRESET|
|PWRDN   |     18    |    nPWRDN|
|DRDY    |     22    |    DRDY|

### Hardware Setup for EEG

Connect sensing electrode to P (+) and ref to SRB1. With default config, the API doesn't enable the bias, that should help if you want to test with only a few electrodes.

## How to use it

It is easy as :

```python
from RaspberryPiADS1299 import ADS1299_API
from time import time, sleep

# init ads api
ads = ADS1299_API()

# init device
ads.openDevice()
# attach default callback
ads.registerClient(DefaultCallback)
# configure ads
ads.configure(sampling_rate=1000)

print "ADS1299 API test stream starting"

# begin test streaming
ads.startTestStream()

# begin EEG streaming
# ads.startEegStream()

# wait
sleep(10)

print "ADS1299 API test stream stopping"

# stop device
ads.stopStream()
# clean up
ads.closeDevice()

sleep(1)
print "Test Over"

```


## Credits

### Author
Fred Simard

### Maintainer
AJ Keller (@aj-ptw)
