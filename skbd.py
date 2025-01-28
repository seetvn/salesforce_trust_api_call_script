import requests as rq

def make_api_call(instance_name=None):
    if not instance_name or len(instance_name) == 0:
        return {"response": "you entered nothing"}
    
    res = rq.get(f"https://api.status.salesforce.com/v1/instances/{instance_name}/status")
    res = res.json()
    print(f"Version is {res['releaseVersion']}" if 'releaseVersion' in res else f"===Instance {instance_name} NOT FOUND ====")
    return res

def run():
    # get user input
    instance_name = input("Please enter instance:").strip()
    response = make_api_call(instance_name)
    if len(response.keys()) == 1:
        return response

run()
