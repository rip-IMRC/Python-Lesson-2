import os
import platform
def shutdown():
    system_name=platform.system()
    if system_name=="Windows":
        os.system("shutdown /s /t 0")
    elif system_name=="Linux" or system_name=="Darwin":
        os.system("shutdown -h now")
    else:
        print("Unsupported operating system")
if __name__=="__main__":
    confirm=input("Are you sure you want to shutdown the computer? (yes/no): ")
    if confirm.lower()=="yes":
        shutdown()
    else:
        print("Shutdown cancelled")