import sys
import argparse
import whois
import dns.resolver
import requests
import shodan
import socket
from colorama import Fore , Back , Style , init

# init(autoreset=True)


# Defining arguments 

desc = 'This tool is used to perform information gathering'
use = 'python3 {} -d/--domain <target-domain_name> [options]'.format(sys.argv[0])
argparse = argparse.ArgumentParser(description=desc,usage=use)

argparse.add_argument('-d','--domain',help='Provide domain of target',required=True)
argparse.add_argument('-i','--ip',help='Provide target-ip ')
argparse.add_argument('-o','--output',help='Provide file name for output')

arguments = argparse.parse_args()

target_domain = arguments.domain

if arguments.ip:
    target_ip = arguments.ip
else:
    target_ip = socket.gethostbyname(target_domain)

output_file = arguments.output

#print("python3 {} {} {}".format(target_domain,target_ip,output_file))

#using colorama for color output
green = Fore.GREEN
red = Fore.RED
blue = Fore.BLUE
reset = Fore.RESET
cyan = Fore.CYAN
yellow = Fore.YELLOW
bright = Style.BRIGHT

#print('{} [+] Getting Domain Info.............'.format(green))  we can also use colorama like this
print(blue)
# Using whois module
print('[+] Getting Domain Info.............\n')
domain_result = ''

try:
    domain_info = whois.query(target_domain) 

    domain_result += 'NAME: {}'.format(domain_info.name) + '\n'
    domain_result += 'CREATION_DATE: {}'.format(domain_info.creation_date) + '\n'
    domain_result += 'LAST_UPDATE: {}'.format(domain_info.last_updated) + '\n'
    domain_result += 'EXPIRY_DATE: {}'.format(domain_info.expiration_date) + '\n'
    domain_result += 'NAME_SERVERs: {}'.format(domain_info.name_servers) + '\n'
    domain_result += 'REGISTRAR: {}'.format(domain_info.registrar) + '\n'
    print(domain_result)
    print(reset)

except:
    pass

# Using dnspython 


print(green)
print('Getting DNS Records details...............\n')
dns_result = ''

try:
    # A Record
    for a in dns.resolver.resolve(target_domain,'A'):
        dns_result += 'A Record: {}'.format(a) + '\n'
    
    # AAAA Record
    for aaaa in dns.resolver.resolve(target_domain,'AAAA'):
        dns_result += 'AAAA Record: {}'.format(aaaa) + '\n'
    
    # MX Record
    for mx in dns.resolver.resolve(target_domain,'MX'):
        dns_result += 'MX record: {}'.format(mx) + '\n'

    # NS Record
    for ns in dns.resolver.resolve(target_domain,'ns'):
        dns_result += 'NS Record: {}'.format(ns) + '\n'
    
    #SOA Record
    for soa in dns.resolver.resolve(target_domain,"SOA"):
        dns_result += 'SOA Record: {}'.format(soa) + '\n'

    
    # TXT Record
    for txt in dns.resolver.resolve(target_domain,"TXT"):
        dns_result += 'TXT Record: {}'.format(txt) + '\n'

    print(dns_result)
    print(reset)

except:
    pass
    
# Using geolocation api for location

# try:
#     res = requests.request('GET','https://geolocation-db.com/json/'+socket.gethostbyname(target_domain)).json
#     print('Country: {}',format(res['country_name']))
#     print('Country Code: {}'.format(res['country_code']))
#     print('Latitude: {}'.format(res['latitude']))
#     print('Longitude: {}'.format(res['longitude']))

# except:
#    print("problem")        -> still in dev........

# Code for shodan 
print(yellow)
print('\n')
choice = input('Did you want Shodan info(yes/no): ')
if choice == 'yes':
    api_key = input('Provide shodan membership api key: ')
    shodan_result = ''
    try:
        api = shodan.Shodan(api_key)
        results = api.search(target_ip)
        shodan_result += '[+] Total Result found is : {}'.format(results['total']) + '\n'

        for result in results['matches']:
            shodan_result += 'IP : {}'.format(results['ip_str']) + '\n'
            shodan_result += 'Data :\n  {}'.format(results['data']) + '\n'
        
        print(shodan_result)

    except shodan.APIError as e:
        print('{} [-] Key is Not Valid!!!!! {}'.format(red,reset))
        #print('error : {}'.format(e)) this error bcz key is not of member
else:
    pass

# Code for output file
if output_file:
    with open(output_file,'w') as file:
        file.write(domain_result)
        file.write(dns_result)
        file.write(shodan_result)
        file.close()
