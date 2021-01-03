import time
time.gmtime()
time.struct_time(tm_year=2020, tm_mon=5, tm_mday=1, tm_hour=19, tm_min=40, tm_sec=35, tm_wday=4, tm_yday=122, tm_isdst=0)
time.localtime()
time.struct_time(tm_year=2020, tm_mon=5, tm_mday=1, tm_hour=15, tm_min=40, tm_sec=38, tm_wday=4, tm_yday=122, tm_isdst=1)
time.mktime(time.gmtime())
1588380538.0


import time
start_time = time.perf_counter()
for i in range(10000):
    i + 2
time.sleep(4)
end_time = time.perf_counter()
print(f"Process Time: {time.process_time()}, Total Time: {end_time - start_time}")
