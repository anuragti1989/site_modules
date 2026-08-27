import importlib.util
from pathlib import Path
import sys

# Define workspace paths relative to this script or absolute
BASE_DIR = Path(__file__).resolve().parent.parent
MODULES_DIR = BASE_DIR / "modules"

def load_and_execute_modules():
    print(f"[*] Scanning workspace modules directory: {MODULES_DIR}")
    
    if not MODULES_DIR.exists():
        print(f"[!] Modules directory not found at {MODULES_DIR}. Create some modules first.")
        return

    # Find all subdirectories inside modules/ that contain a main.py file
    module_folders = [f for f in MODULES_DIR.iterdir() if f.is_dir() and (f / "main.py").exists()]
    
    if not module_folders:
        print("[!] No active modules with a 'main.py' found.")
        return

    print(f"[*] Found {len(module_folders)} module(s). Executing execution sequence...\n")

    for folder in module_folders:
        mod_name = folder.name
        mod_file = folder / "main.py"
        
        print(f"----------------------------------------")
        print(f"[+] Loading Module: [{mod_name}]")
        print(f"----------------------------------------")

        try:
            # Dynamically load the module using importlib
            spec = importlib.util.spec_from_file_location(mod_name, str(mod_file))
            if spec and spec.loader:
                module = importlib.util.module_from_spec(spec)
                sys.modules[mod_name] = module
                spec.loader.exec_module(module)
                
                # Check if the module has a specific entry point function, e.g., 'run()' or 'main()'
                if hasattr(module, "run"):
                    module.run()
                elif hasattr(module, "main"):
                    module.main()
                else:
                    print(f"-> Module '{mod_name}' executed via top-level script parsing.")
            else:
                print(f"[!] Failed to load spec for {mod_name}")
                
        except Exception as e:
            print(f"[!] Error executing module '{mod_name}': {e}")
        
        print()

    print("[*] All modules processed successfully.")

if __name__ == "__main__":
    load_and_execute_modules()
print('Master model script placeholder')


