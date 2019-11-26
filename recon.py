import multiprocessing
import os
import sys

class notification_colors:
    WARNING = '\x1b[93m'
    FAIL = '\x1b[91m'
    INFO = '\x1b[94m'
    OK = '\x1b[92m'
    END = '\x1b[0m'

def process_ip(ip):
    #check if the report directory exists
    if not os.path.isdir('./report'):
        print(notification_colors.WARNING + 'Report directory not found, lets try to create it' + notification_colors.END)
        try:
            os.mkdir('./report')
        except OSError:
            print(notification_colors.FAIL + 'Creation of the directory ./report failed' + notification_colors.END)
        else:           
            print(notification_colors.OK + 'Successfully created' + notification_colors.END)
    else:
        print('Proccessing: {}'.format(ip))
        try:
            os.mkdir('./report/'+ip)
        except OSError:
            print(notification_colors.FAIL + 'Creation of the directory ./report/{} failed'.format(ip) + notification_colors.END)


def process_file(file):
    ips_file = open(targets, 'r')
    print(notification_colors.INFO + 'Reading file: {}'.format(targets) + notification_colors.END)
    ip_list = []
    for ip in ips_file:
        ip_list.append((ip.rstrip(),))
    return ip_list



if len(sys.argv) < 2:
    print()
    print(notification_colors.FAIL + 'Usage: python3 recon.py <PATH TO FILE>' + notification_colors.END)
    pass
    sys.exit()


if __name__ == '__main__':
    multiprocessing.freeze_support()

    #path to targets file
    targets = sys.argv[1]
    
    ip_list = process_file(targets)
    
    #A worker per IP
    number_workers = len(ip_list)

    print(notification_colors.INFO + 'Starting Autorecon' + notification_colors.END)
    with multiprocessing.Pool(processes=number_workers) as pool: # auto closing workers
        results = pool.starmap(process_ip, ip_list)



