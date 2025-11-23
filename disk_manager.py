import os
import psutil
import platform
from logger import log
from wipe_methods import simple_overwrite, dod_3_pass, multi_pass_overwrite, crypto_erase
from certifier import WipeCertifier

class DiskManager:
    """A class to manage listing and wiping disks."""

    def __init__(self):
        self.partitions = psutil.disk_partitions()
        self.os_name = platform.system()
        self.certifier = WipeCertifier()

    def list_disks(self) -> bool:
        """Lists available disk partitions."""
        print(f"[{self.os_name}] Listing available disks:")
        if not self.partitions:
            print("No partitions found.")
            return False
            
        for i, p in enumerate(self.partitions):
            print(f"{i}. {p.device} ({p.mountpoint}, {p.fstype})")
        return True

    def wipe_disk(self, drive_index: int):
        """Prompts user to choose a wipe method. Uses a dummy file for simulation."""
        if not (0 <= drive_index < len(self.partitions)):
            raise IndexError("Drive index out of range.")

        target_disk = self.partitions[drive_index].device
        dummy_file_path = "dummy_file.txt"  

        
        if not os.path.exists(dummy_file_path):
            with open(dummy_file_path, "w") as f:
                f.write("This is dummy data for secure wiping simulation.")

        print(f"[{self.os_name}] Preparing wipe on disk {target_disk}...")
        log(f"Preparing wipe simulation for disk: {target_disk}")
        print(f"For safety, this demo will overwrite '{dummy_file_path}' instead.\n")

        
        print("Select wipe method:")
        print("1. NIST 800-88 (Single-pass random overwrite)")
        print("2. DoD 5220.22-M (3-pass overwrite)")
        print("3. Multi-pass overwrite (configurable)")
        print("4. Crypto erase (simulated)")
        method_choice = input("Enter choice: ")

        event_msg = None  

        if method_choice == '1':
            simple_overwrite(dummy_file_path)
            event_msg = f"Disk {target_disk} wiped using NIST 800-88"
        elif method_choice == '2':
            dod_3_pass(dummy_file_path)
            event_msg = f"Disk {target_disk} wiped using DoD 5220.22-M (3-pass)"
        elif method_choice == '3':
            try:
                passes = int(input("Enter number of passes (e.g., 7): "))
                multi_pass_overwrite(dummy_file_path, passes)
                event_msg = f"Disk {target_disk} wiped using {passes}-pass overwrite"
            except ValueError:
                print("Invalid input for passes. Aborting multi-pass wipe.")
                log("User entered invalid pass count for multi-pass overwrite.")
                return
        elif method_choice == '4':
            crypto_erase(dummy_file_path)
            event_msg = f"Disk {target_disk} wiped using Crypto Erase"
        else:
            print("Invalid choice. Aborting.")
            log(f"User entered invalid wipe method choice: {method_choice}")
            return

        
        if event_msg:
            self.certifier.add_certificate(event_msg)
            print("Certification recorded on MongoDB chain")
            log("Certification recorded on MongoDB chain")
