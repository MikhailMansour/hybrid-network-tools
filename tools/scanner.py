import socket

def scan_ports(target):
    target = target.strip()
    ports = [21, 22, 80, 443]
    
    print(f"\n--- Port Scan Results for: {target} ---") 
    
    results_for_save = f"--- Port Scan Results for: {target} ---\n"
    
    for port in ports:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        try:
            result = s.connect_ex((target, port))
            if result == 0:
                output = f"Port {port}: OPEN"
            else:
                output = f"Port {port}: CLOSED"
            
            print(output) 
            results_for_save += output + "\n"
            
        except Exception as e:
            err = f"Port {port}: Error - {e}"
            print(err)
            results_for_save += err + "\n"
        finally:
            s.close()
            
    return results_for_save 