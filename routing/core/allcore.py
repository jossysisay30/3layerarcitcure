from nornir import InitNornir
from nornir.core.task import Result, Task
from nornir_jinja2.plugins.tasks import template_file
from nornir_utils.plugins.functions import print_result
from nornir_scrapli.tasks import send_configs
import  ipdb
nr = InitNornir(config_file="config.yaml")
def basicconf(task):
    r=task.run(task=template_file,template="inter.j2",path=f"templates/")
    output=r.result
    send=output.splitlines()
    task.run(task=send_configs, configs=send)
def basicconfospf(task):
    r=task.run(task=template_file,template="ospf.j2",path=f"templates/")
    output=r.result
    send=output.splitlines()
    task.run(task=send_configs, configs=send)
def main():
        yaml_results = nr.run(task=basicconf)
        base_results = nr.run(task=basicconfospf)
        print_result(yaml_results)
        print_result(base_results)
if __name__ == '__main__':
        main()
