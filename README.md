# network-tel - Network telemetry tool

## Objetivo

Construir um software em python que possibilite a execução de comandos de forma remota usando o ssh, telnet, WinRM (Windows remote management protocol) e WMI (Windows Management Instrumentation).

## Entregas

O trabalho foi dividido em 5 entregas diferentes que compõem a nota semestral. Tinha uma ideia do iria entregar, porém, devido a situação atual e de não ter o laboratório disponível algumas features sofreram mudanças.

1. Script usando subprocesso - Feito.
2. Acesso remoto pelo subprocesso - Feito, mas não é o padrão no repositório (é necessário apenas alterar uma linha para a chamado do ssh).
3. Execução de rotina personalizada - Feito.
4. Information Gathering da rede - Feito.
5. Testes/Correções - Foram feitas de forma implicita e com limitações de espaço e infra-estrutura. Houve uma mudança para: "Paralelismo baseado em threads".

### Features

Temos algumas features que podem estar contidas no fim desse projeto:

* Execução de Scripts personalizados de maneira remota e coordenada.
* Execução de Scans de rede na rede local a fim de descobrir máquinas "vulneráveis" ao protocolo e consequentemente linguagem utilizada para os scripts.
* Uso de paralelismo baseado em threads na execução de mais de um ataque por vez, ou seja, de forma assíncrona

## Uso do sistema de arquivos

O sistema de arquivos está sendo usado aqui das seguintes maneiras:
* Utilizei o stdin e stdout (buffers de entrada e saída padrão de um processo), que são tradados como arquivo nos sistemas da família UNIX.
* Utilizei as funções de leitura e escrita de arquivos contidas na lib nativa do python 3, essas funções se assemelham ao C quando de maneira abstrata utilizam-se de um ponteiro de arquivos "fp" provenientes a uma requisição ao FS.
* Utilizei alguns comandos GNU (GNU is NOT UNIX) afim de interagir com o host alvo, são eles:
* * ls - list. Lista os conteúdos de um path que esteja gravado na FAT.
* * free. Retorna o "extrato" do sistema de arquivos.
* * Diversos comandos de listagem de dispositivos de rede e etc, esses que mesmo que físicos são tratados como arquivos e estão presentes na árvore gerenciada pelo sistema de arquivos virtual.

## Uso do scanner de rede

O scanner de rede interage com outras máquinas utilizando dos protocolos TCP (nessa implementação), utilizei a abstração do nmap para o python, esta que por sua vez facilita muito a maneira como indexei as máquinas que estão up e possuem uma porta escutando o protocolo que estamos tentando utilizar.

O scanner realiza um scan de serviço apenas e retorna um json com todos os serviços encontrados e estados das portas, e podemos especificar para a API qual porta/protocolo estamos desejando atacar.

## Uso do PID fork

O PID fork foi utilizado de uma maneira diferente da demonstrada nos exemplos. Os exemplos utilizam-se das funções contidas na clib, enquanto que em nossa implementação é utilizado a biblioteca nativa do python para o gerenciamento de subprocessos.

Para realizar um PID fork no python temos que utilizar a lib subprocess, porém temos que prestar atenção em alguns detalhes como qual processo estamos fazendo o fork. Para isso utilizamos o parametro "shell=False" na classe Popen (esta classe é um construtor de processos), este parametro transforma nosso novo processo em subprocesso de shell que executará em si mesma a lista de comandos dos arquivos sh.

Esse processo de criação de subprocesso utiliza a função os.fork() a fim de criar um processo filho (um novo pid partindo do pid atual).

## Uso das Threads

O uso das threads foi pensado de um modo que não tornasse a ferramenta em algo diferente do idealizado no momento de sua concepção. Foi utilizada a mesma forma como o make trata um processo de compilação (o uso de jobs), ou seja, pego partes que são diferentes e as faço serem executadas de forma paralela por meio de processos individuais contidos em cada thread.

Suponhamos que temos uma rede de 254 hosts e nela 10 possuem a porta 22 da pilha tcp aberta, tendo utilizado a flag de scan e indicando para o scanner qual porta (protocolo) estamos procurando, teremos 10 jobs a ser realizados, e esses irão virar subshells do meu processo atual, ou seja, teremos outro PID. Tendo esse novo processo, teremos também um objeto de subprocesso que serão incializados e iniciados em diferentes threads (não concorrentes).

Isso possibilita algo bem interessante, imagine que dessas 254 máquinas, 64 estão vulneráveis, podemos realizar a tentativa de intrusão/telemetria de acordo com nosso hardware ao inves de ser de modo sequencial, podemos ter 8 threads e terminar a atividade em 1/8 do tempo.

## Bash Scripting e Custom Scripts

Temos um arquivo padrão que é utilizado para realizar o reconhecimento do host que temos acesso (res/inf-gathering.sh). 
Embora ele seja bem completo para fins de demonstração, pode ser que o usuário queira usar algo mais adequado a sua situação, ou até mesmo esteja lidando com outra linguagem (bash, bat, python e etc) no endpoint a ser atacado. Para isso temos um parametro "--path" que pode ser passado de maneira absoluta ou relativa ao seu ponto de execução.

## Referências

* Mitre ATT&CK. Disponível em: https://attack.mitre.org/. Acessado em 15/05/2020.
* Atomic Red Team. Red Canary. Disponível em: https://atomicredteam.io/. Acessado em 15/05/2020.
* Python 3.7. Python Software Foundation. Disponível em: https://python.org. Acessado em 15/05/2020.
