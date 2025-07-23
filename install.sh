#!/bin/bash

# install.sh

set -e

echo "Installing dependencies..."
sudo pacman -Syu --noconfirm filebeat logstash

echo "Setting up agent..."
sudo mkdir -p /opt/apache_log_agent
sudo cp -r ./* /opt/apache_log_agent/

cd /opt/apache_log_agent
sudo python3 agent.py --install
sudo systemctl enable filebeat
sudo systemctl enable logstash

echo "✅ Installation complete!"
echo "Use: python3 /opt/apache_log_agent/agent.py --start"