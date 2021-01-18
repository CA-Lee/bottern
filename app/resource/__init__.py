import subprocess


async def get_git_branch_name() -> str:
    try:
        raw_result = subprocess.run(
            ["git", "branch"], stdout=subprocess.PIPE
        ).stdout.decode()
        for branch in raw_result.split("\n"):
            if branch[0] == "*":
                return branch[2:]
    except:
        return "fail to get branch"