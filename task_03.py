import sys
from pathlib import Path
from colorama import init, Fore, Style

# colorama
init(autoreset=True)

def display_tree(directory: Path, prefix: str = ""):
    """
    Tree display via recursion
    """
    
    try:
        # sorting except of some exceptions
        children = sorted([
            path for path in directory.iterdir() 
            if path.name not in ['.git', 'venv']
        ])
    except PermissionError:
        print(f"{prefix}├── {Fore.RED}[Not enough rights for access]")
        return
    except FileNotFoundError:
        print(f"{prefix}├── {Fore.RED}[Directory is not found]")
        return

    # children iteration
    for i, path in enumerate(children):
        # check, if it is last element
        is_last = (i == len(children) - 1)
        
        # setting proper connectors
        connector = "└── " if is_last else "├── "
        
        if path.is_dir():
            # Directory
            print(f"{prefix}{connector}{Fore.BLUE}{Style.BRIGHT}📁 {path.name}")
            
            # proper prefixes
            child_prefix = prefix + ("    " if is_last else "│   ")
            
            # === Recursion call ===
            display_tree(path, prefix=child_prefix)
            
        elif path.is_file():
            # File
            print(f"{prefix}{connector}{Fore.GREEN}📄 {path.name}")
        else:
            # else
            print(f"{prefix}{connector}{Style.DIM}🔗 {path.name}")

def main():
    """
    Main function vizualization
    """
    if len(sys.argv) != 2:
        print(f"{Fore.YELLOW}HOW to use: -> python {sys.argv[0]} <path to dir>")
        print(f"{Fore.CYAN}Example: python {sys.argv[0]} ./someDir")
        sys.exit(1)

    directory_to_show = sys.argv[1]
    target_dir = Path(directory_to_show)

    # Перевірки початкового шляху
    if not target_dir.exists():
        print(f"{Fore.RED}Error: this path do not exist -> '{target_dir}'")
        return
    
    if not target_dir.is_dir():
        print(f"{Fore.RED}Error: this is not the path to directory -> '{target_dir}'")
        return

    # Initial directory
    print(f"{Fore.CYAN}{Style.BRIGHT}📁 {target_dir.resolve().name} {Style.NORMAL}({target_dir.resolve()})")
    
    # Recursion approach
    display_tree(target_dir)

if __name__ == "__main__":
    main()