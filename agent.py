#!/usr/bin/env 

import os
import sys
import subprocess
import shutil
import argparse
from pathlib import Path

CONFIG_DIR = Path(__file__).parent / "config"
SERVICE_DIR = Path(__file__).parent / "service"

SYSTEMD_DIR = Path("/etc/systemd/system")
FILEBEAT_CONFIG_PATH = Path("/etc/filebeat/filebeat.yml")
LOGSTASH_CONFIG_PATH = Path("/etc/logstash/conf.d/logstash.conf")

def run_command(cmd):
    print(f"Running: {' '.join(cmd)}")
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        print("Error:", result.stderr)
        sys.exit(1)
    return result.stdout

def copy_configs():
    print("Copying configuration files...")
    shutil.copy(CONFIG_DIR / "filebeat.yml", FILEBEAT_CONFIG_PATH)
    shutil.copy(CONFIG_DIR / "logstash.conf", LOGSTASH_CONFIG_PATH)

def install_services():
    print("Installing systemd services...")
    shutil.copy(SERVICE_DIR / "filebeat.service", SYSTEMD_DIR)
    shutil.copy(SERVICE_DIR / "logstash.service", SYSTEMD_DIR)
    run_command(["systemctl", "daemon-reload"])

def start_services():
    print("Starting services...")
    run_command(["systemctl", "start", "filebeat"])
    run_command(["systemctl", "start", "logstash"])

def stop_services():
    print("Stopping services...")
    run_command(["systemctl", "stop", "filebeat"])
    run_command(["systemctl", "stop", "logstash"])

def status_services():
    print("Filebeat Status:")
    run_command(["systemctl", "status", "filebeat"])
    print("Logstash Status:")
    run_command(["systemctl", "status", "logstash"])

def main():
    parser = argparse.ArgumentParser(description="Apache Log Agent Manager")
    parser.add_argument("--install", action="store_true", help="Install and configure agent")
    parser.add_argument("--start", action="store_true", help="Start services")
    parser.add_argument("--stop", action="store_true", help="Stop services")
    parser.add_argument("--status", action="store_true", help="Show service status")

    args = parser.parse_args()

    if args.install:
        copy_configs()
        install_services()
        print("Agent installed.")
    elif args.start:
        start_services()
    elif args.stop:
        stop_services()
    elif args.status:
        status_services()
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
