import time
from azure.identity import ClientSecretCredential
from azure.mgmt.resource import ResourceManagementClient 
from config import EVENT_CONFIG

def handler(event, context):
    """Function handles the code to be executed."""
    try:
        credentials, subscription_id = get_credentials(event)

        resource_client = ResourceManagementClient(credentials, subscription_id)
        resource_groups = resource_client.resource_groups.list()
        for rg in resource_groups:
            ## print name of resource groups
            print(rg.name)
            return True
    except Exception as err:
        print(err)
        return False

# get_credentials function
def get_credentials(event):
    """Function handles the authentication to Azure Account"""
    subscription_id = event['environment_params']['subscription_id']
    credentials = ClientSecretCredential(
        client_id=event['credentials']['credential_id'],
        client_secret=event['credentials']['credential_key'],
        tenant_id=event['environment_params']['tenant']
    )
    return credentials, subscription_id

def timed_handler(event, context):
    """Function calculate time to run the script."""
    start = time.time()
    results = handler(event, context)
    end = time.time()
    print(end - start)
    return results

if __name__ == "__main__":
    RESULT = timed_handler(EVENT_CONFIG, None)
    print(RESULT)
