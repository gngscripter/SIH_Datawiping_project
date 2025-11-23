# SIH_project_datawiping

📌 Overview
This project is a simple, educational tool that simulates secure data wiping.
Instead of deleting data directly, it overwrites it first and then performs a simulated wipe.
It also generates a blockchain-style certificate to record each wipe event using MongoDB.
The project is designed for learning secure data deletion, logging, and basic blockchain integrity.

🧠 What the Project Includes:

✔️ Disk Wiping Simulation
-Lists available disks (simulated)
-Allows the user to pick a disk
-Overwrites data using different wipe methods
-Logs every action

✔️ Blockchain-Style Wipe Certificates
Handled by certifier.py:
-Stores each wipe event as a “block”
-Each block includes:
  -index
  -timestamp
  -event message
  -previous block hash
  -its own SHA-256 hash
-Creates a Genesis Block automatically
-Allows chain verification to detect tampering

✔️ Wipe Methods
Inside wipe_methods.py:
  -Contains different overwrite strategies (random overwrite, zero-pass, multi-pass, etc.)
  
✔️ Logging System
-Simple logging stored in wipe_log.txt
-Uses logger.py to record all warnings, errors, and wipe events

📂 Project Structure
secure-wipe/
 ├── certifier.py         # Blockchain-style certificate generator
 ├── disk_manager.py      # Disk listing + wipe operation handler
 ├── wipe_methods.py      # Different wipe algorithms
 ├── logger.py            # Logging utility
 ├── main.py              # Main CLI program
 ├── dummy_file.txt       # Test file for wipe simulation
 ├── wipe_log.txt         # Log output
 ├── README.md            # Documentation

▶️ How to Run
Make sure MongoDB is running locally:
mongodb://localhost:27017/
Then run:
python main.py
Follow the steps shown on the screen.

🎯 Purpose of the Project
This project is mainly educational. It helps users learn:
-How secure wiping works
-Why overwriting is important
-How to log system actions
-How certificate chains work
-How to build modular Python utilities