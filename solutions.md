# Lab Environment: Easy Machines 0x1 (Consolidated)

Each machine is a single, unified container running 5 services, simulating a real-world target with a single IP and multiple exposed ports.

## Port Scheme: 90[Machine#][Service#]

## Machine 1: Infrastructure Health (901x)
| Port | Service | Status | Vulnerability |
|------|---------|--------|---------------|
| 9011 | Web App | **VULNERABLE** | Command Injection in `/api/health` |
| 9012 | SSH     | **VULNERABLE** | Weak Credentials (`root:password123`) |
| 9013 | FTP     | **VULNERABLE** | Anonymous Login Enabled |
| 9014 | Redis   | Secure | Protected Mode Off |
| 9015 | Nginx   | Secure | Default Setup |

## Machine 2: Corporate Gateway (902x)
| Port | Service | Status | Vulnerability |
|------|---------|--------|---------------|
| 9021 | index.php| **VULNERABLE** | PHP 8.1.0-dev Backdoor via `User-Agentt` header (Leaks version in `X-Powered-By`) |
| 9022 | MariaDB | **VULNERABLE** | Weak Credentials (init via entrypoint) |
| 9023 | SMB     | **VULNERABLE** | Guest Access Enabled |
| 9024 | Postgres| Secure | Strong Credentials |
| 9025 | Apache  | Secure | Standard Setup |

## Machine 3: Vision AI (903x)
| Port | Service | Status | Vulnerability |
|------|---------|--------|---------------|
| 9031 | Node App| **VULNERABLE** | Remote Code Execution via `eval()` |
| 9032 | Telnet  | **VULNERABLE** | Weak Credentials (`admin:admin`) |
| 9033 | MongoDB | **VULNERABLE** | Unauthenticated Access |
| 9034 | Memcache| Secure | Default |
| 9035 | Lighttpd| Secure | Default |

## Machine 4: WP Ops (904x)
| Port | Service | Status | Vulnerability |
|------|---------|--------|---------------|
| 9041 | WordPress| **VULNERABLE** | CVE-2020-25213 (WP File Manager RCE) |
| 9042 | SSH      | **VULNERABLE** | Weak Credentials (`root:root`) |
| 9043 | MySQL    | **VULNERABLE** | Exposed Root Access |
| 9044 | Grafana  | **VULNERABLE** | CVE-2021-43798 (Path Traversal) |
| 9045 | Nginx    | Secure         | Default |

## Machine 5: Stellar ERP (905x)
| Port | Service | Status | Vulnerability |
|------|---------|--------|---------------|
| 9051 | Laravel  | **VULNERABLE** | CVE-2021-3129 (Ignition RCE) |
| 9052 | SSH      | Secure         | Strong Password (`root:securepassword`) |
| 9053 | Jenkins  | **VULNERABLE** | CVE-2024-23897 (LFI / File Read) |
| 9054 | Postgres | Secure         | Standard |
| 9055 | Redis    | Secure         | Standard |

## Deployment
```bash
docker compose up -d --build
```

## Quick Test Commands
```bash
# Test Web Apps
curl http://localhost:9011                    # Machine 1 - Command Injection
curl http://localhost:9021                    # Machine 2 - PHP Backdoor
curl http://localhost:9031                    # Machine 3 - Node.js RCE
curl http://localhost:9041                    # Machine 4 - WordPress
curl http://localhost:9051                    # Machine 5 - Laravel

# Test SSH
ssh root@localhost -p 9012                    # Machine 1 (password123)
ssh root@localhost -p 9042                    # Machine 4 (root)

# Test FTP
ftp localhost 9013                            # Machine 1 (anonymous)
```

## Nuclei Detection
All vulnerable services can be detected using:
```bash
nuclei -u http://localhost:9021 -t scripts/php-zerodium-backdoor.yaml # PHP Backdoor
nuclei -u http://localhost:9041 -t cves/      # WordPress CVE
nuclei -u http://localhost:9044 -t cves/      # Grafana CVE
nuclei -u http://localhost:9051 -t cves/      # Laravel CVE
nuclei -u http://localhost:9053 -t cves/      # Jenkins CVE
```
