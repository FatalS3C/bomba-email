#Outros
versao = '0.1'

#Bibliotecas
import os
from os import name, system
import requests
import argparse
import sys
import json
import smtplib
from time import sleep
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

#Classes
class texto():
	reseta = '\u001b[0m'
	negrito = '\u001b[1m'
	italico = '\u001b[3m'
	underline = '\u001b[4m'
	piscapisca = '\u001b[5m'
	invertido = '\u001b[7m'
	strike = '\u001b[9m'
	doisunderline = '\u001b[21m'
	class cor():
		preto = '\u001b[38;5;240m'
		branco = '\u001b[38;5;255m'
		azul = '\u001b[38;5;4m'
		verde = '\u001b[38;5;40m'
		vermelho = '\u001b[38;5;124m'
		amarelo = '\u001b[38;5;11m'
		azul_claro = '\u001b[38;5;87m'
		verde_claro = '\u001b[38;5;85m'
		vermelho_claro = '\u001b[38;5;196m'
		amarelo_claro = '\u001b[38;5;220m'
	class fundo():
		preto = '\u001b[48;5;240m'
		branco = '\u001b[48;5;255m'
		azul = '\u001b[48;5;4m'
		verde = '\u001b[48;5;40m'
		vermelho = '\u001b[48;5;124m'
		amarelo = '\u001b[48;5;11m'
		azul_claro = '\u001b[48;5;87m'
		verde_claro = '\u001b[48;5;85m'
		vermelho_claro = '\u001b[48;5;196m'
		amarelo_claro = '\u001b[48;5;220m'
		
#Defs
def clear():
	if name == 'nt':
	  _ = system('cls')
	else:
	  _ = system('clear')   
	  
def log(txt):
	print(f'{texto.negrito}{texto.italico}{texto.cor.branco}{txt}{texto.reseta}')
def sucesso(txt):
	print (f'{texto.negrito}{texto.cor.verde_claro}{txt}{texto.reseta}')
def erro(txt):
	print (f'{texto.fundo.vermelho} {texto.reseta} {texto.negrito}{texto.italico}{texto.cor.vermelho_claro}{txt}{texto.reseta} {texto.fundo.vermelho} {texto.reseta}')
def alerta(txt):
	print (f'{texto.fundo.amarelo} {texto.reseta} {texto.negrito}{texto.italico}{texto.cor.amarelo_claro}{txt}{texto.reseta} {texto.fundo.amarelo} {texto.reseta}')
def opc(um, dos):
	print (f'{texto.negrito}{texto.cor.branco}[{texto.cor.verde_claro}{um}{texto.cor.branco}] {texto.cor.verde}{dos}{texto.reseta}')
def opc2(um, dos):
	print (f'{texto.negrito}{texto.cor.branco}[{texto.cor.vermelho_claro}{um}{texto.cor.branco}] {texto.cor.vermelho_claro}{dos}{texto.reseta}')
def titulo(tetulorkkkkk):
	print (f'{texto.negrito}{texto.cor.branco}| {texto.underline}{texto.cor.verde}{tetulorkkkkk}{texto.reseta} {texto.negrito}{texto.cor.branco}|{texto.reseta}\n')

def email_txt(alvo, mensagem, base):
	email_do_s = (list(base.keys())[0])
	config = (base[email_do_s])
	smtp_server = (config['server'])
	perfil = json.loads(open('perfil.json', 'r').read())
	message = MIMEText(mensagem, "plain")
	
	message["Subject"] = perfil['subject']
	if (config['relay']) == True:
		email_de_uso = perfil['from']
	else:
		email_de_uso = email_do_s
	with smtplib.SMTP(smtp_server, config['porta']) as server:
		if config['senha'] != False:
			server.login(email_do_s, config['senha'])
		if config['ttls'] != False:
			server.starttls()
		server.sendmail(email_de_uso, alvo, message.as_string())
