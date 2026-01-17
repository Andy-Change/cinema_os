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

def cmd_init(args):
    # Strict Limit: One season per project
    seasons_dir = os.path.join("output", "seasons")
    if os.path.exists(seasons_dir):
        existing = [d for d in os.listdir(seasons_dir) if os.path.isdir(os.path.join(seasons_dir, d))]
        if existing:
            print(f"\033[31m✘ Ошибка:\033[0m Сезон уже существует: \033[36m{existing[0]}\033[0m.")
            print("  В данный момент разрешен только один активный сезон на проект.")
            return

    season_name = args.season or f"Season-01-{datetime.now().strftime('%Y%m')}"
    season_path = os.path.join("output", "seasons", season_name)
    
    os.makedirs(os.path.join(season_path, "blueprints"))
    os.makedirs(os.path.join(season_path, "production"))
    os.makedirs(os.path.join(season_path, "distribution"))
    
    # Create Season DNA Stub
    with open(os.path.join(season_path, "blueprints", "season_dna.yaml"), "w", encoding='utf-8') as f:
        f.write(f"season_id: {season_name}\nstatus: planning\ncreated_at: {datetime.now().isoformat()}")

    # Initialize Project Bible (The Brain)
    bible_path = os.path.join(season_path, "blueprints", "project_bible.json")
    initial_bible = {
        "meta": {
            "season_id": season_name,
            "created_at": datetime.now().isoformat(),
            "version": "1.0.0"
        },
        "core_identity": {},
        "visual_language": {},
        "script_bible": {},
        "distribution_strategy": {}
    }
    with open(bible_path, "w", encoding='utf-8') as f:
        json.dump(initial_bible, f, indent=4)

    print(f"\033[32m✓\033[0m Инициализирован новый сезон: {season_path}")
    print(f"  \033[36m➔\033[0m Создан Project Bible: {bible_path}")

def cmd_update(args):
    print("\033[38;5;244m> Проверка обновлений...\033[0m")
    try:
        # Simple git pull
        result = os.popen("git pull").read()
        print(f"\033[32m{result}\033[0m")
        print("\033[32m✓\033[0m Система обновлена.")
    except Exception as e:
        print(f"\033[31m✘ Ошибка обновления: {e}\033[0m")

def cmd_discovery(args):
    print_banner()
    
    # Detect Season
    seasons_dir = os.path.join("output", "seasons")
    if not os.path.exists(seasons_dir):
        print("\033[31m✘ Ошибка:\033[0m Директория 'output/seasons' не найдена.")
        print("  \033[38;5;250mДействие:\033[0m Пожалуйста, запустите '\033[38;5;63mpython lib/orchestrator.py init\033[0m'.")
        return
        
    seasons = [d for d in os.listdir(seasons_dir) if os.path.isdir(os.path.join(seasons_dir, d))]
    production_seasons = [d for d in seasons if d != "Season-00-Genesis"]
    
    if not production_seasons:
        print("\033[31m✘ Ошибка:\033[0m Активный сезон не найден.")
        print("  \033[38;5;250mДействие:\033[0m Запустите '\033[38;5;63mpython lib/orchestrator.py init\033[0m'.")
        return
        
    active_season = sorted(production_seasons)[-1]
    print(f"\033[38;5;63m▸ Режим Discovery для {active_season} активен.\033[0m")
    print()
    print("  \033[38;5;250mСледующий шаг:\033[0m")
    print("  Пожалуйста, начните свободный диалог с агентом \033[36mMeaning Owner\033[0m.")
    print("  Он проведет вас через интервью и поможет собрать данные для Эпизода 01.")
    print()
def cmd_doctor(args):
    print_banner()
    print("\033[38;5;63m▸ SYSTEM DIAGNOSTICS (THE DOCTOR)\033[0m")
    print()

    checks = [
        ("Core Config", "CLAUDE.md"),
        ("Plugin Manifest", ".claude-plugin/plugin.json"),
        ("Agents Directory", "agents"),
        ("Skills Directory", "skills"),
        ("Library (Lib)", "lib"),
        ("Output Schema", "output/seasons"),
    ]

    all_pass = True
    print("\033[38;5;250m[Checking File Structure]\033[0m")
    for label, path in checks:
        if os.path.exists(path):
            print(f"  \033[32m✓\033[0m {label:<20} Found")
        else:
            print(f"  \033[31m✘\033[0m {label:<20} MISSING ({path})")
            all_pass = False

    print()
    print("\033[38;5;250m[Checking Dependencies]\033[0m")
    
    # Check Git
    git_ver = os.popen("git --version").read().strip()
    if git_ver:
        print(f"  \033[32m✓\033[0m Git                 {git_ver}")
    else:
        print(f"  \033[31m✘\033[0m Git                 NOT FOUND")
        all_pass = False

    print()
    if all_pass:
        print("\033[32m✨ SYSTEM HEALTHY. READY FOR PRODUCTION.\033[0m")
    else:
        print("\033[31m⚠️  C CRITICAL ISSUES DETECTED. PLEASE RE-RUN SETUP.BAT\033[0m")

