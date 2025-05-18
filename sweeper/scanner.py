from .pinger import ping_host
from concurrent.futures import ThreadPoolExecutor

def scan_ips(ip_list, threads=1):
    results = {}
    if threads > 1:
        with ThreadPoolExecutor(max_workers=threads) as executor:
            scan_results = executor.map(ping_host, ip_list)
            for ip, status in zip(ip_list, scan_results):
                results[ip] = status
    else:
        for ip in ip_list:
            results[ip] = ping_host(ip)
    return results