import signal
import time
import sys
from time import sleep

def cleanup_before_exit(signum, frame):
    print("\nCleaning up before exit...")
    with open('pass_status.txt', 'w') as file:
        pass
    print("Cleanup complete.")
    sys.exit(0)

def check_creds(username, password):
    with open('cred_db.txt', 'r') as file:
        creds = file.read().splitlines()
   
        for i in creds:
            cred_pair = i.split(',')
          
            if cred_pair[0] == username and cred_pair[1] == password:
                return True
            else:
                continue

        return False

def get_creds():
    check = 0
    while check < 2:
        with open('passed_creds.txt', 'r') as file:
            creds = file.read()
            creds = creds.split(',')
            check = len(creds)
            # print(creds)
            sleep(2)
        
    clear_microservice()
        
    return creds[0], creds[1]

def clear_microservice():
    with open('passed_creds.txt', 'w') as file:
        pass

def set_status(status):
    with open('pass_status.txt', 'w') as file:
        file.write(str(status))


signal.signal(signal.SIGINT, cleanup_before_exit)

print("Server running...")
try:
    while True:
        creds = get_creds()
        status = check_creds(creds[0],creds[1])
        set_status(status)

except KeyboardInterrupt:
    print("\nCtrl+C pressed. Exiting...")
    cleanup_before_exit(signal.SIGINT, None)