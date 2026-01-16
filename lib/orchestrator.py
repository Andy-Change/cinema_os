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
    
    # Detect Latest Season
    seasons_dir = os.path.join("output", "seasons")
    active_season = "None"
    if os.path.exists(seasons_dir):
        seasons = [d for d in os.listdir(seasons_dir) if os.path.isdir(os.path.join(seasons_dir, d))]
        if seasons:
            active_season = sorted(seasons)[-1]

    # System Status
    print("\033[38;5;63m●\033[0m System \033[32mOnline\033[0m")
    print(f"  Season: \033[36m{active_season}\033[0m")
    print()

    # Active Agents
    # ... (remaining agent scanning code)
    agents_root = "agents"
    found_agents = []
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
    
    agents_by_dept = {}
    for dept_key, name in found_agents:
        if dept_key not in agents_by_dept: 
            agents_by_dept[dept_key] = []
        agents_by_dept[dept_key].append(name)

    for dept_key in sorted(agents_by_dept.keys()):
        label, dept_name, color = dept_map[dept_key]
        print(f"{color}{label}\033[0m {dept_name}")
        for agent in sorted(agents_by_dept[dept_key]):
            print(f"  - {agent}")
        print()
            
    print("\033[38;5;250mAvailable Commands:\033[0m")
    print("  - \033[38;5;63m/film-init\033[0m     Initialize new season")
    print("  - \033[38;5;63m/film-discovery\033[0m Launch discovery phase")
    print("  - \033[38;5;63m/film-status\033[0m   Check agent status")
    print("  - \033[38;5;63m/film-reflect\033[0m  Launch I2A reflection cycle")
    print("  - \033[38;5;63m/film-update\033[0m   Pull latest system updates")
    print()

# ... (cmd_init and cmd_update remains same)

def cmd_discovery(args):
    print_banner()
    
    # Detect Season
    seasons_dir = os.path.join("output", "seasons")
    if not os.path.exists(seasons_dir):
        print("\033[31m✘ Error:\033[0m No seasons found. Run '/film-init' first.")
        return
        
    seasons = [d for d in os.listdir(seasons_dir) if os.path.isdir(os.path.join(seasons_dir, d)) and d != "Season-00-Genesis"]
    if not seasons:
        print("\033[31m✘ Error:\033[0m No active production season found.")
        return
        
    active_season = sorted(seasons)[-1]
    blueprint_path = os.path.join(seasons_dir, active_season, "blueprints")
    report_file = os.path.join(blueprint_path, "discovery_report.md")
    template_path = os.path.join("skills", "project-discovery", "assets", "discovery_report_template.md")

    print(f"\033[38;5;63m▸ Launching Discovery for {active_season}...\033[0m")
    
    # Auto-create report if missing
    if not os.path.exists(report_file):
        if os.path.exists(template_path):
            with open(template_path, 'r', encoding='utf-8') as t, open(report_file, 'w', encoding='utf-8') as r:
                content = t.read().replace("[SEASON_ID]", active_season)
                r.write(content)
            print(f"  \033[32m✓\033[0m Created Discovery Report: {report_file}")
        else:
            print("  \033[33m!\033[0m Template not found. Creating empty report.")
            with open(report_file, 'w', encoding='utf-8') as f:
                f.write(f"# Discovery Report: {active_season}\n\n[Fill based on Project Discovery skill]")
            print(f"  \033[32m✓\033[0m Created empty report: {report_file}")
    else:
        print(f"  \033[36m•\033[0m Report already exists: {report_file}")

    print()
    print("  \033[38;5;250mAction Required:\033[0m")
    print("  1. Open the report file and review the structure.")
    print("  2. Ask your Director agent to start the narrative interview.")
    print()
    print("\033[32m✓\033[0m Environment Ready.")

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
