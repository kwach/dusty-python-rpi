#!/usr/bin/python3

from SDS011 import SDS011
import time

#0: - continuous
#1 - 30[min]: n*60-30 (as 30 sec for a measurement)
WORKING_PERIOD=5

# 0 - report active mode
# 1 - report query mode
QUERY_MODE=True 

def print_res(res):
    if len(res) == 2:
        date = time.strftime("%Y-%m-%d %H:%M:%S")
        print("{}: PM2.5um: {}, PM10um: {}".format(date, res[0], res[1]))
    #print(res)

def main():
    #sensor = SDS011("/dev/ttyUSB0", use_query_mode=QUERY_MODE)
    sensor = SDS011("/dev/ttyS3", use_query_mode=QUERY_MODE)

    sensor.set_work_period(read=False, work_time=WORKING_PERIOD)

    ret=()
    while True:
        if QUERY_MODE == True: 
            ret=sensor.query()
            print_res(ret)
            time.sleep(60*WORKING_PERIOD)
        else:
            ret=sensor.read()
            print_res(ret)
    
if __name__ == "__main__":
    # execute only if run as a script
    main()
