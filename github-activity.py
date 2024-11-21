import argparse
import requests

# Dicionário para armazenar o número total de commits por repositório
commit_count_by_repository = {}

def fetch_repository_name(repository_id):

    url = f"https://api.github.com/repositories/{repository_id}"
    response = requests.get(url)

    if response.status_code == 200:
        return response.json().get('name')
    else:
        return None

def accumulate_commits(payload):

    repository_id = payload.get('repository_id')
    if repository_id:
        repository_name = fetch_repository_name(repository_id)

        if repository_name:
            
            commit_count_by_repository.setdefault(repository_name, 0)

            commit_count_by_repository[repository_name] += payload.get('size', 0)  # 'size' é o número de commits

def print_commits_summary(username):

    if commit_count_by_repository:
        for repository, commits in commit_count_by_repository.items():
            print(f"{username} fez {commits} commits no repositório {repository}")
    else:
        print(f"{username} não fez nenhum commit registrado.")

def print_events(username):
   
    endpoint = f'https://api.github.com/users/{username}/events'
    
    # Faz a requisição à API
    response = requests.get(endpoint)
    
    if response.status_code == 200:
        events = response.json()
        if events:
            # Processa todos os eventos
            for event in events:
                event_type = event.get('type', '')
                repo_name = event['repo']['name']
                if event_type == 'PushEvent':
                    accumulate_commits(event['payload'])
                elif event_type == 'ForkEvent':
                    print(f"{username} fez um *fork* do repositório {repo_name}")
                elif event_type == 'WatchEvent':
                    print(f"{username} deu um *star* no repositório {repo_name}")
                elif event_type == 'IssuesEvent':
                    issue_title = event['payload']['issue']['title']
                    print(f"{username} interagiu com a issue: {issue_title}")
                elif event_type == 'PullRequestEvent':
                    print(f"{username} fez um *pull request* no repositório {repo_name}")
                elif event_type == 'CreateEvent':
                    ref_type = event['payload']['ref_type']
                    print(f"{username} criou um(a) {ref_type} no repositório {repo_name}")
                
            # Imprime o total de commits por repositório
            print_commits_summary(username)
        else:
            print(f"{username} não possui eventos registrados.")
    else:
        print(f"ERRO: retrieve de eventos para o utilizador {username}: Status Code {response.status_code}")

def main():
    parser = argparse.ArgumentParser(description="Fetch GitHub events for a user")
    parser.add_argument("username", help="GitHub username to fetch events for")

    # Processa os argumentos passados na linha de comandos
    args = parser.parse_args()
    username = args.username

    print("GitHub Activity CLI")
    print("Output:")

    # Função para imprimir os eventos
    print_events(username)

if __name__ == '__main__':
    main()
