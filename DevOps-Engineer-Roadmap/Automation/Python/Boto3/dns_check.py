#using example
#python3 dns_check.py 'stackoverflow.com'

import sys

import dns.resolver

NAMESERVERS = ['1.1.1.1', '8.8.8.8']


def is_resolved_same(fqdn):

    res = dns.resolver.Resolver()

    try:

        sys_resolved_ip = res.query(fqdn)

        ex_resolved_ip = set()
        for ns in NAMESERVERS:
            res.nameservers = [ns]
            ex_resolved_ip.update(list(res.query(fqdn)))

        for rdata in sys_resolved_ip:
            if rdata not in ex_resolved_ip:
                return False

    except:
        return False

    return True


if __name__ == "__main__":

    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} 'fqdn'")
        sys.exit(0)
    if is_resolved_same(sys.argv[1]):
        print(f"The same result is returned for {sys.argv[1]}.")
    else:
        print(f"!!!There seems problem with {sys.argv[1]}.!!!")
