import os
from github import Github, Auth


github_token = os.environ["GITHUB_TOKEN"]
my_input = os.environ["MY_INPUT"]
repository = os.environ["REPOSITORY"]
workflow_filename = os.environ["WORKFLOW_FILENAME"]
branch = os.environ["BRANCH"]


def trigger_workflow():
    """Function to trigger a github workflow"""

    # Create an instance of github and pass in our token
    github = Github(auth=Auth.Token(github_token))
    print(f"Logged in as {github.get_user().login}")

    # Get the repository object
    repo = github.get_repo(f"{repository}")
    print(f"Repository: {repo.full_name}")

    # Get the workflow object
    workflow = repo.get_workflow(workflow_filename)
    print(f"Workflow: {workflow.name}")

    # Trigger the workflow
    # ref = the branch name you wish to run the workflow agains
    # inputs = in our case, contains the account_id (see ../.github/workflows/trigger.yml)
    response = workflow.create_dispatch(ref=branch, inputs={"my_input": my_input})
    print(f"Workflow run created: {response}")


trigger_workflow()
