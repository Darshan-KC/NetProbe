import argparse
from sweeper import parse_cidr, parse_range, scan_ips, print_results

def main():
    parser = argparse.ArgumentParser(description="NetProbe - A Simple Ping Sweeper")

    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--cidr", help="CIDR notation (e.g., 192.168.1.0/24)")
    group.add_argument("--range", nargs=2, metavar=('START_IP', 'END_IP'),
                       help="IP range (e.g., 192.168.1.1 192.168.1.10)")

    parser.add_argument("--threads", type=int, default=1, help="Number of threads to use")
    parser.add_argument("--all", action="store_true", help="Show all hosts (alive and dead)")
    parser.add_argument("--output", metavar="FILENAME", help="Output file name")
    parser.add_argument("--format", choices=["txt", "json", "csv"], default="txt",
                        help="Output file format")

    args = parser.parse_args()

    # Parse input IPs
    if args.cidr:
        ip_list = parse_cidr(args.cidr)
    elif args.range:
        ip_list = parse_range(args.range[0], args.range[1])
    else:
        parser.error("You must provide either --cidr or --range")

    print(f"[+] Scanning {len(ip_list)} hosts with {args.threads} thread(s)...")
    results = scan_ips(ip_list, threads=args.threads)

    print("[+] Scan results:")
    print_results(results, show_all=args.all)

    # if args.output:
    #     print(f"[+] Exporting results to {args.output}...")
    #     export_results(results, args.output, filetype=args.format)

if __name__ == "__main__":
    main()
