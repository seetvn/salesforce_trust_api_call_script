import requests as rq

def make_api_call(instance_name=None):
    if not instance_name or len(instance_name) == 0:
        print('empty string')
        return {"response": "you entered nothing"}
    
    res = rq.get(f"https://api.status.salesforce.com/v1/instances/{instance_name}/status")
    res = res.json()
    print(f"Version is {res['releaseVersion']}" if 'releaseVersion' in res else f"===Instance {instance_name} does not have a releaseVersion NOT FOUND ====")
    return res

def run():
    print("type EXIT to leave")
    # get user input
    while True:
        instance_name = input("Please enter instance:").strip()
        if instance_name == "EXIT":
            break
        response = make_api_call(instance_name)

run()
