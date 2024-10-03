# test_analyse_protocols.py

import analyse_protocols
import pytest
from unittest import mock

def test_extract_http_info():
    # Create a mock for the HTTP packet
    http_packet = mock.Mock()
    http_packet.http.request_method = 'GET'
    http_packet.http.status_code = '200'
    http_packet.http.get_field_value.return_value = 'Hello World'

    result = analyse_protocols.extract_http_info(http_packet)
    assert result == {
        'protocolo': 'HTTP',
        'metodo': 'GET',
        'codigo_estado': '200',
        'contenido': 'Hello World'
    }

def test_extract_ftp_info():
    # Create a mock for the FTP packet
    ftp_packet = mock.Mock()
    ftp_packet.ftp.request_command = 'USER'
    ftp_packet.ftp.response_code = '331'

    result = analyse_protocols.extract_ftp_info(ftp_packet)
    assert result == {
        'protocolo': 'FTP',
        'comando': 'USER',
        'codigo_respuesta': '331'
    }

def test_extract_ssh_info():
    # Create a mock for the SSH packet
    ssh_packet = mock.Mock()
    ssh_packet.ssh.protocol_version = 'SSH-2.0'

    result = analyse_protocols.extract_ssh_info(ssh_packet)
    assert result == {
        'protocolo': 'SSH',
        'version': 'SSH-2.0'
    }

def test_analyze_packets(mocker):
    # Create mocks for packets of different protocols
    http_packet = mock.Mock()
    ftp_packet = mock.Mock()
    ssh_packet = mock.Mock()

    # Set up the values for HTTP, FTP, and SSH packets
    http_packet.highest_layer = 'HTTP'
    http_packet.http.request_method = 'GET'
    http_packet.http.status_code = '200'
    http_packet.http.get_field_value.return_value = 'Hello World'

    ftp_packet.highest_layer = 'FTP'
    ftp_packet.ftp.request_command = 'USER'
    ftp_packet.ftp.response_code = '331'

    ssh_packet.highest_layer = 'SSH'
    ssh_packet.ssh.protocol_version = 'SSH-2.0'

    # Mock FileCapture to return these packets
    mock_capture = mocker.patch('pyshark.FileCapture')
    mock_capture.return_value = [http_packet, ftp_packet, ssh_packet]

    # Execute the function and validate the result
    result = analyse_protocols.analyze_packets('mock_capture.pcap')

    expected_result = [
        {
            'protocolo': 'HTTP',
            'metodo': 'GET',
            'codigo_estado': '200',
            'contenido': 'Hello World'
        },
        {
            'protocolo': 'FTP',
            'comando': 'USER',
            'codigo_respuesta': '331'
        },
        {
            'protocolo': 'SSH',
            'version': 'SSH-2.0'
        }
    ]

    assert result == expected_result

# Run the tests
if __name__ == "__main__":
    pytest.main()