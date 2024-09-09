from utils import get_env_vars_from_message

messages = [
    {
        "contentsData": {
            "node1": {
                "environmentVariables": {
                    "body": {
                        "GIT_ORGANIZATION": "org",
                        "GIT_REPOSITORY": "repo"
                    }
                }
            }
        }
    },
    {
        "contentsData": {
            "node1": {
                "environmentVariables": {
                    "body": {
                        "GIT_ORGANIZATION": "org",
                        "GIT_REPOSITORY": "repo"
                    }
                }
            }
        }
    },
    {
        "contentsData": {
            "node1": {
                "environmentVariables": {
                    "body": {
                        "GIT_ORGANIZATION": "org",
                        "GIT_REPOSITORY": "repo"
                    }
                }
            }
        }
    }
]


def lambda_handler(event, context):
    for message in messages:
        print(get_env_vars_from_message(message))
