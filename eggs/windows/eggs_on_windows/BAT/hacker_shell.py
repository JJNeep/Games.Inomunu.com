"""
H4CK3R SHELL — A real interactive terminal, but make it look sick.
Runs actual system commands, just with a hacker aesthetic skin.

Usage:
    python hacker_shell.py

Works on Windows, Mac, and Linux.
No extra dependencies needed.
"""

import subprocess
import os
import sys
import time
import random
import platform
import socket
import getpass
import shutil

# ── ANSI color codes ───────────────────────────────────────────────────────────
G   = "\033[32m"       # green
GB  = "\033[1;32m"     # bright green
GD  = "\033[2;32m"     # dim green
Y   = "\033[33m"       # yellow/amber
YB  = "\033[1;33m"     # bright yellow
R   = "\033[31m"       # red
RB  = "\033[1;31m"     # bright red
C   = "\033[36m"       # cyan
CB  = "\033[1;36m"     # bright cyan
W   = "\033[1;37m"     # white bold
DIM = "\033[2m"        # dim
RST = "\033[0m"        # reset
BLK = "\033[40m"       # black background

def enable_ansi_windows():
    """Enable ANSI escape codes on Windows 10+."""
    if sys.platform == "win32":
        import ctypes
        kernel32 = ctypes.windll.kernel32
        kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)

enable_ansi_windows()

# ── Hacker name maps for common commands ─────────────────────────────────────
COMMAND_FLAVOUR = {
    "ls":    "SCANNING DIRECTORY NODES...",
    "dir":   "SCANNING DIRECTORY NODES...",
    "cd":    "NAVIGATING FILESYSTEM TREE...",
    "pwd":   "LOCATING CURRENT NODE...",
    "echo":  "BROADCASTING TRANSMISSION...",
    "cat":   "EXTRACTING FILE CONTENTS...",
    "type":  "EXTRACTING FILE CONTENTS...",
    "ping":  "PINGING TARGET NODE...",
    "ipconfig": "QUERYING NETWORK INTERFACE...",
    "ifconfig":  "QUERYING NETWORK INTERFACE...",
    "whoami": "IDENTIFYING OPERATOR...",
    "mkdir": "ALLOCATING NEW DIRECTORY SECTOR...",
    "cp":    "DUPLICATING DATA BLOCK...",
    "copy":  "DUPLICATING DATA BLOCK...",
    "mv":    "RELOCATING DATA BLOCK...",
    "move":  "RELOCATING DATA BLOCK...",
    "rm":    "WIPING DATA SECTOR...",
    "del":   "WIPING DATA SECTOR...",
    "python":"SPAWNING PYTHON INTERPRETER...",
    "python3":"SPAWNING PYTHON INTERPRETER...",
    "git":   "INTERFACING WITH VERSION CONTROL...",
    "curl":  "INITIATING HTTP EXFILTRATION...",
    "wget":  "INITIATING FILE DOWNLOAD PROTOCOL...",
    "cls":   "PURGING DISPLAY BUFFER...",
    "clear": "PURGING DISPLAY BUFFER...",
    "tasklist": "ENUMERATING ACTIVE PROCESSES...",
    "ps":    "ENUMERATING ACTIVE PROCESSES...",
    "netstat": "SCANNING OPEN NETWORK SOCKETS...",
    "find":  "SEARCHING FILESYSTEM...",
    "grep":  "PATTERN-MATCHING DATA STREAM...",
    "tree":  "MAPPING DIRECTORY TREE...",
}

GENERIC_FLAVOURS = [
    "EXECUTING MODULE...",
    "INJECTING COMMAND INTO SHELL BUFFER...",
    "DISPATCHING SYSTEM CALL...",
    "INTERFACING WITH OS KERNEL...",
    "RUNNING SUBROUTINE...",
]

def flavour_for(cmd):
    base = cmd.strip().split()[0].lower() if cmd.strip() else ""
    return COMMAND_FLAVOUR.get(base, random.choice(GENERIC_FLAVOURS))

# ── UI helpers ────────────────────────────────────────────────────────────────
def clear():
    os.system("cls" if sys.platform == "win32" else "clear")

def hline(char="─", width=None):
    w = width or shutil.get_terminal_size().columns
    print(GD + char * w + RST)

def hprint(text, color=G, end="\n"):
    print(color + text + RST, end=end)

def status_bar():
    cols = shutil.get_terminal_size().columns
    ts   = time.strftime("%H:%M:%S")
    try:
        host = socket.gethostname()
        ip   = socket.gethostbyname(host)
    except Exception:
        host, ip = "UNKNOWN", "0.0.0.0"
    user = getpass.getuser().upper()
    cwd  = os.getcwd()
    bar  = f" {ts}  |  USER:{user}  |  HOST:{host}  |  IP:{ip}  |  NODE:OMEGA-7 "
    bar  = bar[:cols - 1]
    print(GB + "\033[7m" + bar.ljust(cols - 1) + RST)

