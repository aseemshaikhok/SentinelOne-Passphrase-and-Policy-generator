# SentinelOne Passphrase and Policy Generator

A simple tool to generate passphrases and retrieve policy information using the SentinelOne API.

> Retrieve agent passphrases and audit policies across your SentinelOne environment using the SentinelOne API.
> Download from release, or build using the python code. 
 
---
 
## Overview
 
This tool provides two core capabilities:
 
- **Passphrase Generator** — Retrieve agent passphrases for machines in any state: active, decommissioned, migrated, uninstalled, or still visible on the console.
- **Policy Generator** — Fetch policies at the Account, Site, or Group level to identify mismatches and surface security risk.

## Features
 
### 🔑 Passphrase Generator
 
Retrieve passphrases for endpoints regardless of their current agent state:
 
| Agent State | Supported |
|---|---|
| Active / Visible on Console | ✅ |
| Decommissioned | ✅ |
| Migrated | ✅ |
| Uninstalled | ✅ |
 
### 🛡️ Policy Generator
 
Retrieve and compare SentinelOne policies by providing a single ID at any scope level:
 
| Scope | Input |
|---|---|
| Account | Account ID |
| Site | Site ID |
| Group | Group ID |


<img width="475" height="702" alt="image" src="https://github.com/user-attachments/assets/913caac3-c348-41f0-826a-2b0a94b1deff" />

<img width="1439" height="573" alt="image" src="https://github.com/user-attachments/assets/fadbd8ad-50fb-41e2-8bc3-098d58cbc8b0" />

<img width="1438" height="292" alt="image" src="https://github.com/user-attachments/assets/49350557-d8d1-45c1-8b88-7f37b29fad06" />

