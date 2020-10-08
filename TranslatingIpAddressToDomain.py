# from dns import resolver,reversename
# addr=reversename.from_address("8.8.8.8")
# print(str(resolver.resolve(addr,"PTR")[0]))
# -----------------------------------------------------------------------------------
import asyncio
import logging
import socket
import sys


TARGETS = [
    ('104.20.42.23', 443),
    ('66.33.211.240', 443),
    ('45.55.99.72', 443),

]


async def main(loop, targets):
    for target in targets:
        info = await loop.getnameinfo(target)
        print('{:15}: {} {}'.format(target[0], *info))


event_loop = asyncio.get_event_loop()
try:
    event_loop.run_until_complete(main(event_loop, TARGETS))
finally:
    event_loop.close()
# -0----------------------------------------------------------------------------------
# import asyncio
# import logging
# import socket
# import sys
#
#
# TARGETS = [
#     ('4pda.ru', 'https'),
#     ('doughellmann.com', 'https'),
#     ('python.org', 'https'),
# ]
#
#
# async def main(loop, targets):
#     for target in targets:
#         info = await loop.getaddrinfo(
#             *target,
#             proto=socket.IPPROTO_TCP,
#         )
#
#         for host in info:
#             print('{:20}: {}'.format(target[0], host[4][0]))
#
#
# event_loop = asyncio.get_event_loop()
# try:
#     event_loop.run_until_complete(main(event_loop, TARGETS))
# finally:
#     event_loop.close()

#------------------------------------------------------------
# import socket
# s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# s.connect(("8.8.8.8", 80))
# print(s.getsockname()[0])
# s.close()


# import dns.name
# import dns.message
# import dns.query
# import dns.flags
#
# domain = 'google.com'
# name_server = '8.8.8.8'
# ADDITIONAL_RDCLASS = 65535
#
# domain = dns.name.from_text(domain)
# if not domain.is_absolute():
#     domain = domain.concatenate(dns.name.root)
#
# request = dns.message.make_query(domain, dns.rdatatype.ANY)
# request.flags |= dns.flags.AD
# request.find_rrset(request.additional, dns.name.root, ADDITIONAL_RDCLASS,
#                    dns.rdatatype.OPT, create=True, force_unique=True)
# response = dns.query.udp(request, name_server)
#
#
# print (response.answer)
# print (response.additional)
# print (response.authority)
