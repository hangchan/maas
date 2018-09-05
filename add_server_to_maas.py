import argparse
import csv

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--file', help='file to import', required=True)
    args = parser.parse_args()
    return args.file

def csv_to_var(file):
    dict_list=[]
    with open(file, newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            dict_list.append(row)
        return(dict_list)

def print_cmd(var):
    print('maas sysops machines create',
        'hostname=' + var['hostname'],
        'domain=' + var['domain'],
        'mac_addresses=' + var['mac_addr'],
        'architecture=amd64',
        'power_type=ipmi',
        'power_parameters_power_driver=LAN_2_0',
        'power_parameters_power_user=USER',
        'power_parameters_power_pass=PASSWORD',
        'power_parameters_mac_address=' + var['power_mac_addr'],
        'power_parameters_power_address=' + var['power_ip_addr'])

# get filename to import
csvfile=get_args()
# get a list of host variables
hosts=csv_to_var(csvfile)
# print commands to run
for host in hosts:
    for hostvar in hosts:
        print_cmd(hostvar)