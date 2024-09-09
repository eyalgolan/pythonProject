import logging
from utils import get_env_vars_from_message, process_messages

logging.basicConfig(level=logging.INFO)

messages = [
    {
        "contentsData": {
            "node1": {
                "environmentVariables": {
                    "body": {
                        "GIT_ORGANIZATION": "org1",
                        "GIT_REPOSITORY": "repo1",
                        "AWS_REGION": "us-west-2",
                        "DEBUG": "True"
                    }
                }
            }
        }
    },
    {
        "contentsData": {
            "node2": {
                "environmentVariables": {
                    "body": {
                        "GIT_ORGANIZATION": "org2",
                        "GIT_REPOSITORY": "repo2"
                    }
                }
            }
        }
    },
    {
        "contentsData": {
            "node3": {
                "environmentVariables": {
                    "body": {
                        "GIT_ORGANIZATION": "org3",
                        "GIT_REPOSITORY": "repo3",
                        "DEPLOYMENT_STAGE": "production",
                        "SOME_UNUSED_ENV_VAR": "value"
                    }
                }
            }
        }
    }
]


def lambda_handler(event, context):
    logging.info("Lambda handler started processing messages.")
    try:
        processed_data = process_messages(messages)
        for data in processed_data:
            logging.info(f"Processed message data: {data}")
    except Exception as e:
        logging.error(f"An error occurred: {e}")
