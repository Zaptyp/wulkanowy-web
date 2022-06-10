from tests.checks.status_code import status_check
from tests.endpoints.login import client
from git import Repo
import re


def github_info_test(fg):
    try:
        try:
            repos = Repo(path=r"./wulkanowy-web/")
        except:
            repos = Repo(path=r"../..")
    except:
        repos = Repo(path=r"..")
    current_commit_hash = repos.head.commit.hexsha
    try:
        c_number_master = repos.git.rev_list("--count", "develop")
    except:
        c_number_master = "ERROR - Cannot get develop branch commit number!"
    commit_author = repos.head.commit.author.name
    commit_date = repos.head.commit.committed_datetime.strftime("%d.%m.%Y %H:%M")
    cc = repos.head.commit.message
    repo_url = repos.remote("origin").url
    repo_name = re.search(r"\/[a-zA-Z]+\/[a-zA-Z]+.*", str(repo_url)).group(0)
    try:
        repo_commit_number = repos.git.rev_list("--count", "develop")
    except:
        repo_commit_number = "ERROR - Cannot get repo commit number!"
    current_branch = repos.active_branch.name
    try:
        c_number_current_branch = repos.git.rev_list("--count", "HEAD", current_branch)
    except:
        c_number_current_branch = (
            "ERROR - Connot get " + current_branch + "branch commit number!"
        )
    current_branch_url = repo_url + "/tree/" + current_branch
    try:
        if int(c_number_master) - (int(c_number_current_branch) > 0):
            current_branch_commit_number = int(c_number_current_branch) - int(
                c_number_master
            )
        else:
            current_branch_commit_number = int(c_number_master) - int(
                c_number_current_branch
            )
    except:
        current_branch_commit_number = "ERROR - Cannot calculate!"
    response = client.get(
        "/github",
        headers={},
        json={},
    )
    status_check(response.status_code, response.json(), fg)
    assert response.json()["repo_name"] == repo_name[1:]
    assert response.json()["repo_link"] == repo_url
    assert response.json()["repo_commit_number"] == repo_commit_number
    assert response.json()["branch_info"][0]["active_branch_url"] == current_branch_url
    assert (
        response.json()["branch_info"][0]["active_branch_commit_number"]
        == current_branch_commit_number
    )
    assert (
        response.json()["commit_info"][0]["active_commit_hash_long"]
        == current_commit_hash
    )
    assert response.json()["commit_info"][0]["commit_date"] == commit_date
    assert response.json()["commit_info"][0]["commit_author"] == commit_author