# Scan system for SUID
#
# Test is:
#   find / -perm -4000 2>/dev/null
#
# This will look thorugh the system and try to
# find any files that have the SUID set. Also
# has a filter list.

from subprocess import Popen, PIPE

class scan:
    def __init__(self):
        pass
    
    def filter_scan(slef, scan_results):
        scan_list = scan_results.split('\n')
        clean_list= []
        filter_list = [
            '/usr/bin/mount',
            '/usr/bin/sudo.ws',
            '/usr/bin/sudo',
            '/usr/bin/su',
            '/usr/bin/umount',
            '/usr/bin/pkexec',
            '/usr/bin/passwd',
            '/usr/bin/gpasswd'
        ]
        
        for file in scan_list:
            if file not in filter_list:
                clean_list.append(file)

        return '\n'.join(clean_list)

    def scan_suid(self):
        try:
            scan = Popen(['find', '/', '-perm', '-4000'], stdin = PIPE, stdout = PIPE, stderr = PIPE, text = True, shell = False)
            scanout, scanerr = scan.communicate()
            if 'find:' in str(scanerr) and 'Permission denied' in str(scanerr):
                scanout = self.filter_scan(scanout)
                return "\n" + "_"*10 + "/SUID Scan" + "_"*10 + f"\n\n{scanout}"
            else:
                return "\n" + "_"*10 + "/SUID Scan" + "_"*10 + f"\n\nError:\n\n{scanerr}"
        except Exception as e:
            return "\n" + "_"*10 + "Scan Results" + "_"*10 + f"\n\nThere was an problem running the scan:\n\n{e}"

if __name__ == "__main__":
    pass
    #print(scan().scan_suid())