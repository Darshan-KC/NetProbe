# NetProbe

**NetProbe** is a simple, modular Ping Sweeper tool written in Python that allows you to scan IP addresses using CIDR blocks or IP ranges. It supports concurrent scanning, CLI options, and export in multiple formats.

## Features

- Parse CIDR and IP ranges
- Ping IPs using cross-platform methods
- Multithreaded scanning for speed
- Output results to console, TXT, CSV, or JSON
- Easy-to-use command-line interface

## Installation

```bash
git clone https://github.com/yourusername/NetProbe.git
cd NetProbe
pip install -r requirements.txt
```

## Usage

```bash
python run.py --cidr 192.168.1.0/30
python run.py --range 192.168.1.1 192.168.1.10
```

## Project Structure

```
NetProbe/
│
├── sweeper/                 # Core logic
├── cli/                     # CLI entry point
├── tests/                   # Pytest unit tests
├── docs/                    # Documentation
├── run.py                   # CLI shortcut
├── requirements.txt         # Dependencies
├── setup.py                 # Install support
└── .gitignore               # Ignore rules
```

## License

MIT License

## CIDR Scan
```bash
python run.py --cidr 192.168.1.0/24
```

## IP Range Scan
```bash
python run.py --range 192.168.1.1-192.168.1.50
```

<!-- ## Export to JSON
```bash
python run.py --cidr 192.168.0.0/28 --json output.json
```

## Export to CSV
```bash
python run.py --cidr 192.168.0.0/28 --csv output.csv
```

## Export to TXT
```bash
python run.py --cidr 192.168.0.0/28 --txt output.txt 
```
-->

# LICENSE
MIT License

Copyright (c) 2025 Darshan KC

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software...
