import os
import sys

def lock_folder(folder_path: str) -> None:
    """
    Deny Full Control (read/write/modify) to the 'Everyone' group
    for the specified folder and all its files/subfolders.
    """
    # (OI)(CI) => Object & Container Inherit (files and subfolders)
    cmd = f'icacls "{folder_path}" /deny Everyone:(OI)(CI)F'
    exit_code = os.system(cmd)
    if exit_code == 0:
        print(f"[LOCKED] Folder locked: {folder_path}")
    else:
        print(f"[ERROR] Failed to lock folder: {folder_path} (exit code {exit_code})")

def unlock_folder(folder_path: str) -> None:
    """
    Remove the explicit deny rule for the 'Everyone' group so that
    normal inherited permissions are restored.
    """
    # /remove:d removes deny Access Control Entries
    cmd = f'icacls "{folder_path}" /remove:d Everyone'
    exit_code = os.system(cmd)
    if exit_code == 0:
        print(f"[UNLOCKED] Folder unlocked: {folder_path}")
    else:
        print(f"[ERROR] Failed to unlock folder: {folder_path} (exit code {exit_code})")

# if __name__ == "__main__":
#    if len(sys.argv) != 3 or sys.argv[1] not in {"lock", "unlock"}:
#        print("Usage:")
#        print("  python FolderAccess.py lock   <folder_path>")
#        print("  python FolderAccess.py unlock <folder_path>")
#        sys.exit(1)
#
#    action, folder = sys.argv[1], sys.argv[2]
#
#    if not os.path.exists(folder):
#        print(f"[ERROR] Folder not found: {folder}")
#        sys.exit(1)
#
#    if action == "lock":
#        lock_folder(folder)
#    else:  # action == "unlock"
#        unlock_folder(folder)
#