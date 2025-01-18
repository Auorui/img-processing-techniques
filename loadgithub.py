import os
import subprocess
from pathlib import Path


def run_git_command(command, cwd=None):
    """运行 git 命令，并返回输出"""
    result = subprocess.run(command, cwd=cwd, text=True, capture_output=True)
    if result.returncode != 0:
        print(f"Error running command: {command}")
        print(result.stderr)
    else:
        print(result.stdout)


def upload_to_github(local_folder, repo_url, commit_message="Initial commit"):
    """将文件夹上传到 GitHub 仓库"""
    # 获取目标文件夹的绝对路径
    local_folder = os.path.abspath(local_folder)

    if not os.path.exists(local_folder):
        print(f"The folder {local_folder} does not exist.")
        return

    # 进入目标文件夹
    os.makedirs(local_folder, exist_ok=True)

    # 初始化 Git 仓库
    run_git_command(["git", "init"], cwd=local_folder)

    # 配置用户信息（如果没有全局配置）
    run_git_command(["git", "config", "user.name", "Auorui"], cwd=local_folder)
    run_git_command(["git", "config", "user.email", "2165648225@qq.com"], cwd=local_folder)

    # 强制将本地分支设置为 main
    run_git_command(["git", "branch", "-M", "main"], cwd=local_folder)

    # 添加所有文件
    run_git_command(["git", "add", "."], cwd=local_folder)

    # 提交更改
    run_git_command(["git", "commit", "-m", commit_message], cwd=local_folder)

    # 删除现有的远程 origin（如果存在）
    run_git_command(["git", "remote", "remove", "origin"], cwd=local_folder)

    # 设置远程仓库
    run_git_command(["git", "remote", "add", "origin", repo_url], cwd=local_folder)

    # 拉取远程仓库的 main 分支，使用 rebase 来避免合并提交
    run_git_command(["git", "pull", "--rebase", "origin", "main"], cwd=local_folder)

    # 推送到 GitHub 的 main 分支
    run_git_command(["git", "push", "-u", "origin", "main"], cwd=local_folder)

    print(f"Files from {local_folder} have been successfully uploaded to GitHub.")


if __name__ == "__main__":
    # 目标文件夹路径（替换为你的文件夹路径）
    local_folder = r'D:\PythonProject\img_processing_techniques_main'
    # 你的 GitHub 仓库 URL
    repo_url = "git@github.com:Auorui/img-processing-techniques.git"
    # 提交信息（可选）
    commit_message = "Upload dataset and code"
    # 调用上传函数
    upload_to_github(local_folder, repo_url, commit_message)
