import os
import subprocess
import time

def say_folder_name():
    try:
        # Get the absolute path of the current script
        current_path = os.path.dirname(os.path.abspath(__file__))
        
        # Extract the parent folder name ("Github" in this case)
        parent_folder = os.path.basename(os.path.dirname(current_path))
        
        print(f"Speaking folder name: {parent_folder}")
        
        # Use espeak directly via subprocess with reduced volume (-a 30 sets amplitude to 30% of normal)
        subprocess.run(['espeak', '-a', '50', parent_folder], check=True)
        
        return True
    except Exception as e:
        print(f"Error: {e}")
        print("Make sure espeak is installed with: sudo apt-get install espeak")
        return False

if __name__ == "__main__":
    # Say the folder name
    say_folder_name() 