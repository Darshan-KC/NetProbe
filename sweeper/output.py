try:
    from colorama import Fore, Style, init
    init(autoreset=True)
    COLOR_ENABLED = True
except ImportError:
    COLOR_ENABLED = False


def print_results(results, show_all=False):
    for ip, status in results.items():
        if status or show_all:
            status_text = "Alive" if status else "Dead"
            if COLOR_ENABLED:
                color = Fore.GREEN if status else Fore.RED
                print(f"{color}{ip} - {status_text}")
            else:
                print(f"{ip} - {status_text}")
    print_summary(results)

def print_summary(results):
    total = len(results)
    alive = sum(1 for status in results.values() if status)
    print(f"\nSummary: {alive}/{total} hosts are up")