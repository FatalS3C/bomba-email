![No](https://github.com/FatalS3C/bomba-email/blob/main/BOMBAMAIL.png?raw=true)

# **BOMBA-MAIL**
### Português 🇧🇷

Esta é uma ferramenta poderosa de **SPAM** e até **EMAIL-SPOOFING**, mas lembre-se: a chave está no **uso responsável**! Apenas use com consciência e dentro dos limites da ética.

Como executar? Antes de fazer tal ato, não deixe de obter os requisitos! Que seria:

![Python](https://img.shields.io/badge/python_3-000000?style=for-the-badge&logo=python&logoColor=FFFFFF)

![REQ](https://img.shields.io/badge/Requests-2.32.3-FF0000?labelColor=1a1a1a&style=for-the-badge&logo=pypy&logoColor=FF0000) ![REQ](https://img.shields.io/badge/urllib3-2.3.0-FF0000?labelColor=1a1a1a&style=for-the-badge&logo=pypy&logoColor=FF0000) ![REQ](https://img.shields.io/badge/certifi-2025.1.31-FF0000?labelColor=1a1a1a&style=for-the-badge&logo=pypy&logoColor=FF0000)![REQ](https://img.shields.io/badge/idna-3.10-FF0000?labelColor=1a1a1a&style=for-the-badge&logo=pypy&logoColor=FF0000) ![REQ](https://img.shields.io/badge/charset_normalizer-3.4.1-FF0000?labelColor=1a1a1a&style=for-the-badge&logo=pypy&logoColor=FF0000) 

# Instalação dos requisitos

```sh
pip3 install -r requiriments.txt
```

**Tudo pronto! Vamos para o uso!**
#
**Iniciando a BOMBA-MAIL**

```sh
python3 bomba-mail.py
```
> Já de começo é possível ver a ferramenta rodando! com ajuda, inclusive.

**Atualizando a BOMBA-MAIL**

```sh
python3 bomba-mail.py --update
```
> Infelizmente apenas é possível pegar a versão da GitHub e comparar, a ferramenta em sua fase beta é incapaz de se atualizar sozinha.

**Ajuda na BOMBA-MAIL**

```sh
python3 bomba-mail.py --help
```
> É possível saber seus comandos com o HELP, tentarei atualizar cada vez mais dando mais e mais ajuda!

**Criando seu PERFIL**

```sh
python3 bomba-mail.py --pf
```
> Você poderá criar seu perfil, assim facilitando o SPAM e até SPOOFING!

![Exemplo do --pf](https://github.com/FatalS3C/bomba-email/blob/main/videos/perfil.gif?raw=true)
###### ARGUMENTOS PARA ADICIONAR
| ARGUMENTO | FUNÇÃO |  EXEMPLO |
| ------------- |:-------------:|:-------------:|
| EMAIL      | QUE SERÁ USADO     | blabla@blabla.coom
| SENHA      | A SENHA DE AUTENTICAÇÃO, CASO NÃO PRECISE USE **FALSE**    | senhaforte123
| PORTA      | PORTA DO SERVIDOR     | 2525
| SERVIDOR      | SERVIDOR SMTP     | smtp.google.coom
| TTLS      | DIGA SE É PRECISO TTLS, SE NÃO FOR NECESSÁRIO USE **FALSE**      | true
| RELAY      | DIGA SE É PERMITIDO ENCAMINHAR MENSAGENS PARA DESTINATÁRIOS EXTERNOS SEM EXIGIR AUTENTICAÇÃO. CASO NÃO SEJA USE  **FALSE**     | false

**Um pequeno exemplo de como usar:**
```sh
python3 bomba-mail.py --add email@email.com,false,2525,mail.mail.smtp,false,false
```

**COMO FAZER UM BELO SPAM? 💣💥**
>USE COM CUIDADO!

```sh
python3 bomba-mail.py --spam -t guuuuu@gufum.com -q 5 --sleep 2
```
> Você pode escolher o alvo, e a quantia e SPAM, incluindo com DELAY para não esquentar as requisições!

![BOOOMBA](https://github.com/FatalS3C/bomba-email/blob/main/videos/bomba.gif?raw=true)
| ARGUMENTO | FUNÇÃO |  EXEMPLO |
| ------------- |:-------------:|:-------------:|
| ---spam      | OBRIGATÓRIO    | --spam|
| -t     | INSERE O E-MAIL ALVO    | guuuuu@gufum.coom|
| -q    | A QUANTIA DE SPAM    | 25|
| ---sleep    | O TEMPO DE DELAY, **É OPCIONAL**    | 15|


**FAZENDO SPAM DE UM EMAIL SÓ 💣💥**
>USE COM CUIDADO!

```sh
python3 bomba-mail.py --unico -t guuuuu@gufum.com -q 5 --sleep 2
```

![UMA BOMBA](https://github.com/FatalS3C/bomba-email/blob/main/videos/bomba2.gif?raw=true)

| ARGUMENTO | FUNÇÃO |  EXEMPLO |
| ------------- |:-------------:|:-------------:|
| ---unico      | OBRIGATÓRIO    | ---unico|
| -t     | INSERE O E-MAIL ALVO    | guuuuu@gufum.coom|
| -q    | A QUANTIA DE SPAM    | 25|
| ---sleep    | O TEMPO DE DELAY, **É OPCIONAL**    | 15|


*Muito obrigado!*


# **BOMBA-MAIL**
### English 🇺🇸

This is a powerful **SPAM** and even **EMAIL SPOOFING** tool, but remember: the key is **responsible use**! Use it wisely and within ethical boundaries.

## How to run?

Before proceeding, make sure to install the required dependencies:

![Python](https://img.shields.io/badge/python_3-000000?style=for-the-badge&logo=python&logoColor=FFFFFF)

![REQ](https://img.shields.io/badge/Requests-2.32.3-FF0000?labelColor=1a1a1a&style=for-the-badge&logo=pypy&logoColor=FF0000) ![REQ](https://img.shields.io/badge/urllib3-2.3.0-FF0000?labelColor=1a1a1a&style=for-the-badge&logo=pypy&logoColor=FF0000) ![REQ](https://img.shields.io/badge/certifi-2025.1.31-FF0000?labelColor=1a1a1a&style=for-the-badge&logo=pypy&logoColor=FF0000)![REQ](https://img.shields.io/badge/idna-3.10-FF0000?labelColor=1a1a1a&style=for-the-badge&logo=pypy&logoColor=FF0000) ![REQ](https://img.shields.io/badge/charset_normalizer-3.4.1-FF0000?labelColor=1a1a1a&style=for-the-badge&logo=pypy&logoColor=FF0000) 

# Installing requirements

```sh
pip3 install -r requiriments.txt
```


**All set! Let’s start using it!**
#
**Starting BOMBA-MAIL**

```sh
python3 bomba-mail.py
```
> The tool will start running immediately, including help options.

**Updating BOMBA-MAIL**

```sh
python3 bomba-mail.py --update
```
> The update feature is limited to checking the GitHub version. Since the tool is still in beta, it cannot update itself automatically.

**BOMBA-MAIL Help**

```sh
python3 bomba-mail.py --help
```
> Use the HELP command to check available commands. I will keep updating it to provide better assistance!

**Creating Your PROFILE**

```sh
python3 bomba-mail.py --pf
```
> You can create a profile to facilitate SPAM and even SPOOFING!

![Exemplo do --pf](https://github.com/FatalS3C/bomba-email/blob/main/videos/perfil.gif?raw=true)

### ARGUMENTS TO ADD

| ARGUMENT  | FUNCTION | EXAMPLE |
|-----------|----------|---------|
| EMAIL     | TO BE USED | blabla@blabla.com |
| PASSWORD  | AUTHENTICATION PASSWORD, IF NOT REQUIRED USE **FALSE** | strongpassword123 |
| PORT      | SERVER PORT | 2525 |
| SERVER    | SMTP SERVER | smtp.google.com |
| TTLS      | SPECIFY IF TTLS IS REQUIRED, IF NOT USE **FALSE** | true |
| RELAY     | SPECIFY IF MESSAGE FORWARDING TO EXTERNAL RECIPIENTS WITHOUT AUTHENTICATION IS ALLOWED. IF NOT, USE **FALSE** | false |


**Example Usage:**
```sh
python3 bomba-mail.py --add email@email.com,false,2525,mail.mail.smtp,false,false
```

**HOW TO SPAM LIKE A PRO? 💣💥 💣💥**
>USE WITH CAUTION!

```sh
python3 bomba-mail.py --spam -t guuuuu@gufum.com -q 5 --sleep 2
```
> Choose the target email, the number of messages, and even set a delay to avoid overheating requests!

![BOOOMBA](https://github.com/FatalS3C/bomba-email/blob/main/videos/bomba.gif?raw=true)
| ARGUMENT   | FUNCTION | EXAMPLE |
|------------|----------|---------|
| ---spam    | MANDATORY | ---spam |
| -t         | INSERT TARGET EMAIL | guuuuu@gufum.com |
| -q         | AMOUNT OF SPAM | 25 |
| ---sleep   | DELAY TIME, **OPTIONAL** | 15 |



**SENDING A SINGLE SPAM EMAIL 💣💥**
>USE COM CUIDADO!

```sh
python3 bomba-mail.py --unico -t guuuuu@gufum.com -q 5 --sleep 2
```

![UMA BOMBA](https://github.com/FatalS3C/bomba-email/blob/main/videos/bomba2.gif?raw=true)

| ARGUMENT   | FUNCTION | EXAMPLE |
|------------|----------|---------|
| ---unico    | MANDATORY | ---unico |
| -t         | INSERT TARGET EMAIL | guuuuu@gufum.com |
| -q         | AMOUNT OF SPAM | 25 |
| ---sleep   | DELAY TIME, **OPTIONAL** | 15 |


**Thank you!** 🚀

