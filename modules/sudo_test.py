# Module for running sudo test.
#
# Test is:
#   sudo -S -l
#
# This will see if the current user is able to run the command and provide output

from subprocess import Popen, PIPE

class test:
    def __init__(self):
        pass

    def l_test(acc_pass):
        try:
            test = Popen(['sudo','-S','-l'], stdin = PIPE, stdout = PIPE, stderr = PIPE, text = True)
            testout, testerr = test.communicate(input=(acc_pass + '\n'))
            if test.returncode == 0:
                return "\n" + "_"*10 + "Sudo Test" + "_"*10 + f"\n\nCommand ran.\n\nOutput:\n\n{testout}"
            else:
                return f"\n" + "_"*10 + "Sudo Test" + "_"*10 + f"\n\nError when running sudo:\n\n{testerr}"
        except Exception as e:
            return "\n" + "_"*10 + "Sudo Test" + "_"*10 + f"\n\nThere was an problem running sudo test:\n\n{e}"
        
if __name__ == "__main__":
    pass