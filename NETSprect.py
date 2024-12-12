import scapy.all as scapy
import socket
import argparse
import json

def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    answered = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]
    
    devices = []
    for element in answered:
        devices.append({'ip': element[1].psrc, 'mac': element[1].hwsrc})
    return devices

def scan_ports(ip):
    open_ports = []
    for port in range(1, 1025):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.5)
            result = sock.connect_ex((ip, port))
            if result == 0:
                open_ports.append(port)
            sock.close()
        except:
            pass
    return open_ports

def main():
    parser = argparse.ArgumentParser(description="NetScanPro - Ferramenta de análise de rede.")
    parser.add_argument("--target", help="Alvo ou range de IPs (ex: 192.168.0.1/24)", required=True)
    parser.add_argument("--output", help="Arquivo de saída (JSON)", default="scan_report.json")
    args = parser.parse_args()

    print(f"Scanning network: {args.target}...")
    devices = scan(args.target)

    print("Scanning ports...")
    for device in devices:
        device['open_ports'] = scan_ports(device['ip'])

    with open(args.output, 'w') as f:
        json.dump(devices, f, indent=4)
    print(f"Report saved to {args.output}")

if __name__ == "__main__":
    main()
