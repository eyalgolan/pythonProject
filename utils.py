from typing import Dict, Any, Tuple


def get_env_vars_from_message(message: Dict[str, Any]) -> Tuple[str, str]:
    nodes = message.get("contentsData", {})

    for _, node in nodes.items():
        env_vars_container = node.get("environmentVariables", {})
        if not env_vars_container:
            continue
        env_vars = env_vars_container.get("body", {})
        if not env_vars:
            continue
        git_organization = env_vars.get("GIT_ORGANIZATION")
        git_repository = env_vars.get("GIT_REPOSITORY")

        if git_organization and git_repository:
            return git_organization, git_repository
    raise ValueError("No github env vars found.")
