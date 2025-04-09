# Lista global para armazenar os contatos
contatos = []

# Função principal que exibe o menu e gerencia as opções
def menu_principal():
    while True:
        # Exibe o menu da agenda
        print('\n===AGENDA===\n')
        print('1. Adicionar contato')             
        print('2. Listar contatos')             
        print('3. Buscar contatos')             
        print('4. Editar contatos')             
        print('5. Remover contatos')             
        print('6. Sair') 

        # Solicita ao usuário que escolha uma opção
        opcao = input('\nSelecione a opção adequada ') 

        # Executa a função correspondente à opção escolhida
        if opcao == '1':
            print('--Adicionar contato--\n')
            add_contato()
        elif opcao == '2':
            print('--Lista de Contatos--\n')
            listar_contato()
        elif opcao == '3':
            print('Buscar Contato')
            buscar_contato()
        elif opcao == '4':
            editar_contato()
        elif opcao == '5':
            remover_contato()
        elif opcao == '6':
            print('Saindo...\n')
            break  # Sai do loop e encerra o programa
        else:
            print('Opção Inválida\n')  # Mensagem para opções inválidas

# Função para adicionar um novo contato
def add_contato():
    while True:
        # Solicita o nome do contato
        nome = input('Nome completo: ')
        if not nome.strip():  # Verifica se o nome está vazio
            print('Nome inválido!')
            continue
        
        # Solicita o telefone do contato
        telefone = input('Telefone  (xxxx-xxxx ou (xx) xxxx-xxxx): ')
        if not validar_contato(telefone):  # Valida o formato do telefone
            print('Telefone inválido!')
            continue

        if telefone_existe(telefone):  # Verifica se o telefone já existe
            print('Telefone já existe na agenda!')
            continue

        # Adiciona o contato à lista de contatos
        contatos.append({'nome': nome,'telefone': telefone})
        print('Você adicionou um contato!')
        break

# Função para verificar se um telefone já existe na lista de contatos
def telefone_existe(telefone):
    for contato in contatos:
        if contato['telefone'] == telefone:
            return True
    return False

# Função para obter o sobrenome de um nome completo
def obter_sobrenome(nome_completo):
    partes = nome_completo.split()  # Divide o nome em partes
    return partes[-1] if partes else ""  # Retorna o último elemento (sobrenome)

# Função para extrair o sobrenome de uma tupla de contato
def extrair_sobrenome(tupla_contato):
    return tupla_contato[0]  # Retorna o sobrenome da tupla

# Função para listar todos os contatos em ordem alfabética pelo sobrenome
def listar_contato():
    if not contatos:  # Verifica se a lista de contatos está vazia
        print('\n--Agenda Vazia--\n')
        return
    
    contato_temp = []  # Lista temporária para ordenação

    # Adiciona cada contato à lista temporária com o sobrenome
    for contato in contatos:
        sobrenome = obter_sobrenome(contato['nome'])
        contato_temp.append((sobrenome, contato))

    # Ordena a lista temporária pelo sobrenome
    contato_temp.sort(key=extrair_sobrenome)
    
    # Exibe os contatos ordenados
    print('\n--Lista de Contatos--\n')
    for _, contato in contato_temp:
        print(f"Nome: {contato['nome']} | Tel: {contato['telefone']}")

# Função para buscar contatos por nome ou parte do nome
def buscar_contato():
    busca = input('\nDigite nome ou parte do nome: ').lower()
    print('Buscando...')
    encontrados = []  # Lista para armazenar contatos encontrados

    # Percorre a lista de contatos e verifica se o nome contém a busca
    for contato in contatos:
        if busca in contato['nome'].lower():
            encontrados.append(contato)
        
    if encontrados:  # Se encontrou contatos, exibe-os
        print(f'--\n {len(encontrados)} Contato(s) encontrado(s)--')
        for contato in encontrados:
            print(f"Nome: {contato['nome']} | Tel: {contato['telefone']}")
    else:  # Caso contrário, exibe mensagem de nenhum contato encontrado
        print('\nNenhum contato encontrado\n')

