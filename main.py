print("Defanging an IP Address.")

ip_address = "192.168.48.84"

ip = ip_address.split(".")
lastDot = "[.]".join(ip)
print(lastDot) 


