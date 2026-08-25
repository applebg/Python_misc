'''Execute onedrive --sync at a given time'''
import subprocess
from datetime import time
from datetime import datetime
import time as systemtime
import pexpect
    
# set trigger time
target_time1 = time(hour=21, minute=0)
target_time2 = time(hour=5, minute=0)
target_times = [target_time1, target_time2]
#header
password = "820115"
command1 = ["rsync", "-vrh","/media/eugene/BACKUP HDD/OneDrive", "eugene@192.168.0.122:/media/eugene/BackUp HDD"]
command2 = ["rsync", "-vrh", "/media/eugene/BACKUP HDD/OneDrive", "/media/eugene/Data"] 

def update_x230():
    child = pexpect.spawn(command1[0], command1[1:])
    child.expect("eugene@192.168.0.122's password:")
    child.sendline(password)
    child.expect(pexpect.EOF, timeout = None)
    print(child.before.decode("utf-8"))
    print("command1 over")
def update_HDD():
    output2 = subprocess.run(
                command2)
    print("command2 over")

# Note that when the subprocess is executing, the program will be stuck at
# output = subprocess.run(["onedrive", "--sync])
# Therefore, there is no need to judge the return value of subprocess.run().

if __name__ == "__main__":
    while True:
        print(f"The time now is {datetime.now().hour}:{datetime.now().minute}")
        # check trigger time
        for target_time in target_times:
            if datetime.now().hour == target_time.hour and datetime.now().minute == target_time.minute:
                try:    # use except to ignore error
                    update_x230()
                except:
                    pass

                try:
                    update_HDD()
                except:
                    pass


        # check time every 60 seconds
        systemtime.sleep(60)

# output2 = subprocess.run(command2)

