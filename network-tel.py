#!/usr/bin/env python3

"""
    network-tel ou Network Telemetry retorna sessões (se possível) e informações sobre os hosts na rede local
    com o uso de utilitarios de linha de comando e scanners de rede.
    author: Gabriel Melo
"""

import os  # funcionalidades basicas do os host
import nmap  # network mapper
import json  # json manip lib
import argparse  # cli parser (easier and pretty)
from threading import Thread, ThreadError  # thread lib
import subprocess  # subprocess lib
from random import randint
from res.opening import *  # importando os elementos gráficos

DEFAULT_RECON_SCRIPT = "res/inf-gathering.sh"
BASH_PATH = '/bin/bash'
SSH_PATH = '/bin/ssh'


def getCommandSet(path):
    with open(path, "r") as fp:
        command_set = fp.readlines()
    temp = list()
    for line in command_set:
        if line != "\n" and line[0] != "#":
            temp.append(line)
    return ''.join(line for line in temp)


#Função executa cada uma série de comandos em um host especifico. O ssh será usado em laboratório na data da última entrega.
def execCmds(index):
    #bash_path = "sshpass -p " + "aluno123" + " ssh " + "aluno" + "@" + hosts[index] + " -p" + args.port
    shell = subprocess.Popen(BASH_PATH , stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    out = shell.communicate(input=commands.encode())
    print('host number: ', str(index), ' host: ', hosts[index], '\n\n', out[0].decode())


# Escaneia um host ou uma rede e retorna todos os hosts que possuem a porta especificada na entrada do programa
def scanner(args):
    hosts = list()
    if args.scan:
        scanner = nmap.PortScanner()
        scanner.scan(args.network, args.port)
        for host in scanner.all_hosts():
            if scanner[host].has_tcp(int(args.port)):
                hosts.append(host)
        return hosts
    else:
        return [args.network]


# Cria varias threads e executa uma lista de comandos
def theMultiThreader(args, hosts):
    try:
        threads = list()
        for i in range(0, len(hosts), int(args.jobs)):
            for j in range(0, int(args.jobs), 1):
                if (i+j) >= len(hosts): return
                threads.append(Thread(target=execCmds, args=[i+j]))
                threads[i+j].start()
    except ThreadError as e:
        print(e)


# Monta o menu e o objeto namespace para o inicio do programa
def getArgs():
    parser = argparse.ArgumentParser()
    parser.add_argument('--scan', '-s', action='store_true', help='if you want to scan an entire network or a host tick this flag')
    parser.add_argument('--network', '-n', metavar='string', required=True, help='pass the network address or the host address to the scanner. If the scan flag is not present, then this parameter will be the targeted host')
    parser.add_argument('--port', '-p', metavar='string', help='port for the scanner if the scanner flag is passed')
    parser.add_argument('--path', metavar='string', default=DEFAULT_RECON_SCRIPT ,help='custom script path, if not defined the program will send the default recon.')
    parser.add_argument('--host', metavar='string', help='if you dont want to scan a network, pass the host to execute some remote shit')
    parser.add_argument('--service', metavar='string', default=BASH_PATH, help='if you want to specify the type of service (ssh, telnet, powershell or even your local bash. The default one is bash')
    parser.add_argument('--jobs', '-j', metavar='integer', default='1', help='number of simultaneous subprocesses. The default is 1')

    return parser.parse_args()


if __name__ == "__main__":
    print(openings[randint(0, len(openings)-1)], intro)

    args = getArgs()
    current_job_host = str()
    commands = getCommandSet(args.path)

    hosts = scanner(args)
    theMultiThreader(args, hosts)
