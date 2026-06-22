# Python Security Tools

Coleção de ferramentas simples em Python voltadas para segurança da informação, análise defensiva, triagem de logs e apoio a atividades de Blue Team/SOC.

## Objetivo

Este repositório reúne scripts práticos para auxiliar em tarefas comuns de segurança, como verificação de senhas, varredura de portas, análise de logs, checagem de indicadores de comprometimento, geração de hashes e análise básica de reputação de URLs.

## Ferramentas

### Password Checker
Verifica a força de uma senha com base em tamanho, caracteres especiais, números, letras maiúsculas e minúsculas.

### Port Scanner
Realiza varredura simples de portas TCP em um host informado.

### Log Analyzer
Analisa arquivos de log em busca de eventos suspeitos, erros, falhas de login e padrões anormais.

### IOC Checker
Verifica indicadores de comprometimento como IPs, domínios, URLs e hashes.

### Hash Generator
Gera hashes MD5, SHA1 e SHA256 para arquivos ou textos.

### URL Reputation Checker
Realiza análise básica de URLs suspeitas, verificando padrões comuns de phishing e domínios suspeitos.

## Estrutura

```text
Python-Security-Tools/
├─ tools/
├─ examples/
└─ docs/
