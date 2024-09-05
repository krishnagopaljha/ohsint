import socket
import ssl
import datetime

def get_certificate_details(domain):
    """Retrieve and display SSL/TLS certificate details."""
    context = ssl.create_default_context()
    with socket.create_connection((domain, 443)) as sock:
        with context.wrap_socket(sock, server_hostname=domain) as ssock:
            cert = ssock.getpeercert()
            return cert

def parse_certificate(cert):
    """Parse certificate details."""
    cert_info = {
        'subject': dict(x[0] for x in cert['subject']),
        'issuer': dict(x[0] for x in cert['issuer']),
        'version': cert['version'],
        'serialNumber': cert['serialNumber'],
        'notBefore': cert['notBefore'],
        'notAfter': cert['notAfter']
    }
    return cert_info

if __name__ == "__main__":
    domain = input("Enter the domain to check SSL/TLS certificate: ")
    cert = get_certificate_details(domain)
    cert_info = parse_certificate(cert)
    print("Certificate Details:")
    for key, value in cert_info.items():
        print(f"{key}: {value}")
