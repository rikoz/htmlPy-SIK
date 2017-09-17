from wireless import Wireless

sik_wireless = Wireless()

def sik_iface():
    ifaces = sik_wireless.interfaces()
    return ifaces[0]
