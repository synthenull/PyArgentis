import os
import time
import sys

os.system("color e")

key = "M89309Q7ZVTFK3ERG5NRTEVYSTNWCD5E"

if input("\n [/] Enter the key: ") == key:
    print("\n [+] Valid key!")
    time.sleep(2)
    sys.exit()
else:
    print("\n [-] Invalid Key, exiting...")
    time.sleep(2)
    sys.exit()
