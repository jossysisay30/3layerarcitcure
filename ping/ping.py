from nornir import InitNornir
from nornir_utils.plugins.functions import print_result
from nornir_scrapli.tasks import send_command
from nornir_scrapli.tasks import send_configs
from scrapli import Scrapli
from pprint import pprint
from nornir.core.filter import F
import ipdb
import json
import colorama
from colorama import Fore, Style
from rich import print as rprint
from rich.console import Console
from rich.table import Table
import itertools
ip_add2=[]
nr = InitNornir(config_file="config.yaml")
nn=nr.inventory.hosts
#results = nr.run(task=send_command, command='show ip interface brief')
#res = nr.run(task=send_command, command='ping {}'.format('172.16.222.218'))

#ipdb.set_trace()
active_device=[]
inacive_device=[]
for nnn in nn:
  for x in range(10,40):
    results = nr.run(task=send_command, command='ping 10.139.2.{}'.format(x))
    res2=results[nnn][0].result
    if not '!!!' in res2:
          #print('10.139.2.{}'.format(x) +' failed to respnce')
          inacive_device.append('10.139.2.{}'.format(x))
    else:
          #print('10.139.2.{}'.format(x) +' respnce')
          active_device.append('10.139.2.{}'.format(x))
#print('ACTIVE')
#rprint(active_device)
#print('INACTIVE')
#rprint(inacive_device)
table=Table(title='PING REPORT \n' )
table.add_column('Active Hosts', justify='center', style='green')
table.add_column('INActive Hosts', justify='center', style='red')
for (a,i) in itertools.zip_longest(active_device,inacive_device):
    table.add_row(a,i)
console=Console()
console.print(table)
'''
for nnn in nn:
         #print(nnn)
         results4=results[nnn][0].scrapli_response.genie_parse_output()
         #ipdb.set_trace()
         ip_add=results4['interface']['Vlan2']['ip_address']
         ip_add2.append(ip_add)
         #print(ip_add2)
for x in ip_add2:
     #print(x)
   res = nr.run(task=send_command, command='ping {}'.format(x))
   res2=res[nnn][0].result
   if not '!!!' in res2:
         print(x +' failed to respnce')
   else:
         print(x +' respnce')
         #print(resu)
'''
