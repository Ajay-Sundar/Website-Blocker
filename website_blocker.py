import time
from datetime import datetime as dt
from typing import ContextManager

host_temp=r"C:\Users\HP\PYTHON\Python Applications\Website Blocker App\hosts"
host_path=r"C:\Windows\System32\drivers\etc\hosts"
redirect = "127.0.0.1"
block_list=["www.facebook.com","facebook.com"]

while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,8) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,21):
        print("Working hours , bro")
        with open(host_temp,"r+") as file:
            content=file.read()
            for website in block_list:
                if website in content:
                    pass
                else:
                    file.write(redirect+" "+website+"\n")
    else:
        print("Fun hours , bro")
        with open(host_temp,"r+") as file:
            content=file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in block_list):
                    file.write(line)
            file.truncate()
    time.sleep(5)