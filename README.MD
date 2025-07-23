# 🐍 Apache Log Agent

A lightweight, cross-platform **Python-based agent** for collecting, parsing, and forwarding **Apache web server logs** via an API endpoint to security analytics platforms.

This agent wraps and orchestrates the powerful **ELK Stack components (Filebeat and Logstash)** to provide enterprise-grade log processing capabilities with minimal overhead.

---

## 🎯 Purpose

This agent serves as a complete **log collection and forwarding solution** specifically designed for **Apache HTTP Server** environments.

Rather than reinventing log parsing logic, it **leverages battle-tested tools** while providing a simplified deployment and management interface through Python.

---

## 🔧 Core Components

- **Filebeat**  
  Lightweight log shipper that tails Apache access and error logs in real-time

- **Logstash**  
  Powerful log parser and transformer that applies Grok patterns, GeoIP lookups, and custom field mappings

- **Python Wrapper**  
  Central management interface for installation, configuration, and service orchestration

---

## 🚀 Key Features

### 📊 Smart Log Processing

- Parses Apache Combined Log Format with precision
- Extracts client IP, user agent, response codes, and request details
- Performs automatic GeoIP enrichment for threat analysis
- Normalizes timestamps to UTC with millisecond precision

---

### 🛡️ Security-Oriented Payload Construction

- Builds structured **JSON payloads optimized for SIEM/XDR ingestion**
- Includes security metadata fields like `is_anomaly`, `threat_type`, and `anomaly_score`
- Creates nested data object containing raw log fields for detailed analysis
- Standardizes source identification and timestamp formatting

---

### ⚙️ Easy Deployment & Management

- **Single-command** installation and configuration
- Automatic service management (`start` / `stop` / `status`)
- Cross-distribution compatibility (**systemd-based Linux systems**)
- Self-contained package with all required configurations

---

### 🌐 Flexible Output Options

- Forwards parsed logs to **remote APIs/SIEM solutions via HTTP**
- Console output for debugging and development
- Ready for integration with **Sentinel XDR**, **Elastic SIEM**, or custom backends

---

## 📁 Configuration Highlights

### 📥 Filebeat Input Configuration

- Monitors `/var/log/httpd/*.log` for Apache logs
- Automatically tags events with Apache module metadata
- Supports log rotation and multi-line log handling

---

### 🧪 Logstash Processing Pipeline

- Grok parsing using `%{COMBINEDAPACHELOG}` pattern
- Date parsing and `@timestamp` normalization
- GeoIP enrichment for client IP addresses
- Ruby-based payload restructuring for security use cases
- HTTP output to configured backend APIs

