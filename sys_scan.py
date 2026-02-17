# Script for simple recon of a system.

import modules.hub as hub
import os

if __name__ == "__main__":
    #user = os.getlogin() ## Not working in VSCode 1.109.4 Using alternative
    user = os.environ.get('USER')
    acc_pass = input(f'If you have the current accounts password for {user}, please enter it: ')
    results = hub.tests.full_run(acc_pass)
    print(results)
