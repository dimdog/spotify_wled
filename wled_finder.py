from zeroconf import Zeroconf, ServiceBrowser
import time

class WLEDListener:
    def __init__(self):
        self.devices = []

    def remove_service(self, zeroconf, type, name):
        pass

    def add_service(self, zeroconf, type, name):
        info = zeroconf.get_service_info(type, name)
        if info:
            ip_address = ".".join(map(str, info.addresses[0]))
            print(f"Found WLED device: {name} at {ip_address}")
            self.devices.append((name, ip_address))

    def update_service(self, *args, **kwargs):
        pass

def scan_for_wled_servers() -> dict[str, str]:
    zeroconf = Zeroconf()
    listener = WLEDListener()

    browser = ServiceBrowser(zeroconf, "_wled._tcp.local.", listener)
    time.sleep(5)
    zeroconf.close()
    if listener.devices:
        return {name : ip for name, ip in listener.devices}
    
    

if __name__ == "__main__":
    print(scan_for_wled_servers())