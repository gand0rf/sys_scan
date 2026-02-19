# Module for running pwd test.
#
# Test is:
#   pwd
#
# This will see if the current user is able to run the command and provide output

from modules import home_scan as home_scan
from subprocess import Popen, PIPE

class test:
    def __init__(self):
        pass

    def test():
        try:
            test = Popen(['pwd'], stdin = PIPE, stdout = PIPE, stderr = PIPE, text = True)
            testout, testerr = test.communicate()
            if test.returncode == 0:
                return f"\n" + "_"*10 + "PWD Test" + "_"*10 + f"\n\nCommand ran.\n\nOutput:\n\n{testout}"
            else:
                return f"\n" + "_"*10 + "PWD Test" + "_"*10 + f"\n\nError when running pwd:\n\n{testerr}"
        except Exception as e:
            return "\n" + "_"*10 + "PWD Test" + "_"*10 + f"\n\nThere was an problem running pwd test:\n\n{e}"
        
if __name__ == "__main__":
    pass