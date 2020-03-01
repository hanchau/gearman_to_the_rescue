import json
import yaml
import gearman

with open('configs/global_config.yml', 'r') as cnfg:
    global_config = yaml.load(cnfg, Loader=yaml.FullLoader)

gearman_client = gearman.GearmanClient([global_config.get('GJS_1').get('server_listening_url')])

def get_task():
    return json.dumps({"job_info": [1,2,3]})


gearman_client.submit_job(global_config.get('worker_ids').get('task_distributor'), get_task(), background=True)
