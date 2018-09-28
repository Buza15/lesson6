import re

_ping = """

PING 8.8.8.8 (8.8.8.8) 56(84) bytes of data.
64 bytes from 8.8.8.8: icmp_seq=1 ttl=118 time=12.0 ms
64 bytes from 8.8.8.8: icmp_seq=2 ttl=118 time=13.8 ms
64 bytes from 8.8.8.8: icmp_seq=3 ttl=118 time=12.2 ms
64 bytes from 8.8.8.8: icmp_seq=4 ttl=118 time=12.4 ms

"""

compiled = re.compile(r'\b(icmp_seq=\w+) \b(ttl=\w+) (time=\w+.\w*)')
print(compiled.findall(_ping))
