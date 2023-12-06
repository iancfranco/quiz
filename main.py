import random
import time
import os


class SistemaEstudo:

  def __init__(self, banco_de_questoes):
    self.banco_de_questoes = banco_de_questoes
    self.questoes_selecionadas = []

  def selecionar_questoes(self, quantidade):
    if quantidade <= len(self.banco_de_questoes):
      self.questoes_selecionadas = random.sample(self.banco_de_questoes,
                                                 quantidade)
    else:
      print("Quantidade solicitada maior que o banco de questões.")

  def estudar(self):
    corretas = 0
    incorretas = 0
    for questao in self.questoes_selecionadas:
      print(f"Pergunta: {questao['pergunta']}")
      for i, alternativa in enumerate(questao['alternativas'], 1):
        print(f"{i}. {alternativa}")
      print("-" * 30)
      resposta = input("Escolha a alternativa correta (1 a 5): ")
      if resposta.isdigit() and 1 <= int(resposta) <= 5:
        if questao['alternativas'][int(resposta) - 1] == questao['resposta']:
          print("Correto!")
          corretas += 1
          print("-" * 30)
          time.sleep(1)
          input("Pressione enter para continuar.")
          os.system('clear')
        else:
          print("Incorreto.")
          print(f"A resposta correta é: {questao['resposta']}.")
          incorretas += 1
          print("-" * 30)
          time.sleep(1)
          input("Pressione enter para continuar.")
          os.system('clear')
      else:
        print("Escolha inválida. Por favor, insira um número de 1 a 5.")
    time.sleep(1)
    os.system('clear')
    print("Quiz finalizado.")
    print("Corretas:", corretas)
    print("Incorretas:", incorretas)
    print(f"Final: {corretas}/{quantidade_desejada}")


