import psutil
import time
import psutil
import sys
import datetime
import math


def get_cpu_temperature():
    """
    from subprocess import PIPE, Popen
    process = Popen(['vcgencmd', 'measure_temp'], stdout=PIPE)
    output, _ = process.communicate()
    return output
    """

    try:
        return psutil.sensors_temperatures()['cpu_thermal'][0].current
    except:
        return None

def get_status():
    memory = psutil.virtual_memory()
    disk = psutil.disk_usage('/')
    # Divide from Bytes -> KB -> MB
    return {
        "timestamp": str(datetime.datetime.now()),
        "cpu":{
            "percent": psutil.cpu_percent(0.1),
            "frequency": psutil.cpu_freq().current,
	        "temperature": get_cpu_temperature(),
        },
        "memory":{
            "free": round(memory.available/1024.0/1024.0,1),
            "total": round(memory.total/1024.0/1024.0,1),
            "percent": memory.percent
        },
        "disk":{
            "free":round(disk.free/1024.0/1024.0/1024.0,1),
            "total": round(disk.total/1024.0/1024.0/1024.0,1),
            "percent": disk.percent
        }
        

    }

if __name__ == "__main__":
    delta = 1
    end = math.inf
    try:
        delta = sys.argv[1]
    except:
        pass
    try:
        end = sys.argv[2]
    except:
        pass
    i = 0
    while i < end:
        time.sleep(delta)
        print(get_status())
        i+=1

        #print(psutil.net_io_counters())