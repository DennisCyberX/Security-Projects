
---

### **2. Network Traffic Analysis**
#### `Network-Traffic-Analysis/traffic_analysis.py`
```python
import scapy.all as scapy
from datetime import datetime

def sniff_packets(interface="eth0", count=10):
    print(f"Sniffing {count} packets on interface {interface}...")
    packets = scapy.sniff(iface=interface, count=count)
    for packet in packets:
        print(f"[{datetime.now()}] Packet: {packet.summary()}")

if __name__ == "__main__":
    sniff_packets()
