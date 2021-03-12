from nornir import InitNornir
from nornir_utils.plugins.functions import print_result
#from nornir.core.filter import F
#from pprint import pprint
#from scrapli.driver.core import IOSXEDriver
from nornir_scrapli.tasks import send_command
from scrapli import Scrapli
from pprint import pprint
from nornir.core.filter import F
import ipdb
import json
import colorama
from colorama import Fore, Style

nr = InitNornir(config_file="config.yaml")
nn=nr.inventory.hosts
#macinput=input('please enter mac address:')
results = nr.run(task=send_command, command="show mac address-table")
results2 = nr.run(task=send_command, command="show interfaces status")
macinput=input('please enter the mac last 4 digit:')
#results5 = nr.run(task=send_command, command="show interfaces status")
#ipdb.set_trace()
#print(results)
#pprint(results)
#results2=results["iosxe1"][0].scrapli_response.genie_parse_output()
#pprint(results2)
#results4['interfaces']['GigabitEthernet1/0/37']['vlan']
for nnn in nn:
   #print(nnn)
   results3=results[nnn][0].scrapli_response.textfsm_parse_output()
   results4=results2[nnn][0].scrapli_response.genie_parse_output()
   #macinput=input('please enter the mac last 4 digit:')
   #print(results4)
   #print(json.dumps(results4, indent=2))
   #ipdb.set_trace()    
   '''
   for x in results4['interfaces']:
         z=x.split('t')
         y=z[3]
         x=int['destination_port'].split('i')
         u=x[1]
         if y == '1/0/46':
             print(results4['interfaces']['GigabitEthernet1/0/37']['vlan'])

   '''

   for int in results3:
       #print(int['destination_address'])
          if int['destination_address'].endswith(macinput,10,14):
          #if int['destination_address']=='2c44.fd38.d4d4':
             #print('The switch for Given mac is:',Fore.RED + nnn)
             #print('The vlan for the Given mac is:',Fore.RED+ int['vlan'])
             #print('The interface for the Given mac is:',Fore.RED+ int['destination_port'])

             w=int['destination_port']
             ww=w.split('i')
             www=ww[1]

   for x in results4['interfaces']:
          z=x.split('t')
          y=z[3]
          if y == www:
              #print(w)
              d='GigabitEthernet{}'.format(www)
              #print(d)
              #print(results4['interfaces'][d]['vlan'])
              #print('yes')
   for int in results3:
        #print(int['destination_address'])
        if int['destination_address'].endswith(macinput,10,14) and results4['interfaces'][d]['vlan']!='trunk':
            print('The switch for Given mac is:',Fore.RED + nnn)
            print('The vlan for the Given mac is:',Fore.RED+ int['vlan'])
            print('The interface for the Given mac is:',Fore.RED+ int['destination_port'])
            print('The switchport mode for the given mac is:',Fore.RED+ results4['interfaces'][d]['vlan'])
            w=int['destination_port']
            ww=w.split('i')
            www=ww[1]


   #ipdb.set_trace()
   #results4=results2[nnn].scrapli_response.genie_parse_output()
   #results6=results5[nnn].scrapli_response.genie_parse_output()
   #print(json.dumps(results4, indent=2))
   '''
   for int in results3:
       if int['destination_address']=='aabb.cc00.8000':
           print('The switch for Given mac is:',Fore.RED + nnn)
           print('The vlan for the Given mac is:',Fore.RED+ int['vlan'])
           print('The interface for the Given mac is:',Fore.RED+ int['destination_port'])
           break
           #ipdb.set_trace()
       else:
           print('the Given mac not found')
'''

'''
#results3=results["r9"][0].scrapli_response.textfsm_parse_output()
for int in results4['interfaces']:
         print(results4['interfaces'][int]['vlan'])
for nn in results4:
        print(results4[nn]['mac_address'])

#print(json.dumps(results3, indent=2))

for int in results3:
    if int['destination_address'].endswith(macinput,10,14):
        print(int['vlan'])

'''
#vll=results3[0]
#print(vll)



#for interface in results2:
    #mtu=results2[interface]['vlans']['vlan']
    #pprint(interface)
#ipdb.set_trace()
#pprint(results2.scrapli_response.genie_parse_output())

#sh_int_parsed = results.genie_parse_output()
#print(sh_int_parsed)
#results2=response.genie_parse_output()
#sprint(response)
#task.hosts['facts']=results
#interface=task.hosts['facts'].result
#print(results[key].result)
'''
for key in results.keys():
        response = results[key].result
        response2=response.scrapli_response.genie_parse_output()
print(response2)
'''
