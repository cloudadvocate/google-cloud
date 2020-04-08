import base64
import json
import requests
from googleapiclient import discovery
from pprint import pprint



def hello_pubsub(event, context):
    """Triggered from a message on a Cloud Pub/Sub topic.
    Args:
         event (dict): Event payload.
         context (google.cloud.functions.Context): Metadata for the event.
    """
    pubsub_message = base64.b64decode(event['data']).decode('utf-8')
    final = json.loads(pubsub_message)
    resource_name = final['jsonPayload']['resource']['name']
    project_id = final['resource']['labels']['project_id']
    zone = final['resource']['labels']['zone']
    
    
    #print(pubsub_message)
    print(resource_name)
    
    service = discovery.build('compute', 'v1')  
    # Project ID for this request.
    project = project_id  # TODO: Update placeholder value.

    # The name of the zone for this request.
    zone = zone  # TODO: Update placeholder value.

    # Name of the instance scoping this request.
    instance = resource_name  # TODO: Update placeholder value.

    instances_set_labels_request_body = {
    # TODO: Add desired entries to the request body.
        "labels": {
          "environment": "test"
         },
        "labelFingerprint": "42WmSpB8rSM="
    }

    request = service.instances().setLabels(project=project, zone=zone, instance=instance, body=instances_set_labels_request_body)
    response = request.execute()

    # TODO: Change code below to process the `response` dict:
    pprint(response)
