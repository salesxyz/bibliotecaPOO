import json
import os


#Classe do livro 
class Livro:
    def __init__(self, nome, autor, ano):
        self.nome = nome.strip().lower()
        self.autor = autor.strip()
        self.ano = ano.strip()


#Salvar o livro em JSON 
    def salvar(self, dir_livros):
        caminho = os.path.join(dir_livros, f'{self.nome}.json')
        with open(caminho, 'w', encoding='utf-8') as f:
            json.dump(self.__dict__, f, ensure_ascii=False, indent=4)
 
 
#Carregar o livro 
    @property
    def carregar(nome, dir_livros):
        caminho = os.path.join(dir_livros, f'{nome.strip().lower()}.json')
        if os.path.exists(caminho):
            with open(caminho, 'r', encoding='utf-8') as f:
                dados = json.load(f)
            return Livro(dados['nome'], dados['autor'], dados['ano'])
        return None

    @property
    def apagar(nome, dir_livros):
        caminho = os.path.join(dir_livros, f'{nome.strip().lower()}.json')
        if os.path.exists(caminho):
            os.remove(caminho)
            return True
        return False


#Torna a biblioteca funcional
class Biblioteca:
    def __init__(self, dir_livros='livros'):
        self.dir_livros = dir_livros
        if not os.path.exists(self.dir_livros):
            os.makedirs(self.dir_livros)


#Cadastra um livro dentro da biblioteca
    def cadastrar_livro(self):
        nome = input('Digite o nome do livro que deseja cadastrar: ')
        autor = input('Digite o autor do livro: ')
        ano = input('Digite o ano de publicação: ')
        livro = Livro(nome, autor, ano)
        livro.salvar(self.dir_livros)
        print('Livro cadastrado com sucesso!')


#Atualiza dados do livro (Nome do autor e ano de lancaçamento)
    def atualizar_livro(self):
        nome = input('Informe o nome do livro que deseja atualizar: ')
        livro = Livro.carregar(nome, self.dir_livros)
        if livro:
            print('Dados atuais:', livro.__dict__)
            autor = input('Novo autor: ')
            ano = input('Novo ano: ')
            if autor:
                livro.autor = autor
            if ano:
                livro.ano = ano
            livro.salvar(self.dir_livros)
            print('Livro atualizado')
        else:
            print('Livro não encontrado')


#Apaga um livro salvo na biblioteca
    def apagar_livro(self):
        nome = input('Digite o nome do livro para apagar: ')
        if Livro.apagar(nome, self.dir_livros):
            print('Livro apagado com sucesso!')
        else:
            print('Livro não encontrado!')


#Mostra os livros salvos na biblioteca
    def ver_livros(self):
        arquivos = os.listdir(self.dir_livros)
        if not arquivos:
            print('Nenhum livro cadastrado!')
        else:
            print(f'{"_"*30} LIVROS {"_"*30}')
            for arquivo in arquivos:
                if arquivo.endswith('.json'):
                    with open(os.path.join(self.dir_livros, arquivo), 'r', encoding='utf-8') as f:
                        cadastro_livro = json.load(f)
                    print(f"Nome: {cadastro_livro['nome'].capitalize()}")
                    print(f"Autor: {cadastro_livro['autor']}")
                    print(f"Ano: {cadastro_livro['ano']}")
                    print('_'*60)


#Limpar o terminal depois da execução do codigo
def limpar():
    os.system('cls' if os.name == 'nt' else 'clear')


def main():
    biblioteca = Biblioteca()
    #Menu do sistema 
    while True:
        print('__________BEM VINDO A BIBLIOTECA__________')
        print('1 - cadastrar livro ')
        print('2 - atualizar livros  ')
        print('3 - apagar cadastro de um livro ')
        print('4 - ver livros')
        print('5 - sair da biblioteca')
        
        opcao = input('escolha uma opcao: ')
        limpar()

        match opcao:
            case '1':
                biblioteca.cadastrar_livro()
            case '2':
                biblioteca.atualizar_livro()
            case '3':
                biblioteca.apagar_livro()
            case '4':
                biblioteca.ver_livros()
            case '5':
                print('saindo...')
                break
            case _:
                print('opcao invalida...')


if __name__ == '__main__':
    main()