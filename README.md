# NetInspector

NetInspector es una herramienta basada en Python diseñada para analizar capturas de paquetes de red. Actualmente, soporta la extracción y análisis de información de paquetes HTTP, FTP y SSH.

## Estructura del Proyecto

```
NetInspector/
│
├── analyse_protocols.py     # Script principal para el análisis de paquetes
├── test_analyse_protocols.py # Suite de pruebas
├── sample.pcap              # Archivo de captura de paquetes de muestra para pruebas
└── README.md                # Este archivo
```

## Características

- Analiza archivos PCAP (Packet Capture)
- Extrae información detallada de paquetes HTTP
- Analiza códigos de comando y respuesta FTP
- Identifica versiones de protocolo SSH
- Arquitectura extensible para agregar soporte para protocolos adicionales
- Manejo de errores completo para un análisis de paquetes robusto

## Prerrequisitos

Antes de comenzar, asegúrate de cumplir con los siguientes requisitos:

- Python 3.12 o superior
- pip (instalador de paquetes de Python)
- Biblioteca pyshark

## Instalación

1. Clona el repositorio de NetInspector:
   ```
   git clone https://github.com/elliotsecops/NetInspector.git
   cd NetInspector
   ```

2. Instala la dependencia requerida:
   ```
   pip install pyshark
   ```

## Uso

Para usar NetInspector:

1. Asegúrate de tener un archivo PCAP listo para el análisis. Puedes usar el archivo `sample.pcap` proporcionado para pruebas.

2. Ejecuta el script con tu archivo PCAP:
   ```
   python analyse_protocols.py path/to/your/capture.pcap
   ```

   Por ejemplo, para analizar el archivo de muestra:
   ```
   python analyse_protocols.py sample.pcap
   ```

3. El script mostrará la información analizada de los paquetes para los protocolos HTTP, FTP y SSH.

## Ejecutar Pruebas

Para ejecutar las pruebas de NetInspector:

1. Asegúrate de tener pytest instalado:
   ```
   pip install pytest
   ```

2. Ejecuta las pruebas:
   ```
   pytest -vv
   ```

## Contribuir

¡Las contribuciones a NetInspector son bienvenidas! Aquí hay algunas formas en las que puedes ayudar:

1. Reportar errores e incidencias
2. Sugerir nuevas características o mejoras
3. Enviar solicitudes de extracción (pull requests) con correcciones de errores o nuevas funcionalidades

## Licencia

Este proyecto está licenciado bajo la Licencia MIT - consulta el archivo [LICENSE](LICENSE) para más detalles.

## Agradecimientos

- [pyshark](https://github.com/KimiNewt/pyshark) - Wrapper de Python para tshark, que este proyecto utiliza para el análisis de paquetes

---

¡Feliz análisis de paquetes con NetInspector!

---

# NetInspector

NetInspector is a Python-based tool designed for analyzing network packet captures. It currently supports the extraction and analysis of information from HTTP, FTP, and SSH packets.

## Project Structure

```
NetInspector/
│
├── analyse_protocols.py     # Main script for packet analysis
├── test_analyse_protocols.py # Test suite
├── sample.pcap              # Sample packet capture file for testing
└── README.md                # This file
```

## Features

- Analyze PCAP (Packet Capture) files
- Extract detailed information from HTTP packets
- Parse FTP command and response codes
- Identify SSH protocol versions
- Extensible architecture for adding support for additional protocols
- Comprehensive error handling for robust packet analysis

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.12 or higher
- pip (Python package installer)
- pyshark library

## Installation

1. Clone the NetInspector repository:
   ```
   git clone https://github.com/elliotsecops/NetInspector.git
   cd NetInspector
   ```

2. Install the required dependency:
   ```
   pip install pyshark
   ```

## Usage

To use NetInspector:

1. Ensure you have a PCAP file ready for analysis. You can use the provided `sample.pcap` for testing.

2. Run the script with your PCAP file:
   ```
   python analyse_protocols.py path/to/your/capture.pcap
   ```

   For example, to analyze the sample file:
   ```
   python analyse_protocols.py sample.pcap
   ```

3. The script will output the analyzed packet information for HTTP, FTP, and SSH protocols.

## Running Tests

To run the tests for NetInspector:

1. Ensure you have pytest installed:
   ```
   pip install pytest
   ```

2. Run the tests:
   ```
   pytest -vv
   ```

## Contributing

Contributions to NetInspector are welcome! Here are a few ways you can help:

1. Report bugs and issues
2. Suggest new features or improvements
3. Submit pull requests with bug fixes or new functionality

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [pyshark](https://github.com/KimiNewt/pyshark) - Python wrapper for tshark, which this project uses for packet analysis

---

Happy packet analyzing with NetInspector!
