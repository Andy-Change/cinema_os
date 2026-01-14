import subprocess
import os
import uuid
from datetime import datetime

class GitManager:
    def __init__(self, repo_path):
        self.repo_path = repo_path

    def run_git(self, args):
        """Run a git command and return output."""
        cmd = ["git"] + args
        result = subprocess.run(
            cmd, 
            cwd=self.repo_path, 
            capture_output=True, 
            text=True, 
            encoding='utf-8'
        )
        if result.returncode != 0:
            raise Exception(f"Git Error: {result.stderr}")
        return result.stdout.strip()

    def create_worktree(self, agent_name, task_slug):
        """Creates a new JIT worktree for a specific task."""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        branch_name = f"agent/{agent_name}/{timestamp}_{task_slug}"
        
        # Unique folder for worktree (outside main repo or in specific folder)
        # Using .os-worktrees folder (hidden)
        worktree_path = os.path.join(self.repo_path, ".os-worktrees", branch_name.replace("/", "_"))
        
        # 1. Create Branch
        self.run_git(["branch", branch_name])
        
        # 2. Add Worktree
        self.run_git(["worktree", "add", worktree_path, branch_name])
        
        return {
            "branch": branch_name,
            "path": worktree_path
        }

    def cleanup_worktree(self, worktree_path):
        """Removes a worktree."""
        self.run_git(["worktree", "remove", "--force", worktree_path])

    def merge_worktree(self, branch_name, strategy="theirs"):
        """Merges agent branch back to main."""
        # This assumes we are on main
        self.run_git(["merge", f"-X{strategy}", branch_name])
        self.run_git(["branch", "-D", branch_name])

if __name__ == "__main__":
    # Test CLI interface if needed
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("action", choices=["create", "cleanup"])
    parser.add_argument("--agent", help="Agent Name")
    parser.add_argument("--task", help="Task Slug")
    parser.add_argument("--path", help="Worktree Path")
    
    args = parser.parse_args()
    gm = GitManager(os.getcwd())
    
    if args.action == "create":
        res = gm.create_worktree(args.agent, args.task)
        print(f"CREATED: {res['path']}")
    elif args.action == "cleanup":
        gm.cleanup_worktree(args.path)
        print("CLEANED")