def header():
    clear()
    cols = shutil.get_terminal_size().columns
    hline("═")
    title = "[ H4CK3R_SHELL v2.0 // ROOT ACCESS // MAINFRAME CONNECTED ]"
    print(GB + title.center(cols) + RST)
    hline("═")
    status_bar()
    hline()
    print()

def boot_sequence():
    clear()
    cols = shutil.get_terminal_size().columns
    hline("═")
    print(GB + "[ INITIALIZING H4CK3R_SHELL v2.0 ]".center(cols) + RST)
    hline("═")
    print()

    steps = [
        ("LOADING KERNEL MODULES",         G),
        ("ESTABLISHING TOR CIRCUIT",        G),
        ("SPOOFING DIGITAL FINGERPRINT",    G),
        ("BYPASSING FIREWALL LAYER 7",      Y),
        ("ARMING PAYLOAD DELIVERY SYSTEM",  Y),
        ("CONNECTING TO MAINFRAME",         C),
        ("ROOT ACCESS OBTAINED",            CB),
    ]

    for label, color in steps:
        print(color + f"  {label}".ljust(50) + RST, end="", flush=True)
        time.sleep(random.uniform(0.12, 0.35))
        # fake progress
        bar = ""
        for _ in range(20):
            bar += "█"
            print(f"\r  {label}".ljust(50) + f" [{bar:<20}]", end="", flush=True)
            time.sleep(0.015)
        print(GB + "  OK" + RST)

    print()
    print(GB + "  SYSTEM READY. YOU ARE INVISIBLE.".center(cols) + RST)
    print()
    time.sleep(0.6)

def prompt_str():
    user = getpass.getuser().lower()
    cwd  = os.getcwd()
    # shorten home dir to ~
    home = os.path.expanduser("~")
    if cwd.startswith(home):
        cwd = "~" + cwd[len(home):]
    return (GD + "┌──[" + RST + GB + f"root@mainframe" + RST + GD + "]──[" + RST
            + C + cwd + RST + GD + "]\n└──" + RST + GB + "$ " + RST)

def print_output_line(line):
    """Color-code output lines based on content."""
    l = line.lower()
    if any(w in l for w in ["error","denied","failed","not found","cannot","invalid","no such"]):
        print(R + line + RST)
    elif any(w in l for w in ["warning","warn","caution"]):
        print(Y + line + RST)
    elif any(w in l for w in ["ok","success","done","complete","installed","created"]):
        print(CB + line + RST)
    elif line.startswith(" ") or "\t" in line:
        print(GD + line + RST)
    else:
        print(G + line + RST)

# ── Built-in special commands ─────────────────────────────────────────────────
def cmd_help():
    hline()
    hprint("  AVAILABLE BUILT-IN COMMANDS:", CB)
    builtins = [
        ("help",         "show this help screen"),
        ("hack <msg>",   "dramatically 'hack' something"),
        ("skull",        "display the hacker skull"),
        ("matrix",       "brief matrix rain animation"),
        ("status",       "show system status"),
        ("cls / clear",  "clear the terminal"),
        ("exit / quit",  "terminate the session"),
        ("",             "— any real shell command works too —"),
    ]
    for cmd, desc in builtins:
        print(G + f"  {cmd:<20}" + GD + desc + RST)
    hline()

def cmd_hack(args):
    target = " ".join(args) if args else random.choice(
        ["PENTAGON","NASA","FBI_DATABASE","NORAD","BANK_MAINFRAME","CIA_VAULT_7"]
    )
    buzzwords = [
        f"SCANNING OPEN PORTS ON {target}...",
        "VULNERABILITY FOUND: CVE-2024-" + str(random.randint(1000,9999)),
        "BYPASSING FIREWALL LAYER 7...",
        "INJECTING POLYMORPHIC PAYLOAD INTO KERNEL BUFFER...",
        "DEPLOYING STEALTH ROOTKIT...",
        "ESTABLISHING GHOST PROXY THROUGH TOR NODE DELTA-9...",
        "DOWNLOADING CLASSIFIED FILES...",
    ]
    hline()
    hprint(f"  INITIATING BREACH ON: {target}", YB)
    for bw in buzzwords:
        print(G + f"  {bw}" + RST, end="", flush=True)
        time.sleep(random.uniform(0.15, 0.35))
        bar = ""
        for _ in range(15):
            bar += "█"
            print(f"\r  {bw:<55} [{bar:<15}]", end="", flush=True)
            time.sleep(0.018)
        print(GB + "  DONE" + RST)
    print()
    hprint(f"  ██ ACCESS GRANTED — {target} FULLY COMPROMISED ██", CB)
    hline()

