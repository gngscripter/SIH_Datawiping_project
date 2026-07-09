# 🧹 SIH_project_datawiping

An educational tool that simulates **secure data wiping** — overwriting data before performing a simulated wipe, then generating a **blockchain-style certificate** to record each wipe event. Built to teach secure data deletion, logging, and basic blockchain integrity concepts.

> Built for Smart India Hackathon (SIH).

##  Overview

Instead of deleting data directly, this project overwrites it first and then performs a simulated wipe. Every wipe event is recorded as a block in a blockchain-style ledger (stored via MongoDB), so the history of wipes can later be verified for tampering.

##  Features

- **Disk Wiping Simulation**
  - Lists available disks (simulated)
  - Lets the user pick a disk to wipe
  - Overwrites data using configurable wipe methods
  - Logs every action taken

- **Blockchain-Style Wipe Certificates** (`certifier.py`)
  - Stores each wipe event as a "block"
  - Each block includes: index, timestamp, event message, previous block hash, and its own SHA-256 hash
  - Automatically creates a Genesis Block
  - Supports chain verification to detect tampering

- **Wipe Methods** (`wipe_methods.py`)
  - Multiple overwrite strategies: random overwrite, zero-pass, multi-pass, and more

- **Logging System**
  - All warnings, errors, and wipe events are logged via `logger.py`
  - Output stored in `wipe_log.txt`

##  Project Structure

```
secure-wipe/
├── certifier.py       # Blockchain-style certificate generator
├── disk_manager.py    # Disk listing + wipe operation handler
├── wipe_methods.py     # Different wipe algorithms
├── logger.py           # Logging utility
├── main.py             # Main CLI program
├── dummy_file.txt       # Test file for wipe simulation
├── wipe_log.txt          # Log output
└── README.md             # Documentation
```

##  How to Run

1. Make sure MongoDB is running locally:

   ```
   mongodb://localhost:27017/
   ```

2. Run the main program:

   ```bash
   python main.py
   ```

3. Follow the prompts shown on screen to select a disk and wipe method.

##  Purpose

This project is mainly educational. It helps users learn:

- How secure wiping works
- Why overwriting data before deletion matters
- How to log system actions
- How certificate/blockchain-style chains work
- How to build modular Python utilities

##  Tech Stack

- **Language:** Python
- **Database:** MongoDB (stores wipe certificates/blocks)

##  Contributing

Contributions, issues, and feature requests are welcome.

1. Fork the project
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a pull request

##  License

No license has been specified yet. Let me know if you'd like one added (e.g. MIT) — I can generate the `LICENSE` file for you.

##  Author

**Akshat Chhetri** — [@gngscripter](https://github.com/gngscripter)
