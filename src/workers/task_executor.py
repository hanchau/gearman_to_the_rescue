import json
import yaml
import gearman

with open('configs/global_config.yml', 'r') as cnfg:
    global_config = yaml.load(cnfg, Loader=yaml.FullLoader)

gearman_worker = gearman.GearmanWorker([global_config.get('GJS_1').get('server_listening_url')])

def execute_task(gearman_worker, task):
    print(task.data)
    return json.dumps({})

gearman_worker.register_task(global_config.get('worker_ids').get('task_executor'), execute_task)
gearman_worker.work()
