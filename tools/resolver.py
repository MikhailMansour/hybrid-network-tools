import socket
import dns.resolver as dns

def resolve_domain(domain):
    try:

        ip = socket.gethostbyname(domain)

       
        res_text = "Domain: " + domain + " | IP: " + ip + "\n"

        print(ip)
        print("*" * 20)

        ns_r = dns.resolve(domain, "NS")

        res_text += " Name Servers:\n"

        for ns in ns_r:
            print(ns)
            res_text += str(ns) + "\n"

        return res_text

    except Exception as e:
        print("Error in resolving domain:", e)
        return "Error in resolving " + domain + "\n"

