# network-tel - Network telemetry suite

## Integrantes

* Gabriel Melo
* Michelle Brandão
* Victtor Mendes

## Objetivo

Construir um software em python que possibilite a execução de comandos de forma remota usando o ssh, telnet, WinRM (Windows remote management protocol) e WMI (Windows Management Instrumentation).

### Possíveis Features

Temos algumas features que podem estar contidas no fim desse projeto:
* Execução de Scans de rede na rede local a fim de descobrir máquinas "vulneráveis" ao protocolo/linguagem utilizada para os scripts.
* Sistema servidor de comandos (CnC) multithread (ainda pensando na implementação ~não é tão fácil quanto parece~).
* Geração de relatório sobre estado de operação.

## Uso do sistema de arquivos

O sistema de arquivos está sendo usado aqui das seguintes maneiras:
* Utilizamos o stdin e stdout (buffers de entrada e saída padrão de um processo), que são tradados como arquivo nos sistemas da família UNIX.
* Utilizamos as funções de leitura e escrita de arquivos contidas na lib nativa do python 3, essas funções se assemelham ao C quando de maneira abstrata utilizam-se de um ponteiro de arquivos "fp" provenientes a uma requisição ao FS.
* Utilizamos alguns comandos GNU (GNU is NOT UNIX) afim de interagir com o host alvo, são eles:
* * ls - list. Lista os conteúdos de um path que esteja gravado na FAT.
* * free. Retorna o "extrato" do sistema de arquivos.
* * Diversos comandos de listagem de dispositivos de rede e etc, esses que mesmo que físicos são tratados como arquivos e estão presentes na árvore gerenciada pelo sistema de arquivos virtual.

## Uso do scanner de rede

O scanner de rede interage com outras máquinas utilizando dos protocolos TCP (na nossa implementação), utilizamos a abstração do nmap para o python, esta que por sua vez facilita muito a maneira como indexamos as máquinas que estão up e possuem uma porta escutando o protocolo que estamos tentando utilizar.

## Uso do PID fork

O PID fork foi utilizado de uma maneira diferente da demonstrada nos exemplos. Os exemplos utilizam-se das funções contidas na clib, enquanto que em nossa implementação é utilizado a biblioteca nativa do python para o gerenciamento de subprocessos.

Para realizar um PID fork no python temos que utilizar a lib subprocess, porém temos que prestar atenção em alguns detalhes como qual processo estamos fazendo o fork. Para isso utilizamos o parametro "shell=True" na classe Popen (esta classe é um construtor de processos), este parametro transforma nosso novo processo em subprocesso de shell que executará em si mesma a lista de comandos nos arquivos sh.

Esse processo de criação de subprocesso utiliza a função os.fork() a fim de criar um processo filho (um novo pid partindo do pid atual).

## Conceitos a implementar

### Threads


### Subprocess


## Referências


