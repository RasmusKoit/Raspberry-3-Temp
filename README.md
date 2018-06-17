# Temp Controll

Controls CPU speed based on temperature

## Requirements

* cpufreq
    ```sudo apt-get install cpufrequtils```
    
## Installation

Enable modifications to CPU speed

```
sudo sh -c "echo userspace > /sys/devices/system/cpu/cpu0/cpufreq/scaling_governor"
```

Place python script into proper destination

```
sudo nano /usr/bin/temp_controll.py
```

Depending on your situation you might want to edit the python script for different temperature.

Now place the service file to run said script

```
sudo nano /lib/systemd/system/temp_controll.service
```


## Enable and run

```
sudo systemctl enable temp_controll.service
sudo systemctl start temp_controll
```