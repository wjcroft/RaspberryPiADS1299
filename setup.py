from setuptools import setup, find_packages

setup(name = 'RaspberryPiADS1299',
      packages = ['RaspberryPiADS1299'], # this must be the same as the name above
      version = '0.1.1',
      description = 'A lib for running ADS1299 on Rasberry Pi',
      author='Fredric Simard',
      author_email='frederic.simard.1@outlook.com',
      license='MIT',
      packages=find_packages(),
      install_requires=['numpy'],
      url='https://github.com/PushTheWorld/RaspberryPiADS1299',  # use the URL to the github repo
      download_url='https://github.com/PushTheWorld/RaspberryPiADS1299/archive/0.1.0.tar.gz',
      keywords=['device', 'control', 'eeg', 'emg', 'ekg', 'ads1299', 'raspberry', 'pi'],  # arbitrary keywords
      zip_safe=False)