def email_html(alvo, mensagem, base):
	email_do_s = (list(base.keys())[0])
	config = (base[email_do_s])
	smtp_server = (config['server'])
	perfil = json.loads(open('perfil.json', 'r').read())
	message = MIMEText(mensagem, "html")
	
	message["Subject"] = perfil['subject']
	if (config['relay']) == True:
		email_de_uso = perfil['from']
	else:
		email_de_uso = email_do_s
	with smtplib.SMTP(smtp_server, config['porta']) as server:
		if config['senha'] != False:
			server.login(email_do_s, config['senha'])
		if config['ttls'] != False:
			server.starttls()
		server.sendmail(email_de_uso, alvo, message.as_string())
#COMEÇO
# Argumentos
parser = argparse.ArgumentParser(description='Essa é uma ferramenta de SPAM em email, use --help para pedir ajuda!', prog='bombamail.py', usage='''Você pode editar os seus perfis, armazém de email e atualizar a ferramenta da seguinte forma:

Atualizar: python3 bomba-mail.py --update
Spam: python3 bomba-mail.py --spam -t email@alvo.com -q 25 --sleep 2 
Adicionar um novo email ao banco: python3 bomba-mail.py --add EMAIL,SENHA,PORTA,SERVIDOR,TTLS,RELAY
Resetar o banco: python3 bomba-mail.py --reset
Iniciar o modo edição de perfil: python3 bomba-mail.py --pf''')
parser.add_argument('--update', action='store_true', help='Atualiza a ferramenta para a versão mais nova.')
parser.add_argument('--spam', action='store_true', help='Spam em alvos.')
parser.add_argument('--unico', action='store_true', help='Spam UNICO em alvos.')
parser.add_argument('--banco', action='store_true', help='Veja informações sobre seu armazém e perfil.')
parser.add_argument('-t', dest='email', required=False, help='Indica o alvo para spam (OBRIGATÓRIO quando --spam)')
parser.add_argument('-q', dest='quantidade', required=False, type=int, help='Indica a quantidade de spam (OBRIGATÓRIO quando --spam)')
parser.add_argument('--sleep', dest='sleep', type=int, help='Tempo de espera entre os spams em segundos (OPCIONAL)')
parser.add_argument('--pf', action='store_true', required=False, help='Você pode criar um novo perfil de spam')
parser.add_argument('--add', dest='email_alvo', required=False, help='adicione um novo email ao seu armazém')
parser.add_argument('--reset', action='store_true', help='Reseta o armazém')
args = parser.parse_args()


banner = (f'''{texto.negrito}
{texto.cor.vermelho_claro}▗▄▄▖  ▗▄▖ ▗▖  ▗▖▗▄▄▖  ▗▄▖ {texto.cor.verde_claro}▗▖  ▗▖ ▗▄▖ ▗▄▄▄▖▗▖   
{texto.cor.vermelho_claro}▐▌ ▐▌▐▌ ▐▌▐▛▚▞▜▌▐▌ ▐▌▐▌ ▐▌{texto.cor.verde_claro}▐▛▚▞▜▌▐▌ ▐▌  █  ▐▌   
{texto.cor.vermelho_claro}▐▛▀▚▖▐▌ ▐▌▐▌  ▐▌▐▛▀▚▖▐▛▀▜▌{texto.cor.verde_claro}▐▌  ▐▌▐▛▀▜▌  █  ▐▌   
{texto.cor.vermelho_claro}▐▙▄▞▘▝▚▄▞▘▐▌  ▐▌▐▙▄▞▘▐▌ ▐▌{texto.cor.verde_claro}▐▌  ▐▌▐▌ ▐▌▗▄█▄▖▐▙▄▄▖
{texto.cor.branco}   > Desenvolvido por @Fatalsec_archon < {texto.cor.verde} [V {versao}]{texto.reseta}
-https://github.com/FatalS3C
''')

clear()
print (banner)
if len(sys.argv) == 1:
    print(f'Você pode usar {texto.cor.verde}--help{texto.reseta} para te ajudar!')

