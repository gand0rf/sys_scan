# Module for scanning the /home directory.
#
# Test is:
#   ls -al /home
#
# This will look for all folders in the /home directory

from subprocess import Popen, PIPE

class scan:
    def __init__(self):
        pass

    def scan_home():
        try:
            scan = Popen(['ls','-al','/home'], stdin = PIPE, stdout = PIPE, stderr = PIPE, text = True)
            scanout, scanerr = scan.communicate()
            if scan.returncode == 0:
                return "\n" + "_"*10 + "/home Scan" + "_"*10 + f"\n\n{scanout}"
            else:
                return "\n" + "_"*10 + "/home Scan" + "_"*10 + f"\n\nError:\n\n{scanerr}"
        except Exception as e:
            return "\n" + "_"*10 + "Scan Results" + "_"*10 + f"\n\nThere was an problem running the scan:\n\n{e}"

if __name__ == "__main__":
    pass