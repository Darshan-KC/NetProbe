from sweeper import parse_cidr, parse_range, scan_ips, print_results

def demo():
    # Example input (you can change this to any CIDR or IP range)
    cidr_input = "192.168.1.0/24"  # Gives 192.168.1.1 and 192.168.1.2

    print("[+] Parsing CIDR range...")
    ip_list = parse_cidr(cidr_input)

    print(f"[+] Scanning {len(ip_list)} hosts...")
    results = scan_ips(ip_list, threads=5)

    print("[+] Scan results:")
    print_results(results)

    # print("[+] Exporting results to 'results.txt'...")
    # export_results(results, "results.txt", filetype="txt")

if __name__ == "__main__":
    demo()
