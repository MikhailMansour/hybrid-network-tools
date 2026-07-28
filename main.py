from tools.resolver import resolve_domain
from tools.scanner import scan_ports
from tools.analyzer import analyze_http
from tools.chat import start_server
import socket

def save(data):
    try:
         with open("results.txt", "a", encoding="utf-8") as f:
            f.write(str(data) + "\n" + "-"*30 + "\n")

    except:
        print("error saving to file ")


while True:
    print("\n====================")
    print("HYBRID NETWORK TOOL")
    print("====================")
    print("1- Domain Resolver")
    print("2- Port Scanner")
    print("3- HTTP Analyzer")
    print("4- Chat Server")
    print("5- Integration (Full Scan)")
    print("6- Exit")

    choice = input("Select: ").strip()

    if choice == "1":
        d = input("Enter Domain: ")
        res = resolve_domain(d)
        print(res)
        save(res)

    elif choice == "2":
        ip = input("Enter IP: ")
        res = scan_ports(ip)
        print(res)
        save(res)

    elif choice == "3":
        url = input("URL: ")
        res = analyze_http(url) 
        print(res)             
        save(res)             

    elif choice == "4":
        print("[*] Starting Chat Server... Waiting for connection.")
        start_server()

    elif choice == "5":
      
        domain = input("Enter Domain for full analysis: ")
        try:
            print("Resolving...")
            ip = socket.gethostbyname(domain)
            print("Scanning IP: " + ip)
            res = scan_ports(ip)
            print(res)
            save("Full Integration Scan for " + domain + " (" + ip + "):\n" + res)
        except:
            print("Integration failed - Check domain")

    elif choice == "6":
        print("Closing Program...")
        break

    else:
        print("Invalid choice, please try again.")