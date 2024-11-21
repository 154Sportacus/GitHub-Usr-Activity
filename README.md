# GitHub USER Activity CLI

Este projeto é um CLI em Python que permite exibir atividades de um utilizador no GitHub. Utiliza a API do GitHub para procurar eventos de um utilizador exibindo informações sobre os mesmos, tais como: commits, forks, stars, issues, ...

## Funcionalidade

O script realiza as seguintes funções:

- Procura eventos de um utilizador no GitHub.
- Exibe a quantidade total de commits feitos pelo utilizador por repositório.
- Exibe eventos como forks, stars, interações com issues, pull requests e outros.

### Tipos de eventos:
- **PushEvent**: Mostra o número de commits feitos num repositório.
- **ForkEvent**: O utilizador fez um fork dum repositório.
- **WatchEvent**: O utilizador deu star num repositório.
- **IssuesEvent**: Exibe interações com issues de repositórios.
- **PullRequestEvent**: Informa sobre pull requests feitos pelo utilizador.
- **CreateEvent**: Informa sobre a criação de branches ou tags no repositório.

## Como Usar

1. **Clone do repositório**:

   ```bash
   git clone https://github.com/154Sportacus/GitHub-User-Activity.git

2. **Instalar dependências**:

   ```bash
   pip install requests

3. **Executar a Script**:

   ```bash
   python github-activity.py <username>



