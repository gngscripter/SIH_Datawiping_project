import sys
from disk_manager import DiskManager
from logger import log

def main():
    """Main entry point for the Secure Data Wiping Utility."""
    print("==============================")
    print(" Secure Data Wiping Utility ")
    print("==============================")
    print("1. Proceed with wiping (SIMULATION)")
    print("2. Exit safely")

    
    try:
        choice = input("Enter choice: ")
        if choice != '1':
            print("Aborted. No action taken.")
            sys.exit(0)
    except (ValueError, EOFError):
        print("\nInvalid input. Aborting.")
        sys.exit(1)

    log("User chose to proceed with wiping.")
    dm = DiskManager()

    
    if not dm.list_disks():
        log("No disks found or error listing disks. Exiting.")
        sys.exit(1)

    
    try:
        idx_str = input("Select disk index to wipe: ")
        idx = int(idx_str)
        log(f"User selected disk index: {idx}")
        dm.wipe_disk(idx)
    except (ValueError, IndexError):
        error_msg = f"Invalid index '{idx_str}'. Please enter a number from the list."
        print(error_msg)
        log(error_msg)
    except Exception as e:
        error_msg = f"An unexpected error occurred: {e}"
        print(error_msg)
        log(error_msg)



if __name__ == "__main__":
    main()
