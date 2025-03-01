contatos = []

def menu_principal():

    while True:
        print('\n===AGENDA===\n')
        print('1. Adicionar contato')             
        print('2. Listar contatos')             
        print('3. Buscar contatos')             
        print('4. Editar contatos')             
        print('5. Remover contatos')             
        print('6. Sair') 

        opcao = input('\nSelecione a opção adequada ') 

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
            break 
        else:
            print('Opção Inválida\n')

def add_contato():
    while True:
        nome = input('Nome completo: ')
        if not nome.strip():
            print('Nome inválido!')
            continue
        
        telefone = input('Telefone  (xxxx-xxxx ou (xx) xxxx-xxxx): ')
        if not validar_contato(telefone):
            print('Telefone inválido!')
            continue

        if telefone_existe(telefone):
            print('Telefone já existe na agenda!')
            continue

        contatos.append({'nome': nome,'telefone': telefone})
        print('Você adicionou um contato!')
        break

def telefone_existe(telefone):
    for contato in contatos:
        if contato['telefone'] == telefone:
            return True
    return False

def obter_sobrenome(nome_completo):
    partes = nome_completo.split()
    return partes[-1] if partes else ""

def extrair_sobrenome(tupla_contato):
    return tupla_contato[0]
    
def listar_contato():
    if not contatos:
        print('\n--Agenda Vazia--\n')
        return
    
    contato_temp = []

    for contato in contatos:
        sobrenome = obter_sobrenome(contato['nome'])
        contato_temp.append((sobrenome, contato))

    contato_temp.sort(key=extrair_sobrenome)
    
    print('\n--Lista de Contatos--\n')
    for _, contato in contato_temp:
        print(f"Nome: {contato['nome']} | Tel: {contato['telefone']}")

def buscar_contato():
    busca = input('\nDigite nome ou parte do nome: ').lower()
    print('Buscando...')
    encontrados = [] 

    for contato in contatos:
        if busca in contato['nome'].lower():
            encontrados.append(contato)
        
    if encontrados:
        print(f'--\n {len(encontrados)} Contato(s) encontrado(s)--')
        for contato in encontrados:
            print(f"Nome: {contato['nome']} | Tel: {contato['telefone']}")
    else:
        print('\nNenhum contato encontrado\n')

def editar_contato():
    nome_busca = input('\nDigite contato que deseja editar: ').strip()

    ctt_encontrados = []

    for contato in contatos:
        if nome_busca.lower() in contato['nome'].lower():
            ctt_encontrados.append(contato)
    
    if not ctt_encontrados:
        print('\n---Contato não encontrado---') 
        return
    
    if len(ctt_encontrados) > 1:
        print('\n---Contatos Encontratos---')
        for i, contato in enumerate(ctt_encontrados, 1):
            print(f" {i}: {contato['nome']} | Tel: {contato['telefone']}")

        try:
            escolha = int(input('\nEscolha o telefone do contato para editar: '))
            if escolha < 1 or escolha > len(ctt_encontrados):
                print('Opção inválida!')
                return
            
            contato = ctt_encontrados[escolha -1]

        except ValueError:
            print('Valor inválido!')
            return
    
    else:
        contato = ctt_encontrados[0]

    print('\n---Editando Contato---')
    print(f" Nome: {contato['nome']} | Tel: {contato['telefone']}")
    novo_nome = input('Edite o nome (Enter vazio para manter): ').strip()
    novo_tel = input('Edite o telefone (Enter vazio para manter): ').strip()

    if novo_nome:
        contato['nome'] = novo_nome
    if novo_tel:
        if validar_contato(novo_tel):
            contato['telefone'] = novo_tel
        else:
            print('Telefone inválido! Contato não foi alterado')
    print('---\nContato atualizado---')

def remover_contato():
    nome_busca = input('\nDigite contato que deseja remover: ').strip()

    ctt_encontrados = []

    for contato in contatos:
        if nome_busca.lower() in contato['nome'].lower():
            ctt_encontrados.append(contato)
    
    if not ctt_encontrados:
        print('\nContato não encontrado') 
        return
    
    if len(ctt_encontrados) > 1:
        print('\n--Contatos Encontrados--')
        for i, contato in enumerate(ctt_encontrados, 1):
            print(f" {i}: {contato['nome']} | Tel: {contato['telefone']}")

        try:
            escolha = int(input('\nEscolha o telefone do contato para remover: '))
            if escolha < 1 or escolha >= len(ctt_encontrados):
                print('Opção inválida!')
                return
            
            contato = ctt_encontrados[escolha -1]

        except ValueError:
            print('Valor inválido!')
            return
    
    else:
        contato = ctt_encontrados[0]

    print('\n---Remover contato---\n')
    print(f" Nome: {contato['nome']} | Tel: {contato['telefone']}")
    remover = input('Tem certeza que deseja remover contato (S/N): ').strip().lower()

    if remover == 's':
        contatos.remove(contato)
        print('\n---Contato removido---\n')
    else:
        print('\n---Remoção Cancelada---\n')

def validar_contato(telefone):
    telefone = telefone.replace(" ", "")

    if len(telefone) == 9 and telefone[4] == '-':   
        parte1 = telefone[:4]
        parte2 = telefone[5:]

        if parte1.isdigit() and parte2.isdigit():
            return True
            
    elif len(telefone) == 13:
        if telefone[0] == '(' and telefone[3] == ')' and telefone[8] == '-':
            ddd = telefone[1:3]
            parte1 = telefone[4:8]
            parte2 = telefone[9:]

            if ddd.isdigit and parte1.isdigit() and parte2.isdigit():
                return True
    return False


if __name__ == "__main__":
    menu_principal() 