def cmd_export(args):
    print_banner()
    print("\033[38;5;63m▸ PRODUCTION BOOK EXPORT\033[0m")

    # 1. Detect Active Season
    seasons_dir = os.path.join("output", "seasons")
    if not os.path.exists(seasons_dir):
        print("No seasons found.")
        return

    seasons = [d for d in os.listdir(seasons_dir) if os.path.isdir(os.path.join(seasons_dir, d))]
    production_seasons = [d for d in seasons if d != "Season-00-Genesis"]
    
    if not production_seasons:
        print("No active production season found.")
        return
        
    active_season = sorted(production_seasons)[-1]
    season_path = os.path.join(seasons_dir, active_season)
    bible_path = os.path.join(season_path, "blueprints", "project_bible.json")
    
    if not os.path.exists(bible_path):
        print(f"\033[31m✘ Error:\033[0m project_bible.json not found in {active_season}.")
        return

    # 2. Read Data
    with open(bible_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # 3. Simple Template Engine (Jinja2-lite)
    template_path = os.path.join("templates", "production_book.md")
    if not os.path.exists(template_path):
        # Fallback if template missing
        content = f"# Production Book: {active_season}\n\n(Template missing)"
    else:
        with open(template_path, 'r', encoding='utf-8') as f:
            content = f.read()

    # Replace Placeholders safely
    # Meta
    content = content.replace("{{ season_id }}", data.get("meta", {}).get("season_id", "N/A"))
    content = content.replace("{{ version }}", data.get("meta", {}).get("version", "1.0"))
    content = content.replace("{{ date }}", datetime.now().strftime("%Y-%m-%d"))

    # Identity
    identity = data.get("core_identity", {})
    content = content.replace("{{ logline }}", identity.get("logline", "TBD"))
    content = content.replace("{{ theme }}", identity.get("theme", "TBD"))
    content = content.replace("{{ genre }}", identity.get("genre", "TBD"))
    content = content.replace("{{ tone }}", ", ".join(identity.get("tone", [])))

    # Visuals
    visuals = data.get("visual_language", {})
    content = content.replace("{{ cinematic_style }}", visuals.get("cinematic_style", "Standard"))
    
    # Simple Loop Replacements (Manual for now to avoid Jinja dependency)
    # Palette
    palette_block = ""
    for color in visuals.get("color_palette", []):
         palette_block += f"*   {color}\n"
    content = content.replace("{% for color in color_palette %}\n*   {{ color }}\n{% endfor %}", palette_block)

    # Rules
    rules_block = ""
    for rule in visuals.get("rules", []):
         rules_block += f"*   {rule}\n"
    content = content.replace("{% for rule in rules %}\n*   {{ rule }}\n{% endfor %}", rules_block)

    # Script
    script = data.get("script_bible", {})
    protagonist = script.get("protagonist", {})
    content = content.replace("{{ protagonist_name }}", protagonist.get("name", "TBD"))
    content = content.replace("{{ protagonist_goal }}", protagonist.get("goal", "TBD"))
    content = content.replace("{{ protagonist_flaw }}", protagonist.get("flaw", "TBD"))

    # Act Loop
    acts_block = ""
    for act in script.get("acts", []):
         name = act.get("name", "Act")
         desc = act.get("description", "...")
         acts_block += f"*   **{name}:** {desc}\n"
    content = content.replace("{% for act in acts %}\n*   **{{ act.name }}:** {{ act.description }}\n{% endfor %}", acts_block)
    
    # Distribution
    dist = data.get("distribution_strategy", {})
    content = content.replace("{{ target_audience }}", dist.get("target_audience", "TBD"))
    content = content.replace("{{ platforms }}", ", ".join(dist.get("platforms", [])))

    # 4. Write Output
    output_file = os.path.join(season_path, "production_book.md")
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"\033[32m✓\033[0m Exported Production Book: {output_file}")

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

    # Command: doctor
    parser_doctor = subparsers.add_parser("doctor", help="Run system diagnostics")

    # Command: export
    parser_export = subparsers.add_parser("export", help="Generate Production Book from Project Bible")

    args = parser.parse_args()
    
    if args.command == "status":
        cmd_status(args)
    elif args.command == "init":
        cmd_init(args)
    elif args.command == "update":
        cmd_update(args)
    elif args.command == "discovery":
        cmd_discovery(args)
    elif args.command == "doctor":
        cmd_doctor(args)
    elif args.command == "export":
        cmd_export(args)
    else:
        # Welcome Tour (No args)
        print_banner()
        print("  \033[36mDobro pozhalovat (Welcome), Director.\033[0m")
        print("  OS Cinema v1.0 is ready.")
        print()
        print("  \033[38;5;250mStart your journey:\033[0m")
        print("  1. Run '\033[38;5;63mpython lib/orchestrator.py doctor\033[0m' to check health.")
        print("  2. Run '\033[38;5;63mpython lib/orchestrator.py init\033[0m' to create a season.")
        print()
        parser.print_help()

if __name__ == "__main__":
    main()
