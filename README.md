# GitHub Workflow Trigger

This repository contains an exmaple Python script which demonstrates how to trigger a github workflow using the PyGithub library. It also contains an example basic github workflow.

## What the Code Does

`.github/workflows/workflow.yml` will create a basic workflow which is triggered on a workflow dispatch and accepts one input named `my_input`

`workflow_trigger.py` does the following:

1. Retrieves environment variables for the GitHub token, my input, repository name, workflow filename, and branch name.
2. Defines a function `trigger_workflow` that:
   - Creates an instance of GitHub and logs in using the provided token.
   - Retrieves the repository object.
   - Retrieves the workflow object from the repository.
   - Triggers the workflow on the specified branch, passing the account ID as an input.
3. Calls the `trigger_workflow` function.

## How to Use

1. Clone/Fork this repository and make sure it creates a new workflow named "Example Workflow".
2. Generate a PAT token with at least read/write scope for Actions.
3. Set the following environment variables on your local machine:
   - `GITHUB_TOKEN`: Your GitHub PAT token from step 2.
   - `MY_INPUT`: A simple string, for example "Hello World".
   - `REPOSITORY`: The name of your repository in the format `owner/repo`.
   - `WORKFLOW_FILENAME`: The filename of your workflow file in the `.github/workflows` directory.
   - `BRANCH`: The name of the branch you want to run the workflow on.
3. Run the script locally with the command `python workflow_trigger.py`.

Profit