#--unico
if args.unico:
	perfil = json.loads(open('perfil.json', 'r').read())
	emails = json.loads(open('emails.json', 'r').read())
	print (f'{texto.negrito}{texto.cor.verde_claro}Quantidade de emails: {texto.cor.vermelho_claro}{len(emails["emails"])}{texto.reseta}')
	for i in range(len(emails["emails"])):
		email = (emails['emails'][i])
		print (f'{texto.negrito}{texto.cor.amarelo_claro}[{i+1}] {texto.cor.branco}{list(email.keys())[0]}{texto.reseta}')
	n = int(input('Escolha o email a ser usado: '))
	email_usado = list(emails['emails'][n-1].keys())[0]
	confg = (emails['emails'][n-1])
	print(f'{texto.negrito}{texto.cor.verde_claro}Usando {texto.cor.vermelho_claro}{email_usado} {texto.cor.verde_claro}!{texto.reseta}')
	if (perfil['tipo-texto']) == 'html':
		try:
			email_html(args.email, perfil['mensagem'], confg)
			print(f'{texto.negrito}{texto.cor.vermelho_claro}SPAM! [{list(email.keys())[0]}] {texto.cor.branco}> {texto.negrito}{texto.cor.verde_claro}{args.email} {texto.cor.branco}{i+1}{texto.negrito}{texto.cor.verde_claro}/{texto.cor.branco}{args.quantidade}{texto.reseta}')
		except Exception as e:
			print (e)
			erro(f'SPAM [{i+1}] FALHOU!')

spam_mail = False
#--spam
if args.spam:
	if not args.email or not args.quantidade:
		erro("Erro: Quando --spam é usado, os argumentos -t (email) e -q (quantidade) são obrigatórios.")
	else:
		print (f'{texto.negrito}{texto.cor.verde_claro}ALVO{texto.cor.branco}: {texto.cor.amarelo_claro}{args.email}\n{texto.cor.verde_claro}SPAM{texto.cor.branco}: {texto.cor.amarelo_claro}{args.quantidade}{texto.reseta}')
		if args.sleep:
			print (f'{texto.negrito}{texto.cor.verde_claro}DELAY{texto.cor.branco}: {texto.cor.amarelo_claro}{args.sleep}{texto.reseta}')
			sleeper = True
		else:
			log("Nenhum tempo de espera especificado, enviando sem delay.")
			sleeper = False
		spam_mail = True
	if spam_mail == True:
		perfil = json.loads(open('perfil.json', 'r').read())
		emails = json.loads(open('emails.json', 'r').read())
		print (f'{texto.negrito}{texto.cor.verde_claro}Quantidade de emails: {texto.cor.vermelho_claro}{len(emails["emails"])}{texto.reseta}')
	
		for email in emails['emails']:
			print (f'{texto.negrito}{texto.cor.verde_claro}Usando E-mail{texto.cor.branco}: {texto.cor.amarelo_claro}{list(email.keys())[0]}{texto.reseta}')
			for i in range(args.quantidade):
				if (perfil['tipo-texto']) == 'html':
					try:
						if sleeper == True:
							sleep(args.sleep)
						email_html(args.email, perfil['mensagem'], email)
						print(f'{texto.negrito}{texto.cor.vermelho_claro}SPAM! [{list(email.keys())[0]}] {texto.cor.branco}> {texto.negrito}{texto.cor.verde_claro}{args.email} {texto.cor.branco}{i+1}{texto.negrito}{texto.cor.verde_claro}/{texto.cor.branco}{args.quantidade}{texto.reseta}')
					except:
						erro(f'SPAM [{i+1}] FALHOU!')
				else:
					try:
						if sleeper == True:
							sleep(args.sleep)
						email_txt(args.email, perfil['mensagem'], email)
						print(f'{texto.negrito}{texto.cor.vermelho_claro}SPAM! [{list(email.keys())[0]}] {texto.cor.branco}> {texto.negrito}{texto.cor.verde_claro}{args.email} {texto.cor.branco}{i+1}{texto.negrito}{texto.cor.verde_claro}/{texto.cor.branco}{args.quantidade}{texto.reseta}')
					except:
						erro(f'SPAM [{i+1}] FALHOU!')				

#--unico
if args.unico:
	if not args.email or not args.quantidade:
		erro("Erro: Quando --unico é usado, os argumentos -t (email) e -q (quantidade) são obrigatórios.")
	else:
		print (f'{texto.negrito}{texto.cor.verde_claro}ALVO{texto.cor.branco}: {texto.cor.amarelo_claro}{args.email}\n{texto.cor.verde_claro}SPAM{texto.cor.branco}: {texto.cor.amarelo_claro}{args.quantidade}{texto.reseta}')

