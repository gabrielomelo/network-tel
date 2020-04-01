#!/usr/bin/env python3


"""
    network-tel ou Network Telemetry retorna sessões (se possível) e informações sobre os hosts na rede local
    com o uso de utilitarios de linha de comando e scanners de rede.
    author: Gabriel Melo
"""


import os  # funcionalidades basicas do os host
import nmap  # network mapper
import json  # json manip lib
import socket  # socket para criar o server
import threading  # thread lib
import subprocess  # subprocess lib

from host import Host

# escaneia uma rede e uma lista de portas (int)
def scanNetwork(network, ports):

    scanner = nmap.PortScanner()

    res = scanner.scan(network, ports)
    print(json.dumps(res, indent=2))

    return res


# recebe o resultado de um scan e cria os objetos de host
def getScannedHosts(scan_result):
    return []


def getCommandSet(path):
    return []


if __name__ == "__main__":

    network = "127.0.0.1"
    ports = "22-8080"

    commands = getCommandSet("telemetry.sh")

    s_result = scanNetwork(network, ports)

    hosts = getScannedHosts(s_result)

"""
    for h in hosts: h.getSession()

    for h in hosts:
        h.setCommands(commands)
        h.execCommands()
"""