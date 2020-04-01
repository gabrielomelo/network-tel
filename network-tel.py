#!/usr/bin/env python3


"""
    network-tel ou Network Telemetry retorna sessões (se possível) e informações sobre os hosts na rede local
    com o uso de utilitarios de linha de comando e scanners de rede.
    author: Gabriel Melo
"""


import os  # funcionalidades basicas do os host
import nmap  # network mapper
import json  # json manip lib
import threading  # thread lib
import subprocess  # subprocess lib

def getCommandSet(path):
    
    with open(path, "r") as fp:
        command_set = fp.readlines()

    temp = list()
    
    for line in command_set:
        if line != "\n" and line[0] != "#":
            temp.append(line)

    return ''.join(line for line in temp)

"""
    Função executa cada uma série de comandos em um host especifico. O ssh será usado em laboratório na data da última entrega.
"""
def execCmds(user, host, port, password, cmds):
    #bash_path = "sshpass -p " + password + " ssh " + user + "@" + host + " -p" + port
    
    bash_path = '/bin/bash'

    shell = subprocess.Popen(bash_path , stdin=subprocess.PIPE, stdout=subprocess.PIPE)

    out, err = shell.communicate(input=cmds.encode())

    print(out.decode())


# Começo do processo principal

if __name__ == "__main__":

    network = "127.0.0.1"
    ports = "22-8080"

    # Conjunto de comandos é coletado do arquivo shell script
    commands = getCommandSet("inf-gathering.sh")

    # Comandos são executados em um subprocesso (podendo ser este o ssh) 
    execCmds('', '', '22', '', commands)

    # tirar os comentários para ver o resultado do scaneamento
    """
    scanner = nmap.PortScanner()
    s_result = scanner.scan(network, ports)
    print(json.dumps(s_result, indent=2))
    """
