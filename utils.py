import logging
from typing import Dict, Any, Tuple, List, Optional

# Set up logging
logging.basicConfig(level=logging.INFO)


# Function to extract environment variables from message
def get_env_vars_from_message(message: Dict[str, Any]) -> Tuple[str, str, Optional[str], Optional[str]]:
    nodes = message.get("contentsData", {})
    logging.debug(f"Extracting environment variables from message: {message}")

    for node_key, node in nodes.items():
        env_vars_container = node.get("environmentVariables", {})
        if not env_vars_container:
            logging.warning(f"No environment variables found for node {node_key}. Skipping...")
            continue

        env_vars = env_vars_container.get("body", {})
        if not env_vars:
            logging.warning(f"No 'body' found in environment variables for node {node_key}. Skipping...")
            continue

        git_organization = env_vars.get("GIT_ORGANIZATION")
        git_repository = env_vars.get("GIT_REPOSITORY")
        aws_region = env_vars.get("AWS_REGION", "us-east-1")  # Default to us-east-1 if not present
        deployment_stage = env_vars.get("DEPLOYMENT_STAGE")  # Optional field

        if git_organization and git_repository:
            logging.info(f"Found GitHub organization: {git_organization}, repository: {git_repository}.")
            return git_organization, git_repository, aws_region, deployment_stage
        else:
            logging.warning(f"Missing required GitHub environment variables in node {node_key}.")

    raise ValueError("No valid GitHub environment variables found in the message.")


# Function to process a list of messages
def process_messages(messages: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    processed_data = []

    for idx, message in enumerate(messages):
        logging.info(f"Processing message {idx + 1}/{len(messages)}...")
        try:
            git_organization, git_repository, aws_region, deployment_stage = get_env_vars_from_message(message)
            processed_data.append({
                "Git Organization": git_organization,
                "Git Repository": git_repository,
                "AWS Region": aws_region,
                "Deployment Stage": deployment_stage or "Not specified"
            })
        except ValueError as e:
            logging.error(f"Error processing message {idx + 1}: {e}")

    return processed_data
