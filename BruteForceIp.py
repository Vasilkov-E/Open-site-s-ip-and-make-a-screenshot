from ipaddress import IPv4Network
import TranslatingIpAddressToDomain
import SscreenshotOfWebPage


def brute_force_ip(ip: str):
    '''
    :param ip:  entered in the format '12.32.23.12' or '12.32.23.0/24'
    :return:
    '''
    range_ip = IPv4Network(ip)
    ip = []
    for el in range_ip:
        ip.append((str(el), 443))

    urls = TranslatingIpAddressToDomain.qwe(ip)
    SscreenshotOfWebPage.screenshot_of_web_page(urls)