# Exemplo de uso
banco_de_questoes = [{
    "pergunta":
    "O que o comando 'ver' faz no prompt de comando?",
    "alternativas": [
        "A) Mostra a versão do Windows", "B) Limpa a tela",
        "C) Lista os diretórios", "D) Move um arquivo para outro diretório",
        "E) Cria uma nova pasta"
    ],
    "resposta":
    "A) Mostra a versão do Windows"
}, {
    "pergunta":
    "Como você limparia a tela no prompt de comando?",
    "alternativas": ["A) ver", "B) cls", "C) dir", "D) cd", "E) mkdir"],
    "resposta":
    "B) cls"
}, {
    "pergunta":
    "Explique como o comando 'dir' é utilizado e o que ele faz.",
    "alternativas": [
        "A) Move um arquivo para outro diretório", "B) Lista os diretórios",
        "C) Renomeia uma pasta", "D) Remove uma pasta",
        "E) Copia um arquivo para uma pasta"
    ],
    "resposta":
    "B) Lista os diretórios"
}, {
    "pergunta":
    "Qual comando você usaria para entrar em um diretório?",
    "alternativas": ["A) cd ..", "B) dir", "C) cls", "D) mkdir", "E) move"],
    "resposta":
    "A) cd .."
}, {
    "pergunta":
    "Como voltar para o diretório anterior usando o prompt de comando?",
    "alternativas": ["A) cd ..", "B) dir", "C) cls", "D) mkdir", "E) move"],
    "resposta":
    "A) cd .."
}, {
    "pergunta":
    "Como a tecla TAB pode ser útil ao trabalhar com o prompt de comando?",
    "alternativas": [
        "A) Completa automaticamente nomes de arquivos e pastas",
        "B) Move para o diretório anterior", "C) Lista todos os arquivos",
        "D) Remove uma pasta", "E) Copia um arquivo"
    ],
    "resposta":
    "A) Completa automaticamente nomes de arquivos e pastas"
}, {
    "pergunta":
    "Como criar uma nova pasta no diretório atual usando o comando 'mkdir'?",
    "alternativas":
    ["A) move", "B) ipconfig", "C) mkdir", "D) xcopy", "E) rd"],
    "resposta":
    "C) mkdir"
}, {
    "pergunta":
    "Descreva o comando 'move' e como você o usaria para mover um arquivo para outro diretório.",
    "alternativas": [
        "A) Renomeia uma pasta", "B) Lista os diretórios",
        "C) Move um arquivo para outro diretório", "D) Remove uma pasta",
        "E) Copia um arquivo para uma pasta"
    ],
    "resposta":
    "C) Move um arquivo para outro diretório"
}, {
    "pergunta":
    "Como renomear uma pasta usando o comando 'move'?",
    "alternativas": [
        "A) move arquivoTeste novaPasta", "B) move novaPasta arquivoTeste",
        "C) move arquivoTeste", "D) rd arquivoTeste", "E) cls"
    ],
    "resposta":
    "A) move arquivoTeste novaPasta"
}, {
    "pergunta":
    "Qual comando é usado para remover/deletar uma pasta no diretório atual?",
    "alternativas": ["A) rd", "B) cls", "C) cd", "D) mkdir", "E) move"],
    "resposta":
    "A) rd"
}, {
    "pergunta":
    "Descreva a diferença entre os comandos 'copy' e 'xcopy'.",
    "alternativas": [
        "A) Renomeia uma pasta", "B) Lista os diretórios",
        "C) Copia um arquivo específico dentro de uma pasta",
        "D) Move todos os arquivos dentro de uma pasta", "E) Remove uma pasta"
    ],
    "resposta":
    "C) Copia um arquivo específico dentro de uma pasta"
}, {
    "pergunta":
    "Como o comando 'time' pode ser usado para modificar o horário da máquina?",
    "alternativas": [
        "A) Execute o comando e digite o novo horário",
        "B) Move um arquivo para outro diretório", "C) Lista os diretórios",
        "D) Remove uma pasta", "E) Copia um arquivo para uma pasta"
    ],
    "resposta":
    "A) Execute o comando e digite o novo horário"
}, {
    "pergunta":
    "O que o comando 'arp -a' mostra?",
    "alternativas": [
        "A) Move um arquivo para outro diretório", "B) Lista os diretórios",
        "C) Mostra a interface de rede com nossos IPs", "D) Remove uma pasta",
        "E) Copia um arquivo para uma pasta"
    ],
    "resposta":
    "C) Mostra a interface de rede com nossos IPs"
}, {
    "pergunta":
    "Explique o propósito do comando 'ipconfig' e o que ele exibe.",
    "alternativas": [
        "A) Renomeia uma pasta", "B) Lista os diretórios",
        "C) Move um arquivo para outro diretório",
        "D) Mostra as configurações de rede da máquina atual",
        "E) Remove uma pasta"
    ],
    "resposta":
    "D) Mostra as configurações de rede da máquina atual"
}, {
    "pergunta":
    "Como o PowerShell é comparado ao CMD em termos de semelhança com o terminal do Linux?",
    "alternativas": [
        "A) Menos semelhante", "B) Mais semelhante",
        "C) Igualmente semelhante", "D) Não tem semelhança",
        "E) Inversamente semelhante"
    ],
    "resposta":
    "B) Mais semelhante"
}, {
    "pergunta":
    "Qual comando é utilizado para limpar a tela no PowerShell?",
    "alternativas": ["A) clear", "B) cls", "C) ls", "D) dir", "E) mv"],
    "resposta":
    "A) clear"
}, {
    "pergunta":
    "Qual comando é equivalente ao 'dir' do CMD no PowerShell?",
    "alternativas": ["A) clear", "B) cls", "C) ls", "D) dir", "E) mv"],
    "resposta":
    "C) ls"
}, {
    "pergunta":
    "O que o comando 'mkdir' faz no PowerShell?",
    "alternativas": [
        "A) Limpa a tela", "B) Lista diretórios", "C) Cria pastas",
        "D) Navega entre pastas", "E) Move uma pasta"
    ],
    "resposta":
    "C) Cria pastas"
}, {
    "pergunta":
    "Qual comando é utilizado para navegar entre pastas no PowerShell?",
    "alternativas": ["A) clear", "B) cls", "C) ls", "D) dir", "E) cd"],
    "resposta":
    "E) cd"
}, {
    "pergunta":
    "O que o TAB faz no PowerShell?",
    "alternativas": [
        "A) Completa automaticamente nomes de arquivos e pastas",
        "B) Limpa a tela", "C) Lista todos os arquivos", "D) Remove uma pasta",
        "E) Copia um arquivo"
    ],
    "resposta":
    "A) Completa automaticamente nomes de arquivos e pastas"
}, {
    "pergunta":
    "Qual comando é equivalente ao 'xcopy' do CMD no PowerShell?",
    "alternativas": ["A) cp", "B) mv", "C) rn", "D) rd", "E) xcopy"],
    "resposta":
    "A) cp"
}, {
    "pergunta":
    "O que o comando 'rn' faz no PowerShell?",
    "alternativas": [
        "A) Renomeia uma pasta", "B) Lista os diretórios",
        "C) Move um arquivo para outro diretório", "D) Remove uma pasta",
        "E) Copia um arquivo para uma pasta"
    ],
    "resposta":
    "A) Renomeia uma pasta"
}, {
    "pergunta":
    "Qual comando é equivalente ao 'move' do CMD no PowerShell?",
    "alternativas": ["A) rn", "B) mv", "C) cp", "D) rd", "E) move"],
    "resposta":
    "B) mv"
}, {
    "pergunta":
    "Segundo a observação fornecida, por que é recomendável utilizar os comandos nativos do PowerShell em vez dos do CMD?",
    "alternativas": [
        "A) Não há diferença", "B) São mais rápidos",
        "C) São exclusivos do PowerShell", "D) Se assemelham aos do Linux",
        "E) Têm menos funcionalidades"
    ],
    "resposta":
    "D) Se assemelham aos do Linux"
}, {
    "pergunta":
    "Quais comandos do CMD também são utilizados no PowerShell, conforme a observação?",
    "alternativas": [
        "A) cls", "B) ipconfig e arp -a", "C) dir e clear", "D) xcopy e mv",
        "E) rd e ls"
    ],
    "resposta":
    "B) ipconfig e arp -a"
}, {
    "pergunta":
    "O que é empacotar arquivos no contexto mencionado?",
    "alternativas": [
        "A) Aumentar o tamanho dos arquivos",
        "B) Juntar arquivos sem alterar o tamanho", "C) Comprimir arquivos",
        "D) Renomear arquivos", "E) Excluir arquivos"
    ],
    "resposta":
    "B) Juntar arquivos sem alterar o tamanho"
}, {
    "pergunta":
    "Qual comando é utilizado para verificar o tamanho (espaço ocupado) de uma pasta ou diretório?",
    "alternativas":
    ["A) du -f", "B) ls -h", "C) du -h", "D) size -r", "E) df -s"],
    "resposta":
    "C) du -h"
}, {
    "pergunta":
    "Como o comando 'tar' é usado para empacotar arquivos?",
    "alternativas": [
        "A) tar -cf [arquivo].tar [arquivo1] [arquivo2]",
        "B) tar -xf [arquivo] [arquivo1] [arquivo2]", "C) tar -tf [arquivo]",
        "D) tar -czf [arquivo].tar.gz [arquivo1] [arquivo2]",
        "E) tar -sjf [arquivo].tar.bz2 [arquivo1] [arquivo2]"
    ],
    "resposta":
    "A) tar -cf [arquivo].tar [arquivo1] [arquivo2]"
}, {
    "pergunta":
    "Como listar os nomes dos arquivos contidos em um arquivo empacotado usando o comando 'tar'?",
    "alternativas": [
        "A) tar -xf [arquivo]",
        "B) tar -czf [arquivo].tar.gz [arquivo1] [arquivo2]",
        "C) tar -cf [arquivo].tar [arquivo1] [arquivo2]",
        "D) tar -tf [arquivo]",
        "E) tar -sjf [arquivo].tar.bz2 [arquivo1] [arquivo2]"
    ],
    "resposta":
    "D) tar -tf [arquivo]"
}, {
    "pergunta":
    "Como descompactar arquivos usando o comando 'tar'?",
    "alternativas": [
        "A) tar -tf [arquivo]", "B) tar -xf [arquivo]",
        "C) tar -czf [arquivo].tar.gz [arquivo1] [arquivo2]",
        "D) tar -cf [arquivo].tar [arquivo1] [arquivo2]",
        "E) tar -sjf [arquivo].tar.bz2 [arquivo1] [arquivo2]"
    ],
    "resposta":
    "B) tar -xf [arquivo]"
}, {
    "pergunta":
    "Qual método de compressão é identificado pelo parâmetro '-j' ao usar o comando 'tar'?",
    "alternativas": ["A) gzip", "B) bzip", "C) zip", "D) tar", "E) 7z"],
    "resposta":
    "A) gzip"
}, {
    "pergunta":
    "Qual método de compressão é identificado pelo parâmetro '-z' ao usar o comando 'tar'?",
    "alternativas": ["A) gzip", "B) bzip", "C) zip", "D) tar", "E) 7z"],
    "resposta":
    "B) bzip"
}, {
    "pergunta":
    "Como localizar arquivos ou diretórios na máquina usando o comando 'find'?",
    "alternativas": [
        "A) find -type d", "B) find -size -10mb", "C) find / -iname (nome)*",
        "D) find -tf (diretório)", "E) find -z (diretório)"
    ],
    "resposta":
    "C) find / -iname (nome)*"
}, {
    "pergunta":
    "Qual opção é usada com o comando 'find' para localizar apenas diretórios?",
    "alternativas":
    ["A) -size", "B) -type f", "C) -iname", "D) -type d", "E) -tf"],
    "resposta":
    "D) -type d"
}, {
    "pergunta":
    "Como o parâmetro '-size' é usado com o comando 'find' para localizar arquivos menores que 10mb?",
    "alternativas": [
        "A) -size 10mb", "B) -size +10mb", "C) -size -10mb", "D) -size 10",
        "E) -size +10"
    ],
    "resposta":
    "C) -size -10mb"
}, {
    "pergunta":
    "Qual comando é utilizado para ativar o root no terminal do Ubuntu?",
    "alternativas":
    ["A) sudo", "B) root", "C) su", "D) enable-root", "E) activate-root"],
    "resposta":
    "C) su"
}, {
    "pergunta":
    "O que o comando 'history' faz no terminal?",
    "alternativas": [
        "A) Lista os comandos de um diretório",
        "B) Exibe o histórico de comandos executados na sessão do terminal",
        "C) Cria um histórico de navegação",
        "D) Atualiza o histórico do sistema",
        "E) Remove o histórico do terminal"
    ],
    "resposta":
    "B) Exibe o histórico de comandos executados na sessão do terminal"
}, {
    "pergunta":
    "Como reiniciar a máquina usando o terminal do Ubuntu?",
    "alternativas": [
        "A) shutdown", "B) restart", "C) reboot", "D) power-off",
        "E) restart-machine"
    ],
    "resposta":
    "C) reboot"
}, {
    "pergunta":
    "Qual comando é utilizado para fazer uma atualização das partes essenciais do Linux, como segurança, traduções, etc.?",
    "alternativas": [
        "A) apt-get update", "B) apt-get upgrade", "C) apt-get autoremove",
        "D) apt-get install", "E) apt-get remove"
    ],
    "resposta":
    "A) apt-get update"
}, {
    "pergunta":
    "O que o comando 'apt-get upgrade' faz?",
    "alternativas": [
        "A) Atualiza completamente o sistema",
        "B) Atualiza apenas as partes essenciais do Linux",
        "C) Remove pacotes desnecessários",
        "D) Atualiza o histórico do terminal",
        "E) Limpa os pacotes substituídos por uma versão mais recente"
    ],
    "resposta":
    "A) Atualiza completamente o sistema"
}, {
    "pergunta":
    "O que o comando 'apt-get autoremove' faz?",
    "alternativas": [
        "A) Remove arquivos e pacotes de um serviço",
        "B) Remove todos os arquivos e pacotes de um serviço",
        "C) Atualiza completamente o sistema",
        "D) Limpa pacotes substituídos por uma versão mais recente",
        "E) Limpa os pacotes desnecessários após update ou upgrade"
    ],
    "resposta":
    "E) Limpa os pacotes desnecessários após update ou upgrade"
}, {
    "pergunta":
    "Como o comando 'dpkg -i [nome_arquivo]' é utilizado para instalar arquivos e programas .deb?",
    "alternativas": [
        "A) dpkg -i install [nome_arquivo]",
        "B) dpkg -i upgrade [nome_arquivo]",
        "C) dpkg -i update [nome_arquivo]", "D) dpkg -i [nome_arquivo].deb",
        "E) dpkg -install [nome_arquivo]"
    ],
    "resposta":
    "D) dpkg -i [nome_arquivo]"
}, {
    "pergunta":
    "Como o comando 'rm' é utilizado no terminal do Ubuntu para remover uma pasta e seu conteúdo?",
    "alternativas": [
        "A) rm -r pasta", "B) rm -d pasta", "C) rm -rf pasta",
        "D) rm -delete pasta", "E) rm -remove pasta"
    ],
    "resposta":
    "C) rm -rf pasta"
}, {
    "pergunta":
    "Qual comando é utilizado para listar os arquivos dentro de um pacote empacotado usando o 'tar'?",
    "alternativas": [
        "A) tar -xf [arquivo]",
        "B) tar -czf [arquivo].tar.gz [arquivo1] [arquivo2]",
        "C) tar -cf [arquivo].tar [arquivo1] [arquivo2]",
        "D) tar -tf [arquivo]",
        "E) tar -sjf [arquivo].tar.bz2 [arquivo1] [arquivo2]"
    ],
    "resposta":
    "D) tar -tf [arquivo]"
}, {
    "pergunta":
    "O que significa o parâmetro '-rf' no comando 'rm -rf'?",
    "alternativas": [
        "A) Remove rapidamente", "B) Remove para a lixeira",
        "C) Remove forever", "D) Remove de forma recursiva",
        "E) Remove da raiz"
    ],
    "resposta":
    "C) Remove forever"
}, {
    "pergunta":
    "Como o comando 'su' é utilizado no terminal do Ubuntu?",
    "alternativas": [
        "A) su -activate", "B) su -root", "C) su -admin", "D) su",
        "E) su -enable"
    ],
    "resposta":
    "D) su"
}, {
    "pergunta":
    "O que acontece quando você pressiona 'i' após iniciar o comando 'vim'?",
    "alternativas": [
        "A) O terminal é reiniciado", "B) Inicia a inserção de texto",
        "C) Lista os arquivos no diretório", "D) Ativa o modo de busca",
        "E) Remove um arquivo"
    ],
    "resposta":
    "B) Inicia a inserção de texto"
}, {
    "pergunta":
    "Qual comando é utilizado para forçar o salvamento e sair do editor de texto 'vim'?",
    "alternativas": [
        "A) vim -force", "B) vim -save-exit", "C) vim -wq", "D) vim -quit",
        "E) vim -exit-save"
    ],
    "resposta":
    "C) vim -wq"
}, {
    "pergunta":
    "Como o comando 'find' pode ser utilizado para localizar apenas diretórios?",
    "alternativas": [
        "A) find -type f", "B) find -size -10mb", "C) find / -type d",
        "D) find -z (diretório)", "E) find -type dir"
    ],
    "resposta":
    "C) find / -type d"
}, {
    "pergunta":
    "O que o comando 'ls' faz no terminal do Ubuntu?",
    "alternativas": [
        "A) Limpa a tela", "B) Lista diretórios",
        "C) Lista arquivos no diretório atual", "D) Remove um arquivo",
        "E) Renomeia um arquivo"
    ],
    "resposta":
    "C) Lista arquivos no diretório atual"
}, {
    "pergunta":
    "Qual é a principal função da VPN em relação à segurança dos dados na rede?",
    "alternativas": [
        "A) Filtrar conteúdo",
        "B) Criar um túnel seguro entre cliente e servidor",
        "C) Ativar root no terminal", "D) Reiniciar a máquina remotamente",
        "E) Instalar programas .deb"
    ],
    "resposta":
    "B) Criar um túnel seguro entre cliente e servidor"
}, {
    "pergunta":
    "Como a VPN difere do proxy em relação ao tráfego do sistema operacional?",
    "alternativas": [
        "A) A VPN não intercepta o tráfego do sistema operacional",
        "B) A VPN redireciona o tráfego do sistema operacional",
        "C) A VPN não criptografa o tráfego do sistema operacional",
        "D) A VPN não mantém seguro os dados do sistema operacional",
        "E) A VPN não cria um túnel entre cliente e servidor"
    ],
    "resposta":
    "B) A VPN redireciona o tráfego do sistema operacional"
}, {
    "pergunta":
    "O que o comando 'proxychains' faz no contexto do proxychains service?",
    "alternativas": [
        "A) Inicia o serviço de proxychains",
        "B) Ativa a cadeia de proxys para qualquer aplicação ou programa",
        "C) Desativa o uso do proxy",
        "D) Remove o histórico de comandos do proxychains",
        "E) Atualiza a configuração do proxychains"
    ],
    "resposta":
    "B) Ativa a cadeia de proxys para qualquer aplicação ou programa"
}, {
    "pergunta":
    "Qual opção do proxychains.conf garante que a conexão final será realizada mesmo se um proxy não estiver funcionando?",
    "alternativas": [
        "A) Strict chain", "B) Random chain", "C) Dynamic chain",
        "D) Proxy_dns", "E) Tor_dns"
    ],
    "resposta":
    "C) Dynamic chain"
}, {
    "pergunta":
    "O que significa a opção 'proxy_dns' no contexto do proxychains.conf?",
    "alternativas": [
        "A) Remove o histórico de comandos",
        "B) Força o uso do encapsulamento DNS", "C) Ativa a cadeia de proxys",
        "D) Desativa o uso do proxy", "E) Reinicia o serviço tor"
    ],
    "resposta":
    "B) Força o uso do encapsulamento DNS"
}, {
    "pergunta":
    "O que o comando 'dpkg -i [nome_arquivo]' faz no contexto da instalação de arquivos e programas .deb?",
    "alternativas": [
        "A) Atualiza o sistema completamente",
        "B) Remove arquivos e pacotes desnecessários",
        "C) Instala pacotes remotamente",
        "D) Instala pacotes já baixados no dispositivo",
        "E) Ativa o serviço de proxychains"
    ],
    "resposta":
    "D) Instala pacotes já baixados no dispositivo"
}, {
    "pergunta":
    "Como o Onion Proxy seleciona os servidores relays na rede Tor?",
    "alternativas": [
        "A) Aleatoriamente", "B) Com base na localização geográfica",
        "C) Pela velocidade de conexão",
        "D) Pelo número de servidores disponíveis",
        "E) De acordo com a largura de banda disponível"
    ],
    "resposta":
    "A) Aleatoriamente"
}, {
    "pergunta":
    "O que acontece quando a opção 'proxy_dns' está desconectada no proxychains.conf?",
    "alternativas": [
        "A) O serviço tor não inicia", "B) A conexão final não é realizada",
        "C) O encapsulamento DNS não ocorre",
        "D) A cadeia de proxys é desativada",
        "E) O histórico de comandos é removido"
    ],
    "resposta":
    "C) O encapsulamento DNS não ocorre"
}, {
    "pergunta":
    "Quais são os tipos de servidores proxy mencionados e qual é sua principal diferença?",
    "alternativas": [
        "A) HTTP e FTP; HTTP é de alto nível e FTP é de baixo nível",
        "B) HTTP e SOCKS; HTTP é de baixo nível e SOCKS é de alto nível",
        "C) FTP e SOCKS; FTP é de alto nível e SOCKS é de baixo nível",
        "D) HTTP e SOCKS; HTTP é de alto nível e SOCKS é de baixo nível",
        "E) DNS e TLS; DNS é de baixo nível e TLS é de alto nível"
    ],
    "resposta":
    "D) HTTP e SOCKS; HTTP é de alto nível e SOCKS é de baixo nível"
}, {
    "pergunta":
    "O que o navegador Tor fornece aos usuários durante a navegação na internet?",
    "alternativas": [
        "A) Filtragem de conteúdo", "B) Proteção da identidade e privacidade",
        "C) Ativação do serviço tor",
        "D) Conexão direta entre cliente e servidor",
        "E) Acesso a domínios .com"
    ],
    "resposta":
    "B) Proteção da identidade e privacidade"
}, {
    "pergunta":
    "Qual é o propósito principal da VPN em relação ao provedor de internet?",
    "alternativas": [
        "A) Criar uma conexão direta entre cliente e servidor",
        "B) Criptografar e manter seguro os dados na rede",
        "C) Monitorar as requisições do usuário",
        "D) Permitir acesso a domínios .onion",
        "E) Desativar o serviço de proxychains"
    ],
    "resposta":
    "B) Criptografar e manter seguro os dados na rede"
}, {
    "pergunta":
    "Como a VPN se diferencia do proxy no que diz respeito à conexão entre cliente e servidor?",
    "alternativas": [
        "A) A VPN redireciona o tráfego do sistema operacional",
        "B) A VPN cria um túnel seguro entre cliente e servidor",
        "C) A VPN não criptografa o tráfego do sistema operacional",
        "D) A VPN não mantém seguro os dados do sistema operacional",
        "E) A VPN não intercepta o tráfego do sistema operacional"
    ],
    "resposta":
    "B) A VPN cria um túnel seguro entre cliente e servidor"
}, {
    "pergunta":
    "Qual a importância de utilizar VPNs confiáveis em comparação com proxies?",
    "alternativas": [
        "A) VPNs são sempre mais lentas que proxies",
        "B) VPNs não criptografam os dados do sistema operacional",
        "C) Proxies são mais seguros que VPNs",
        "D) VPNs garantem segurança ao trafegar todo o tráfego do sistema operacional",
        "E) Proxies não têm monitoramento por parte da empresa da VPN"
    ],
    "resposta":
    "D) VPNs garantem segurança ao trafegar todo o tráfego do sistema operacional"
}, {
    "pergunta":
    "O que a opção 'proxy_dns' faz no contexto do arquivo de configuração do proxychains?",
    "alternativas": [
        "A) Remove o histórico de comandos",
        "B) Força o uso do encapsulamento DNS", "C) Ativa a cadeia de proxys",
        "D) Desativa o uso do proxy", "E) Reinicia o serviço tor"
    ],
    "resposta":
    "B) Força o uso do encapsulamento DNS"
}, {
    "pergunta":
    "Por que é recomendável desconectar a opção 'proxy_dns' no arquivo de configuração do proxychains?",
    "alternativas": [
        "A) Para acelerar a conexão", "B) Para aumentar a segurança",
        "C) Para permitir a conexão direta entre cliente e servidor",
        "D) Para remover o histórico de comandos",
        "E) Para desativar o serviço tor"
    ],
    "resposta":
    "C) Para permitir a conexão direta entre cliente e servidor"
}, {
    "pergunta":
    "Qual opção do proxychains.conf garante que a conexão final será realizada mesmo se um proxy não estiver funcionando?",
    "alternativas": [
        "A) Strict chain", "B) Random chain", "C) Dynamic chain",
        "D) Proxy_dns", "E) Tor_dns"
    ],
    "resposta":
    "C) Dynamic chain"
}, {
    "pergunta":
    "O que acontece quando a opção 'proxy_dns' está desconectada no proxychains.conf?",
    "alternativas": [
        "A) O serviço tor não inicia", "B) A conexão final não é realizada",
        "C) O encapsulamento DNS não ocorre",
        "D) A cadeia de proxys é desativada",
        "E) O histórico de comandos é removido"
    ],
    "resposta":
    "C) O encapsulamento DNS não ocorre"
}, {
    "pergunta":
    "Como o Onion Proxy seleciona os servidores relays na rede Tor?",
    "alternativas": [
        "A) Aleatoriamente", "B) Com base na localização geográfica",
        "C) Pela velocidade de conexão",
        "D) Pelo número de servidores disponíveis",
        "E) De acordo com a largura de banda disponível"
    ],
    "resposta":
    "A) Aleatoriamente"
}, {
    "pergunta":
    "O que a opção 'proxy_dns' faz no contexto do arquivo de configuração do proxychains?",
    "alternativas": [
        "A) Remove o histórico de comandos",
        "B) Força o uso do encapsulamento DNS", "C) Ativa a cadeia de proxys",
        "D) Desativa o uso do proxy", "E) Reinicia o serviço tor"
    ],
    "resposta":
    "B) Força o uso do encapsulamento DNS"
}, {
    "pergunta":
    "Quais são os tipos de servidores proxy mencionados e qual é sua principal diferença?",
    "alternativas": [
        "A) HTTP e FTP; HTTP é de alto nível e FTP é de baixo nível",
        "B) HTTP e SOCKS; HTTP é de baixo nível e SOCKS é de alto nível",
        "C) FTP e SOCKS; FTP é de alto nível e SOCKS é de baixo nível",
        "D) HTTP e SOCKS; HTTP é de alto nível e SOCKS é de baixo nível",
        "E) DNS e TLS; DNS é de baixo nível e TLS é de alto nível"
    ],
    "resposta":
    "D) HTTP e SOCKS; HTTP é de alto nível e SOCKS é de baixo nível"
}, {
    "pergunta":
    "Qual é o sistema operacional baseado em Debian que prioriza a segurança e anonimato do usuário?",
    "alternativas":
    ["A) Ubuntu", "B) Fedora", "C) Tails", "D) Kali Linux", "E) Arch Linux"],
    "resposta":
    "C) Tails"
}, {
    "pergunta":
    "Por que o Tails é recomendado ser utilizado por meio de um pendrive?",
    "alternativas": [
        "A) Para aumentar o desempenho", "B) Para facilitar a instalação",
        "C) Para garantir a segurança e anonimato",
        "D) Para evitar o uso do tor", "E) Para acelerar a inicialização"
    ],
    "resposta":
    "C) Para garantir a segurança e anonimato"
}, {
    "pergunta":
    "O que o Tails faz ao desligar o computador para garantir maior segurança?",
    "alternativas": [
        "A) Substitui parte da memória RAM", "B) Exclui todos os dados",
        "C) Reinicia o sistema", "D) Desativa o tor",
        "E) Compacta os arquivos no disco rígido"
    ],
    "resposta":
    "A) Substitui parte da memória RAM"
}, {
    "pergunta":
    "Por que o Tails força a utilização da navegação HTTPS e SSL?",
    "alternativas": [
        "A) Para reduzir o consumo de recursos",
        "B) Para aumentar a velocidade da navegação",
        "C) Para garantir a autenticidade dos arquivos",
        "D) Para otimizar a inicialização do sistema",
        "E) Para priorizar a segurança na comunicação"
    ],
    "resposta":
    "E) Para priorizar a segurança na comunicação"
}, {
    "pergunta":
    "Qual programa já instalado no Tails é utilizado para armazenar senhas de forma criptografada?",
    "alternativas": [
        "A) Gtkhash", "B) Onion circuits", "C) Onion share", "D) Keypass",
        "E) Tor"
    ],
    "resposta":
    "D) Keypass"
}, {
    "pergunta":
    "O que o programa Gtkhash faz no Tails?",
    "alternativas": [
        "A) Inicia o tor", "B) Armazena senhas criptografadas",
        "C) Mostra a hash de um arquivo ou texto",
        "D) Compartilha arquivos via rede onion",
        "E) Gerencia os circuitos da rede onion"
    ],
    "resposta":
    "C) Mostra a hash de um arquivo ou texto"
}, {
    "pergunta":
    "Para que serve o programa Onion circuits no Tails?",
    "alternativas": [
        "A) Armazenar senhas", "B) Mostrar a hash de arquivos",
        "C) Compartilhar arquivos via rede onion", "D) Iniciar o tor",
        "E) Gerenciar circuitos da rede onion"
    ],
    "resposta":
    "E) Gerenciar circuitos da rede onion"
}, {
    "pergunta":
    "O que o Onion share permite fazer no Tails?",
    "alternativas": [
        "A) Armazenar senhas criptografadas",
        "B) Compartilhar arquivos via rede onion",
        "C) Mostrar a hash de um arquivo", "D) Iniciar o tor",
        "E) Gerenciar circuitos da rede onion"
    ],
    "resposta":
    "B) Compartilhar arquivos via rede onion"
}, {
    "pergunta":
    "Por que o modelo OSI foi criado em 1984?",
    "alternativas": [
        "A) Para padronizar redes sem fio",
        "B) Para garantir compatibilidade entre hardwares e softwares",
        "C) Para substituir completamente o TCP/IP",
        "D) Para criar uma nova linguagem de programação",
        "E) Para estabelecer uma nova tecnologia de conexão"
    ],
    "resposta":
    "B) Para garantir compatibilidade entre hardwares e softwares"
}, {
    "pergunta": "Quantas camadas compõem o modelo OSI?",
    "alternativas": ["A) 3", "B) 5", "C) 7", "D) 10", "E) 12"],
    "resposta": "C) 7"
}, {
    "pergunta":
    "Qual camada do modelo OSI fornece serviços de rede ao usuário final?",
    "alternativas": [
        "A) Camada de Transporte", "B) Camada de Apresentação",
        "C) Camada de Aplicação", "D) Camada Física", "E) Camada de Enlace"
    ],
    "resposta":
    "C) Camada de Aplicação"
}, {
    "pergunta":
    "Qual protocolo opera na camada de Aplicação e permite a comunicação entre usuários e navegadores na rede?",
    "alternativas": ["A) HTTP", "B) TCP", "C) UDP", "D) IP", "E) SMTP"],
    "resposta":
    "A) HTTP"
}, {
    "pergunta":
    "O que a camada de Apresentação realiza?",
    "alternativas": [
        "A) Divide a mensagem em pacotes",
        "B) Criptografa e descriptografa os dados",
        "C) Estabelece, gerencia e termina sessões de comunicação",
        "D) Garante a transmissão segura dos dados",
        "E) Garante que os dados sejam transmitidos corretamente entre dispositivos conectados"
    ],
    "resposta":
    "B) Criptografa e descriptografa os dados"
}, {
    "pergunta":
    "O que a camada de Sessão faz?",
    "alternativas": [
        "A) Divide a mensagem em pacotes",
        "B) Criptografa e descriptografa os dados",
        "C) Estabelece, gerencia e termina sessões de comunicação",
        "D) Garante a transmissão segura dos dados",
        "E) Garante que os dados sejam transmitidos corretamente entre dispositivos conectados"
    ],
    "resposta":
    "C) Estabelece, gerencia e termina sessões de comunicação"
}, {
    "pergunta":
    "Qual é o principal objetivo da camada de Transporte?",
    "alternativas": [
        "A) Criptografar os dados",
        "B) Garantir a transmissão transparente de sequências de bits",
        "C) Gerenciar o controle lógico da transmissão",
        "D) Dividir a mensagem em pacotes",
        "E) Garantir que os dados sejam enviados de forma segura, eficiente e confiável"
    ],
    "resposta":
    "E) Garantir que os dados sejam enviados de forma segura, eficiente e confiável"
}, {
    "pergunta":
    "Quais são os protocolos mais conhecidos da camada de Transporte?",
    "alternativas": [
        "A) ICMP e SMTP", "B) HTTP e UDP", "C) TCP e UDP", "D) DNS e FTP",
        "E) HTTPS e SSH"
    ],
    "resposta":
    "C) TCP e UDP"
}, {
    "pergunta":
    "O que caracteriza o protocolo TCP?",
    "alternativas": [
        "A) É não confiável e sem conexão",
        "B) Garante a entrega dos dados sem erros e na ordem correta",
        "C) É amplamente utilizado em streaming de áudio e vídeo",
        "D) Realiza o controle de acesso ao meio de transmissão",
        "E) Cuida da transmissão transparente de sequências de bits"
    ],
    "resposta":
    "B) Garante a entrega dos dados sem erros e na ordem correta"
}, {
    "pergunta":
    "O que caracteriza o protocolo UDP?",
    "alternativas": [
        "A) É não confiável e sem conexão",
        "B) Garante a entrega dos dados sem erros e na ordem correta",
        "C) É amplamente utilizado em streaming de áudio e vídeo",
        "D) Realiza o controle de acesso ao meio de transmissão",
        "E) Cuida da transmissão transparente de sequências de bits"
    ],
    "resposta":
    "A) É não confiável e sem conexão"
}, {
    "pergunta":
    "Qual é a responsabilidade da camada de Redes?",
    "alternativas": [
        "A) Criptografar os dados",
        "B) Garantir a transmissão transparente de sequências de bits",
        "C) Dividir a mensagem em pacotes",
        "D) Estabelecer, gerenciar e terminar sessões de comunicação",
        "E) Colocar endereços em cada pacote e escolher o caminho certo pela rede"
    ],
    "resposta":
    "E) Colocar endereços em cada pacote e escolher o caminho certo pela rede"
}, {
    "pergunta":
    "O que a camada de Redes faz para evitar congestionamentos?",
    "alternativas": [
        "A) Divide a mensagem em pacotes",
        "B) Criptografa e descriptografa os dados",
        "C) Estabelece, gerencia e termina sessões de comunicação",
        "D) Coloca endereços em cada pacote e escolhe o caminho certo pela rede",
        "E) Garante que os dados sejam transmitidos corretamente entre dispositivos conectados"
    ],
    "resposta":
    "D) Coloca endereços em cada pacote e escolhe o caminho certo pela rede"
}, {
    "pergunta":
    "O que caracteriza a camada de Enlace?",
    "alternativas": [
        "A) Divide a mensagem em pacotes",
        "B) Garante a transmissão transparente de sequências de bits",
        "C) Criptografa e descriptografa os dados",
        "D) Estabelece, gerencia e termina sessões de comunicação",
        "E) Garante que os dados sejam transmitidos corretamente entre dispositivos conectados"
    ],
    "resposta":
    "E) Garante que os dados sejam transmitidos corretamente entre dispositivos conectados"
}, {
    "pergunta":
    "O que a subcamada MAC realiza?",
    "alternativas": [
        "A) Controla o acesso ao meio de transmissão e fornece endereçamento único",
        "B) Fornece serviços de controle lógico de enlace",
        "C) Cuida do controle de fluxo e correção de erros",
        "D) Realiza a transmissão transparente de sequências de bits",
        "E) Garante a entrega dos dados sem erros e na ordem correta"
    ],
    "resposta":
    "A) Controla o acesso ao meio de transmissão e fornece endereçamento único"
}, {
    "pergunta":
    "O que caracteriza a subcamada LLC?",
    "alternativas": [
        "A) Controla o acesso ao meio de transmissão e fornece endereçamento único",
        "B) Fornece serviços de controle lógico de enlace",
        "C) Cuida do controle de fluxo e correção de erros",
        "D) Realiza a transmissão transparente de sequências de bits",
        "E) Garante a entrega dos dados sem erros e na ordem correta"
    ],
    "resposta":
    "B) Fornece serviços de controle lógico de enlace"
}, {
    "pergunta":
    "Qual é a função da subcamada LLC?",
    "alternativas": [
        "A) Controlar o acesso ao meio de transmissão e fornecer endereçamento único",
        "B) Fornecer serviços de controle lógico de enlace",
        "C) Cuidar do controle de fluxo e correção de erros",
        "D) Realizar a transmissão transparente de sequências de bits",
        "E) Garantir a entrega dos dados sem erros e na ordem correta"
    ],
    "resposta":
    "B) Fornecer serviços de controle lógico de enlace"
}, {
    "pergunta":
    "O que a camada Física do modelo OSI trata?",
    "alternativas": [
        "A) Criptografia de dados", "B) Controle de fluxo",
        "C) Divisão de mensagens em pacotes",
        "D) Transmissão transparente de sequências de bits",
        "E) Gerenciamento de conexões"
    ],
    "resposta":
    "D) Transmissão transparente de sequências de bits"
},

                     {"pergunta": "O que é um protocolo na comunicação de redes?", "alternativas": ["A) Um conjunto de regras utilizadas por dispositivos para estabelecer a comunicação entre eles", "B) Um sistema operacional para redes", "C) Um programa de antivírus", "D) Um endereço IP", "E) Um dispositivo de rede"], "resposta": "A) Um conjunto de regras utilizadas por dispositivos para estabelecer a comunicação entre eles"},

                     {"pergunta": "O que significa TCP na sigla TCP/IP?", "alternativas": ["A) Transfer Control Protocol", "B) Transmission Code Protocol", "C) Transmission Control Protocol", "D) Telecommunication Control Protocol", "E) Telecommunication Code Protocol"], "resposta": "C) Transmission Control Protocol"},

                     {"pergunta": "Qual é a função principal do TCP?", "alternativas": ["A) Envio e roteamento de dados", "B) Controle de envio e recebimento de dados em uma rede", "C) Estabelecimento e encerramento de sessões de comunicação", "D) Divisão dos dados em pacotes", "E) Criptografia dos dados"], "resposta": "B) Controle de envio e recebimento de dados em uma rede"},

                     {"pergunta": "O que o TCP garante durante a transmissão de dados?", "alternativas": ["A) Entrega correta, ordenada e sem erros", "B) Velocidade máxima de transmissão", "C) Envia pacotes sem confirmar o recebimento", "D) Não realiza divisão dos dados", "E) Prioriza a velocidade em ambientes estáveis"], "resposta": "A) Entrega correta, ordenada e sem erros"},

                     {"pergunta": "O que o IP significa na sigla TCP/IP?", "alternativas": ["A) Internet Protocol", "B) Internet Process", "C) Interconnection Protocol", "D) Information Processing", "E) Interface Protocol"], "resposta": "A) Internet Protocol"},

                     {"pergunta": "Qual é a responsabilidade principal do IP?", "alternativas": ["A) Controle de envio e recebimento de dados", "B) Endereçamento e roteamento dos pacotes de dados", "C) Estabelecimento e encerramento de sessões de comunicação", "D) Divisão dos dados em pacotes", "E) Criptografia dos dados"], "resposta": "B) Endereçamento e roteamento dos pacotes de dados"},

                     {"pergunta": "O que é um endereço IP?", "alternativas": ["A) Uma identificação única para cada dispositivo conectado a uma rede", "B) Uma forma de criptografia de dados", "C) Um protocolo de comunicação", "D) Um tipo de vírus de computador", "E) Um método de controle de fluxo"], "resposta": "A) Uma identificação única para cada dispositivo conectado a uma rede"},

                     {"pergunta": "Como o IP realiza o roteamento dos pacotes na rede?", "alternativas": ["A) Através de um mecanismo de handshake de três vias", "B) Dividindo os dados em pacotes", "C) Utilizando números de sequência", "D) Baseando-se nos endereços IP de origem e destino", "E) Controlando o acesso ao meio de transmissão"], "resposta": "D) Baseando-se nos endereços IP de origem e destino"},

                     {"pergunta": "Quais são as versões do protocolo IP mencionadas?", "alternativas": ["A) TCP e UDP", "B) IP e ICMP", "C) IPv4 e IPv6", "D) HTTP e FTP", "E) DNS e DHCP"], "resposta": "C) IPv4 e IPv6"},

                     {"pergunta": "O que diferencia o IPv4 do IPv6 em termos de formato de endereço IP?", "alternativas": ["A) O IPv4 possui um formato de 32 bits, enquanto o IPv6 possui um formato de 128 bits", "B) O IPv6 possui um formato de 32 bits, enquanto o IPv4 possui um formato de 128 bits", "C) Ambos possuem um formato de 64 bits", "D) O IPv4 e IPv6 possuem o mesmo formato de endereço IP", "E) O IPv4 e IPv6 utilizam um formato de 16 bits"], "resposta": "A) O IPv4 possui um formato de 32 bits, enquanto o IPv6 possui um formato de 128 bits"},

                     {"pergunta": "Qual é a função da camada de Interface de Rede no modelo TCP/IP?", "alternativas": ["A) Envio e roteamento de dados", "B) Controle de envio e recebimento de dados em uma rede", "C) Transmissão física dos dados entre os dispositivos de rede", "D) Estabelecimento e encerramento de sessões de comunicação", "E) Criptografia dos dados"], "resposta": "C) Transmissão física dos dados entre os dispositivos de rede"},

                     {"pergunta": "O que a camada de Internet do modelo TCP/IP faz em termos de roteamento?", "alternativas": ["A) Utiliza números de porta para identificar os aplicativos nos dispositivos", "B) Divide os dados em pacotes e controla o acesso ao meio de transmissão", "C) Determina o caminho mais eficiente para enviar os dados através de roteadores", "D) Cuida do controle lógico da transmissão, gerenciando o fluxo de dados", "E) Realiza a transmissão transparente de sequências de bits"], "resposta": "C) Determina o caminho mais eficiente para enviar os dados através de roteadores"},

                     {"pergunta": "O que é endereçamento IP na camada de Internet do modelo TCP/IP?", "alternativas": ["A) Um serviço que faz a tradução entre nomes de domínio e endereços IP", "B) Uma identificação única para cada dispositivo conectado a uma rede", "C) Um protocolo utilizado para atribuir automaticamente endereços IP", "D) Uma forma de criptografia de dados", "E) Um método de controle de fluxo"], "resposta": "B) Uma identificação única para cada dispositivo conectado a uma rede"},

                     {"pergunta": "O que significa TCP na sigla TCP/IP e qual é sua principal função?", "alternativas": ["A) Total Control Protocol - responsável pelo endereçamento IP", "B) Transmission Control Protocol - controle de envio e recebimento de dados", "C) Technical Communication Protocol - garantia de entrega de pacotes", "D) Transferable Computing Protocol - roteamento eficiente de dados", "E) Traffic Control Protocol - controle de congestionamento na rede"], "resposta": "B) Transmission Control Protocol - controle de envio e recebimento de dados"},

                     {"pergunta": "Qual é a diferença entre endereço IP e número de porta na comunicação em rede?", "alternativas": ["A) Endereço IP é exclusivo para identificar dispositivos, enquanto número de porta identifica aplicativos", "B) Endereço IP e número de porta são termos intercambiáveis", "C) Endereço IP identifica o provedor de internet, enquanto número de porta identifica o dispositivo", "D) Endereço IP e número de porta são usados indistintamente para identificar dispositivos", "E) Endereço IP é usado apenas na camada de Internet"], "resposta": "A) Endereço IP é exclusivo para identificar dispositivos, enquanto número de porta identifica aplicativos"},

                     {"pergunta": "O que é a camada física no modelo TCP/IP e qual é sua principal responsabilidade?", "alternativas": ["A) Trata da transmissão física de dados e define padrões mecânicos, funcionais e elétricos", "B) Lida com o roteamento de pacotes na rede", "C) Responsável pelo controle de acesso ao meio de transmissão", "D) Garante a entrega correta e ordenada dos dados", "E) Fornece serviços de rede ao usuário final"], "resposta": "A) Trata da transmissão física de dados e define padrões mecânicos, funcionais e elétricos"},

                     {"pergunta": "Explique a função da subcamada MAC (Media Access Control) na camada de Enlace.", "alternativas": ["A) Controla o acesso ao meio de transmissão e fornece endereçamento IP exclusivo", "B) Segura a transmissão física de dados entre dispositivos", "C) Gerencia o controle de fluxo e correção de erros", "D) Responsável pelo controle de acesso ao meio e atribuição de endereços MAC exclusivos", "E) Estabelece conexões lógicas entre dispositivos finais"], "resposta": "D) Responsável pelo controle de acesso ao meio e atribuição de endereços MAC exclusivos"},

                     {"pergunta": "Qual é a principal função da camada de Transporte no modelo OSI?", "alternativas": ["A) Divisão dos dados em pacotes e controle de fluxo", "B) Controle de envio e recebimento de dados em uma rede", "C) Transmitir sequências de bits pelo meio físico", "D) Atribuir endereços IP aos dispositivos conectados", "E) Gerenciar o estabelecimento e término de sessões de comunicação"], "resposta": "B) Controle de envio e recebimento de dados em uma rede"},

                     {"pergunta": "Explique a diferença entre os protocolos TCP (Transmission Control Protocol) e UDP (User Datagram Protocol).", "alternativas": ["A) TCP é orientado à conexão e garante a entrega confiável, enquanto o UDP é mais rápido, mas menos confiável", "B) Ambos são protocolos orientados à conexão", "C) TCP e UDP são termos intercambiáveis", "D) UDP é orientado à conexão e mais confiável que o TCP", "E) TCP e UDP são protocolos de camadas diferentes no modelo OSI"], "resposta": "A) TCP é orientado à conexão e garante a entrega confiável, enquanto o UDP é mais rápido, mas menos confiável"},

                     {"pergunta": "O que a camada de Sessão realiza no modelo OSI?", "alternativas": ["A) Lida com o estabelecimento, gerenciamento e término das sessões de comunicação entre dispositivos", "B) Realiza a criptografia dos dados transmitidos", "C) Divide a mensagem em pacotes e coloca endereços em cada pacote", "D) Controla o acesso exclusivo aos recursos de comunicação", "E) Garante que os dados sejam enviados de forma segura e eficiente"], "resposta": "A) Lida com o estabelecimento, gerenciamento e término das sessões de comunicação entre dispositivos"},

                     {"pergunta": "Qual é a função da camada de Apresentação no modelo OSI?", "alternativas": ["A) Processamento e conversão dos dados de um formato para o outro", "B) Garante a entrega segura dos dados na rede", "C) Realiza a transmissão física de sequências de bits", "D) Responsável pelo estabelecimento e encerramento das conexões", "E) Divide a mensagem em pacotes e coloca endereços em cada pacote"], "resposta": "A) Processamento e conversão dos dados de um formato para o outro"},

                     {"pergunta": "Cite três exemplos de protocolos da camada de Aplicação no modelo TCP/IP e explique suas funções.", "alternativas": ["A) HTTP, FTP, DNS - HTTP é utilizado para transferir páginas web, FTP para transferência de arquivos, e DNS para tradução de nomes de domínio", "B) TCP, UDP, IP - TCP controla envio e recebimento, UDP é orientado à conexão, IP realiza endereçamento e roteamento", "C) DHCP, SSL, ICMP - DHCP atribui automaticamente endereços IP, SSL fornece segurança na comunicação, ICMP lida com mensagens de controle", "D) SMTP, POP3, IMAP - SMTP envia e-mails, POP3 e IMAP recebem e armazenam e-mails", "E) MAC, LLC, DNS - MAC controla acesso ao meio, LLC gerencia o controle lógico de enlace, DNS traduz nomes de domínio em endereços IP"], "resposta": "A) HTTP, FTP, DNS - HTTP é utilizado para transferir páginas web, FTP para transferência de arquivos, e DNS para tradução de nomes de domínio"},

                     {"pergunta": "Explique a diferença entre os protocolos TCP e UDP na camada de Transporte, destacando em que situações cada um é mais adequado.", "alternativas": ["A) TCP é orientado à conexão e adequado para aplicações que exigem entrega confiável, enquanto o UDP é mais rápido e adequado para aplicações que priorizam velocidade sobre confiabilidade, como streaming de vídeo e jogos online", "B) Ambos são adequados apenas para aplicações de alta segurança", "C) TCP e UDP são termos intercambiáveis na camada de Transporte", "D) UDP é orientado à conexão e mais confiável que o TCP", "E) TCP é exclusivamente utilizado para transferência de arquivos"], "resposta": "A) TCP é orientado à conexão e adequado para aplicações que exigem entrega confiável, enquanto o UDP é mais rápido e adequado para aplicações que priorizam velocidade sobre confiabilidade, como streaming de vídeo e jogos online"},

                     {"pergunta": "Qual é a principal motivação por trás da criação do modelo OSI?", "alternativas": ["A) Padronizar as redes e garantir compatibilidade entre hardwares e softwares", "B) Estabelecer um novo protocolo de comunicação", "C) Controlar o congestionamento na rede", "D) Melhorar a segurança na transmissão de dados", "E) Garantir a transmissão física eficiente de sequências de bits"], "resposta": "A) Padronizar as redes e garantir compatibilidade entre hardwares e softwares"},

                     {"pergunta": "Como a camada de Redes (Layer 3) no modelo OSI lida com a divisão de mensagens em pacotes?", "alternativas": ["A) Atribui endereços IP", "B) Segrega os dados em pacotes e adiciona informações de controle", "C) Envia os dados diretamente ao destino sem divisão", "D) Converte os dados para um formato adequado à transmissão", "E) Adiciona números de sequência aos pacotes para garantir a ordem correta de entrega"], "resposta": "B) Segrega os dados em pacotes e adiciona informações de controle"},

                     {"pergunta": "O que significa o acrônimo IP na sigla TCP/IP e qual é sua função principal?", "alternativas": ["A) Internet Protocol - controla envio e recebimento de dados", "B) Internet Package - roteamento eficiente de pacotes", "C) Internet Process - responsável pelo controle de acesso ao meio", "D) Information Protocol - garante a entrega confiável de dados", "E) Interface Port - divide a mensagem em pacotes"], "resposta": "A) Internet Protocol - controla envio e recebimento de dados"},

                     {"pergunta": "Na arquitetura do modelo TCP/IP, o que é tratado pela camada de Interface de Rede (Interface Layer 1)?", "alternativas": ["A) Controle de envio e recebimento de dados", "B) Transmissão física dos dados entre dispositivos de rede", "C) Segmentação e remontagem de dados", "D) Controle de congestionamento na rede", "E) Gerenciamento de sessões de comunicação"], "resposta": "B) Transmissão física dos dados entre dispositivos de rede"},

                     {"pergunta": "Explique a função da camada de Internet no modelo TCP/IP, destacando o papel do endereçamento IP.", "alternativas": ["A) Gerencia o controle de fluxo e correção de erros", "B) Divide a mensagem em pacotes e adiciona endereços IP", "C) Controla o acesso exclusivo aos recursos de comunicação", "D) Estabelece e gerencia sessões de comunicação", "E) Realiza a transmissão física de sequências de bits"], "resposta": "B) Divide a mensagem em pacotes e adiciona endereços IP"},

                     {"pergunta": "Quais são as funções principais da camada de Transporte no modelo TCP/IP?", "alternativas": ["A) Controle de envio e recebimento de dados, divisão dos dados em pacotes", "B) Transmissão física de dados e controle de acesso ao meio", "C) Roteamento eficiente de pacotes e controle de congestionamento", "D) Controle de fluxo e correção de erros", "E) Estabelecimento e término de sessões de comunicação"], "resposta": "A) Controle de envio e recebimento de dados, divisão dos dados em pacotes"},

                     {"pergunta": "Como a camada de Aplicação do modelo TCP/IP interage com os aplicativos e serviços utilizados pelos usuários?", "alternativas": ["A) Fornece endereçamento IP exclusivo para dispositivos", "B) Lida diretamente com os aplicativos, oferecendo interfaces e protocolos", "C) Controla o acesso ao meio de transmissão", "D) Gerencia o estabelecimento e encerramento de sessões", "E) Divide a mensagem em pacotes e adiciona endereços de origem e destino"], "resposta": "B) Lida diretamente com os aplicativos, oferecendo interfaces e protocolos"},

                     {"pergunta": "Qual é a principal responsabilidade da camada física no modelo OSI?", "alternativas": ["A) Transmissão física de sequências de bits", "B) Controle de envio e recebimento de dados", "C) Roteamento eficiente de pacotes", "D) Estabelecimento e gerenciamento de sessões de comunicação", "E) Processamento e conversão dos dados de um formato para o outro"], "resposta": "A) Transmissão física de sequências de bits"},

                     {"pergunta": "Explique a diferença entre os protocolos TCP (Transmission Control Protocol) e UDP (User Datagram Protocol) na camada de Transporte.", "alternativas": ["A) TCP é orientado à conexão e garante a entrega confiável, enquanto o UDP é mais rápido, mas menos confiável", "B) Ambos são protocolos de camadas diferentes no modelo OSI", "C) UDP é exclusivamente utilizado para transferência de arquivos", "D) TCP e UDP são termos intercambiáveis na camada de Transporte", "E) TCP é orientado à conexão e mais rápido que o UDP"], "resposta": "A) TCP é orientado à conexão e garante a entrega confiável, enquanto o UDP é mais rápido, mas menos confiável"},

                     {"pergunta": "Qual é a função da subcamada LLC (Logical Link Control) na camada de Enlace?", "alternativas": ["A) Controla o acesso ao meio de transmissão e fornece endereçamento IP exclusivo", "B) Garante a entrega correta e ordenada dos dados", "C) Segmenta os dados em unidades menores, chamadas de quadros", "D) Atribui endereços MAC exclusivos a cada dispositivo na rede", "E) Realiza a transmissão física de sequências de bits"], "resposta": "C) Segmenta os dados em unidades menores, chamadas de quadros"},

                     {"pergunta": "Como a camada de Redes (Layer 3) no modelo OSI lida com o controle de congestionamento na rede?", "alternativas": ["A) Divide a mensagem em pacotes e adiciona endereços de origem e destino", "B) Atribui endereços IP exclusivos", "C) Controla a velocidade de envio dos pacotes", "D) Estabelece conexões lógicas entre dispositivos finais", "E) Gerencia o estabelecimento e término de sessões de comunicação"], "resposta": "C) Controla a velocidade de envio dos pacotes"},

                     {"pergunta": "Quais são os principais serviços oferecidos pela camada de Aplicação no modelo TCP/IP?", "alternativas": ["A) Controle de envio e recebimento de dados, divisão dos dados em pacotes", "B) Transmissão física de dados e controle de acesso ao meio", "C) Roteamento eficiente de pacotes e controle de congestionamento", "D) Oferece interfaces e protocolos para aplicativos, como HTTP, FTP e DNS", "E) Controle de fluxo e correção de erros"], "resposta": "D) Oferece interfaces e protocolos para aplicativos, como HTTP, FTP e DNS"},

                     {"pergunta": "O que significa o acrônimo LAN?", "alternativas": ["A) Local Área Network", "B) Long Área Network", "C) Lateral Área Network", "D) Large Área Network", "E) Limited Área Network"], "resposta": "A) Local Área Network"},

                     {"pergunta": "Qual é a principal característica de uma LAN?", "alternativas": ["A) Alcance global", "B) Conecta dispositivos em diferentes localidades", "C) Rede de curta distância", "D) Utiliza fibra óptica para conexão", "E) Conexão sem fio"], "resposta": "C) Rede de curta distância"},

                     {"pergunta": "O que a conexão WAN abrange em termos de alcance geográfico?", "alternativas": ["A) Apenas um município", "B) Diferentes localidades, como países e continentes", "C) Alcance médio entre escritórios", "D) Conexão apenas em cidades vizinhas", "E) Limitada a uma residência ou escritório específico"], "resposta": "B) Diferentes localidades, como países e continentes"},

                     {"pergunta": "O que significa o acrônimo WLAN?", "alternativas": ["A) World Local Area Network", "B) Wireless Local Area Network", "C) Wired Local Area Network", "D) Wide Local Area Network", "E) Web Local Area Network"], "resposta": "B) Wireless Local Area Network"},

                     {"pergunta": "Qual é a principal diferença entre LAN e WAN em termos de alcance?", "alternativas": ["A) LAN é sempre sem fio, enquanto WAN é com fio", "B) LAN tem alcance global, WAN tem alcance local", "C) LAN é de curta distância, WAN é de longa distância", "D) LAN conecta países, WAN conecta residências", "E) LAN e WAN têm alcances semelhantes"], "resposta": "C) LAN é de curta distância, WAN é de longa distância"},

                     {"pergunta": "O que é uma VLAN?", "alternativas": ["A) World Local Area Network", "B) Conexão sem fio", "C) Virtual LAN", "D) Alcance global", "E) Conexão de alta velocidade"], "resposta": "C) Virtual LAN"},

                     {"pergunta": "Qual é a função principal de uma SAN?", "alternativas": ["A) Conexão de alta velocidade por fibra óptica", "B) Armazenar dados da rede e conectar servidor e dispositivos", "C) Estabelecer conexão entre escritórios", "D) Rede de curta distância", "E) Conexão entre redes de campos"], "resposta": "B) Armazenar dados da rede e conectar servidor e dispositivos"},

                     {"pergunta": "O que a sigla MAN representa em termos de redes?", "alternativas": ["A) Modem Area Network", "B) Municipal Area Network", "C) Mainframe Area Network", "D) Metro Area Network", "E) Mobile Area Network"], "resposta": "D) Metro Area Network"},

                     {"pergunta": "Qual é a abreviação correta para Personal Area Network?", "alternativas": ["A) PAN", "B) WAN", "C) SAN", "D) LAN", "E) WLAN"], "resposta": "A) PAN"},

                     {"pergunta": "Em que consiste uma RAN?", "alternativas": ["A) Rede de curta distância", "B) Regional Área Network com conexão sem fio", "C) Conexão de alta velocidade por fibra óptica", "D) Armazenamento de dados em rede", "E) Conexão entre escritórios no mesmo município"], "resposta": "B) Regional Área Network com conexão sem fio"},

                     {"pergunta": "O que é uma WWAN?", "alternativas": ["A) Wide Wireless Area Network", "B) Web Wide Area Network", "C) World Wide Area Network", "D) Wireless Wide Area Network", "E) Wired Wide Area Network"], "resposta": "D) Wireless Wide Area Network"},

                     {"pergunta": "Quais são as redes mencionadas que operam em formato wireless?", "alternativas": ["A) PAN e LAN", "B) MAN e SAN", "C) WAN e RAN", "D) WLAN e WWAN", "E) CAN e VLAN"], "resposta": "D) WLAN e WWAN"},

                     {"pergunta": "O que caracteriza uma PAN?", "alternativas": ["A) Rede de alta velocidade por fibra óptica", "B) Conexão entre escritórios no mesmo município", "C) Personal Área Network de longo alcance", "D) Conexão de curta distância, como o Bluetooth", "E) Armazenamento de dados em rede"], "resposta": "D) Conexão de curta distância, como o Bluetooth"},

                     {"pergunta": "Qual é a função principal de uma VLAN?", "alternativas": ["A) Conexão sem fio", "B) Virtual Local Area Network", "C) Armazenar dados da rede", "D) Conectar dispositivos em diferentes localidades", "E) Reduzir a velocidade de envio de pacotes"], "resposta": "B) Virtual Local Area Network"},

                     {"pergunta": "O que a sigla SAN representa no contexto de redes de computadores?", "alternativas": ["A) Simple Area Network", "B) Storage Area Network", "C) System Area Network", "D) Secure Area Network", "E) Shared Area Network"], "resposta": "B) Storage Area Network"},

                     {"pergunta": "Como a VLAN difere de uma LAN física?", "alternativas": ["A) VLAN é uma rede sem fio, enquanto LAN é uma rede com fio", "B) VLAN reúne máquinas de forma física, enquanto LAN é lógica", "C) VLAN é uma rede global, enquanto LAN é local", "D) VLAN é uma rede de curta distância, enquanto LAN pode abranger grandes áreas", "E) VLAN é uma rede lógica, enquanto LAN é física"], "resposta": "E) VLAN é uma rede lógica, enquanto LAN é física"},

                     {"pergunta": "Qual é a principal responsabilidade de uma WWAN?", "alternativas": ["A) Armazenamento de dados em rede", "B) Conexão entre escritórios no mesmo município", "C) Conexão de alta velocidade por fibra óptica", "D) Conexão sem fio de longa distância", "E) Rede de campos para conexão entre mesmos complexos"], "resposta": "D) Conexão sem fio de longa distância"},

                     {"pergunta": "O que caracteriza uma rede LAN?", "alternativas": ["A) Conexão sem fio entre dispositivos", "B) Alcance global", "C) Rede local ou de curta distância", "D) Conexão de alta velocidade por fibra óptica", "E) Armazenamento de dados em rede"], "resposta": "C) Rede local ou de curta distância"},

                     {"pergunta": "Qual é a principal função da camada de interface de rede?", "alternativas": ["A) Enviar pacotes pela fibra óptica", "B) Controlar o congestionamento da rede", "C) Dividir mensagens em pacotes menores", "D) Lidar com a transmissão física dos dados", "E) Roteamento de pacotes pela internet"], "resposta": "D) Lidar com a transmissão física dos dados"},

                     {"pergunta": "O que é CAN em termos de redes?", "alternativas": ["A) Connection Area Network", "B) Centralized Area Network", "C) Campus Area Network", "D) Computer Area Network", "E) Compressed Area Network"], "resposta": "C) Campus Area Network"},

                     {"pergunta": "Quais são os dois principais tipos de serviços de entrega na camada de transporte?", "alternativas": ["A) UDP e DNS", "B) HTTP e FTP", "C) TCP e UDP", "D) DHCP e SMTP", "E) VLAN e WLAN"], "resposta": "C) TCP e UDP"},

                     {"pergunta": "O que o IP faz na pilha de protocolos TCP/IP?", "alternativas": ["A) Controla o acesso exclusivo aos recursos de comunicação", "B) Fornece uma identificação única para cada dispositivo na rede", "C) Lida com o estabelecimento e término de sessões de comunicação", "D) Realiza a transmissão física de sequências de bits", "E) Controla o fluxo, correção de erros e compartilhamento da conexão"], "resposta": "B) Fornece uma identificação única para cada dispositivo na rede"},

                     {"pergunta": "O que é topologia de rede?", "alternativas": ["A) Representação de dispositivos computacionais", "B) Forma como os dispositivos estão conectados", "C) Desenho organizacional da rede", "D) Todos os anteriores", "E) Nenhuma das opções"], "resposta": "D) Todos os anteriores"},

                     {"pergunta": "Qual é a principal característica da topologia física?", "alternativas": ["A) Descreve o desenho organizacional da rede", "B) Representa o fluxo de dados na rede", "C) É uma representação em forma de layout", "D) Define o layout físico da rede", "E) Nenhuma das opções"], "resposta": "D) Define o layout físico da rede"},

                     {"pergunta": "O que a topologia lógica descreve?", "alternativas": ["A) O desenho organizacional da rede", "B) O fluxo de dados na rede", "C) A conexão ponto a ponto", "D) O circuito fechado de dispositivos", "E) A conexão em estrela"], "resposta": "B) O fluxo de dados na rede"},

                     {"pergunta": "O que caracteriza a conexão ponta a ponta?", "alternativas": ["A) Hierarquia de conexão", "B) Conexão através de um Switch", "C) Um cabo de dados ligado em dois computadores", "D) Formação de uma malha de conexão", "E) Conexão em circuito fechado"], "resposta": "C) Um cabo de dados ligado em dois computadores"},

                     {"pergunta": "Como é definida a topologia estrela?", "alternativas": ["A) Forma um circuito fechado de dispositivos", "B) Todos os computadores são conectados diretamente a um Hub", "C) Conexão obedecendo uma hierarquia", "D) Todos conectados com todos formando uma malha", "E) Utiliza várias topologias para construir a rede"], "resposta": "B) Todos os computadores são conectados diretamente a um Hub"},

                     {"pergunta": "O que caracteriza a topologia em malha?", "alternativas": ["A) Um ponto central de conexão", "B) Uma hierarquia de conexão", "C) Várias conexões diretas ponto a ponto", "D) Compartilha o mesmo meio físico linear", "E) Conexão através de um Switch"], "resposta": "C) Várias conexões diretas ponto a ponto"},

                     {"pergunta": "O que define a topologia árvore?", "alternativas": ["A) Um ponto central de conexão", "B) Compartilha o mesmo meio físico linear", "C) Hierarquia de conexão", "D) Conexão através de um Switch", "E) Conexão ponto a ponto"], "resposta": "C) Hierarquia de conexão"},

                     {"pergunta": "O que caracteriza a topologia híbrida?", "alternativas": ["A) Todos os computadores conectados diretamente a um Hub", "B) Formação de uma malha ou mesh de conexão", "C) Uso de várias topologias na construção da rede", "D) Hierarquia de conexão com computadores derivados", "E) Conexão em circuito fechado"], "resposta": "C) Uso de várias topologias na construção da rede"},

                     {"pergunta": "O que é topologia física?", "alternativas": ["A) Descreve o fluxo de dados na rede", "B) Representa o layout físico da rede", "C) Define a hierarquia de conexão", "D) Estabelece uma conexão ponto a ponto", "E) Nenhuma das opções"], "resposta": "B) Representa o layout físico da rede"},

                     {"pergunta": "Como é caracterizada a topologia lógica?", "alternativas": ["A) Descreve o desenho organizacional da rede", "B) Define a hierarquia de conexão", "C) Representa o fluxo de dados na rede", "D) Estabelece uma conexão ponto a ponto", "E) Nenhuma das opções"], "resposta": "C) Representa o fluxo de dados na rede"},

                     {"pergunta": "O que é a conexão ponto a ponto?", "alternativas": ["A) Uma conexão em estrela", "B) Hierarquia de conexão", "C) Um cabo de dados ligado em dois computadores", "D) Uma conexão em malha", "E) Nenhuma das opções"], "resposta": "C) Um cabo de dados ligado em dois computadores"},

                     {"pergunta": "Qual é a característica da topologia estrela?", "alternativas": ["A) Hierarquia de conexão", "B) Várias conexões diretas ponto a ponto", "C) Compartilha o mesmo meio físico linear", "D) Todos os computadores conectados diretamente a um Hub", "E) Nenhuma das opções"], "resposta": "D) Todos os computadores conectados diretamente a um Hub"},

                     {"pergunta": "O que define a topologia em malha?", "alternativas": ["A) Uma hierarquia de conexão", "B) Um ponto central de conexão", "C) Várias conexões diretas ponto a ponto", "D) Compartilha o mesmo meio físico linear", "E) Nenhuma das opções"], "resposta": "C) Várias conexões diretas ponto a ponto"},

                     {"pergunta": "Como é caracterizada a topologia árvore?", "alternativas": ["A) Uma hierarquia de conexão", "B) Várias conexões diretas ponto a ponto", "C) Um ponto central de conexão", "D) Compartilha o mesmo meio físico linear", "E) Nenhuma das opções"], "resposta": "A) Uma hierarquia de conexão"},

                     {"pergunta": "O que caracteriza a topologia híbrida?", "alternativas": ["A) Uso de várias topologias na construção da rede", "B) Uma hierarquia de conexão", "C) Todos os computadores conectados diretamente a um Hub", "D) Conexão ponto a ponto", "E) Nenhuma das opções"], "resposta": "A) Uso de várias topologias na construção da rede"},

                     {"pergunta": "O que é LAN?", "alternativas": ["A) Local Área Network", "B) Wide Área Network", "C) Regional Área Network", "D) Personal Área Network", "E) Storage Área Network"], "resposta": "A) Local Área Network"},

                     {"pergunta": "Qual é a característica da LAN?", "alternativas": ["A) Alcance maior, conectando dispositivos de diferentes localidades", "B) Conexão de alta velocidade através da fibra óptica", "C) Rede local ou de curta distância", "D) Hierarquia de conexão com computadores derivados", "E) Uso de várias topologias na construção da rede"], "resposta": "C) Rede local ou de curta distância"},

                     {"pergunta": "O que é WAN?", "alternativas": ["A) Local Área Network", "B) Wide Área Network", "C) Regional Área Network", "D) Personal Área Network", "E) Storage Área Network"], "resposta": "B) Wide Área Network"},

                     {"pergunta": "Qual é a principal diferença entre LAN e WAN?", "alternativas": ["A) Hierarquia de conexão", "B) Conexão ponto a ponto", "C) Alcance da rede", "D) Todos os computadores conectados diretamente a um Hub", "E) Conexão em malha"], "resposta": "C) Alcance da rede"},

                     {"pergunta": "Quais são as portas comumente associadas ao protocolo FTP?", "alternativas": ["A) 22/23", "B) 20/21", "C) 80/81", "D) 53/54", "E) 443/444"], "resposta": "B) 20/21"},

                     {"pergunta": "No protocolo FTP, qual a função da porta 21?", "alternativas": ["A) Comunicação de controle", "B) Comunicação de dados", "C) Transferência de arquivos criptografados", "D) Estabelecer conexões seguras", "E) Nenhuma das opções"], "resposta": "A) Comunicação de controle"},

                     {"pergunta": "Quais são os dois modos de operação principais no FTP?", "alternativas": ["A) Modo ativo e Modo passivo", "B) Modo rápido e Modo lento", "C) Modo seguro e Modo inseguro", "D) Modo primário e Modo secundário", "E) Modo principal e Modo alternativo"], "resposta": "A) Modo ativo e Modo passivo"},

                     {"pergunta": "Por que o modo passivo é mais comumente usado no protocolo FTP atualmente?", "alternativas": ["A) Porque é mais rápido", "B) Porque não é afetado por firewalls que bloqueiam conexões de saída não solicitadas", "C) Porque é mais seguro", "D) Porque requer menos recursos de rede", "E) Nenhuma das opções"], "resposta": "B) Porque não é afetado por firewalls que bloqueiam conexões de saída não solicitadas"},

                     {"pergunta": "Além do FTP, quais são os dois protocolos mais seguros mencionados como alternativas a serem consideradas pelas organizações?", "alternativas": ["A) TFTP e HTTP", "B) SFTP e FTPS", "C) SMTP e POP3", "D) DNS e DHCP", "E) SNMP e ICMP"], "resposta": "B) SFTP e FTPS"},

                     {"pergunta": "Qual é a porta padrão associada ao protocolo SSH?", "alternativas": ["A) 20", "B) 21", "C) 22", "D) 23", "E) 24"], "resposta": "C) 22"},

                     {"pergunta": "O que o protocolo SSH proporciona durante a comunicação entre dois sistemas?", "alternativas": ["A) Autenticação segura", "B) Velocidade de transmissão", "C) Maior largura de banda", "D) Conexões não criptografadas", "E) Nenhuma das opções"], "resposta": "A) Autenticação segura"},

                     {"pergunta": "Como o SSH utiliza criptografia durante o processo de autenticação?", "alternativas": ["A) Criptografia simétrica", "B) Criptografia assimétrica", "C) Criptografia de chave única", "D) Criptografia de chave pública", "E) Criptografia de chave privada"], "resposta": "B) Criptografia assimétrica"},

                     {"pergunta": "Além do SSH, qual outro protocolo utiliza criptografia durante a transferência de arquivos de forma segura?", "alternativas": ["A) FTP", "B) Telnet", "C) SCP", "D) DNS", "E) HTTP"], "resposta": "C) SCP"},

                     {"pergunta": "Qual protocolo substituiu o Telnet, oferecendo uma comunicação mais segura?", "alternativas": ["A) HTTP", "B) FTP", "C) SNMP", "D) SSH", "E) SMTP"], "resposta": "D) SSH"},

                     {"pergunta": "Quais são as duas portas associadas ao protocolo FTP e qual a função de cada uma?", "alternativas": ["A) 20 - Comunicação de controle, 21 - Comunicação de dados", "B) 21 - Comunicação de controle, 20 - Comunicação de dados", "C) 22 - Transferência de arquivos, 23 - Estabelecer conexões seguras", "D) 20 - Transferência de arquivos, 21 - Estabelecer conexões seguras", "E) 21 - Comunicação de controle, 22 - Comunicação de dados"], "resposta": "B) 21 - Comunicação de controle, 20 - Comunicação de dados"},

                     {"pergunta": "Quais são os dois modos de operação principais no FTP e em que situações cada um é mais adequado?", "alternativas": ["A) Modo rápido e Modo lento", "B) Modo seguro e Modo inseguro", "C) Modo ativo e Modo passivo", "D) Modo principal e Modo alternativo", "E) Modo primário e Modo secundário"], "resposta": "C) Modo ativo e Modo passivo"},

                     {"pergunta": "Quais são alguns dos comandos utilizados no protocolo FTP para interação entre cliente e servidor?", "alternativas": ["A) GET e POST", "B) USER e PASS", "C) READ e WRITE", "D) UPLOAD e DOWNLOAD", "E) CONNECT e DISCONNECT"], "resposta": "B) USER e PASS"},

                     {"pergunta": "Por que muitas organizações têm migrado para protocolos mais seguros em substituição ao FTP?", "alternativas": ["A) Porque o FTP é mais rápido", "B) Porque o FTP não permite transferência de arquivos", "C) Porque o FTP não é mais suportado", "D) Devido às limitações de segurança do FTP, especialmente a transmissão de informações de autenticação em texto simples", "E) Nenhuma das opções"], "resposta": "D) Devido às limitações de segurança do FTP, especialmente a transmissão de informações de autenticação em texto simples"},

                     {"pergunta": "Além do SFTP e FTPS, mencione outro protocolo seguro para transferência de arquivos que utiliza o SSH.", "alternativas": ["A) SCP", "B) HTTP", "C) Telnet", "D) SMTP", "E) POP3"], "resposta": "A) SCP"},

                     {"pergunta": "Além da autenticação segura, quais outros benefícios o protocolo SSH oferece durante a comunicação entre dois sistemas?", "alternativas": ["A) Maior largura de banda", "B) Menor latência", "C) Velocidade de transmissão", "D) Confidencialidade dos dados e integridade das informações transmitidas", "E) Nenhuma das opções"], "resposta": "D) Confidencialidade dos dados e integridade das informações transmitidas"},

                     {"pergunta": "Como o SSH utiliza criptografia assimétrica durante o processo de autenticação?", "alternativas": ["A) Através de uma única chave compartilhada", "B) Utilizando uma chave privada compartilhada por todos", "C) Com chaves públicas e privadas", "D) Com chaves públicas e chaves simétricas", "E) Não utiliza criptografia durante a autenticação"], "resposta": "C) Com chaves públicas e privadas"},

                     {"pergunta": "Quais são alguns dos serviços para os quais o protocolo SSH é comumente utilizado?", "alternativas": ["A) Streaming de vídeo e downloads", "B) Transferência de arquivos e cópias de segurança", "C) Compartilhamento de fotos e atualizações de software", "D) Jogos online e chamadas de voz", "E) Nenhuma das opções"], "resposta": "B) Transferência de arquivos e cópias de segurança"},

                     {"pergunta": "Como o SSH protege a comunicação entre cliente e servidor?", "alternativas": ["A) Transmitindo dados em texto simples", "B) Sem autenticação", "C) Usando um canal de comunicação não criptografado", "D) Criptografando todas as informações transmitidas", "E) Permitindo conexões não seguras"], "resposta": "D) Criptografando todas as informações transmitidas"},

                     {"pergunta": "Qual protocolo mais antigo o SSH substituiu, oferecendo uma alternativa mais segura?", "alternativas": ["A) FTP", "B) Telnet", "C) HTTP", "D) DNS", "E) SMTP"], "resposta": "B) Telnet"},

                     {"pergunta": "Qual é a principal finalidade do protocolo Telnet?", "alternativas": ["A) Transferência segura de arquivos", "B) Comunicação remota com outros sistemas por meio de uma sessão de texto simples", "C) Transmissão de e-mails", "D) Navegação segura na web", "E) Nenhuma das opções"], "resposta": "B) Comunicação remota com outros sistemas por meio de uma sessão de texto simples"},

                     {"pergunta": "Por que o Telnet é considerado inseguro, e quais são suas principais limitações de segurança?", "alternativas": ["A) Porque não permite comunicação remota", "B) Devido à falta de criptografia e autenticação adequadas", "C) Porque foi descontinuado", "D) Porque não suporta comandos de terminal", "E) Nenhuma das opções"], "resposta": "B) Devido à falta de criptografia e autenticação adequadas"},

                     {"pergunta": "O que acontece quando um cliente se conecta a uma porta 23 em um servidor usando o protocolo Telnet?", "alternativas": ["A) Estabelece uma conexão VPN", "B) Inicia uma chamada de voz", "C) Estabelece uma comunicação remota por meio de uma sessão de texto simples", "D) Realiza uma transferência de arquivos", "E) Nenhuma das opções"], "resposta": "C) Estabelece uma comunicação remota por meio de uma sessão de texto simples"},

                     {"pergunta": "Por que o uso do Telnet tem sido gradualmente substituído pelo protocolo SSH?", "alternativas": ["A) Porque o Telnet é mais rápido", "B) Porque o SSH não oferece autenticação", "C) Devido às limitações de segurança do Telnet, como a transmissão em texto simples e falta de criptografia robusta", "D) Porque o Telnet não requer autenticação", "E) Nenhuma das opções"], "resposta": "C) Devido às limitações de segurança do Telnet, como a transmissão em texto simples e falta de criptografia robusta"},

                     {"pergunta": "Além da falta de criptografia, quais são as limitações de autenticação do Telnet?", "alternativas": ["A) Autenticação robusta com chaves públicas e privadas", "B) Senhas transmitidas em texto simples", "C) Não possui limitações de autenticação", "D) Autenticação baseada em biometria", "E) Nenhuma das opções"], "resposta": "B) Senhas transmitidas em texto simples"},

                     {"pergunta": "Quando um usuário se conecta a uma máquina remota usando Telnet, como as informações, como comandos e respostas, são transmitidas?", "alternativas": ["A) Por meio de chamadas de voz", "B) Em formato binário", "C) Usando criptografia robusta", "D) Em uma sessão de texto simples", "E) Nenhuma das opções"], "resposta": "D) Em uma sessão de texto simples"},

                     {"pergunta": "Qual é a principal desvantagem da transmissão em texto simples do Telnet?", "alternativas": ["A) Maior largura de banda", "B) Maior segurança", "C) Possibilidade de interceptação e leitura por terceiros", "D) Velocidade de transmissão reduzida", "E) Nenhuma das opções"], "resposta": "C) Possibilidade de interceptação e leitura por terceiros"},

                     {"pergunta": "O Telnet é amplamente utilizado na transmissão de quais tipos de dados?", "alternativas": ["A) Arquivos criptografados", "B) Dados de sensores", "C) Dados financeiros", "D) Dados em uma sessão de texto simples", "E) Nenhuma das opções"], "resposta": "D) Dados em uma sessão de texto simples"},

                     {"pergunta": "Em que década o Telnet foi desenvolvido e se tornou um dos protocolos mais antigos ainda em uso?", "alternativas": ["A) Anos 50", "B) Anos 60", "C) Anos 70", "D) Anos 80", "E) Anos 90"], "resposta": "C) Anos 70"},

                     {"pergunta": "Qual é a função da porta 23 associada ao Telnet?", "alternativas": ["A) Transferência segura de arquivos", "B) Comunicação remota com outros sistemas por meio de uma sessão de texto simples", "C) Transmissão de e-mails", "D) Navegação segura na web", "E) Nenhuma das opções"], "resposta": "B) Comunicação remota com outros sistemas por meio de uma sessão de texto simples"},

                     {"pergunta": "O que significa a sigla SMTP?", "alternativas": ["A) Simple Mail Transfer Protocol", "B) Secure Mail Transfer Protocol", "C) Server Mail Transfer Protocol", "D) Standard Mail Transfer Protocol", "E) Nenhuma das opções"], "resposta": "A) Simple Mail Transfer Protocol"},

                     {"pergunta": "Qual é a função principal do protocolo SMTP?", "alternativas": ["A) Transferência segura de arquivos", "B) Comunicação remota", "C) Envio e encaminhamento de e-mails entre servidores de e-mail", "D) Navegação segura na web", "E) Nenhuma das opções"], "resposta": "C) Envio e encaminhamento de e-mails entre servidores de e-mail"},

                     {"pergunta": "Qual é a diferença principal entre as portas 25 e 587 associadas ao SMTP?", "alternativas": ["A) A porta 25 é usada para comunicação criptografada, enquanto a porta 587 é para comunicação não criptografada", "B) A porta 587 é usada para comunicação criptografada, enquanto a porta 25 é para comunicação não criptografada", "C) Ambas as portas são usadas para comunicação criptografada", "D) Ambas as portas são usadas para comunicação não criptografada", "E) Nenhuma das opções"], "resposta": "B) A porta 587 é usada para comunicação criptografada, enquanto a porta 25 é para comunicação não criptografada"},

                     {"pergunta": "Por que o uso de criptografia na comunicação SMTP se tornou mais comum nos últimos anos?", "alternativas": ["A) Para aumentar a velocidade da comunicação", "B) Porque a criptografia não é segura", "C) Devido à ênfase na segurança da comunicação de e-mail", "D) Porque a criptografia não é suportada pelo SMTP", "E) Nenhuma das opções"], "resposta": "C) Devido à ênfase na segurança da comunicação de e-mail"},

                     {"pergunta": "Além da porta 587, qual é outra porta historicamente associada ao SMTP com SSL/TLS?", "alternativas": ["A) Porta 22", "B) Porta 53", "C) Porta 465", "D) Porta 67", "E) Nenhuma das opções"], "resposta": "C) Porta 465"},

                     {"pergunta": "O que é STARTTLS em relação ao SMTP?", "alternativas": ["A) Um novo protocolo de transferência de arquivos", "B) Uma versão mais antiga do SMTP", "C) Um mecanismo de criptografia que inicia uma comunicação segura durante uma conexão existente", "D) Um protocolo de navegação segura", "E) Nenhuma das opções"], "resposta": "C) Um mecanismo de criptografia que inicia uma comunicação segura durante uma conexão existente"},

                     {"pergunta": "Por que a porta 465 associada ao SMTP está sendo desencorajada?", "alternativas": ["A) Porque não suporta criptografia", "B) Porque é reservada para outros fins", "C) Porque a criptografia é insegura", "D) Em favor do uso da porta 587 com STARTTLS", "E) Nenhuma das opções"], "resposta": "D) Em favor do uso da porta 587 com STARTTLS"},

                     {"pergunta": "Qual é a principal responsabilidade do SMTP ao enviar e-mails?", "alternativas": ["A) Armazenar e-mails", "B) Criar e-mails", "C) Enviar e encaminhar e-mails entre servidores de e-mail", "D) Ler e-mails", "E) Nenhuma das opções"], "resposta": "C) Enviar e encaminhar e-mails entre servidores de e-mail"},

                     {"pergunta": "O que acontece quando um cliente de e-mail envia um e-mail usando o SMTP?", "alternativas": ["A) O e-mail é armazenado localmente no dispositivo", "B) O e-mail é enviado diretamente ao destinatário", "C) O cliente se conecta ao servidor de e-mail do destinatário usando a porta 25 ou 587, autentica-se e envia a mensagem", "D) O e-mail é impresso em papel", "E) Nenhuma das opções"], "resposta": "C) O cliente se conecta ao servidor de e-mail do destinatário usando a porta 25 ou 587, autentica-se e envia a mensagem"},

                     {"pergunta": "Qual é a importância do SMTP na comunicação de e-mails?", "alternativas": ["A) Não é importante", "B) Permite a transferência de arquivos", "C) Possibilita a comunicação eficiente e confiável entre servidores de e-mail", "D) É usado apenas para navegação na web", "E) Nenhuma das opções"], "resposta": "C) Possibilita a comunicação eficiente e confiável entre servidores de e-mail"},

                     {"pergunta": "O que significa a sigla DNS?", "alternativas": ["A) Domain Name System", "B) Dynamic Network System", "C) Digital Naming Service", "D) Data Network Security", "E) Nenhuma das opções"], "resposta": "A) Domain Name System"},

                     {"pergunta": "Qual é a função principal do protocolo DNS?", "alternativas": ["A) Enviar e-mails", "B) Traduzir nomes de domínio legíveis por humanos em endereços IP", "C) Estabelecer conexões seguras entre servidores", "D) Gerenciar redes dinâmicas", "E) Nenhuma das opções"], "resposta": "B) Traduzir nomes de domínio legíveis por humanos em endereços IP"},

                     {"pergunta": "Como o DNS opera para resolver consultas de nomes de domínio?", "alternativas": ["A) Enviando e-mails", "B) Traduzindo nomes de domínio em endereços IP", "C) Estabelecendo conexões seguras", "D) Gerenciando redes sem fio", "E) Nenhuma das opções"], "resposta": "B) Traduzindo nomes de domínio em endereços IP"},

                     {"pergunta": "Qual é a porta padrão associada ao serviço DNS?", "alternativas": ["A) Porta 22", "B) Porta 53", "C) Porta 67", "D) Porta 25", "E) Nenhuma das opções"], "resposta": "B) Porta 53"},

                     {"pergunta": "O que acontece quando você digita um nome de site, como 'www.exemplo.com', em seu navegador?", "alternativas": ["A) O site é carregado imediatamente", "B) O navegador se conecta ao servidor DNS usando a porta 53", "C) O nome de domínio é convertido em endereço IP", "D) Uma mensagem é enviada ao servidor DHCP", "E) Nenhuma das opções"], "resposta": "C) O nome de domínio é convertido em endereço IP"},

                     {"pergunta": "Como o servidor DNS responde à pergunta feita pelo seu computador?", "alternativas": ["A) Enviando um e-mail", "B) Usando a porta 53 para enviar a resposta", "C) Criando uma conexão segura", "D) Gerenciando redes de computadores", "E) Nenhuma das opções"], "resposta": "B) Usando a porta 53 para enviar a resposta"},

                     {"pergunta": "Qual é o benefício de usar o DNS?", "alternativas": ["A) Criptografar comunicações", "B) Traduzir nomes de domínio em endereços IP", "C) Estabelecer conexões seguras", "D) Gerenciar redes dinâmicas", "E) Nenhuma das opções"], "resposta": "B) Traduzir nomes de domínio em endereços IP"},

                     {"pergunta": "Qual é a importância do DNS na navegação na web?", "alternativas": ["A) Não tem importância", "B) Permite a transferência de arquivos", "C) Possibilita a comunicação eficiente entre servidores", "D) Traduz nomes de domínio para endereços IP, permitindo o acesso a recursos de rede", "E) Nenhuma das opções"], "resposta": "D) Traduz nomes de domínio para endereços IP, permitindo o acesso a recursos de rede"},

                     {"pergunta": "O que aconteceria se o DNS não estivesse disponível?", "alternativas": ["A) Navegação normal na web", "B) Os sites ainda seriam acessíveis", "C) Incapacidade de acessar sites por nome, apenas por endereço IP", "D) O navegador usaria uma porta diferente", "E) Nenhuma das opções"], "resposta": "C) Incapacidade de acessar sites por nome, apenas por endereço IP"},

                     {"pergunta": "Por que é mais fácil lembrar nomes de domínio do que endereços IP?", "alternativas": ["A) Porque os nomes de domínio são mais curtos", "B) Porque os nomes de domínio são mais seguros", "C) Porque os nomes de domínio são únicos", "D) Porque os endereços IP são mais fáceis de lembrar", "E) Nenhuma das opções"], "resposta": "C) Porque os nomes de domínio são únicos"},

                     {"pergunta": "O que significa a sigla DHCP?", "alternativas": ["A) Dynamic Host Configuration Protocol", "B) Digital Hosting Control Protocol", "C) Data Hub Connection Protocol", "D) Domain Hosting Configuration Protocol", "E) Nenhuma das opções"], "resposta": "A) Dynamic Host Configuration Protocol"},

                     {"pergunta": "Qual é a função principal do protocolo DHCP?", "alternativas": ["A) Enviar e-mails", "B) Atribuir configurações de rede automaticamente a dispositivos", "C) Estabelecer conexões seguras entre servidores", "D) Gerenciar redes dinâmicas", "E) Nenhuma das opções"], "resposta": "B) Atribuir configurações de rede automaticamente a dispositivos"},

                     {"pergunta": "Quando um dispositivo se conecta a uma rede usando DHCP, o que ele envia para o servidor DHCP através da porta 67?", "alternativas": ["A) Um e-mail", "B) Uma solicitação de informações de configuração", "C) Um arquivo de configuração", "D) Uma mensagem criptografada", "E) Nenhuma das opções"], "resposta": "B) Uma solicitação de informações de configuração"},

                     {"pergunta": "Qual é o papel da porta 67 no protocolo DHCP?", "alternativas": ["A) Receber mensagens do servidor", "B) Enviar mensagens ao servidor", "C) Estabelecer uma conexão segura", "D) Gerenciar redes sem fio", "E) Nenhuma das opções"], "resposta": "B) Enviar mensagens ao servidor"},

                     {"pergunta": "O que o servidor DHCP envia de volta ao dispositivo após receber a solicitação?", "alternativas": ["A) Uma lista de todos os dispositivos na rede", "B) Uma resposta criptografada", "C) Informações de configuração, como endereço IP, máscara de sub-rede, gateway e servidores DNS", "D) Uma mensagem de boas-vindas", "E) Nenhuma das opções"], "resposta": "C) Informações de configuração, como endereço IP, máscara de sub-rede, gateway e servidores DNS"},

                     {"pergunta": "Qual é o benefício do uso do DHCP em uma rede?", "alternativas": ["A) Criptografar comunicações", "B) Facilitar a configuração automática de dispositivos na rede", "C) Estabelecer conexões seguras", "D) Gerenciar redes dinâmicas", "E) Nenhuma das opções"], "resposta": "B) Facilitar a configuração automática de dispositivos na rede"},

                     {"pergunta": "Como o DHCP torna a conexão à rede mais fácil para os dispositivos?", "alternativas": ["A) Atribuindo manualmente endereços IP a cada dispositivo", "B) Requerendo que os dispositivos usem portas específicas", "C) Permitindo que os dispositivos solicitem e obtenham informações de configuração automaticamente", "D) Bloqueando o acesso a dispositivos não autorizados", "E) Nenhuma das opções"], "resposta": "C) Permitindo que os dispositivos solicitem e obtenham informações de configuração automaticamente"},

                     {"pergunta": "Quais informações o servidor DHCP fornece a um dispositivo?", "alternativas": ["A) Nome do dispositivo", "B) Lista de dispositivos na rede", "C) Informações de configuração, como endereço IP, máscara de sub-rede, gateway e servidores DNS", "D) Histórico de conexão do dispositivo", "E) Nenhuma das opções"], "resposta": "C) Informações de configuração, como endereço IP, máscara de sub-rede, gateway e servidores DNS"},

                     {"pergunta": "O que aconteceria se uma rede não utilizasse o DHCP?", "alternativas": ["A) Os dispositivos não poderiam se conectar à rede", "B) Os dispositivos teriam que configurar manualmente suas informações de rede", "C) O DHCP não faz diferença na configuração da rede", "D) A rede se tornaria mais segura", "E) Nenhuma das opções"], "resposta": "B) Os dispositivos teriam que configurar manualmente suas informações de rede"},

                     {"pergunta": "Como o DHCP contribui para a eficiência de uma rede?", "alternativas": ["A) Aumentando a complexidade da configuração", "B) Reduzindo a necessidade de configuração manual", "C) Bloqueando dispositivos na rede", "D) Limitando o número de dispositivos conectados", "E) Nenhuma das opções"], "resposta": "B) Reduzindo a necessidade de configuração manual"},

                     {"pergunta": "O que significa a sigla FTP?", "alternativas": ["A) File Transfer Protocol", "B) File Transmission Protocol", "C) File Tracking Protocol", "D) File Teleportation Protocol", "E) Nenhuma das opções"], "resposta": "A) File Transfer Protocol"},

                     {"pergunta": "Quais são as portas associadas ao protocolo FTP?", "alternativas": ["A) 20/21", "B) 22", "C) 23", "D) 53", "E) Nenhuma das opções"], "resposta": "A) 20/21"},

                     {"pergunta": "Qual é a função da porta 21 no protocolo FTP?", "alternativas": ["A) Comunicação de controle", "B) Comunicação de dados", "C) Criptografia das comunicações", "D) Autenticação do usuário", "E) Nenhuma das opções"], "resposta": "A) Comunicação de controle"},

                     {"pergunta": "Como o FTP lida com a transferência de arquivos no modo ativo?", "alternativas": ["A) O servidor abre uma porta de dados (porta 20) e o cliente se conecta a essa porta", "B) O cliente abre uma porta de dados (porta 20) e o servidor se conecta a essa porta", "C) O servidor e o cliente compartilham a mesma porta", "D) O FTP não permite transferência de arquivos no modo ativo", "E) Nenhuma das opções"], "resposta": "A) O servidor abre uma porta de dados (porta 20) e o cliente se conecta a essa porta"},

                     {"pergunta": "No modo passivo do FTP, como é estabelecida a conexão de dados?", "alternativas": ["A) O cliente solicita ao servidor uma porta de dados e se conecta a ela", "B) O servidor solicita ao cliente uma porta de dados e se conecta a ela", "C) A conexão de dados é estabelecida pela porta 21", "D) Não há transferência de dados no modo passivo", "E) Nenhuma das opções"], "resposta": "A) O cliente solicita ao servidor uma porta de dados e se conecta a ela"},

                     {"pergunta": "Por que muitas organizações migraram do FTP para protocolos mais seguros, como SFTP ou FTPS?", "alternativas": ["A) Porque o FTP não permite transferência de arquivos", "B) Devido a limitações de segurança do FTP, como a transmissão de informações de autenticação em texto simples", "C) Porque o FTP é mais eficiente", "D) Porque o FTP é mais fácil de configurar", "E) Nenhuma das opções"], "resposta": "B) Devido a limitações de segurança do FTP, como a transmissão de informações de autenticação em texto simples"},

                     {"pergunta": "Quais são os modos de operação principais no FTP?", "alternativas": ["A) Ativo e passivo", "B) Rápido e lento", "C) Seguro e não seguro", "D) Público e privado", "E) Nenhuma das opções"], "resposta": "A) Ativo e passivo"},

                     {"pergunta": "Como o modo passivo do FTP lida com firewalls ou roteadores que bloqueiam conexões de entrada não solicitadas?", "alternativas": ["A) O modo passivo não é afetado por firewalls", "B) O cliente se conecta diretamente ao servidor, contornando o firewall", "C) O servidor solicita ao cliente uma porta de dados e se conecta a ela", "D) O modo passivo não pode ser usado com firewalls", "E) Nenhuma das opções"], "resposta": "B) O cliente se conecta diretamente ao servidor, contornando o firewall"},

                     {"pergunta": "Qual é a principal limitação do FTP em relação à segurança?", "alternativas": ["A) Criptografia forte", "B) Transmissão de informações de autenticação em texto simples", "C) Autenticação baseada em chaves", "D) Modo passivo", "E) Nenhuma das opções"], "resposta": "B) Transmissão de informações de autenticação em texto simples"},

                     {"pergunta": "Como os modos ativo e passivo do FTP lidam com a abertura de portas para transferência de arquivos?", "alternativas": ["A) Ambos exigem que o servidor abra uma porta de dados", "B) Apenas o modo ativo exige que o servidor abra uma porta de dados", "C) Apenas o modo passivo exige que o servidor abra uma porta de dados", "D) Ambos contornam a necessidade de abrir portas de dados", "E) Nenhuma das opções"], "resposta": "A) Ambos exigem que o servidor abra uma porta de dados"},

                     {"pergunta": "O que significa a sigla SSH?", "alternativas": ["A) Secure Shell", "B) Simple Server Hosting", "C) Secure Socket Hosting", "D) System Security Handler", "E) Nenhuma das opções"], "resposta": "A) Secure Shell"},

                     {"pergunta": "Qual é a porta padrão associada ao protocolo SSH?", "alternativas": ["A) 20", "B) 22", "C) 25", "D) 53", "E) Nenhuma das opções"], "resposta": "B) 22"},

                     {"pergunta": "O que o protocolo SSH proporciona em uma conexão?", "alternativas": ["A) Comunicação remota insegura", "B) Comunicação remota criptografada e segura", "C) Transmissão de arquivos não segura", "D) Compartilhamento de arquivos", "E) Nenhuma das opções"], "resposta": "B) Comunicação remota criptografada e segura"},

                     {"pergunta": "Além do acesso remoto seguro, qual é outra função do protocolo SSH?", "alternativas": ["A) Transferência de arquivos não segura", "B) Transferência de arquivos criptografada", "C) Compartilhamento de arquivos em redes sociais", "D) Autenticação por meio de senhas em texto simples", "E) Nenhuma das opções"], "resposta": "B) Transferência de arquivos criptografada"},

                     {"pergunta": "Qual tipo de criptografia o SSH utiliza durante o processo de autenticação?", "alternativas": ["A) Criptografia simétrica", "B) Criptografia assimétrica (chaves públicas e privadas)", "C) Criptografia por substituição", "D) Criptografia de chave única", "E) Nenhuma das opções"], "resposta": "B) Criptografia assimétrica (chaves públicas e privadas)"},

                     {"pergunta": "Por que o SSH substituiu protocolos mais antigos, como o Telnet?", "alternativas": ["A) Porque o Telnet oferece criptografia forte", "B) Porque o Telnet é mais eficiente", "C) Porque o Telnet utiliza chaves públicas e privadas", "D) Porque o Telnet é inseguro devido à falta de criptografia e autenticação adequadas", "E) Nenhuma das opções"], "resposta": "D) Porque o Telnet é inseguro devido à falta de criptografia e autenticação adequadas"},

                     {"pergunta": "Além do SSH, qual é outro protocolo usado para transferência segura de arquivos?", "alternativas": ["A) FTP", "B) Telnet", "C) SFTP", "D) DNS", "E) Nenhuma das opções"], "resposta": "C) SFTP"},

                     {"pergunta": "O que é SFTP?", "alternativas": ["A) Sistema de Transferência de Protocolo Seguro", "B) Secure File Transfer Protocol", "C) Simple File Transfer Protocol", "D) Standard File Transfer Protocol", "E) Nenhuma das opções"], "resposta": "B) Secure File Transfer Protocol"},

                     {"pergunta": "Como o SSH estabelece uma conexão segura?", "alternativas": ["A) Utilizando senhas em texto simples", "B) Por meio de criptografia assimétrica durante o processo de autenticação", "C) Transmitindo informações em texto simples", "D) Utilizando chaves públicas e privadas apenas no modo passivo", "E) Nenhuma das opções"], "resposta": "B) Por meio de criptografia assimétrica durante o processo de autenticação"},

                     {"pergunta": "Qual é a principal característica que torna o SSH uma opção segura para acesso remoto?", "alternativas": ["A) Ausência de autenticação", "B) Criptografia forte durante toda a sessão", "C) Transmissão de informações em texto simples", "D) Uso do Telnet como base", "E) Nenhuma das opções"], "resposta": "B) Criptografia forte durante toda a sessão"},

                     {"pergunta": "O que significa a sigla Telnet?", "alternativas": ["A) Telecom Network", "B) Text Network", "C) Telecommunication Network", "D) Terminal Network", "E) Nenhuma das opções"], "resposta": "D) Terminal Network"},

                     {"pergunta": "Qual é a porta padrão associada ao protocolo Telnet?", "alternativas": ["A) 20", "B) 22", "C) 23", "D) 25", "E) Nenhuma das opções"], "resposta": "C) 23"},

                     {"pergunta": "Como o Telnet permite a comunicação remota?", "alternativas": ["A) Através de uma conexão segura", "B) Por meio de uma sessão de texto simples", "C) Utilizando criptografia assimétrica", "D) Permitindo o compartilhamento de arquivos", "E) Nenhuma das opções"], "resposta": "B) Por meio de uma sessão de texto simples"},

                     {"pergunta": "Quais são as limitações de segurança do Telnet?", "alternativas": ["A) Comunicação criptografada", "B) Autenticação baseada em chaves", "C) Transmissão de dados em texto simples", "D) Uso de criptografia assimétrica", "E) Nenhuma das opções"], "resposta": "C) Transmissão de dados em texto simples"},

                     {"pergunta": "Por que o Telnet é considerado inseguro?", "alternativas": ["A) Devido à sua eficiência", "B) Devido à falta de criptografia e autenticação adequadas", "C) Por utilizar chaves públicas e privadas", "D) Por ser um protocolo recente", "E) Nenhuma das opções"], "resposta": "B) Devido à falta de criptografia e autenticação adequadas"},

                     {"pergunta": "Qual protocolo mais seguro tem substituído gradualmente o Telnet?", "alternativas": ["A) SSH", "B) FTP", "C) SFTP", "D) DNS", "E) Nenhuma das opções"], "resposta": "A) SSH"},

                     {"pergunta": "Além da falta de criptografia, qual é outra vulnerabilidade do Telnet?", "alternativas": ["A) Autenticação forte", "B) Compatibilidade com firewalls", "C) Uso de chaves públicas", "D) Interceptação de dados devido à transmissão em texto simples", "E) Nenhuma das opções"], "resposta": "D) Interceptação de dados devido à transmissão em texto simples"},

                     {"pergunta": "O que acontece durante uma conexão Telnet padrão?", "alternativas": ["A) Comunicação criptografada", "B) Estabelecimento de uma conexão segura", "C) Transmissão de dados em texto simples", "D) Uso de criptografia assimétrica", "E) Nenhuma das opções"], "resposta": "C) Transmissão de dados em texto simples"},

                     {"pergunta": "Por que o Telnet era amplamente utilizado no passado?", "alternativas": ["A) Pela eficiência na transferência de arquivos", "B) Pela transmissão de dados em texto simples", "C) Pela segurança em ambientes de rede", "D) Pela falta de vulnerabilidades", "E) Nenhuma das opções"], "resposta": "B) Pela transmissão de dados em texto simples"},

                     {"pergunta": "O que o Telnet permite que um usuário faça em um sistema remoto?", "alternativas": ["A) Controle um sistema remoto apenas visualmente", "B) Execute comandos e acesse recursos como se estivesse localmente presente", "C) Realize compartilhamento de arquivos", "D) Comunique-se apenas por meio de mensagens de texto", "E) Nenhuma das opções"], "resposta": "B) Execute comandos e acesse recursos como se estivesse localmente presente"},

                     {"pergunta": "O que significa a sigla SMTP?", "alternativas": ["A) Simple Mail Transfer Protocol", "B) Secure Mail Transfer Protocol", "C) System Mail Transfer Protocol", "D) Standard Mail Transfer Protocol", "E) Nenhuma das opções"], "resposta": "A) Simple Mail Transfer Protocol"},

                     {"pergunta": "Qual é a principal função do protocolo SMTP?", "alternativas": ["A) Transferência segura de arquivos", "B) Transferência de mensagens de correio eletrônico", "C) Transferência de dados em redes locais", "D) Autenticação segura entre dispositivos", "E) Nenhuma das opções"], "resposta": "B) Transferência de mensagens de correio eletrônico"},

                     {"pergunta": "Como o SMTP opera na comunicação de e-mails?", "alternativas": ["A) Usando criptografia assimétrica", "B) Estabelecendo uma conexão segura", "C) Transferindo mensagens entre servidores de e-mail", "D) Realizando transferência de arquivos em modo passivo", "E) Nenhuma das opções"], "resposta": "C) Transferindo mensagens entre servidores de e-mail"},

                     {"pergunta": "Qual é a porta padrão associada ao SMTP?", "alternativas": ["A) 20", "B) 22", "C) 23", "D) 25", "E) Nenhuma das opções"], "resposta": "D) 25"},

                     {"pergunta": "Por que a criptografia através do STARTTLS ou TLS tem se tornado mais comum no SMTP?", "alternativas": ["A) Para melhorar a eficiência da comunicação", "B) Para garantir a segurança das mensagens de e-mail", "C) Para permitir a transferência de arquivos em modo passivo", "D) Para suportar a transferência de mensagens em modo ativo", "E) Nenhuma das opções"], "resposta": "B) Para garantir a segurança das mensagens de e-mail"},

                     {"pergunta": "Além da porta 25, qual outra porta está associada ao SMTP?", "alternativas": ["A) 53", "B) 67", "C) 110", "D) 587", "E) Nenhuma das opções"], "resposta": "D) 587"},

                     {"pergunta": "O que é STARTTLS no contexto do SMTP?", "alternativas": ["A) Um protocolo de transferência de arquivos seguro", "B) Uma técnica de criptografia para comunicações SMTP", "C) Um método de autenticação forte", "D) Um protocolo de comunicação para redes locais", "E) Nenhuma das opções"], "resposta": "B) Uma técnica de criptografia para comunicações SMTP"},

                     {"pergunta": "Qual é o principal propósito do STARTTLS no SMTP?", "alternativas": ["A) Facilitar a transferência de arquivos", "B) Criptografar as comunicações SMTP", "C) Autenticar os usuários do sistema", "D) Suportar a transferência de dados em modo passivo", "E) Nenhuma das opções"], "resposta": "B) Criptografar as comunicações SMTP"},

                     {"pergunta": "Por que a porta 465 está sendo desencorajada em favor da porta 587 no contexto do SMTP?", "alternativas": ["A) Devido a problemas de eficiência", "B) Para melhorar a segurança das comunicações", "C) Por ser uma porta reservada para outros serviços", "D) Por questões de compatibilidade com firewalls", "E) Nenhuma das opções"], "resposta": "B) Para melhorar a segurança das comunicações"},

                     {"pergunta": "Qual protocolo mais seguro tem sido uma opção mais confiável para acessar sistemas remotos de forma segura em comparação com o SMTP?", "alternativas": ["A) Telnet", "B) SSH", "C) FTP", "D) SFTP", "E) Nenhuma das opções"], "resposta": "B) SSH"},

                     {"pergunta": "O que significa a sigla TFTP?", "alternativas": ["A) Trivial File Transfer Protocol", "B) Transfer File Transmission Protocol", "C) Total File Transfer Protocol", "D) Terminal File Transmission Protocol", "E) Nenhuma das opções"], "resposta": "A) Trivial File Transfer Protocol"},

                     {"pergunta": "Qual é o propósito principal do TFTP?", "alternativas": ["A) Transferência de arquivos de forma segura", "B) Transferência de grandes volumes de dados", "C) Transferência rápida de arquivos de configuração ou firmware", "D) Autenticação segura entre dispositivos", "E) Nenhuma das opções"], "resposta": "C) Transferência rápida de arquivos de configuração ou firmware"},

                     {"pergunta": "Como o TFTP trabalha na transferência de arquivos?", "alternativas": ["A) Utilizando pacotes de dados TCP", "B) Utilizando pacotes de dados UDP", "C) Estabelecendo conexões seguras", "D) Transferindo arquivos em modo passivo", "E) Nenhuma das opções"], "resposta": "B) Utilizando pacotes de dados UDP"},

                     {"pergunta": "Quais são as características de segurança do TFTP por padrão?", "alternativas": ["A) Criptografia e autenticação embutidas", "B) Ausência de recursos de segurança embutidos", "C) Utilização exclusiva de conexões seguras", "D) Autenticação baseada em chaves", "E) Nenhuma das opções"], "resposta": "B) Ausência de recursos de segurança embutidos"},

                     {"pergunta": "Em que situações o TFTP é frequentemente utilizado?", "alternativas": ["A) Transferência de arquivos grandes", "B) Atualização de firmware em dispositivos de rede", "C) Transferência segura de arquivos", "D) Compartilhamento de arquivos em redes locais", "E) Nenhuma das opções"], "resposta": "B) Atualização de firmware em dispositivos de rede"},

                     {"pergunta": "O que é TFTP seguro (TFTP over SSH)?", "alternativas": ["A) Uma versão mais rápida do TFTP", "B) Uma versão com criptografia e autenticação", "C) Uma versão exclusiva para grandes volumes de dados", "D) Uma versão para transferência de arquivos em modo ativo", "E) Nenhuma das opções"], "resposta": "B) Uma versão com criptografia e autenticação"},

                     {"pergunta": "Por que é importante adicionar camadas extras de segurança, como TFTP seguro, em algumas implementações do TFTP?", "alternativas": ["A) Para melhorar a eficiência da transferência de arquivos", "B) Para garantir a transferência de arquivos grandes", "C) Para adicionar autenticação e criptografia", "D) Para suportar conexões seguras em modo ativo", "E) Nenhuma das opções"], "resposta": "C) Para adicionar autenticação e criptografia"},

                     {"pergunta": "Qual é a principal diferença entre o TFTP e o FTP em termos de recursos?", "alternativas": ["A) TFTP oferece recursos mais avançados", "B) FTP é mais leve e rápido", "C) TFTP é baseado em texto, enquanto o FTP utiliza criptografia", "D) FTP oferece autenticação embutida", "E) Nenhuma das opções"], "resposta": "C) TFTP é baseado em texto, enquanto o FTP utiliza criptografia"},

                     {"pergunta": "Quais são as principais limitações do TFTP?", "alternativas": ["A) Ausência de limitações", "B) Falta de suporte para grandes volumes de dados", "C) Inexistência de problemas de segurança", "D) Suporte exclusivo para transferência de arquivos grandes", "E) Nenhuma das opções"], "resposta": "B) Falta de suporte para grandes volumes de dados"},

                     {"pergunta": "O que é comum em situações de inicialização de dispositivos de rede, onde o TFTP é frequentemente utilizado?", "alternativas": ["A) Transferência de arquivos grandes", "B) Transferência rápida de arquivos de configuração iniciais", "C) Utilização de protocolos de criptografia", "D) Ausência de necessidade de atualização de firmware", "E) Nenhuma das opções"], "resposta": "B) Transferência rápida de arquivos de configuração iniciais"},

                     {"pergunta": "Qual é a principal função do protocolo Finger?", "alternativas": ["A) Transferência de arquivos", "B) Obter informações sobre usuários conectados", "C) Envio seguro de e-mails", "D) Autenticação em redes locais", "E) Nenhuma das opções"], "resposta": "B) Obter informações sobre usuários conectados"},

                     {"pergunta": "O que acontece quando um cliente envia uma solicitação Finger para um servidor?", "alternativas": ["A) O servidor envia e-mails ao cliente", "B) O servidor processa a solicitação e envia informações sobre usuários conectados", "C) O servidor estabelece uma conexão segura com o cliente", "D) O cliente envia informações sobre usuários para o servidor", "E) Nenhuma das opções"], "resposta": "B) O servidor processa a solicitação e envia informações sobre usuários conectados"},

                     {"pergunta": "O que o protocolo Finger responde quando um cliente faz uma solicitação?", "alternativas": ["A) Status de transferência de arquivos", "B) Informações sobre usuários conectados ao sistema", "C) Confirmação de envio de e-mails", "D) Dados criptografados sobre usuários", "E) Nenhuma das opções"], "resposta": "B) Informações sobre usuários conectados ao sistema"},

                     {"pergunta": "Por que o protocolo Finger foi descontinuado em muitos sistemas e redes?", "alternativas": ["A) Devido à falta de recursos avançados", "B) Devido a preocupações com privacidade e segurança", "C) Devido à ausência de funcionalidades úteis", "D) Devido a problemas de transferência de arquivos", "E) Nenhuma das opções"], "resposta": "B) Devido a preocupações com privacidade e segurança"},

                     {"pergunta": "Qual é uma alternativa mais segura ao protocolo Finger para obter informações sobre usuários em sistemas modernos?", "alternativas": ["A) Protocolo Telnet", "B) Protocolo FTP", "C) Serviços de diretório baseados em LDAP", "D) Transferência segura de arquivos", "E) Nenhuma das opções"], "resposta": "C) Serviços de diretório baseados em LDAP"},

                     {"pergunta": "O que o protocolo Finger não inclui por padrão, levando a preocupações de segurança?", "alternativas": ["A) Criptografia e autenticação", "B) Transferência rápida de arquivos", "C) Sincronização de pastas", "D) Conexões seguras por padrão", "E) Nenhuma das opções"], "resposta": "A) Criptografia e autenticação"},

                     {"pergunta": "Quando o cliente envia uma solicitação Finger, as informações sobre os usuários são transmitidas de forma criptografada?", "alternativas": ["A) Sim, por padrão", "B) Não, por padrão", "C) Somente se o servidor suportar", "D) Apenas em redes locais", "E) Nenhuma das opções"], "resposta": "B) Não, por padrão"},

                     {"pergunta": "O que o servidor Finger geralmente fornece em sua resposta?", "alternativas": ["A) Status de transferência de arquivos", "B) Informações sobre usuários conectados e seus detalhes", "C) Criptografia de dados", "D) Configurações de rede", "E) Nenhuma das opções"], "resposta": "B) Informações sobre usuários conectados e seus detalhes"},

                     {"pergunta": "Por que muitos administradores de sistemas optaram por desabilitar ou restringir a funcionalidade do Finger?", "alternativas": ["A) Devido a problemas de desempenho", "B) Devido a problemas de transferência de arquivos", "C) Para proteger a privacidade e segurança dos usuários", "D) Porque o Finger não é mais suportado", "E) Nenhuma das opções"], "resposta": "C) Para proteger a privacidade e segurança dos usuários"},

                     {"pergunta": "Qual é a principal diferença entre o protocolo Finger e serviços modernos de gerenciamento de usuários?", "alternativas": ["A) Finger oferece criptografia", "B) Serviços modernos utilizam FTP", "C) Serviços modernos utilizam LDAP e têm foco em segurança", "D) Finger é mais rápido", "E) Nenhuma das opções"], "resposta": "C) Serviços modernos utilizam LDAP e têm foco em segurança"},

                     {"pergunta": "O que significa a sigla HTTP?", "alternativas": ["A) Hypertext Transfer Protocol", "B) High Transfer Protocol", "C) Hyperlink Transmission Protocol", "D) Host Transfer Protocol", "E) Nenhuma das opções"], "resposta": "A) Hypertext Transfer Protocol"},

                     {"pergunta": "Qual é a porta padrão associada ao serviço HTTP?", "alternativas": ["A) 80", "B) 443", "C) 23", "D) 25", "E) Nenhuma das opções"], "resposta": "A) 80"},

                     {"pergunta": "O que o HTTP permite realizar na World Wide Web?", "alternativas": ["A) Transferência segura de arquivos", "B) Envio de e-mails", "C) Transferência de grandes volumes de dados", "D) Transferência de dados na World Wide Web", "E) Nenhuma das opções"], "resposta": "D) Transferência de dados na World Wide Web"},

                     {"pergunta": "Quando você digita um endereço de site no navegador, qual protocolo é utilizado por padrão?", "alternativas": ["A) HTTPS", "B) FTP", "C) HTTP", "D) Telnet", "E) Nenhuma das opções"], "resposta": "C) HTTP"},

                     {"pergunta": "O que a solicitação HTTP contém?", "alternativas": ["A) Conteúdo da página", "B) Informações sobre a transferência de arquivos", "C) Tipo de ação desejada e outros cabeçalhos", "D) Dados criptografados", "E) Nenhuma das opções"], "resposta": "C) Tipo de ação desejada e outros cabeçalhos"},

                     {"pergunta": "Como o servidor web responde à solicitação HTTP?", "alternativas": ["A) Enviando e-mails", "B) Enviando uma resposta HTTP com o status da solicitação", "C) Transferindo grandes volumes de dados", "D) Conectando-se ao servidor FTP", "E) Nenhuma das opções"], "resposta": "B) Enviando uma resposta HTTP com o status da solicitação"},

                     {"pergunta": "Além da porta 80, em que situações o HTTP pode ser usado com outras portas?", "alternativas": ["A) Nunca pode ser usado com outras portas", "B) Em situações de transferência segura de arquivos", "C) Quando a porta 80 está ocupada", "D) HTTPS utiliza a porta 443", "E) Nenhuma das opções"], "resposta": "D) HTTPS utiliza a porta 443"},

                     {"pergunta": "O que é o HTTPS e qual é sua principal diferença em relação ao HTTP?", "alternativas": ["A) Hypertext Transfer Protocol Secure; utiliza uma porta diferente", "B) HTTP Secure; utiliza a mesma porta do HTTP", "C) Host Transfer Protocol Secure; utiliza a porta 80", "D) High Transfer Protocol Secure; não utiliza criptografia", "E) Nenhuma das opções"], "resposta": "A) Hypertext Transfer Protocol Secure; utiliza uma porta diferente"},

                     {"pergunta": "Qual é a função principal do HTTP em uma transação na Web?", "alternativas": ["A) Transferência de arquivos grandes", "B) Envio de e-mails", "C) Transferência de dados entre navegadores e servidores web", "D) Conexão segura entre servidores", "E) Nenhuma das opções"], "resposta": "C) Transferência de dados entre navegadores e servidores web"},

                     {"pergunta": "Por que o HTTP é considerado um protocolo baseado em texto?", "alternativas": ["A) Porque transfere apenas texto sem formatação", "B) Porque utiliza apenas caracteres alfanuméricos", "C) Porque as solicitações e respostas são enviadas em formato legível por humanos", "D) Porque é um protocolo mais lento", "E) Nenhuma das opções"], "resposta": "C) Porque as solicitações e respostas são enviadas em formato legível por humanos"},

                     {"pergunta": "O que significa a sigla POP?", "alternativas": ["A) Post Office Protocol", "B) Power Over Protocol", "C) Personal Operating Protocol", "D) Public Online Protocol", "E) Nenhuma das opções"], "resposta": "A) Post Office Protocol"},

                     {"pergunta": "Qual é a porta padrão associada ao serviço POP?", "alternativas": ["A) 25", "B) 80", "C) 110", "D) 143", "E) Nenhuma das opções"], "resposta": "C) 110"},

                     {"pergunta": "O que o POP permite realizar em relação aos e-mails?", "alternativas": ["A) Envio de e-mails", "B) Transferência segura de arquivos", "C) Download de e-mails do servidor para o cliente de e-mail", "D) Compartilhamento de pastas", "E) Nenhuma das opções"], "resposta": "C) Download de e-mails do servidor para o cliente de e-mail"},

                     {"pergunta": "Quando um cliente de e-mail se conecta ao servidor POP, o que acontece?", "alternativas": ["A) O servidor envia e-mails ao cliente", "B) O cliente envia uma solicitação para enviar e-mails", "C) O cliente envia uma solicitação para baixar e-mails", "D) O servidor envia uma solicitação para o cliente", "E) Nenhuma das opções"], "resposta": "C) O cliente envia uma solicitação para baixar e-mails"},

                     {"pergunta": "Qual é uma característica importante do POP em relação ao armazenamento de e-mails?", "alternativas": ["A) Mantém os e-mails no servidor após o download", "B) Remove os e-mails do servidor após o download", "C) Envia cópias dos e-mails para o servidor", "D) Usa a porta 143 para comunicação", "E) Nenhuma das opções"], "resposta": "B) Remove os e-mails do servidor após o download"},

                     {"pergunta": "O que significa POP3, uma variante do protocolo POP?", "alternativas": ["A) Protocol Over Port 3", "B) Post Office Protocol 3", "C) Power Online Protocol 3", "D) Personal Operating Protocol 3", "E) Nenhuma das opções"], "resposta": "B) Post Office Protocol 3"},

                     {"pergunta": "O que o POP3 permite em relação ao armazenamento de e-mails no servidor?", "alternativas": ["A) Manter uma cópia dos e-mails no servidor", "B) Remover os e-mails do servidor após o download", "C) Enviar e-mails ao servidor", "D) Utilizar a porta 80 para comunicação", "E) Nenhuma das opções"], "resposta": "B) Remover os e-mails do servidor após o download"},

                     {"pergunta": "Por que o POP é considerado mais adequado para situações em que os e-mails precisam ser armazenados localmente?", "alternativas": ["A) Porque utiliza criptografia por padrão", "B) Porque mantém os e-mails no servidor após o download", "C) Porque remove os e-mails do servidor após o download", "D) Porque utiliza a porta 143", "E) Nenhuma das opções"], "resposta": "C) Porque remove os e-mails do servidor após o download"},

                     {"pergunta": "O que é o protocolo IMAP e como ele se diferencia do protocolo POP?", "alternativas": ["A) Internet Message Access Protocol; utiliza a porta 80", "B) Internet Mail and Authentication Protocol; utiliza a porta 110", "C) Internet Message Access Protocol; permite acessar e-mails diretamente no servidor", "D) Internet Mail Protocol; remove os e-mails do servidor após o download", "E) Nenhuma das opções"], "resposta": "C) Internet Message Access Protocol; permite acessar e-mails diretamente no servidor"},

                     {"pergunta": "Qual é a principal desvantagem do protocolo POP em comparação com o protocolo IMAP?", "alternativas": ["A) POP permite o acesso direto aos e-mails no servidor", "B) IMAP remove os e-mails do servidor após o download", "C) POP não oferece criptografia", "D) IMAP não permite o download de e-mails para o cliente", "E) Nenhuma das opções"], "resposta": "C) POP não oferece criptografia"},

                     {"pergunta": "O que significa a sigla NTP?", "alternativas": ["A) Network Transfer Protocol", "B) National Time Protocol", "C) Network Time Protocol", "D) National Transfer Protocol", "E) Nenhuma das opções"], "resposta": "C) Network Time Protocol"},

                     {"pergunta": "Qual é a porta padrão associada ao serviço NTP?", "alternativas": ["A) 25", "B) 80", "C) 110", "D) 123", "E) Nenhuma das opções"], "resposta": "D) 123"},

                     {"pergunta": "O que o NTP busca garantir em uma rede?", "alternativas": ["A) Largura de banda", "B) Sincronização precisa dos relógios dos dispositivos", "C) Segurança dos dados", "D) Conexões seguras", "E) Nenhuma das opções"], "resposta": "B) Sincronização precisa dos relógios dos dispositivos"},

                     {"pergunta": "Como o NTP compensa a latência e a variação na rede?", "alternativas": ["A) Utilizando criptografia", "B) Utilizando algoritmos sofisticados", "C) Removendo os e-mails do servidor após o download", "D) Utilizando a porta 143", "E) Nenhuma das opções"], "resposta": "B) Utilizando algoritmos sofisticados"},

                     {"pergunta": "Além da sincronização de relógios, o que mais o NTP oferece?", "alternativas": ["A) Autenticação", "B) Download de arquivos", "C) Compartilhamento de pastas", "D) Transferência segura de dados", "E) Nenhuma das opções"], "resposta": "A) Autenticação"},

                     {"pergunta": "Qual é a importância da sincronização precisa do tempo em uma rede?", "alternativas": ["A) Aumenta a largura de banda", "B) Facilita a transferência de arquivos", "C) Permite o funcionamento adequado de diversas aplicações e serviços", "D) Utiliza a porta 25 para comunicação", "E) Nenhuma das opções"], "resposta": "C) Permite o funcionamento adequado de diversas aplicações e serviços"},

                     {"pergunta": "O que é a versão NTPv4?", "alternativas": ["A) Uma variante do SNMP", "B) Uma versão do protocolo POP", "C) Uma versão do protocolo NTP", "D) Uma versão do protocolo TFTP", "E) Nenhuma das opções"], "resposta": "C) Uma versão do protocolo NTP"},

                     {"pergunta": "Além do NTP, qual é outra versão relacionada do protocolo?", "alternativas": ["A) IMAP", "B) SNMP", "C) POP", "D) HTTPS", "E) Nenhuma das opções"], "resposta": "B) SNMP"},

                     {"pergunta": "O que é o SNTP, relacionado ao NTP?", "alternativas": ["A) Uma versão simplificada do NTP", "B) Uma versão segura do NTP", "C) Uma variante do SNMP", "D) Uma variante do POP", "E) Nenhuma das opções"], "resposta": "A) Uma versão simplificada do NTP"},

                     {"pergunta": "Qual é o objetivo principal do SNTP?", "alternativas": ["A) Sincronização de relógios", "B) Transferência segura de dados", "C) Monitoramento de rede", "D) Acesso a e-mails", "E) Nenhuma das opções"], "resposta": "A) Sincronização de relógios"},

                     {"pergunta": "O que significa a sigla SNMP?", "alternativas": ["A) Simple Network Management Protocol", "B) Secure Network Messaging Protocol", "C) System Network Monitoring Protocol", "D) Simple Notification Messaging Protocol", "E) Nenhuma das opções"], "resposta": "A) Simple Network Management Protocol"},

                     {"pergunta": "Qual é a porta padrão associada ao serviço SNMP?", "alternativas": ["A) 25", "B) 80", "C) 110", "D) 161", "E) Nenhuma das opções"], "resposta": "D) 161"},

                     {"pergunta": "Qual é a principal função do SNMP?", "alternativas": ["A) Transferência de arquivos", "B) Sincronização de relógios", "C) Monitorar e gerenciar dispositivos em uma rede", "D) Acesso a e-mails", "E) Nenhuma das opções"], "resposta": "C) Monitorar e gerenciar dispositivos em uma rede"},

                     {"pergunta": "Quando um dispositivo de rede está configurado para suportar o SNMP, em qual porta ele escuta para receber solicitações de gerenciamento?", "alternativas": ["A) 25", "B) 80", "C) 110", "D) 161", "E) Nenhuma das opções"], "resposta": "D) 161"},

                     {"pergunta": "O que são os gerentes de rede no contexto do SNMP?", "alternativas": ["A) Dispositivos gerenciados", "B) Protocolos de rede", "C) Computadores ou servidores que enviam solicitações SNMP", "D) Dispositivos que enviam notificações SNMP Trap", "E) Nenhuma das opções"], "resposta": "C) Computadores ou servidores que enviam solicitações SNMP"},

                     {"pergunta": "O SNMP é baseado em qual arquitetura?", "alternativas": ["A) Arquitetura ponto a ponto", "B) Arquitetura cliente-servidor", "C) Arquitetura de comutação", "D) Arquitetura de hub", "E) Nenhuma das opções"], "resposta": "B) Arquitetura cliente-servidor"},

                     {"pergunta": "O que é a MIB no contexto do SNMP?", "alternativas": ["A) Um tipo de arquivo de configuração", "B) Uma linguagem de programação", "C) Um objeto gerenciado", "D) Uma estrutura de gerenciamento de informações", "E) Nenhuma das opções"], "resposta": "D) Uma estrutura de gerenciamento de informações"},

                     {"pergunta": "Qual é a finalidade da MIB?", "alternativas": ["A) Acesso à internet", "B) Definir objetos gerenciados e informações disponíveis para monitoramento e configuração", "C) Transferência de arquivos", "D) Estabelecer conexões seguras", "E) Nenhuma das opções"], "resposta": "B) Definir objetos gerenciados e informações disponíveis para monitoramento e configuração"},

                     {"pergunta": "O SNMP oferece suporte a diferentes versões. Qual é uma dessas versões?", "alternativas": ["A) SNMPv1", "B) SNMPv2", "C) SNMPv3", "D) Todas as opções estão corretas", "E) Nenhuma das opções"], "resposta": "D) Todas as opções estão corretas"},

                     {"pergunta": "O que é o SNMP Trap?", "alternativas": ["A) Um tipo de isca para capturar informações de rede", "B) Uma função do SNMP que permite a execução de ações proativas em dispositivos gerenciados", "C) Uma versão mais antiga do SNMP", "D) Uma armadilha para hackers", "E) Nenhuma das opções"], "resposta": "B) Uma função do SNMP que permite a execução de ações proativas em dispositivos gerenciados"},

                     {"pergunta": "O que significa a sigla HTTPS?", "alternativas": ["A) Hypertext Transfer Protocol Secure", "B) High Transmission Performance Service", "C) Home Text Processing Service", "D) Hyperlink and Text Transfer System", "E) Nenhuma das opções"], "resposta": "A) Hypertext Transfer Protocol Secure"},

                     {"pergunta": "Qual é a porta padrão associada ao serviço HTTPS?", "alternativas": ["A) 25", "B) 80", "C) 110", "D) 443", "E) Nenhuma das opções"], "resposta": "D) 443"},

                     {"pergunta": "O que o HTTPS utiliza para proteger a confidencialidade dos dados transmitidos entre o navegador e o servidor?", "alternativas": ["A) Criptografia", "B) Compressão", "C) Redes privadas virtuais", "D) Protocolo IPsec", "E) Nenhuma das opções"], "resposta": "A) Criptografia"},

                     {"pergunta": "Qual protocolo o HTTPS utiliza para estabelecer uma conexão segura entre o cliente e o servidor?", "alternativas": ["A) HTTP", "B) FTP", "C) SSL/TLS", "D) SNMP", "E) Nenhuma das opções"], "resposta": "C) SSL/TLS"},

                     {"pergunta": "O que acontece quando um navegador acessa um site que utiliza HTTPS?", "alternativas": ["A) A conexão não é criptografada", "B) A conexão é criptografada usando SSL/TLS", "C) A conexão é criptografada usando FTP", "D) A conexão é criptografada usando SNMP", "E) Nenhuma das opções"], "resposta": "B) A conexão é criptografada usando SSL/TLS"},

                     {"pergunta": "Por que o HTTPS é amplamente utilizado em sites que envolvem transações financeiras?", "alternativas": ["A) Porque é mais rápido que o HTTP", "B) Porque é mais fácil de configurar", "C) Porque é mais barato", "D) Porque protege a confidencialidade dos dados transmitidos", "E) Nenhuma das opções"], "resposta": "D) Porque protege a confidencialidade dos dados transmitidos"},

                     {"pergunta": "O que acontece após a conexão segura ser estabelecida no HTTPS?", "alternativas": ["A) Os dados são transmitidos em formato de texto simples", "B) Os dados são transmitidos sem criptografia", "C) Os dados são transmitidos em formato criptografado", "D) Os dados são comprimidos antes de serem transmitidos", "E) Nenhuma das opções"], "resposta": "C) Os dados são transmitidos em formato criptografado"},

                     {"pergunta": "Qual é a principal vantagem do HTTPS em relação ao HTTP?", "alternativas": ["A) Velocidade de transferência", "B) Facilidade de implementação", "C) Segurança na transmissão de dados", "D) Compatibilidade com todos os navegadores", "E) Nenhuma das opções"], "resposta": "C) Segurança na transmissão de dados"},

                     {"pergunta": "O que o uso do HTTPS ajuda a proteger contra?", "alternativas": ["A) Ataques de força bruta", "B) Interceptação de dados por terceiros", "C) Vírus no servidor", "D) Ataques de negação de serviço", "E) Nenhuma das opções"], "resposta": "B) Interceptação de dados por terceiros"},

                     {"pergunta": "Qual a importância da adoção do HTTPS para a classificação nos resultados de pesquisa?", "alternativas": ["A) Não afeta a classificação nos resultados de pesquisa", "B) Ajuda a melhorar a classificação nos resultados de pesquisa", "C) Piora a classificação nos resultados de pesquisa", "D) Não há relação entre HTTPS e classificação nos resultados de pesquisa", "E) Nenhuma das opções"], "resposta": "B) Ajuda a melhorar a classificação nos resultados de pesquisa"},

                     {"pergunta": "O que significa a sigla OSINT?", "alternativas": ["A) Open Source Information Technology", "B) Operational Security and Intelligence", "C) Open Source Intelligence", "D) Online Security Investigation Network", "E) Nenhuma das opções"], "resposta": "C) Open Source Intelligence"},

                    {"pergunta": "Quais são algumas das fontes públicas utilizadas no OSINT?", "alternativas": ["A) Apenas redes sociais", "B) Apenas sites de busca", "C) Redes sociais, blogs, fóruns, deep web, jornais, revistas, televisão, eventos, conferências, entre outros", "D) Apenas jornais e revistas", "E) Nenhuma das opções"], "resposta": "C) Redes sociais, blogs, fóruns, deep web, jornais, revistas, televisão, eventos, conferências, entre outros"},

                    {"pergunta": "O que são rastros na Internet no contexto do OSINT?", "alternativas": ["A) Impressões digitais digitais", "B) Pegadas deixadas por animais selvagens", "C) Informações encontradas em sites de busca", "D) Ações realizadas na Internet que geram registros", "E) Nenhuma das opções"], "resposta": "D) Ações realizadas na Internet que geram registros"},

                    {"pergunta": "Mesmo desativando cookies ou JavaScript, por que ainda é possível ser rastreado na Internet?", "alternativas": ["A) Porque os navegadores não coletam informações", "B) Porque os sites não realizam rastreamento", "C) Porque os rastros são como impressões digitais e podem ser coletados de outras maneiras", "D) Porque a Internet é totalmente anônima", "E) Nenhuma das opções"], "resposta": "C) Porque os rastros são como impressões digitais e podem ser coletados de outras maneiras"},

                    {"pergunta": "Quais são os passos a serem realizados no OSINT?", "alternativas": ["A) Coleta de dados, análise de dados, conclusão de dados", "B) Coleta de dados, processamento de informações, conclusão das informações", "C) Coleta de fontes para busca, coleta de dados, processamento das informações, análise das informações, conclusão das informações", "D) Análise de informações, coleta de dados, conclusão de dados", "E) Nenhuma das opções"], "resposta": "C) Coleta de fontes para busca, coleta de dados, processamento das informações, análise das informações, conclusão das informações"},

                    {"pergunta": "O que é Google Hacking no contexto do OSINT?", "alternativas": ["A) Ataque ao sistema do Google", "B) Uso de pesquisas no Google e informações públicas a favor do usuário", "C) Manipulação de resultados de busca no Google", "D) Hacking do motor de busca do Google", "E) Nenhuma das opções"], "resposta": "B) Uso de pesquisas no Google e informações públicas a favor do usuário"},

                    {"pergunta": "Quais são alguns dos comandos mais utilizados no Google Hacking?", "alternativas": ["A) search=, list=, find=", "B) info=, browse=, locate=", "C) intitle=, inurl=, filetype=", "D) research=, query=, discover=", "E) Nenhuma das opções"], "resposta": "C) intitle=, inurl=, filetype="},

                    {"pergunta": "O que o Shodan busca na Internet?", "alternativas": ["A) Páginas da web", "B) Dispositivos conectados na Internet", "C) Imagens online", "D) Vídeos públicos", "E) Nenhuma das opções"], "resposta": "B) Dispositivos conectados na Internet"},

                    {"pergunta": "Além de dispositivos conectados, o que o Shodan fornece detalhes sobre?", "alternativas": ["A) Informações meteorológicas", "B) Aplicações vulneráveis/desatualizadas em servidores", "C) Receitas de culinária", "D) Histórico de navegação", "E) Nenhuma das opções"], "resposta": "B) Aplicações vulneráveis/desatualizadas em servidores"},

                    {"pergunta": "O que significa a sigla NMAP?", "alternativas": ["A) Network Management and Protocol", "B) Network Mapper", "C) Network Monitoring and Analysis Program", "D) Network Masking and Processing", "E) Nenhuma das opções"], "resposta": "B) Network Mapper"},

                    {"pergunta": "Como o endereço IP é representado no IPv4?", "alternativas": ["A) 64 bits", "B) 32 bits", "C) 16 bits", "D) 128 bits", "E) Nenhuma das opções"], "resposta": "B) 32 bits"},

                    {"pergunta": "Quantos octetos compõem um endereço IP no IPv4?", "alternativas": ["A) Dois octetos", "B) Três octetos", "C) Quatro octetos", "D) Cinco octetos", "E) Nenhuma das opções"], "resposta": "C) Quatro octetos"},

                    {"pergunta": "Como são representados os octetos em um endereço IP?", "alternativas": ["A) Números binários", "B) Números hexadecimais", "C) Números decimais de 0 a 255", "D) Números decimais de 0 a 127", "E) Nenhuma das opções"], "resposta": "C) Números decimais de 0 a 255"},

                    {"pergunta": "O que a máscara de sub-rede define em um endereço IP?", "alternativas": ["A) Identifica o país", "B) Identifica o host", "C) Identifica a rede", "D) Identifica a versão do protocolo", "E) Nenhuma das opções"], "resposta": "C) Identifica a rede"},

                    {"pergunta": "Como a máscara de sub-rede é representada?", "alternativas": ["A) Dois números decimais", "B) Um número decimal", "C) Quatro números decimais", "D) Números hexadecimais", "E) Nenhuma das opções"], "resposta": "C) Quatro números decimais"},

                    {"pergunta": "O que os bits '1' na máscara de sub-rede identificam?", "alternativas": ["A) A parte da rede", "B) A parte do host", "C) A parte do país", "D) A parte da cidade", "E) Nenhuma das opções"], "resposta": "A) A parte da rede"},

                    {"pergunta": "Qual é a principal diferença entre IP Público e IP Privado?", "alternativas": ["A) A cor", "B) A localização geográfica", "C) A classe de endereçamento", "D) A roteabilidade na Internet", "E) Nenhuma das opções"], "resposta": "D) A roteabilidade na Internet"},

                    {"pergunta": "O que são endereços IP privados utilizados para?", "alternativas": ["A) Acesso direto pela Internet", "B) Roteabilidade na Internet", "C) Uso interno em redes locais", "D) Acesso por qualquer dispositivo", "E) Nenhuma das opções"], "resposta": "C) Uso interno em redes locais"},

                    {"pergunta": "Quantos octetos são utilizados para identificar a rede na Classe A de endereçamento IP?", "alternativas": ["A) Um octeto", "B) Dois octetos", "C) Três octetos", "D) Quatro octetos", "E) Nenhuma das opções"], "resposta": "A) Um octeto"},

                    {"pergunta": "O que a notação CIDR representa em um endereço IP, por exemplo, 192.168.1.0/24?", "alternativas": ["A) A cidade do IP", "B) O país do IP", "C) O tamanho da rede e dos hosts", "D) A versão do protocolo IP", "E) Nenhuma das opções"], "resposta": "C) O tamanho da rede e dos hosts"},

                    {"pergunta": "Qual é a função principal do NMAP?", "alternativas": ["A) Gerenciamento de rede", "B) Mapeamento de rede", "C) Análise de tráfego", "D) Encriptação de dados", "E) Nenhuma das opções"], "resposta": "B) Mapeamento de rede"},

                    {"pergunta": "Como o NMAP identifica dispositivos em uma rede?", "alternativas": ["A) Enviando pacotes ICMP", "B) Rastreando registros DNS", "C) Analisando logs do servidor", "D) Enviando solicitações HTTP", "E) Nenhuma das opções"], "resposta": "A) Enviando pacotes ICMP"},

                    {"pergunta": "O que significa a sigla CIDR?", "alternativas": ["A) Configuração de Roteador Dinâmico de IP", "B) Controle de Identificação de Dispositivos Roteados", "C) Configuração de Intervalo Dinâmico de Rede", "D) Roteamento de Colapso de Identificadores de Destino", "E) Nenhuma das opções"], "resposta": "C) Configuração de Intervalo Dinâmico de Rede"},

                    {"pergunta": "Qual é a principal função das máscaras de sub-rede?", "alternativas": ["A) Criptografar o tráfego de rede", "B) Identificar dispositivos na rede", "C) Definir a faixa de endereços disponíveis", "D) Gerenciar servidores DNS", "E) Nenhuma das opções"], "resposta": "C) Definir a faixa de endereços disponíveis"},

                    {"pergunta": "O que são classes de endereçamento IP e qual é o propósito delas?", "alternativas": ["A) São grupos de dispositivos com IPs semelhantes", "B) São faixas de IPs reservadas para fins específicos", "C) São níveis de qualidade de serviço para IPs", "D) São categorias de IPs baseadas em localização geográfica", "E) Nenhuma das opções"], "resposta": "B) São faixas de IPs reservadas para fins específicos"},

                    {"pergunta": "Quantos bits são utilizados para representar um octeto em um endereço IP?", "alternativas": ["A) 4 bits", "B) 8 bits", "C) 16 bits", "D) 32 bits", "E) Nenhuma das opções"], "resposta": "B) 8 bits"},

                    {"pergunta": "O que é um IP Público?", "alternativas": ["A) Um endereço IP reservado para uso interno", "B) Um endereço IP roteável na Internet", "C) Um endereço IP utilizado apenas para servidores DNS", "D) Um endereço IP comum em redes domésticas", "E) Nenhuma das opções"], "resposta": "B) Um endereço IP roteável na Internet"},

                    {"pergunta": "Quais são os comandos mais utilizados no Google Hacking?", "alternativas": ["A) copy, paste, delete", "B) intitle, inurl, filetype", "C) search, browse, download", "D) encrypt, decrypt, authenticate", "E) Nenhuma das opções"], "resposta": "B) intitle, inurl, filetype"},

                    {"pergunta": "Qual é a principal função do Shodan?", "alternativas": ["A) Buscar dispositivos conectados na Internet", "B) Criar redes privadas virtuais", "C) Analisar tráfego de rede", "D) Gerenciar servidores de e-mail", "E) Nenhuma das opções"], "resposta": "A) Buscar dispositivos conectados na Internet"},

                    {"pergunta": "O que o Maltego permite buscar?", "alternativas": ["A) Receitas de culinária", "B) Informações sobre domínios, pessoas, emails, endereços, etc.", "C) Notícias de última hora", "D) Jogos online", "E) Nenhuma das opções"], "resposta": "B) Informações sobre domínios, pessoas, emails, endereços, etc."},

                    {"pergunta": "O que é o NMAP e qual é sua finalidade?", "alternativas": ["A) Um sistema operacional", "B) Uma linguagem de programação", "C) Uma ferramenta para varredura de rede", "D) Um tipo de firewall", "E) Nenhuma das opções"], "resposta": "C) Uma ferramenta para varredura de rede"},

                    {"pergunta": "Quais são os tipos de scan do NMAP mencionados?", "alternativas": ["A) sS / sT / sA / sW / sM", "B) sU", "C) sN / sF / sX", "D) Todas as opções acima", "E) Nenhuma das opções"], "resposta": "D) Todas as opções acima"},

                    {"pergunta": "Qual é a finalidade do parâmetro -v no NMAP?", "alternativas": ["A) Ocultar a saída do comando", "B) Exibir todas as informações durante a análise", "C) Redefinir o host", "D) Desativar o scan SYN", "E) Nenhuma das opções"], "resposta": "B) Exibir todas as informações durante a análise"},

                    {"pergunta": "Para que serve o parâmetro -sn no NMAP?", "alternativas": ["A) Encontrar hosts ativos na rede", "B) Definir a faixa de máscara de redes", "C) Fechar portas abertas", "D) Analisar tráfego UDP", "E) Nenhuma das opções"], "resposta": "A) Encontrar hosts ativos na rede"},

                    {"pergunta": "Como é possível facilitar as pesquisas de hosts ativos usando o NMAP?", "alternativas": ["A) Aumentando a faixa de máscara de redes", "B) Utilizando o parâmetro -p", "C) Desativando o scan UDP", "D) Ocultando informações durante a análise", "E) Nenhuma das opções"], "resposta": "A) Aumentando a faixa de máscara de redes"},

                    {"pergunta": "Qual é a função do parâmetro -p no NMAP?", "alternativas": ["A) Desativar o scan SYN", "B) Exibir todas as informações durante a análise", "C) Passar como parâmetro as portas a serem verificadas", "D) Realizar um bypass em firewalls", "E) Nenhuma das opções"], "resposta": "C) Passar como parâmetro as portas a serem verificadas"},

                    {"pergunta": "O que significa o termo 'SYN Scan' no contexto do NMAP?", "alternativas": ["A) Scan via TCP", "B) Scan via UDP", "C) Cria uma meia conexão, enviando um pacote para uma porta", "D) Realiza análise de tráfego", "E) Nenhuma das opções"], "resposta": "C) Cria uma meia conexão, enviando um pacote para uma porta"},

                    {"pergunta": "Qual é a finalidade do UDP Scan no NMAP?", "alternativas": ["A) Analisar tráfego UDP", "B) Encontrar portas abertas", "C) Realizar análise de tráfego TCP", "D) Desativar firewalls", "E) Nenhuma das opções"], "resposta": "A) Analisar tráfego UDP"},

                    {"pergunta": "Por que o protocolo UDP pode apresentar desafios durante o scan?", "alternativas": ["A) Emite respostas de conexão", "B) Possui respostas padrão", "C) Não emite respostas de conexão", "D) Requer confirmação de terceiros", "E) Nenhuma das opções"], "resposta": "C) Não emite respostas de conexão"},

                    {"pergunta": "Qual é a principal vantagem do FIN Scan no NMAP?", "alternativas": ["A) Bypass em firewalls", "B) Analisar tráfego UDP", "C) Criar uma conexão completa", "D) Encontrar portas abertas", "E) Nenhuma das opções"], "resposta": "A) Bypass em firewalls"},

                    {"pergunta": "Quantos bits são utilizados para representar um octeto em um endereço IP?", "alternativas": ["A) 4 bits", "B) 8 bits", "C) 16 bits", "D) 32 bits", "E) Nenhuma das opções"], "resposta": "B) 8 bits"},

                    {"pergunta": "O que o parâmetro -sU no NMAP realiza?", "alternativas": ["A) Analisa tráfego TCP", "B) Realiza scan UDP", "C) Desativa firewalls", "D) Exibe todas as informações durante a análise", "E) Nenhuma das opções"], "resposta": "B) Realiza scan UDP"},

                    {"pergunta": "Qual é a finalidade do parâmetro -sN no NMAP?", "alternativas": ["A) Realiza scan UDP", "B) Envia pacotes ICMP", "C) Desativa firewalls", "D) Analisa tráfego TCP", "E) Nenhuma das opções"], "resposta": "D) Analisa tráfego TCP"},

                    {"pergunta": "O que é o CIDR e como é utilizado atualmente?", "alternativas": ["A) Um sistema de encriptação de dados", "B) Uma linguagem de programação", "C) Uma faixa de IPs reservada para uso interno", "D) Uma notação para definir o tamanho das redes", "E) Nenhuma das opções"], "resposta": "D) Uma notação para definir o tamanho das redes"},

                    {"pergunta": "Quais são os benefícios de utilizar o parâmetro -v no NMAP?", "alternativas": ["A) Ocultar informações durante a análise", "B) Exibir todas as informações durante a análise", "C) Aumentar a velocidade do scan", "D) Desativar o scan SYN", "E) Nenhuma das opções"], "resposta": "B) Exibir todas as informações durante a análise"},

                    {"pergunta": "Como o NMAP pode ser utilizado na descoberta de dispositivos em uma rede?", "alternativas": ["A) Através da análise de tráfego UDP", "B) Realizando análise de tráfego TCP", "C) Através de varredura de portas", "D) Desativando firewalls", "E) Nenhuma das opções"], "resposta": "C) Através de varredura de portas"},

                    {"pergunta": "O que são endereços IP públicos e privados?", "alternativas": ["A) Endereços IP utilizados apenas por servidores DNS", "B) Endereços IP roteáveis na Internet e utilizados em redes locais, respectivamente", "C) Endereços IP reservados para uso interno", "D) Endereços IP utilizados exclusivamente por firewalls", "E) Nenhuma das opções"], "resposta": "B) Endereços IP roteáveis na Internet e utilizados em redes locais, respectivamente"},

                    {"pergunta": "Qual é a função das máscaras de sub-rede?", "alternativas": ["A) Encriptar o tráfego de rede", "B) Identificar dispositivos na rede", "C) Definir a faixa de endereços disponíveis", "D) Gerenciar servidores DNS", "E) Nenhuma das opções"], "resposta": "C) Definir a faixa de endereços disponíveis"},

                    {"pergunta": "O que é um IP Público?", "alternativas": ["A) Um endereço IP reservado para uso interno", "B) Um endereço IP roteável na Internet", "C) Um endereço IP utilizado apenas para servidores DNS", "D) Um endereço IP comum em redes domésticas", "E) Nenhuma das opções"], "resposta": "B) Um endereço IP roteável na Internet"},

                    {"pergunta": "O que significa o status 'open' em relação às portas?", "alternativas": ["A) A porta está bloqueada por um firewall", "B) A aplicação está aceitando pacotes nessa porta", "C) A porta está fechada e não responde a pacotes", "D) Não é possível determinar o status da porta", "E) Nenhuma das opções"], "resposta": "B) A aplicação está aceitando pacotes nessa porta"},

                    {"pergunta": "Qual é a interpretação correta do status 'closed' em uma porta?", "alternativas": ["A) A porta está bloqueada por um firewall", "B) A aplicação está aceitando pacotes nessa porta", "C) A porta está fechada e não responde a pacotes", "D) Não é possível determinar o status da porta", "E) Nenhuma das opções"], "resposta": "C) A porta está fechada e não responde a pacotes"},

                    {"pergunta": "O que o status 'Open|Filtered' indica em relação a uma porta?", "alternativas": ["A) A porta está bloqueada por um firewall", "B) A aplicação está aceitando pacotes nessa porta", "C) Não é possível determinar se a porta está bloqueada por firewall ou se está aberta", "D) A porta está fechada e não responde a pacotes", "E) Nenhuma das opções"], "resposta": "C) Não é possível determinar se a porta está bloqueada por firewall ou se está aberta"},

                    {"pergunta": "Por que o NMAP testa as portas aleatoriamente por padrão?", "alternativas": ["A) Para acelerar o processo de varredura", "B) Para evitar que firewalls identifiquem padrões de varredura", "C) Para testar apenas portas sequenciais", "D) Para garantir que todas as portas sejam verificadas", "E) Nenhuma das opções"], "resposta": "B) Para evitar que firewalls identifiquem padrões de varredura"},

                    {"pergunta": "Qual é a utilidade do status 'Closed' ao identificar um host ativo?", "alternativas": ["A) Indica que a porta está bloqueada por um firewall", "B) Mostra que a porta está fechada, mas responde aos pacotes do NMAP", "C) Indica que a porta está aberta e aceitando pacotes", "D) Não tem utilidade na identificação de hosts ativos", "E) Nenhuma das opções"], "resposta": "B) Mostra que a porta está fechada, mas responde aos pacotes do NMAP"},

                    {"pergunta": "Em que contexto o status 'Open|Filtered' pode ser um desafio na interpretação?", "alternativas": ["A) Quando todas as portas estão fechadas", "B) Quando o firewall está desativado", "C) Quando o NMAP testa as portas sequencialmente", "D) Quando não é possível determinar se a porta está bloqueada ou aberta", "E) Nenhuma das opções"], "resposta": "D) Quando não é possível determinar se a porta está bloqueada ou aberta"},

                    {"pergunta": "O que significa a expressão 'Open|Filtered' em relação à aplicação que responde aos pacotes?", "alternativas": ["A) A aplicação está aceitando pacotes em portas abertas", "B) A aplicação está bloqueando pacotes em portas fechadas", "C) A aplicação está respondendo de maneira inconsistente", "D) A aplicação não está instalada no host", "E) Nenhuma das opções"], "resposta": "C) A aplicação está respondendo de maneira inconsistente"},

                    {"pergunta": "Quais são os possíveis valores de status para uma porta, de acordo com o NMAP?", "alternativas": ["A) Open / Closed", "B) Open / Closed / Filtered", "C) Open / Blocked", "D) Closed / Filtered", "E) Nenhuma das opções"], "resposta": "B) Open / Closed / Filtered"},

                    {"pergunta": "O que é necessário para que uma porta seja classificada como 'Closed'?", "alternativas": ["A) A aplicação está bloqueando pacotes nessa porta", "B) A aplicação está aceitando pacotes nessa porta", "C) A porta está fechada e não responde a pacotes", "D) A porta está bloqueada por um firewall", "E) Nenhuma das opções"], "resposta": "C) A porta está fechada e não responde a pacotes"},

                    {"pergunta": "Como o NMAP diferencia uma porta 'Closed' de uma porta 'Open|Filtered'?", "alternativas": ["A) Pelo tempo de resposta", "B) Pela quantidade de pacotes enviados", "C) Pela resposta da aplicação", "D) Pelo número de firewalls encontrados", "E) Nenhuma das opções"], "resposta": "C) Pela resposta da aplicação"},

                    {"pergunta": "Qual é a principal razão para um firewall interferir na identificação do status de uma porta pelo NMAP?", "alternativas": ["A) Por não reconhecer a varredura aleatória do NMAP", "B) Por bloquear pacotes do NMAP", "C) Por não responder a pacotes do NMAP", "D) Por permitir que todas as portas sejam verificadas", "E) Nenhuma das opções"], "resposta": "B) Por bloquear pacotes do NMAP"},

                    {"pergunta": "O que pode ser inferido quando uma porta apresenta o status 'Open|Filtered'?", "alternativas": ["A) A porta está aberta", "B) A porta está bloqueada por um firewall", "C) Não é possível determinar se a porta está bloqueada ou aberta", "D) A aplicação está aceitando pacotes", "E) Nenhuma das opções"], "resposta": "C) Não é possível determinar se a porta está bloqueada ou aberta"},

                    {"pergunta": "Em que situação o status 'Open|Filtered' pode indicar uma possível presença de firewall?", "alternativas": ["A) Quando a aplicação responde consistentemente", "B) Quando a aplicação não responde", "C) Quando a porta está fechada", "D) Quando não é possível determinar se a porta está bloqueada ou aberta", "E) Nenhuma das opções"], "resposta": "D) Quando não é possível determinar se a porta está bloqueada ou aberta"},

                    {"pergunta": "Qual é a desvantagem do status 'Open|Filtered'?", "alternativas": ["A) Facilita a identificação de portas abertas", "B) Dificulta a determinação precisa do status da porta", "C) Indica claramente que a porta está fechada", "D) Não interfere na interpretação das portas", "E) Nenhuma das opções"], "resposta": "B) Dificulta a determinação precisa do status da porta"},

                    {"pergunta": "O que a expressão 'Open|Filtered' indica sobre a porta?", "alternativas": ["A) A porta está aberta", "B) A porta está bloqueada por um firewall", "C) Não é possível determinar se a porta está bloqueada ou aberta", "D) A aplicação está aceitando pacotes", "E) Nenhuma das opções"], "resposta": "C) Não é possível determinar se a porta está bloqueada ou aberta"},

                    {"pergunta": "Como o NMAP determina se uma porta está 'Filtered'?", "alternativas": ["A) Pela resposta da aplicação", "B) Pela ausência de resposta", "C) Pela velocidade de varredura", "D) Pelo número de firewalls encontrados", "E) Nenhuma das opções"], "resposta": "B) Pela ausência de resposta"},

                    {"pergunta": "Qual é a característica essencial de uma porta 'Open'?", "alternativas": ["A) Responder a pacotes", "B) Estar bloqueada por um firewall", "C) Estar fechada e não responder a pacotes", "D) Não ter uma aplicação associada", "E) Nenhuma das opções"], "resposta": "A) Responder a pacotes"},

                    {"pergunta": "Em uma varredura de rede, por que a presença de portas 'Open|Filtered' pode ser considerada ambígua?", "alternativas": ["A) Porque indica claramente que a porta está aberta", "B) Porque a aplicação responde consistentemente", "C) Porque não é possível determinar se a porta está bloqueada ou aberta", "D) Porque todas as portas estão fechadas", "E) Nenhuma das opções"], "resposta": "C) Porque não é possível determinar se a porta está bloqueada ou aberta"},

                    {"pergunta": "O que é o 'Three-Way Handshake' em relação a uma conexão TCP?", "alternativas": ["A) Um método de criptografia de dados", "B) Um procedimento para estabelecer uma conexão confiável entre dois dispositivos", "C) Um tipo de ataque de firewall", "D) Um protocolo de roteamento", "E) Nenhuma das opções"], "resposta": "B) Um procedimento para estabelecer uma conexão confiável entre dois dispositivos"},

                    {"pergunta": "Quantas etapas compõem o 'Three-Way Handshake'?", "alternativas": ["A) Quatro", "B) Duas", "C) Três", "D) Cinco", "E) Seis"], "resposta": "C) Três"},

                    {"pergunta": "Qual é a função da mensagem SYN na primeira etapa do 'Three-Way Handshake'?", "alternativas": ["A) Confirmar a aceitação da conexão", "B) Solicitar o início da conexão", "C) Indicar que o dispositivo está pronto para iniciar a comunicação", "D) Finalizar a comunicação", "E) Nenhuma das opções"], "resposta": "B) Solicitar o início da conexão"},

                    {"pergunta": "O que significa a sigla SYN-ACK na segunda etapa do 'Three-Way Handshake'?", "alternativas": ["A) Synchronized Acknowledge", "B) System Acknowledge", "C) Synced Acknowledge", "D) Synchronize-Acknowledge", "E) Nenhuma das opções"], "resposta": "D) Synchronize-Acknowledge"},

                    {"pergunta": "O que a mensagem ACK na terceira etapa do 'Three-Way Handshake' confirma?", "alternativas": ["A) A aceitação da conexão", "B) O recebimento da mensagem SYN-ACK", "C) A conclusão da comunicação", "D) A recusa da conexão", "E) Nenhuma das opções"], "resposta": "B) O recebimento da mensagem SYN-ACK"},

                    {"pergunta": "Por que o 'Three-Way Handshake' é considerado essencial para a confiabilidade do TCP?", "alternativas": ["A) Para acelerar a comunicação", "B) Para garantir que as portas estejam fechadas", "C) Para estabelecer uma conexão confiável antes da troca de dados", "D) Para evitar o uso de firewalls", "E) Nenhuma das opções"], "resposta": "C) Para estabelecer uma conexão confiável antes da troca de dados"},

                    {"pergunta": "O que acontece após a conclusão do 'Three-Way Handshake' em relação à comunicação entre os dispositivos?", "alternativas": ["A) A comunicação é encerrada imediatamente", "B) Os dispositivos podem começar a enviar e receber dados", "C) Os dispositivos são desconectados", "D) É necessário realizar um 'Four-Way Handshake'", "E) Nenhuma das opções"], "resposta": "B) Os dispositivos podem começar a enviar e receber dados"},

                    {"pergunta": "Qual é a importância do 'Three-Way Handshake' em relação à identificação de portscans por firewalls?", "alternativas": ["A) Aumenta a probabilidade de ser identificado por firewalls", "B) Reduz a probabilidade de ser identificado por firewalls", "C) Não tem impacto na identificação por firewalls", "D) Torna o portscan indetectável", "E) Nenhuma das opções"], "resposta": "B) Reduz a probabilidade de ser identificado por firewalls"},

                    {"pergunta": "Por que o uso do parâmetro -sT no NMAP pode resultar em bloqueio pelo firewall?", "alternativas": ["A) Por realizar um scan silencioso", "B) Por enviar pacotes excessivos e fazer barulho", "C) Por utilizar o método de varredura SYN", "D) Por evitar a identificação por firewalls", "E) Nenhuma das opções"], "resposta": "B) Por enviar pacotes excessivos e fazer barulho"},

                    {"pergunta": "Qual é a principal diferença entre os parâmetros -sT e -sS no NMAP?", "alternativas": ["A) Ambos realizam o Three-Way Handshake", "B) -sT faz uma conexão completa, enquanto -sS realiza uma meia conexão", "C) -sS faz uma conexão completa, enquanto -sT realiza uma meia conexão", "D) Ambos utilizam o método de varredura UDP", "E) Nenhuma das opções"], "resposta": "B) -sT faz uma conexão completa, enquanto -sS realiza uma meia conexão"},

                    {"pergunta": "O que é a opção -D no NMAP e como ela pode ser usada para burlar firewalls?", "alternativas": ["A) Define o tempo de varredura", "B) Ativa o modo stealth", "C) Utiliza IPs falsificados para enganar firewalls", "D) Configura o método de varredura SYN", "E) Nenhuma das opções"], "resposta": "C) Utiliza IPs falsificados para enganar firewalls"},

                    {"pergunta": "Como a opção -g pode ser utilizada em conjunto com o parâmetro decoy no NMAP?", "alternativas": ["A) Para definir o tempo de varredura", "B) Para ativar o modo stealth", "C) Para configurar o método de varredura SYN", "D) Para passar uma porta diferente ao firewall", "E) Nenhuma das opções"], "resposta": "D) Para passar uma porta diferente ao firewall"},

                    {"pergunta": "Qual é a utilidade da opção -sN no NMAP?", "alternativas": ["A) Realizar um scan UDP", "B) Bypassar o firewall sem enviar nenhuma flag", "C) Configurar o método de varredura SYN", "D) Realizar um scan TCP FYN", "E) Nenhuma das opções"], "resposta": "B) Bypassar o firewall sem enviar nenhuma flag"},

                    {"pergunta": "O que é o método de varredura TCP FYN utilizado pela opção -sF no NMAP?", "alternativas": ["A) Envia apenas fragmentos de pacotes", "B) Utiliza a flag FYN para enganar o firewall", "C) Realiza um scan silencioso", "D) Ativa o modo stealth", "E) Nenhuma das opções"], "resposta": "B) Utiliza a flag FYN para enganar o firewall"},

                    {"pergunta": "Qual é a finalidade da opção -f no NMAP?", "alternativas": ["A) Definir o tempo de varredura", "B) Ativar o modo stealth", "C) Enviar apenas fragmentos de pacotes", "D) Configurar o método de varredura SYN", "E) Nenhuma das opções"], "resposta": "C) Enviar apenas fragmentos de pacotes"},

                    {"pergunta": "Por que a opção -Pn no NMAP pode ser útil em uma varredura de rede?", "alternativas": ["A) Para realizar um scan UDP", "B) Para evitar o bloqueio pelo firewall", "C) Para definir o tempo de varredura", "D) Para realizar um scan TCP FYN", "E) Nenhuma das opções"], "resposta": "B) Para evitar o bloqueio pelo firewall"},

                    {"pergunta": "O que a opção --top-ports=valor no NMAP realiza durante uma varredura de rede?", "alternativas": ["A) Configura o método de varredura SYN", "B) Define o tempo de varredura", "C) Pesquisa as portas mais comumente usadas", "D) Ativa o modo stealth", "E) Nenhuma das opções"], "resposta": "C) Pesquisa as portas mais comumente usadas"},

                    {"pergunta": "Qual é a finalidade dos níveis de agressividade de scans no NMAP, como -T0, -T1, -T2, -T3, -T4 e -T5?", "alternativas": ["A) Configurar o método de varredura SYN", "B) Definir o tempo de varredura", "C) Ajustar a agressividade da varredura", "D) Ativar o modo stealth", "E) Nenhuma das opções"], "resposta": "C) Ajustar a agressividade da varredura"}                    
]

quantidade_desejada = int(
    input("Insira a quantidade de questões que deseja estudar: "))

sistema = SistemaEstudo(banco_de_questoes)
sistema.selecionar_questoes(quantidade_desejada)
sistema.estudar()