#--pf
if args.pf == True:
	w = open('perfil.json', 'w')
	base = '{}'
	x = json.loads(base)
 	
	log('Criando perfil ...')
	w = open('perfil.json', 'w')
	print (f'{texto.cor.vermelho_claro}[{texto.cor.branco}1{texto.cor.vermelho_claro}] {texto.negrito}{texto.cor.branco} HTML\n{texto.cor.vermelho_claro}[{texto.cor.branco}2{texto.cor.vermelho_claro}] {texto.negrito}{texto.cor.branco} TEXTO\n{texto.reseta}')
	n1 = int(input('Escolha o formato: '))
	if n1 == 1:	
		v = {'tipo-texto':'html'}
		x.update(v)
	else:
		v = {'tipo-texto':'texto'}
		x.update(v)

	n2 = input('Assunto (subject): ')		
	v = {'subject':n2}
	x.update(v)
	
	log('\nAconselho usar seu próprio email caso o servidor selecionado não suporte SMTP-RELAY')
	n3 = input('De (from): ')		
	v = {'from':n3}
	x.update(v)
	
	if (x['tipo-texto']) == 'texto':
		print('Deseja digitar a mensagem para enviar agora? (se selecionar "N" você pode escolher um arquivo de texto para o envio.')
		n = input('s/n ')
		if n.lower() == 'n':
			while True:
				ark = input('Arquivo: ')
				try:
					mensagem = open(ark, 'r').read()
				except FileNotFoundError:
					erro(f'O arquivo {ark} Não foi encontrado!')
					continue
				break
		else:
			log('Digite a mensagem')
			mensagem = input(': ')
	else:
		while True:
			ark = input('Arquivo [HTML]: ')
			try:
				mensagem = open(ark, 'r').read()
			except FileNotFoundError:
				erro(f'O arquivo HTML {ark} Não foi encontrado!')
				continue
			break
		
	v = {'mensagem':mensagem}
	x.update(v)
	w.write(json.dumps(x, ensure_ascii=False, indent=2))
	w.close()
	sucesso('Perfil criado!')
	exit()
#--reset
if args.reset == True:
	w = open('emails.json', 'w')
	base = '{}'
	x = json.loads(base)
	v = {'emails':[]}
	x.update(v)
	w.write(json.dumps(x, ensure_ascii=False, indent=2))
	w.close()
	sucesso('O armazém "emails.json" foi reseatado!')
	exit()

#--add
if args.email_alvo:
	while True:
		splitos = (args.email_alvo.split(','))
		email = splitos[0]
		if splitos[1].lower() == 'false':
			senha = False
		else:
			senha = splitos[1]
		porta = int(splitos[2])
		servidor = splitos[3]
		if splitos[4].lower() == 'false':
			ttls = False
		else:
			ttls = True
		if splitos[5].lower() == 'false':
			relay = False
		else:
			relay = True
			
		try:
			z = open('emails.json', 'r').read()
			break
		except FileNotFoundError:
			alerta('Arquivo emails.json inexistente!, criando ...')
			w = open('emails.json', 'w')
			base = '{}'
			x = json.loads(base)
			v = {'emails':[]}
			x.update(v)
			w.write(json.dumps(x, ensure_ascii=False, indent=2))
			w.close()
			continue
	log('Carregando ...')
	r = json.loads(open('emails.json', 'r').read())
	emails = r['emails']
	v = {email:{'server':servidor, 'senha':senha, 'porta':porta, 'ttls':ttls, 'relay':relay}}
	emails.append(v)
	w = open('emails.json', 'w')
	w.write (json.dumps(r, ensure_ascii=False, indent=2))
	w.close()
	sucesso(f'Email {email} adicionado!')
	exit()
	

#--update
if args.update == True:
	log('Comparando ...')
	r = requests.get('https://raw.githubusercontent.com/FatalS3C/bomba-email/refs/heads/main/versao').text.replace('\n', '')
	if r != versao:
		alerta(f'A VERSÃO {r} ESTÁ DISPONÍVEL!')
	if r == versao:
		sucesso('Sua ferramenta está atualizada!')
exit()
