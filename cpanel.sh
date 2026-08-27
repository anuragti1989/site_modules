#!/bin/bash

# Termux Module Control Panel
while true; do
    clear
    echo "==============================="
    echo "   TERMUX MODULE CPANEL"
    echo "==============================="
    echo "1. Initialize Environment & Folders"
    echo "2. Create New Python Module"
    echo "3. Run/Deploy Local Build Model"
    echo "4. Exit"
    read -p "Select an option [1-4]: " choice

    case $choice in
        1)
            echo "Initializing environment and folders..."
            mkdir -p modules
            python3 -m venv env
            echo "Environment ready."
            read -p "Press Enter to continue..."
            ;;
        2)
            read -p "Enter new module name: " mod_name
            mkdir -p "modules/$mod_name"
            echo "def run():" > "modules/$mod_name/main.py"
            echo "    print('[+] Executing $mod_name...') " >> "modules/$mod_name/main.py"
            echo "Module created successfully."
            read -p "Press Enter to continue..."
            ;;
        3)
            echo "Starting local python execution build..."
            if [ -d "env" ]; then
                source env/bin/activate
            fi
            python3 -c '
import os, importlib.util

modules_dir = "modules"
print(f"[*] Scanning workspace modules directory: {os.path.abspath(modules_dir)}")
if os.path.exists(modules_dir):
    mods = [d for d in os.listdir(modules_dir) if os.path.isdir(os.path.join(modules_dir, d))]
    print(f"[*] Found {len(mods)} module(s). Executing execution sequence...\n")
    for mod in mods:
        print("-" * 40)
        print(f"[+] Loading Module: [{mod}]")
        print("-" * 40)
        mod_path = os.path.join(modules_dir, mod, "main.py")
        if os.path.exists(mod_path):
            spec = importlib.util.spec_from_file_location(mod, mod_path)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            if hasattr(module, "run"):
                module.run()
            else:
                print(f"-> Module {mod} loaded, but no run() function found.")
        else:
            print(f"[!] main.py missing in {mod}")
print("\n[*] All modules processed successfully.")
'
            read -p "Press Enter to continue..."
            ;;
        4)
            echo "Exiting..."
            exit 0
            ;;
        *)
            echo "Invalid option, please choose between 1-4."
            sleep 2
            ;;
    esac
done


