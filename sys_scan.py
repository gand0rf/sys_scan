# Script for simple recon of a system.

import modules.hub as hub
import os
import socket

if __name__ == "__main__":
    try:
        #user = os.getlogin() ## Not working in VSCode 1.109.4 Using alternative
        user = os.environ.get('USER')
        acc_pass = input(f'If you have the current accounts password for {user}, please enter it: ')
        results = hub.tests.full_run(acc_pass)

        # Write results out to a file
        hostname = socket.gethostname()
        with open(f'{hostname}-scan.txt', 'w') as f:
            f.writelines(results)

        # Let user know scan is completed and whre to find the FileExistsError
        print(f'\nScan comleted. Results are saved in {hostname}-scan.txt file\n')

    except Exception as e:
        print(f'Unabel to complete scan due to error:\n{e}')
