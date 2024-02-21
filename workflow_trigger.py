from github import Auth, Github, GithubException, InputGitAuthor
 
github_token = "your_github_token"
 
github = Github(auth=Auth.Token(github_token))
login = github.get_user().login
 
 
def trigger_github_action():
    """ function to trigger the github action """
    github.trigger_github_action(
        inputs={"ACCOUNT_ID": "12345678910"},
    )