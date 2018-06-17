#!/usr/bin/python3

from subprocess import check_output, call

while True:
    value = float(str(check_output(["/opt/vc/bin/vcgencmd", "measure_temp"]))[7:-5])

    if (value > 60):
        print("too hot")
        call(["cpufreq-set", "-r", "-f", "600000"])
    else:
        print("its alright")
        call(["cpufreq-set", "-r", "-f", "1200000"])
