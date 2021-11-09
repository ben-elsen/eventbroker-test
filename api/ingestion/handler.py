import epsagon
import os
import boto3
import json

# Initiate Espagon
epsagon.init(
    token=os.environ['espagon_token'],
    app_name=os.environ['app_name_stage'],
    metadata_only=False,
)

# Prepare the eventbridge client
eventBridgeClient = boto3.client('events')


@epsagon.lambda_wrapper
def lambda_handler(event, context):
    """ Lambda to ingest events

    :param dict event: The event of AWS
    :param dict context: The context of AWS
    """

    """
    # Trigger the following event
    eventBridgeClient.put_events(
        Entries=[
            {
                "EventBusName": "default",
                "DetailType": "New Connection",
                "Source": "microservice-user",
                "Detail": json.dumps({
                    "connection_initator": initatorId,
                    "sourceTimestamp": time.time(),
                }),
            }
        ]
    )
    """
    print(json.dumps(event))

    # Return
    return {
        "statusCode": 200,
        "body": json.dumps({
            "boe": "hoejoojooo"
        }),
        "isBase64Encoded": False
    }
