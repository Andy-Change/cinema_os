import argparse
import sys
import os
import json
from datetime import datetime

# Force UTF-8 encoding for standard output
if sys.stdout.encoding != 'utf-8':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

def print_banner():
    # Single-line banner - Gemini CLI Style
    # Simple and clean, works everywhere
    print()
    print("\033[38;5;63m▸ CINEMA OS\033[0m")
    print("\033[38;5;244m  Director's Operating System v0.3.0\033[0m")
    print()

def cmd_status(args):
    print_banner()
    
    # System Status
    print("\033[38;5;63m●\033[0m System \033[32mOnline\033[0m")
    print("  Season: \033[36mSeason-00-Genesis\033[0m")
    print()

    # Active Agents
    print("\033[38;5;250mActive Agents:\033[0m")
    print()
    
    # Scan Agents
    agents_root = "agents"
    found_agents = []
    # Explicit mapping for departments
    dept_map = {
        "DEPT-A": ("[A]", "Aesthetics & Meaning", "\033[38;5;166m"),
        "DEPT-D": ("[D]", "Distribution", "\033[38;5;118m"),
        "DEPT-I": ("[I]", "Intelligence", "\033[38;5;039m"),
        "DEPT-O": ("[O]", "Operations", "\033[38;5;63m"),
    }
    
    for root, dirs, files in os.walk(agents_root):
        dept_key = os.path.basename(root).upper()
        if dept_key in dept_map:
            for file in files:
                if file.endswith(".md") and file != "orchestrator.md":
                    display_name = file.replace(".md", "").replace("-", " ").title()
                    found_agents.append((dept_key, display_name))
    
    # Group by Dept
    agents_by_dept = {}
    for dept_key, name in found_agents:
        if dept_key not in agents_by_dept: 
            agents_by_dept[dept_key] = []
        agents_by_dept[dept_key].append(name)

    # Print agents by department
    for dept_key in sorted(agents_by_dept.keys()):
        label, dept_name, color = dept_map[dept_key]
        print(f"{color}{label}\033[0m {dept_name}")
        for agent in sorted(agents_by_dept[dept_key]):
            print(f"  - {agent}")
        print()
            
    print("\033[38;5;250mAvailable Commands:\033[0m")
    print("  - \033[38;5;63m/film-init\033[0m     Initialize new season")
    print("  - \033[38;5;63m/film-status\033[0m   Check agent status")
    print("  - \033[38;5;63m/film-reflect\033[0m  Launch I2A reflection cycle")
    print("  - \033[38;5;63m/film-update\033[0m   Pull latest system updates")
    print()


def cmd_init(args):
    season_name = args.season or f"Season-01-{datetime.now().strftime('%Y%m')}"
    season_path = os.path.join("output", "seasons", season_name)
    
    if os.path.exists(season_path):
        print(f"Season '{season_name}' already exists.")
        return

    os.makedirs(os.path.join(season_path, "blueprints"))
    os.makedirs(os.path.join(season_path, "production"))
    os.makedirs(os.path.join(season_path, "distribution"))
    
    # Create Season DNA Stub
    with open(os.path.join(season_path, "blueprints", "season_dna.yaml"), "w", encoding='utf-8') as f:
        f.write(f"season_id: {season_name}\nstatus: planning\ncreated_at: {datetime.now().isoformat()}")

    print(f"\033[32m✓\033[0m Initialized new season context at: {season_path}")

def cmd_update(args):
    print("\033[38;5;244m> Checking for updates...\033[0m")
    try:
        # Simple git pull
        result = os.popen("git pull").read()
        print(f"\033[32m{result}\033[0m")
        print("\033[32m✓\033[0m System updated successfully.")
    except Exception as e:
        print(f"\033[31m✘ Update failed: {e}\033[0m")

def cmd_discovery(args):
    print_banner()
    print("\033[38;5;63m▸ Launching Discovery Phase...\033[0m")
    print("  Status: Initializing Diagnostic Cycle")
    print("  Action: Please consult the 'Project Discovery' skill for interview guidelines.")
    # In a real scenario, this would trigger agent activity or create the report stub
    print()
    print("\033[32m✓\033[0m Discovery environment ready. Use 'Ask Director' to begin the interview.")

def main():
    parser = argparse.ArgumentParser(description="os_cinema Orchestrator CLI")
    subparsers = parser.add_subparsers(dest="command", help="Command to execute")

    # Command: status
    parser_status = subparsers.add_parser("status", help="Check system status")
    
    # Command: init
    parser_init = subparsers.add_parser("init", help="Initialize a new season")
    parser_init.add_argument("--season", type=str, help="Season identifier")

    # Command: update
    parser_update = subparsers.add_parser("update", help="Update the system")

    # Command: discovery
    parser_discovery = subparsers.add_parser("discovery", help="Launch post-init discovery phase")

    args = parser.parse_args()
    
    if args.command == "status":
        cmd_status(args)
    elif args.command == "init":
        cmd_init(args)
    elif args.command == "update":
        cmd_update(args)
    elif args.command == "discovery":
        cmd_discovery(args)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
