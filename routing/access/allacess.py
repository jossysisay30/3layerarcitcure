from nornir import InitNornir
from nornir.core.task import Result, Task
#from nornir.plugins.tasks.networking import netmiko_send_config
from nornir_jinja2.plugins.tasks import template_file
#from nornir.plugins.tasks.text import template_file
#from nornir.core.task import template_file
from nornir_utils.plugins.functions import print_result
from nornir_scrapli.tasks import send_configs
import  ipdb
#from nornir_scrapli.tasks import send_configs

nr = InitNornir(config_file="config.yaml")

def basicconf(task):
    r=task.run(task=template_file,template="inter.j2",path=f"template/")
    output=r.result
    #output=task.host["config"]
    send=output.splitlines()
    #ipdb.set_trace()
    task.run(task=send_configs, configs=send)
def basicvlan(task):
    r=task.run(task=template_file,template="vlann.j2",path=f"template/")
    output=r.result
    #output=task.host["config"]
    send=output.splitlines()
    #ipdb.set_trace()
    task.run(task=send_configs, configs=send)
def df(task):
    r=task.run(task=template_file,template="df.j2",path=f"template/")
    output=r.result
    #output=task.host["config"]
    send=output.splitlines()
    #ipdb.set_trace()
    task.run(task=send_configs, configs=send)
def main():
        interface= nr.run(task=basicconf)
        vlan=  nr.run(task=basicvlan)
        dff = nr.run(task=df)
        print_result(interface)
        print_result(vlan)
        print_result(dff)
if __name__ == '__main__':
        main()
