import pyshark

def extract_http_info(packet):
    return {
        'protocolo': 'HTTP',
        'metodo': packet.http.request_method,
        'codigo_estado': packet.http.status_code,
        'contenido': packet.http.get_field_value('file_data') or ''
    }

def extract_ftp_info(packet):
    return {
        'protocolo': 'FTP',
        'comando': packet.ftp.request_command,
        'codigo_respuesta': packet.ftp.response_code
    }

def extract_ssh_info(packet):
    return {
        'protocolo': 'SSH',
        'version': packet.ssh.protocol_version
    }

def analyze_packets(pcap_file):
    capture = pyshark.FileCapture(pcap_file)
    results = []

    for packet in capture:
        try:
            if packet.highest_layer == 'HTTP':
                info = extract_http_info(packet)
                results.append(info)
            elif packet.highest_layer == 'FTP':
                info = extract_ftp_info(packet)
                results.append(info)
            elif packet.highest_layer == 'SSH':
                info = extract_ssh_info(packet)
                results.append(info)
        except AttributeError:
            # Handle potential errors if a field doesn't exist in the packet
            continue

    return results

# If you want to run this script directly, you can add:
if __name__ == "__main__":
    # Add any code here that you want to run when the script is executed directly
    pass