# Função para editar um contato existente
def editar_contato():
    nome_busca = input('\nDigite contato que deseja editar: ').strip()

    ctt_encontrados = []  # Lista para armazenar contatos encontrados

    # Busca contatos que contenham o nome informado
    for contato in contatos:
        if nome_busca.lower() in contato['nome'].lower():
            ctt_encontrados.append(contato)
    
    if not ctt_encontrados:  # Se nenhum contato for encontrado
        print('\n---Contato não encontrado---') 
        return
    
    if len(ctt_encontrados) > 1:  # Se houver mais de um contato encontrado
        print('\n---Contatos Encontratos---')
        for i, contato in enumerate(ctt_encontrados, 1):
            print(f" {i}: {contato['nome']} | Tel: {contato['telefone']}")

        try:
            # Solicita ao usuário que escolha qual contato editar
            escolha = int(input('\nEscolha o telefone do contato para editar: '))
            if escolha < 1 or escolha > len(ctt_encontrados):
                print('Opção inválida!')
                return
            
            contato = ctt_encontrados[escolha -1]

        except ValueError:
            print('Valor inválido!')
            return
    
    else:  # Se houver apenas um contato encontrado
        contato = ctt_encontrados[0]

    # Exibe o contato selecionado e solicita as novas informações
    print('\n---Editando Contato---')
    print(f" Nome: {contato['nome']} | Tel: {contato['telefone']}")
    novo_nome = input('Edite o nome (Enter vazio para manter): ').strip()
    novo_tel = input('Edite o telefone (Enter vazio para manter): ').strip()

    # Atualiza o nome e o telefone, se informados
    if novo_nome:
        contato['nome'] = novo_nome
    if novo_tel:
        if validar_contato(novo_tel):  # Valida o novo telefone
            contato['telefone'] = novo_tel
        else:
            print('Telefone inválido! Contato não foi alterado')
    print('---\nContato atualizado---')

# Função para remover um contato
def remover_contato():
    nome_busca = input('\nDigite contato que deseja remover: ').strip()

    ctt_encontrados = []  # Lista para armazenar contatos encontrados

    # Busca contatos que contenham o nome informado
    for contato in contatos:
        if nome_busca.lower() in contato['nome'].lower():
            ctt_encontrados.append(contato)
    
    if not ctt_encontrados:  # Se nenhum contato for encontrado
        print('\nContato não encontrado') 
        return
    
    if len(ctt_encontrados) > 1:  # Se houver mais de um contato encontrado
        print('\n--Contatos Encontrados--')
        for i, contato in enumerate(ctt_encontrados, 1):
            print(f" {i}: {contato['nome']} | Tel: {contato['telefone']}")

        try:
            # Solicita ao usuário que escolha qual contato remover
            escolha = int(input('\nEscolha o telefone do contato para remover: '))
            if escolha < 1 or escolha > len(ctt_encontrados):
                print('Opção inválida!')
                return
            
            contato = ctt_encontrados[escolha -1]

        except ValueError:
            print('Valor inválido!')
            return
    
    else:  # Se houver apenas um contato encontrado
        contato = ctt_encontrados[0]

    # Confirma a remoção do contato
    print('\n---Remover contato---\n')
    print(f" Nome: {contato['nome']} | Tel: {contato['telefone']}")
    remover = input('Tem certeza que deseja remover contato (S/N): ').strip().lower()

    if remover == 's':  # Remove o contato se confirmado
        contatos.remove(contato)
        print('\n---Contato removido---\n')
    else:  # Cancela a remoção
        print('\n---Remoção Cancelada---\n')

# Função para validar o formato do telefone
def validar_contato(telefone):
    telefone = telefone.replace(" ", "")  # Remove espaços em branco

    # Verifica o formato xxxx-xxxx
    if len(telefone) == 9 and telefone[4] == '-':   
        parte1 = telefone[:4]
        parte2 = telefone[5:]

        if parte1.isdigit() and parte2.isdigit():
            return True
            
    # Verifica o formato (xx) xxxx-xxxx
    elif len(telefone) == 13:
        if telefone[0] == '(' and telefone[3] == ')' and telefone[8] == '-':
            ddd = telefone[1:3]
            parte1 = telefone[4:8]
            parte2 = telefone[9:]

            if ddd.isdigit and parte1.isdigit() and parte2.isdigit():
                return True
    return False  # Retorna False se o formato for inválido

# Inicia o programa chamando a função menu_principal
if __name__ == "__main__":
    menu_principal()