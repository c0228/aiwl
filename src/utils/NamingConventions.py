import os
import random
from pathlib import Path
from src.utils.FolderAccess import lock_folder, unlock_folder
#import sys
#
#sys.path.append(str(Path(__file__).resolve().parents[1]))  # parent directory
#from FolderAccess import lock_folder, unlock_folder

def generate_unique_profile_id(data_dir: str) -> str:
    """
    Generate a unique folder name in the format PRF-### under <PROJECT_ROOT_DIRECTORY>/name.
    Returns the unique folder name (e.g., 'PRF-042').
    """
    # Temporarily unlock the protected 'data' folder
    data_path = Path(data_dir)        
    if data_path.exists():
        unlock_folder(str(data_dir))

    # Ensure the 'name' directory exists
    os.makedirs(data_dir, exist_ok=True)

    try:
        while True:
            # Generate a random 3-digit number with leading zeros (000–999)
            folder_id = f"{random.randint(0, 999):03d}"
            folder_name = f"PRF-{folder_id}"
            folder_path = os.path.join(data_dir, folder_name)

            # Check if folder already exists
            if not os.path.exists(folder_path):
                return folder_name
    finally:
        # Always relock the data folder—even if an exception occurs
        if data_path.exists():
            lock_folder(str(data_dir))
    
if __name__ == "__main__":
    PROJECT_ROOT = r"D:\workspace\aiwl\data"
    folderName = generate_unique_profile_id(PROJECT_ROOT)
    print(f"Created profile folder: {folderName}")