def cmd_skull():
    skull = [
        "    ██████████████████████    ",
        "  ██░░░░░░░░░░░░░░░░░░░░██  ",
        " ██░░░░░░░░░░░░░░░░░░░░░░██ ",
        "██░░░░████░░░░░░░░████░░░░██",
        "██░░░░████░░░░░░░░████░░░░██",
        "██░░░░░░░░░░░░░░░░░░░░░░░░██",
        " ██░░░░░░████████░░░░░░░░██ ",
        "  ██░░░░░░░░░░░░░░░░░░░░██  ",
        "   ██████████████████████   ",
        "    ██░░██░░░░░░░░██░░██    ",
        "    ██░░██░░░░░░░░██░░██    ",
        "     ████  ██████  ████     ",
        "       YOU HAVE BEEN PWNED  ",
    ]
    print()
    for row in skull:
        hprint("  " + row, GB)
        time.sleep(0.04)
    print()

def cmd_matrix():
    chars = "01アイウエオカキクケコサシスセソ<>{}[]#$%"
    cols  = shutil.get_terminal_size().columns
    print()
    for _ in range(18):
        line = "".join(random.choice(chars) for _ in range(cols - 1))
        # random bright char
        bright_pos = random.randint(0, len(line) - 1)
        colored = ""
        for i, ch in enumerate(line):
            if i == bright_pos:
                colored += W + ch + RST
            elif random.random() < 0.15:
                colored += GD + ch + RST
            else:
                colored += G + ch + RST
        print(colored)
        time.sleep(0.04)
    print()

def cmd_status():
    try:
        host = socket.gethostname()
        ip   = socket.gethostbyname(host)
    except Exception:
        host, ip = "UNKNOWN", "0.0.0.0"
    user = getpass.getuser()
    cwd  = os.getcwd()
    plat = platform.platform()
    py   = sys.version.split()[0]

    hline()
    hprint("  SYSTEM STATUS REPORT", CB)
    fields = [
        ("OPERATOR",  user.upper()),
        ("HOST",      host),
        ("IP",        ip),
        ("OS",        plat[:60]),
        ("PYTHON",    py),
        ("CWD",       cwd),
        ("FIREWALL",  "BYPASSED"),
        ("PROXY",     "TOR + VPN ACTIVE"),
        ("PAYLOAD",   "ARMED"),
        ("IDENTITY",  "SPOOFED"),
    ]
    for k, v in fields:
        print(GD + f"  {k:<14}" + RST + G + v + RST)
    hline()

# ── Command execution ─────────────────────────────────────────────────────────
def run_command(raw):
    raw = raw.strip()
    if not raw:
        return

    parts = raw.split()
    base  = parts[0].lower()
    args  = parts[1:]

    # ── Built-ins ─────────────────────────────────────────────────────────────
    if base in ("exit", "quit"):
        hprint("\n  TERMINATING SESSION. WIPING LOGS. GOODBYE.\n", RB)
        time.sleep(0.5)
        sys.exit(0)

    if base == "help":
        cmd_help(); return

    if base == "hack":
        cmd_hack(args); return

    if base == "skull":
        cmd_skull(); return

    if base == "matrix":
        cmd_matrix(); return

    if base == "status":
        cmd_status(); return

    if base in ("cls", "clear"):
        header(); return

    # ── Real shell command ────────────────────────────────────────────────────
    flavour = flavour_for(raw)
    print(GD + f"  // {flavour}" + RST)

    # Handle cd specially (must affect this process)
    if base == "cd":
        target = args[0] if args else os.path.expanduser("~")
        try:
            os.chdir(target)
        except FileNotFoundError:
            hprint(f"  cd: {target}: No such directory", R)
        except Exception as e:
            hprint(f"  cd: {e}", R)
        return

    # Run everything else as a real subprocess
    try:
        result = subprocess.run(
            raw,
            shell=True,
            text=True,
            capture_output=True
        )
        output = result.stdout
        errors = result.stderr

        if output:
            for line in output.splitlines():
                print_output_line(line)

        if errors:
            for line in errors.splitlines():
                hprint(line, R)

        if result.returncode != 0 and not errors and not output:
            hprint(f"  PROCESS EXITED WITH CODE {result.returncode}", Y)

    except Exception as e:
        hprint(f"  EXECUTION FAILED: {e}", RB)

# ── Main loop ─────────────────────────────────────────────────────────────────
def main():
    boot_sequence()
    header()
    hprint("  Type 'help' for built-in commands, or any real shell command.", GD)
    hprint("  Examples: ls / dir, ping google.com, python --version, git status", GD)
    print()

    history = []

    while True:
        try:
            raw = input(prompt_str())
        except (EOFError, KeyboardInterrupt):
            hprint("\n\n  CTRL+C DETECTED — SESSION TERMINATED.\n", RB)
            break

        if raw.strip():
            history.append(raw.strip())

        print()
        run_command(raw)
        print()

if __name__ == "__main__":
    main()
