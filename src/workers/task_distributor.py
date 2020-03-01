import json
import yaml
import gearman

# import pdb; pdb.set_trace()
with open('configs/global_config.yml', 'r') as cnfg:
    global_config = yaml.load(cnfg, Loader=yaml.FullLoader)

gearman_client = gearman.GearmanClient([global_config.get('GJS_1').get('server_listening_url')])
gearman_worker = gearman.GearmanWorker([global_config.get('GJS_1').get('server_listening_url')])

def get_task(i):
    return json.dumps({"job_info": [i+1,i+2,i+3]})

def distribute_task(gearman_worker, task):
    print(task.data)
    for i in range(5):
        new_task = get_task(i)
        gearman_client.submit_job(global_config.get('worker_ids').get('task_executor'), new_task, background=True)
    return json.dumps({})

gearman_worker.register_task(global_config.get('worker_ids').get('task_distributor'), distribute_task)
gearman_worker.work()
