import sys
import re
import urllib.request
from googleapiclient import discovery
from oauth2client.client import GoogleCredentials

location = sys.argv[1]
project = sys.argv[2]
rule = sys.argv[3]

# 1. get current ip
my_ip = urllib.request.urlopen("https://{location}-{project}.cloudfunctions.net/checkip".format(location=location, project=project)).read().decode('utf-8')
print('Your ip:', my_ip)

# 2. get current firewall rule
credentials = GoogleCredentials.get_application_default()
service = discovery.build('compute', 'v1', credentials=credentials)

request = service.firewalls().get(project=project, firewall=rule)
response = request.execute()

# 3. find old ip address

cidr_expr = re.compile("/\d\d?$")
for source_range in response['sourceRanges']:
    if not cidr_expr.search(source_range):
        old_range = source_range

if (old_range == my_ip):
    print('Your firewall rule [', rule, '] already allows your current IP [', my_ip, ']')
    print('Nothing to do.')
    quit()

# 4. update firewall rule with new ip address

new_rule = response
new_rule['sourceRanges'].remove(old_range)
new_rule['sourceRanges'].append(my_ip)

request = service.firewalls().update(project=project, firewall=rule, body=new_rule)
response = request.execute()

print('Replaced', old_range, 'with', my_ip, 'in rule [', rule, ']')
print('Done.')
