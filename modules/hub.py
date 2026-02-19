import modules.sudo_test as sudo_test
import modules.pwd_test as pwd_test
import modules.home_scan as home_scan

class tests():
    def __init__(self):
        pass

    def full_run(acc_pass):
        results = sudo_test.test.l_test(acc_pass)
        results += pwd_test.test.test()
        results += home_scan.scan.scan_home()
        return results

if __name__ == "__main__":
    pass