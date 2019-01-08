'''
Created on May 10, 2017

@author: Anthony Local
'''
import shutil
import sys
try:
    shutil.copy2('C:\\Users\\Anthony\\Pictures\\iCloud Photos\\Downloads\\desktop.ini',
                 'F:\\DellBackupA\\Pictures\\iCloud Photos\\Downloads\\desktop.ini')

except PermissionError as perr:
    print("Permission error: {}".format(perr))
except Exception as e:
    print("Unexpected error: {}".format(sys.exc_info()[0]))
    print("Error info: {}".format(e))
    raise

if __name__ == '__main__':
    pass
