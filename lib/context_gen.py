import os
import yaml

class ContextGenerator:
    def __init__(self, project_root):
        self.root = project_root

    def generate_task_context(self, agent_name, task_description, output_path):
        """Generates a TASK.md file for a specific agent execution."""
        
        # 1. Load Agent Definition
        agent_def_path = self._find_agent_file(agent_name)
        if not agent_def_path:
            raise Exception(f"Agent {agent_name} not found.")

        with open(agent_def_path, 'r', encoding='utf-8') as f:
            agent_content = f.read()

        # 2. Construct Context
        context = f"""# TASK CONTEXT: {task_description}

## YOUR ROLE
{agent_content}

## INSTRUCTIONS
1. Execute the task described in the header.
2. Use the provided tools.
3. When finished, report back.

## PROJECT DNA
(Placeholder for Season DNA injection)
"""
        
        # 3. Write to Worktree
        with open(os.path.join(output_path, "TASK.md"), "w", encoding='utf-8') as f:
            f.write(context)

        return os.path.join(output_path, "TASK.md")

    def _find_agent_file(self, agent_name):
        for root, dirs, files in os.walk(os.path.join(self.root, "agents")):
            for file in files:
                if file == f"{agent_name}.md" or file == agent_name:
                    return os.path.join(root, file)
        return None

if __name__ == "__main__":
    # Test
    cg = ContextGenerator(os.getcwd())
    # print(cg._find_agent_file("writer.md")) 
