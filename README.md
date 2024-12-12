# 🛠️ NetSpectre

![NetSpectre](assets/imagem/)

NetSpectre é uma ferramenta de análise de rede poderosa, desenvolvida por DEDSEC. Ela permite varrer redes locais, identificar dispositivos conectados, descobrir portas abertas e verificar vulnerabilidades comuns em serviços. Ideal para **pentesters** e **hackers éticos** que desejam explorar e proteger suas redes.

---

## ✨ **Funcionalidades**

- **Varredura de dispositivos**:
  - Identifica todos os dispositivos conectados à rede usando requisições ARP.

- **Scan de portas abertas**:
  - Realiza varredura de portas TCP/UDP abertas.

- **Verificação de vulnerabilidades comuns**:
  - Detecta serviços conhecidos por apresentarem falhas de segurança, como FTP anônimo ou SMB vulnerável.

- **Relatório completo**:
  - Gera relatórios detalhados em formato JSON ou PDF.

---

## 📋 **Pré-requisitos**

Certifique-se de que você tenha os seguintes itens instalados:

- **Python 3.6+**
- Bibliotecas necessárias (instaladas via `pip`):
  ```bash
  pip install scapy argparse json
  ```

---

## 🖥️ **Como usar**

1. Clone o repositório:
   ```bash
   git clone https://github.com/suaconta/NetSpectre.git
   cd NetSpectre
   ```

2. Execute o script:
   ```bash
   python netspectre.py --target <REDE/ALVO> --output <ARQUIVO_DE_SAÍDA>
   ```

3. Exemplos:
   - Varredura de uma rede inteira (sub-rede 192.168.0.0/24):
     ```bash
     python netspectre.py --target 192.168.0.0/24 --output scan.json
     ```
   - Varredura de um único dispositivo:
     ```bash
     python netspectre.py --target 192.168.0.10 --output device_report.json
     ```

---

## 📊 **Relatório gerado**

O relatório inclui informações como:

- Endereço IP e MAC dos dispositivos conectados.
- Portas abertas e serviços associados.
- Possíveis vulnerabilidades.

Exemplo de saída JSON:
```json
[
  {
    "ip": "192.168.0.1",
    "mac": "AA:BB:CC:DD:EE:FF",
    "open_ports": [22, 80, 443]
  },
  {
    "ip": "192.168.0.105",
    "mac": "FF:EE:DD:CC:BB:AA",
    "open_ports": [21, 23]
  }
]
```

---

## 🤝 **Contribuição**

Quer melhorar o NetSpectre? Contribuições são bem-vindas! Siga os passos abaixo:

1. Faça um fork do repositório.
2. Crie um branch para suas alterações:
   ```bash
   git checkout -b feature/melhorias
   ```
3. Faça commit das alterações:
   ```bash
   git commit -m "Adiciona nova funcionalidade X"
   ```
4. Envie o branch:
   ```bash
   git push origin feature/melhorias
   ```
5. Abra um **Pull Request** no GitHub.

---

## 📜 **Licença**

Este projeto está licenciado sob a Licença MIT. Consulte o arquivo LICENSE para mais detalhes.

---

## ⚠️ **Aviso Legal**

A DEDESC está revelando a verdade, porém, nos não somos responsaveis pelas suas ações com nosso software, criamos com o objetivo de ajudar pessoas que trabalham ou estudam Cybersegurança. Bom uso.
