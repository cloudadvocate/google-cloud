import base64
import json
import requests
from pprint import pprint
from googleapiclient import discovery


def get_labelFingerprint(response):
    return (response["labelFingerprint"])

def set_label_instance(event, context):
    
    pubsub_message = base64.b64decode(event['data']).decode('utf-8')
    #print(pubsub_message)
    final = json.loads(pubsub_message)
    resource_name = final['protoPayload']['request']['name']
    project_id = final['resource']['labels']['project_id']
    zone = final['resource']['labels']['zone']
    
    print(resource_name)
    print(project_id)
    print(zone)
    
    
    service = discovery.build('compute', 'v1')  
    # Project ID for this request.
    project = project_id  # TODO: Update placeholder value.

    # The name of the zone for this request.
    zone = zone  # TODO: Update placeholder value.

    # Name of the instance scoping this request.
    instance = resource_name  # TODO: Update placeholder value.   
    
#main code starts here:create instance 
    service = discovery.build('compute', 'v1')

    request = service.instances().get(project=project, zone=zone, instance=instance)
    response = request.execute()
    
#call to get_labelFingerprint() to get labelFingerprint value
    labelFingerprint=get_labelFingerprint(response)
    print("labelFingerprint:-->"+labelFingerprint)

    instances_set_labels_request_body = {
    # TODO: Add desired entries to the request body.
        "labels": {
          "environment": "test_environment"
         },
       'labelFingerprint': labelFingerprint
    }

    request = service.instances().setLabels(project=project, zone=zone, instance=instance, body=instances_set_labels_request_body)
    response = request.execute()

    # TODO: Change code below to process the `response` dict:
    #pprint(response)


