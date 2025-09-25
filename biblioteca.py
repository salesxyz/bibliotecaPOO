# Gerenciamento de biblioteca 

import json
import os
livros_dir = 'livros'
if not os.path.exists(livros_dir):
    os.makedirs(livros_dir)
limpar = lambda: os.system('cls' if os.name == 'nt' else 'clear')

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
            nome = input('Digite o nome do livro que deseja cadastrar: ').strip().lower()
            autor = input('Digite o autor do livro: ').strip()
            ano = input('Digite o ano de publicação: ').strip()
            cadastro_livro = {
                'nome': nome,
                'autor': autor,
                'ano': ano
            }
            with open(os.path.join(livros_dir, f'{nome}.json'), 'w', encoding='utf-8') as f:
                json.dump(cadastro_livro, f, ensure_ascii=False, indent=4)
            limpar()
            print('Livro cadastrado com sucesso!')
            continue
        case '2':
            nome = input('Informe o nome do livro que deseja atualizar: ').strip().lower()
            caminho = os.path.join(livros_dir, f'{nome}.json')
            if os.path.exists(caminho):
                with open(caminho, 'r', encoding='utf-8') as f:
                    cadastro_livro = json.load(f)
                print('Dados atuais:', cadastro_livro)
                autor = input('Novo autor: ').strip()
                ano = input('Novo ano: ').strip()
                if autor:
                    cadastro_livro['autor'] = autor
                if ano:
                    cadastro_livro['ano'] = ano
                with open(caminho, 'w', encoding='utf-8') as f:
                    json.dump(cadastro_livro, f, ensure_ascii=False, indent=4)
                limpar()
                print('Livro atualizado')
            else:
                print('Livro não encontrado')
            continue
        case '3':
            nome = input('Digite o nome do livro para apagar: ').strip().lower()
            caminho = os.path.join(livros_dir, f'{nome}.json')
            if os.path.exists(caminho):
                os.remove(caminho)
                print('Livro apagado com sucesso!')
            else:
                print('Livro não encontrado!')
            continue
        case '4':
            arquivos = os.listdir(livros_dir)
            if not arquivos:
                print('Nenhum livro cadastrado!')
            else:
                print(f'{'_'*30} LIVROS {'_'*30}')
                for arquivo in arquivos:
                    if arquivo.endswith('.json'):
                        with open(os.path.join(livros_dir, arquivo), 'r', encoding='utf-8') as f:
                            cadastro_livro = json.load(f)
                        print(f"Nome: {cadastro_livro['nome'].capitalize()}")
                        print(f"Autor: {cadastro_livro['autor']}")
                        print(f"Ano: {cadastro_livro['ano']}")
                        print('_'*60)
        case '5':
            print('saindo...')
            break
        case _:
            print('opcao invalida...')