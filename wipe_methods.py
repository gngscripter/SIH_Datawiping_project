import os
import secrets
from logger import log

CHUNK_SIZE = 1024 * 1024  


def simple_overwrite(path: str):
    """NIST 800-88: Single-pass overwrite with random data."""
    try:
        size = os.path.getsize(path)
    except FileNotFoundError:
        print(f"Could not open file: {path}")
        log(f"Error: File not found at {path}")
        return

    if size == 0:
        print(f"File '{path}' is empty. Nothing to overwrite.")
        log(f"Skipping overwrite for empty file: {path}")
        return

    try:
        with open(path, 'wb') as f:
            remaining = size
            while remaining > 0:
                chunk = os.urandom(min(CHUNK_SIZE, remaining))
                f.write(chunk)
                remaining -= len(chunk)

        msg = f"NIST 800-88 wipe completed on: {path}"
        print(msg)
        log(msg)

    except Exception as e:
        error_msg = f"Error in simple overwrite: {e}"
        print(error_msg)
        log(error_msg)


def dod_3_pass(path: str):
    """DoD 5220.22-M (3-pass method)."""
    try:
        size = os.path.getsize(path)
    except FileNotFoundError:
        print(f"Could not open file: {path}")
        log(f"Error: File not found at {path}")
        return

    if size == 0:
        print(f"File '{path}' is empty. Nothing to overwrite.")
        log(f"Skipping DoD wipe for empty file: {path}")
        return

    try:
        passes = [
            b"\x00",  
            b"\xFF",  
            None      
        ]

        for i, pattern in enumerate(passes, start=1):
            with open(path, 'wb') as f:
                remaining = size
                while remaining > 0:
                    if pattern:
                        chunk = pattern * min(CHUNK_SIZE, remaining)
                    else:
                        chunk = os.urandom(min(CHUNK_SIZE, remaining))
                    f.write(chunk)
                    remaining -= len(chunk)

            msg = f"DoD 3-pass wipe: Completed pass {i} on {path}"
            print(msg)
            log(msg)

        log(f"DoD 5220.22-M wipe fully completed on {path}")

    except Exception as e:
        error_msg = f"Error in DoD wipe: {e}"
        print(error_msg)
        log(error_msg)


def multi_pass_overwrite(path: str, passes: int = 7):
    """Configurable multi-pass overwrite (random data)."""
    try:
        size = os.path.getsize(path)
    except FileNotFoundError:
        print(f"Could not open file: {path}")
        log(f"Error: File not found at {path}")
        return

    if size == 0:
        print(f"File '{path}' is empty. Nothing to overwrite.")
        log(f"Skipping multi-pass overwrite for empty file: {path}")
        return

    try:
        for i in range(1, passes + 1):
            with open(path, 'wb') as f:
                remaining = size
                while remaining > 0:
                    chunk = os.urandom(min(CHUNK_SIZE, remaining))
                    f.write(chunk)
                    remaining -= len(chunk)

            msg = f"Multi-pass overwrite: Completed pass {i}/{passes} on {path}"
            print(msg)
            log(msg)

        log(f"Multi-pass overwrite ({passes} passes) completed on {path}")

    except Exception as e:
        error_msg = f"Error in multi-pass overwrite: {e}"
        print(error_msg)
        log(error_msg)


def crypto_erase(path: str):
    """Simulates crypto erase by overwriting with encrypted random data and 'forgetting' the key."""
    try:
        size = os.path.getsize(path)
    except FileNotFoundError:
        print(f"Could not open file: {path}")
        log(f"Error: File not found at {path}")
        return

    if size == 0:
        print(f"File '{path}' is empty. Nothing to overwrite.")
        log(f"Skipping crypto erase for empty file: {path}")
        return

    try:
        
        encryption_key = secrets.token_bytes(32)

        
        with open(path, 'wb') as f:
            f.write(os.urandom(size))

        msg = f"Crypto erase simulated on {path} (key destroyed)"
        print(msg)
        log(msg)

    except Exception as e:
        error_msg = f"Error in crypto erase: {e}"
        print(error_msg)
        log(error_msg)
