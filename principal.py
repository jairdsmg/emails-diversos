import diversos
import textos
from diversos import *
from time import sleep
import pyperclip
import PySimpleGUI as sg

# Variaveis globais usadas no armazenamento dos contratos
contratos = []
cont = 1
i = 0

numero_processo=''
codigo_email=''
usuario = diversos.get_user()
add='+'

#abrev ='lay'


#CRIAÇÃO DAS JANELAS---------------------
#Componentes da Janela Principal
def janela_principal():
    sg.theme('Reddit')
    menu_def = [
        ['Email', [
                  'CRI',['Solicitação de Parecer'],
                  'Defensoria', ['Encaminhamento de Ofício'],
                  'Distribuidor', ['Distribuição de CP via Malote Digital', 'Devolução de CP via Malote Digital'],
                  'INSS',
                  'Perito',['Intimação de Nomeação',['Justiça Gratuita','Estimativa de Honorários'],
                             'Cienficação de Expedição de MLE'],
                   ]],

        ['Cartas', ['Intimação', 'autor', 'reu', ['malo'], 'Citação']],
    ]

    layout_painel = [
        [sg.Text('Para:'), sg.Text("",key='destinatario')],
        [sg.HorizontalSeparator()],
        [sg.Text('Assunto:'), sg.Text("",key='assunt')],
        [sg.HorizontalSeparator()],
        [sg.Text("", key='texto_email')],
    ]

    layout_requisitos = [
        [sg.Text("", key='req1')],
        [sg.HorizontalSeparator()],
        [sg.Text("", key='req2')],
        [sg.HorizontalSeparator()],
        [sg.Text("", key='req3')],
    ]

    layout_esquerda = [
        [sg.Image(f'assets/descanso.png')],

    ]

    layout_direita = [
               [sg.Menu(menu_def)],
               [sg.Text('Selecione um modelo de e-mail', size=(300, 1), font=('Arial', 18),text_color=('red'), key='tit1')],
               #[sg.HorizontalSeparator()],
               [sg.Frame('Email', layout=layout_painel)],
               [sg.HorizontalSeparator()],
               [sg.Text(' Pré-Requisitos ', size=(300, 1), font=('Arial', 18), text_color=('blue'))],
               #[sg.HorizontalSeparator()],
               [sg.Frame('Preenchimentos obrigatórios', layout=layout_requisitos)],
               [sg.Button('Selecionar', size=(30, 1), button_color=('gray'))],
               [sg.StatusBar(f'usuario: {usuario}', justification='right')],
             ]

    #dividi o layout em 02 colunas, nomeando em esquerda e direita
    layout = [
        [sg.Column(layout_esquerda), sg.VSeparator(), sg.Column(layout_direita)],

    ]

    return sg.Window('Principal', layout=layout, size=(905, 480), finalize=True)





#Componentes da Janela Email
def janela_scpc():

    sg.theme('Reddit')

    if(codigo_email==1):
        lay = [
            [sg.Button('Malote', size=(10, 1), button_color=('gray'))],

            [sg.Text('Preencha apenas os campos do modelo escolhido', size=(300, 1), font=('Arial', 22, 'bold'),
                     text_color=('red'))],
            # [sg.HorizontalSeparator()],
            [sg.Text('Num. Processo:', font=('Arial', 14, 'bold')), sg.Input(key='num_proc', size=(28, 3), font=(18)),
             sg.Text('obrigatório', font=('Arial', 10), text_color=('red')),
             sg.Text('             Decisão - Fls:', font=('Arial', 14, 'bold')),
             sg.Input(key='fls_dec', size=(10, 3), font=(18))],
            [sg.Text('Requerente:       ', font=('Arial', 14, 'bold'), visible=False),
             sg.Input(key='nome_autor', size=(70, 2), font=(18), visible=False)],
            [sg.Text('RG:                       ', font=('Arial', 14, 'bold'), visible=False),
             sg.Input(key='rg_autor', size=(20, 2), font=(18), visible=False), sg.Text('         ', visible=False),
             sg.Radio('CPF:', 'tp_doc_autor', key='docm_cpf', default=True, font=('Arial', 14, 'bold'), visible=False),
             sg.Radio('CNPJ:', 'tp_doc_autor', key='docm_cnpj', font=('Arial', 14, 'bold'), visible=False),
             sg.Input(key='cpf_autor', size=(22, 2), font=(18), visible=False)],
            [sg.Text('Requerido:         ', font=('Arial', 14, 'bold'), visible=False),
             sg.Input(key='nome_reu', size=(70, 2), font=(18), visible=False)],
            [sg.Text('RG:                       ', font=('Arial', 14, 'bold'), visible=False),
             sg.Input(key='rg_reu', size=(20, 2), font=(18), visible=False), sg.Text('         ', visible=False),
             sg.Radio('CPF:', 'tp_doc_reu', key='doc_cpf', font=('Arial', 14, 'bold'), visible=False),
             sg.Radio('CNPJ:', 'tp_doc_reu', key='doc_cnpj', default=True, font=('Arial', 14, 'bold'), visible=False),
             sg.Input(key='cnpj_reu', size=(22, 1), font=(18), visible=False)],
            [sg.Text('Contrato:            ', font=('Arial', 14, 'bold'), visible=False),
             sg.Input(key='num_contrato', size=(20, 1), font=(18), visible=False), sg.Text(' ', visible=False),
             sg.Text('Valor - R$', font=('Arial', 14, 'bold'), visible=False),
             sg.Input(key='valor_contrato', size=(12, 1), font=(18), visible=False), sg.Text('  ', visible=False),
             sg.Text('Data:', font=('Arial', 14, 'bold'), visible=False),
             sg.Input(key='data_contrato', size=(12, 1), font=(18), visible=False),
             sg.Button(add, size=(5, 1), font=('Arial', 10, 'bold'), tooltip=('  Adicionar outro contrato  '), visible=False)],
            [sg.HorizontalSeparator(color='black')],
            # sg.Checkbox('Anexar Ofício', key='check_oficio', size=(70, 70),  font=('Arial', 12, 'bold')),
            [sg.Checkbox('Anexar Senha de Acesso', key='check_senha', size=(70, 70), font=('Arial', 12, 'bold'))],
            [sg.Checkbox('Anexar Ofício', key='check_oficio', size=(70, 70), font=('Arial', 12, 'bold'))],
            [sg.Text('Qtd de Outros Anexos:', font=('Arial', 12, 'bold')),
             sg.Spin([i for i in range(0, 11)], initial_value=1, size=(5, 10), key=('qtd'),
                     font=(18))],
            [sg.Checkbox('Imprimir após enviar', key='check_impressao', size=(70, 70), font=('Arial', 12, 'bold'))],
            [sg.Button('Enviar Email', size=(52, 1), disabled=(False), font=('Arial', 14, 'bold')),
             sg.Button('Voltar', size=(20, 1), button_color=('gray'), font=('Arial', 14, 'bold'))],
        ]
    elif(codigo_email==2):
        lay = [
            [sg.Button('Malote', size=(10, 1), button_color=('gray'))],

            [sg.Text('Preencha apenas os campos do modelo escolhido', size=(300, 1), font=('Arial', 22, 'bold'),
                     text_color=('red'))],
            # [sg.HorizontalSeparator()],
            [sg.Text('Num. Processo:', font=('Arial', 14, 'bold')), sg.Input(key='num_proc', size=(28, 3), font=(18)),
             sg.Text('obrigatório', font=('Arial', 10), text_color=('red')),
             sg.Text('             Decisão - Fls:', font=('Arial', 14, 'bold'), visible=False),
             sg.Input(key='fls_dec', size=(10, 3), font=(18), visible=False)],
            [sg.Text('Requerente:       ', font=('Arial', 14, 'bold')),
             sg.Input(key='nome_autor', size=(70, 2), font=(18))],
            [sg.Text('RG:                       ', font=('Arial', 14, 'bold')),
             sg.Input(key='rg_autor', size=(20, 2), font=(18)), sg.Text('         '),
             sg.Radio('CPF:', 'tp_doc_autor', key='docm_cpf', default=True, font=('Arial', 14, 'bold')),
             sg.Radio('CNPJ:', 'tp_doc_autor', key='docm_cnpj', font=('Arial', 14, 'bold')),
             sg.Input(key='cpf_autor', size=(22, 2), font=(18))],
            [sg.Text('Requerido:         ', font=('Arial', 14, 'bold')),
             sg.Input(key='nome_reu', size=(70, 2), font=(18))],
            [sg.Text('RG:                       ', font=('Arial', 14, 'bold')),
             sg.Input(key='rg_reu', size=(20, 2), font=(18)), sg.Text('         '),
             sg.Radio('CPF:', 'tp_doc_reu', key='doc_cpf', font=('Arial', 14, 'bold')),
             sg.Radio('CNPJ:', 'tp_doc_reu', key='doc_cnpj', default=True, font=('Arial', 14, 'bold')),
             sg.Input(key='cnpj_reu', size=(22, 1), font=(18))],
            [sg.Text('Contrato:            ', font=('Arial', 14, 'bold')),
             sg.Input(key='num_contrato', size=(20, 1), font=(18)), sg.Text(' '),
             sg.Text('Valor - R$', font=('Arial', 14, 'bold')),
             sg.Input(key='valor_contrato', size=(12, 1), font=(18)), sg.Text('  '),
             sg.Text('Data:', font=('Arial', 14, 'bold')),
             sg.Input(key='data_contrato', size=(12, 1), font=(18)),
             sg.Button(add, size=(5, 1), font=('Arial', 10, 'bold'), tooltip=('  Adicionar outro contrato  '))],
            [sg.HorizontalSeparator(color='black')],
            # sg.Checkbox('Anexar Ofício', key='check_oficio', size=(70, 70),  font=('Arial', 12, 'bold')),
            [sg.Checkbox('Anexar Senha de Acesso', key='check_senha', size=(70, 70), font=('Arial', 12, 'bold'))],
            [sg.Checkbox('Anexar Ofício', key='check_oficio', size=(70, 70), font=('Arial', 12, 'bold'))],
            [sg.Text('Qtd de Outros Anexos:', font=('Arial', 12, 'bold')),
             sg.Spin([i for i in range(0, 11)], initial_value=1, size=(5, 10), key=('qtd'),
                     font=(18))],
            [sg.Checkbox('Imprimir após enviar', key='check_impressao', size=(70, 70), font=('Arial', 12, 'bold'))],
            [sg.Button('Enviar Email', size=(52, 1), disabled=(False), font=('Arial', 14, 'bold')),
             sg.Button('Voltar', size=(20, 1), button_color=('gray'), font=('Arial', 14, 'bold'))],
        ]
    elif (codigo_email == 3):
        lay = [
            [sg.Button('Malote', size=(10, 1), button_color=('gray'))],

            [sg.Text('Preencha apenas os campos do modelo escolhido', size=(300, 1), font=('Arial', 22, 'bold'),
                     text_color=('red'))],
            # [sg.HorizontalSeparator()],
            [sg.Text('Num. Processo:', font=('Arial', 14, 'bold')), sg.Input(key='num_proc', size=(28, 3), font=(18)),
             sg.Text('obrigatório', font=('Arial', 10), text_color=('red')),
             sg.Text('             Decisão - Fls:', font=('Arial', 14, 'bold')),
             sg.Input(key='fls_dec', size=(10, 3), font=(18))],
            [sg.Text('Requerente:       ', font=('Arial', 14, 'bold'), visible=False),
             sg.Input(key='nome_autor', size=(70, 2), font=(18), visible=False)],
            [sg.Text('RG:                       ', font=('Arial', 14, 'bold'), visible=False),
             sg.Input(key='rg_autor', size=(20, 2), font=(18), visible=False), sg.Text('         ', visible=False),
             sg.Radio('CPF:', 'tp_doc_autor', key='docm_cpf', default=True, font=('Arial', 14, 'bold'), visible=False),
             sg.Radio('CNPJ:', 'tp_doc_autor', key='docm_cnpj', font=('Arial', 14, 'bold'), visible=False),
             sg.Input(key='cpf_autor', size=(22, 2), font=(18), visible=False)],
            [sg.Text('Requerido:         ', font=('Arial', 14, 'bold'), visible=False),
             sg.Input(key='nome_reu', size=(70, 2), font=(18), visible=False)],
            [sg.Text('RG:                       ', font=('Arial', 14, 'bold'), visible=False),
             sg.Input(key='rg_reu', size=(20, 2), font=(18), visible=False), sg.Text('         ', visible=False),
             sg.Radio('CPF:', 'tp_doc_reu', key='doc_cpf', font=('Arial', 14, 'bold'), visible=False),
             sg.Radio('CNPJ:', 'tp_doc_reu', key='doc_cnpj', default=True, font=('Arial', 14, 'bold'), visible=False),
             sg.Input(key='cnpj_reu', size=(22, 1), font=(18), visible=False)],
            [sg.Text('Contrato:            ', font=('Arial', 14, 'bold'), visible=False),
             sg.Input(key='num_contrato', size=(20, 1), font=(18), visible=False), sg.Text(' ', visible=False),
             sg.Text('Valor - R$', font=('Arial', 14, 'bold'), visible=False),
             sg.Input(key='valor_contrato', size=(12, 1), font=(18), visible=False), sg.Text('  ', visible=False),
             sg.Text('Data:', font=('Arial', 14, 'bold'), visible=False),
             sg.Input(key='data_contrato', size=(12, 1), font=(18), visible=False),
             sg.Button(add, size=(5, 1), font=('Arial', 10, 'bold'), tooltip=('  Adicionar outro contrato  '),
                       visible=False)],
            [sg.HorizontalSeparator(color='black')],
            # sg.Checkbox('Anexar Ofício', key='check_oficio', size=(70, 70),  font=('Arial', 12, 'bold')),
            [sg.Checkbox('Anexar Senha de Acesso', key='check_senha', size=(70, 70), font=('Arial', 12, 'bold'))],
            [sg.Checkbox('Anexar Ofício', key='check_oficio', size=(70, 70), font=('Arial', 12, 'bold'))],
            [sg.Text('Qtd de Outros Anexos:', font=('Arial', 12, 'bold')),
             sg.Spin([i for i in range(0, 11)], initial_value=1, size=(5, 10), key=('qtd'),
                     font=(18))],
            [sg.Checkbox('Imprimir após enviar', key='check_impressao', size=(70, 70), font=('Arial', 12, 'bold'))],
            [sg.Button('Enviar Email', size=(52, 1), disabled=(False), font=('Arial', 14, 'bold')),
             sg.Button('Voltar', size=(20, 1), button_color=('gray'), font=('Arial', 14, 'bold'))],
        ]
    elif (codigo_email == 4):
        lay = [
            [sg.Button('Malote', size=(10, 1), button_color=('gray'))],

            [sg.Text('Preencha apenas os campos do modelo escolhido', size=(300, 1), font=('Arial', 22, 'bold'),
                     text_color=('red'))],
            # [sg.HorizontalSeparator()],
            [sg.Text('Num. Processo:', font=('Arial', 14, 'bold')), sg.Input(key='num_proc', size=(28, 3), font=(18)),
             sg.Text('obrigatório', font=('Arial', 10), text_color=('red')),
             sg.Text('             Decisão - Fls:', font=('Arial', 14, 'bold')),
             sg.Input(key='fls_dec', size=(10, 3), font=(18))],
            [sg.Text('Requerente:       ', font=('Arial', 14, 'bold'), visible=False),
             sg.Input(key='nome_autor', size=(70, 2), font=(18), visible=False)],
            [sg.Text('RG:                       ', font=('Arial', 14, 'bold'), visible=False),
             sg.Input(key='rg_autor', size=(20, 2), font=(18), visible=False), sg.Text('         ', visible=False),
             sg.Radio('CPF:', 'tp_doc_autor', key='docm_cpf', default=True, font=('Arial', 14, 'bold'), visible=False),
             sg.Radio('CNPJ:', 'tp_doc_autor', key='docm_cnpj', font=('Arial', 14, 'bold'), visible=False),
             sg.Input(key='cpf_autor', size=(22, 2), font=(18), visible=False)],
            [sg.Text('Requerido:         ', font=('Arial', 14, 'bold'), visible=False),
             sg.Input(key='nome_reu', size=(70, 2), font=(18), visible=False)],
            [sg.Text('RG:                       ', font=('Arial', 14, 'bold'), visible=False),
             sg.Input(key='rg_reu', size=(20, 2), font=(18), visible=False), sg.Text('         ', visible=False),
             sg.Radio('CPF:', 'tp_doc_reu', key='doc_cpf', font=('Arial', 14, 'bold'), visible=False),
             sg.Radio('CNPJ:', 'tp_doc_reu', key='doc_cnpj', default=True, font=('Arial', 14, 'bold'), visible=False),
             sg.Input(key='cnpj_reu', size=(22, 1), font=(18), visible=False)],
            [sg.Text('Contrato:            ', font=('Arial', 14, 'bold'), visible=False),
             sg.Input(key='num_contrato', size=(20, 1), font=(18), visible=False), sg.Text(' ', visible=False),
             sg.Text('Valor - R$', font=('Arial', 14, 'bold'), visible=False),
             sg.Input(key='valor_contrato', size=(12, 1), font=(18), visible=False), sg.Text('  ', visible=False),
             sg.Text('Data:', font=('Arial', 14, 'bold'), visible=False),
             sg.Input(key='data_contrato', size=(12, 1), font=(18), visible=False),
             sg.Button(add, size=(5, 1), font=('Arial', 10, 'bold'), tooltip=('  Adicionar outro contrato  '),
                       visible=False)],
            [sg.HorizontalSeparator(color='black')],
            # sg.Checkbox('Anexar Ofício', key='check_oficio', size=(70, 70),  font=('Arial', 12, 'bold')),
            [sg.Checkbox('Anexar Senha de Acesso', key='check_senha', size=(70, 70), font=('Arial', 12, 'bold'))],
            [sg.Checkbox('Anexar Ofício', key='check_oficio', size=(70, 70), font=('Arial', 12, 'bold'))],
            [sg.Text('Qtd de Outros Anexos:', font=('Arial', 12, 'bold')),
             sg.Spin([i for i in range(0, 11)], initial_value=1, size=(5, 10), key=('qtd'),
                     font=(18))],
            [sg.Checkbox('Imprimir após enviar', key='check_impressao', size=(70, 70), font=('Arial', 12, 'bold'))],
            [sg.Button('Enviar Email', size=(52, 1), disabled=(False), font=('Arial', 14, 'bold')),
             sg.Button('Voltar', size=(20, 1), button_color=('gray'), font=('Arial', 14, 'bold'))],
        ]
    elif (codigo_email == 5):
        lay = [
            [sg.Button('Malote', size=(10, 1), button_color=('gray'))],

            [sg.Text('Preencha apenas os campos do modelo escolhido', size=(300, 1), font=('Arial', 22, 'bold'),
                     text_color=('red'))],
            # [sg.HorizontalSeparator()],
            [sg.Text('Num. Processo:', font=('Arial', 14, 'bold')), sg.Input(key='num_proc', size=(28, 3), font=(18)),
             sg.Text('obrigatório', font=('Arial', 10), text_color=('red')),
             sg.Text('             Decisão - Fls:', font=('Arial', 14, 'bold')),
             sg.Input(key='fls_dec', size=(10, 3), font=(18))],
            [sg.Text('Requerente:       ', font=('Arial', 14, 'bold'), visible=False),
             sg.Input(key='nome_autor', size=(70, 2), font=(18), visible=False)],
            [sg.Text('RG:                       ', font=('Arial', 14, 'bold'), visible=False),
             sg.Input(key='rg_autor', size=(20, 2), font=(18), visible=False), sg.Text('         ', visible=False),
             sg.Radio('CPF:', 'tp_doc_autor', key='docm_cpf', default=True, font=('Arial', 14, 'bold'), visible=False),
             sg.Radio('CNPJ:', 'tp_doc_autor', key='docm_cnpj', font=('Arial', 14, 'bold'), visible=False),
             sg.Input(key='cpf_autor', size=(22, 2), font=(18), visible=False)],
            [sg.Text('Requerido:         ', font=('Arial', 14, 'bold'), visible=False),
             sg.Input(key='nome_reu', size=(70, 2), font=(18), visible=False)],
            [sg.Text('RG:                       ', font=('Arial', 14, 'bold'), visible=False),
             sg.Input(key='rg_reu', size=(20, 2), font=(18), visible=False), sg.Text('         ', visible=False),
             sg.Radio('CPF:', 'tp_doc_reu', key='doc_cpf', font=('Arial', 14, 'bold'), visible=False),
             sg.Radio('CNPJ:', 'tp_doc_reu', key='doc_cnpj', default=True, font=('Arial', 14, 'bold'), visible=False),
             sg.Input(key='cnpj_reu', size=(22, 1), font=(18), visible=False)],
            [sg.Text('Contrato:            ', font=('Arial', 14, 'bold'), visible=False),
             sg.Input(key='num_contrato', size=(20, 1), font=(18), visible=False), sg.Text(' ', visible=False),
             sg.Text('Valor - R$', font=('Arial', 14, 'bold'), visible=False),
             sg.Input(key='valor_contrato', size=(12, 1), font=(18), visible=False), sg.Text('  ', visible=False),
             sg.Text('Data:', font=('Arial', 14, 'bold'), visible=False),
             sg.Input(key='data_contrato', size=(12, 1), font=(18), visible=False),
             sg.Button(add, size=(5, 1), font=('Arial', 10, 'bold'), tooltip=('  Adicionar outro contrato  '),
                       visible=False)],
            [sg.HorizontalSeparator(color='black')],
            # sg.Checkbox('Anexar Ofício', key='check_oficio', size=(70, 70),  font=('Arial', 12, 'bold')),
            [sg.Checkbox('Anexar Senha de Acesso', key='check_senha', size=(70, 70), font=('Arial', 12, 'bold'))],
            [sg.Checkbox('Anexar Ofício', key='check_oficio', size=(70, 70), font=('Arial', 12, 'bold'))],
            [sg.Text('Qtd de Outros Anexos:', font=('Arial', 12, 'bold')),
             sg.Spin([i for i in range(0, 11)], initial_value=1, size=(5, 10), key=('qtd'),
                     font=(18))],
            [sg.Checkbox('Imprimir após enviar', key='check_impressao', size=(70, 70), font=('Arial', 12, 'bold'))],
            [sg.Button('Enviar Email', size=(52, 1), disabled=(False), font=('Arial', 14, 'bold')),
             sg.Button('Voltar', size=(20, 1), button_color=('gray'), font=('Arial', 14, 'bold'))],
        ]
    elif (codigo_email == 6):
        lay = [
            [sg.Button('Malote', size=(10, 1), button_color=('gray'))],

            [sg.Text('Preencha apenas os campos do modelo escolhido', size=(300, 1), font=('Arial', 22, 'bold'),
                     text_color=('red'))],
            # [sg.HorizontalSeparator()],
            [sg.Text('Num. Processo:', font=('Arial', 14, 'bold')), sg.Input(key='num_proc', size=(28, 3), font=(18)),
             sg.Text('obrigatório', font=('Arial', 10), text_color=('red')),
             sg.Text('             Decisão - Fls:', font=('Arial', 14, 'bold')),
             sg.Input(key='fls_dec', size=(10, 3), font=(18))],
            [sg.Text('Requerente:       ', font=('Arial', 14, 'bold'), visible=False),
             sg.Input(key='nome_autor', size=(70, 2), font=(18), visible=False)],
            [sg.Text('RG:                       ', font=('Arial', 14, 'bold'), visible=False),
             sg.Input(key='rg_autor', size=(20, 2), font=(18), visible=False), sg.Text('         ', visible=False),
             sg.Radio('CPF:', 'tp_doc_autor', key='docm_cpf', default=True, font=('Arial', 14, 'bold'), visible=False),
             sg.Radio('CNPJ:', 'tp_doc_autor', key='docm_cnpj', font=('Arial', 14, 'bold'), visible=False),
             sg.Input(key='cpf_autor', size=(22, 2), font=(18), visible=False)],
            [sg.Text('Requerido:         ', font=('Arial', 14, 'bold'), visible=False),
             sg.Input(key='nome_reu', size=(70, 2), font=(18), visible=False)],
            [sg.Text('RG:                       ', font=('Arial', 14, 'bold'), visible=False),
             sg.Input(key='rg_reu', size=(20, 2), font=(18), visible=False), sg.Text('         ', visible=False),
             sg.Radio('CPF:', 'tp_doc_reu', key='doc_cpf', font=('Arial', 14, 'bold'), visible=False),
             sg.Radio('CNPJ:', 'tp_doc_reu', key='doc_cnpj', default=True, font=('Arial', 14, 'bold'), visible=False),
             sg.Input(key='cnpj_reu', size=(22, 1), font=(18), visible=False)],
            [sg.Text('Contrato:            ', font=('Arial', 14, 'bold'), visible=False),
             sg.Input(key='num_contrato', size=(20, 1), font=(18), visible=False), sg.Text(' ', visible=False),
             sg.Text('Valor - R$', font=('Arial', 14, 'bold'), visible=False),
             sg.Input(key='valor_contrato', size=(12, 1), font=(18), visible=False), sg.Text('  ', visible=False),
             sg.Text('Data:', font=('Arial', 14, 'bold'), visible=False),
             sg.Input(key='data_contrato', size=(12, 1), font=(18), visible=False),
             sg.Button(add, size=(5, 1), font=('Arial', 10, 'bold'), tooltip=('  Adicionar outro contrato  '),
                       visible=False)],
            [sg.HorizontalSeparator(color='black')],
            # sg.Checkbox('Anexar Ofício', key='check_oficio', size=(70, 70),  font=('Arial', 12, 'bold')),
            [sg.Checkbox('Anexar Senha de Acesso', key='check_senha', size=(70, 70), font=('Arial', 12, 'bold'))],
            [sg.Checkbox('Anexar Ofício', key='check_oficio', size=(70, 70), font=('Arial', 12, 'bold'))],
            [sg.Text('Qtd de Outros Anexos:', font=('Arial', 12, 'bold')),
             sg.Spin([i for i in range(0, 11)], initial_value=1, size=(5, 10), key=('qtd'),
                     font=(18))],
            [sg.Checkbox('Imprimir após enviar', key='check_impressao', size=(70, 70), font=('Arial', 12, 'bold'))],
            [sg.Button('Enviar Email', size=(52, 1), disabled=(False), font=('Arial', 14, 'bold')),
             sg.Button('Voltar', size=(20, 1), button_color=('gray'), font=('Arial', 14, 'bold'))],
        ]
    elif (codigo_email == 7):
        lay = [
            [sg.Button('Malote', size=(10, 1), button_color=('gray'))],

            [sg.Text('Preencha apenas os campos do modelo escolhido', size=(300, 1), font=('Arial', 22, 'bold'),
                     text_color=('red'))],
            # [sg.HorizontalSeparator()],
            [sg.Text('Num. Processo:', font=('Arial', 14, 'bold')), sg.Input(key='num_proc', size=(28, 3), font=(18)),
             sg.Text('obrigatório', font=('Arial', 10), text_color=('red')),
             sg.Text('             Decisão - Fls:', font=('Arial', 14, 'bold')),
             sg.Input(key='fls_dec', size=(10, 3), font=(18))],
            [sg.Text('Requerente:       ', font=('Arial', 14, 'bold'), visible=False),
             sg.Input(key='nome_autor', size=(70, 2), font=(18), visible=False)],
            [sg.Text('RG:                       ', font=('Arial', 14, 'bold'), visible=False),
             sg.Input(key='rg_autor', size=(20, 2), font=(18), visible=False), sg.Text('         ', visible=False),
             sg.Radio('CPF:', 'tp_doc_autor', key='docm_cpf', default=True, font=('Arial', 14, 'bold'), visible=False),
             sg.Radio('CNPJ:', 'tp_doc_autor', key='docm_cnpj', font=('Arial', 14, 'bold'), visible=False),
             sg.Input(key='cpf_autor', size=(22, 2), font=(18), visible=False)],
            [sg.Text('Requerido:         ', font=('Arial', 14, 'bold'), visible=False),
             sg.Input(key='nome_reu', size=(70, 2), font=(18), visible=False)],
            [sg.Text('RG:                       ', font=('Arial', 14, 'bold'), visible=False),
             sg.Input(key='rg_reu', size=(20, 2), font=(18), visible=False), sg.Text('         ', visible=False),
             sg.Radio('CPF:', 'tp_doc_reu', key='doc_cpf', font=('Arial', 14, 'bold'), visible=False),
             sg.Radio('CNPJ:', 'tp_doc_reu', key='doc_cnpj', default=True, font=('Arial', 14, 'bold'), visible=False),
             sg.Input(key='cnpj_reu', size=(22, 1), font=(18), visible=False)],
            [sg.Text('Contrato:            ', font=('Arial', 14, 'bold'), visible=False),
             sg.Input(key='num_contrato', size=(20, 1), font=(18), visible=False), sg.Text(' ', visible=False),
             sg.Text('Valor - R$', font=('Arial', 14, 'bold'), visible=False),
             sg.Input(key='valor_contrato', size=(12, 1), font=(18), visible=False), sg.Text('  ', visible=False),
             sg.Text('Data:', font=('Arial', 14, 'bold'), visible=False),
             sg.Input(key='data_contrato', size=(12, 1), font=(18), visible=False),
             sg.Button(add, size=(5, 1), font=('Arial', 10, 'bold'), tooltip=('  Adicionar outro contrato  '),
                       visible=False)],
            [sg.HorizontalSeparator(color='black')],
            # sg.Checkbox('Anexar Ofício', key='check_oficio', size=(70, 70),  font=('Arial', 12, 'bold')),
            [sg.Checkbox('Anexar Senha de Acesso', key='check_senha', size=(70, 70), font=('Arial', 12, 'bold'))],
            [sg.Checkbox('Anexar Ofício', key='check_oficio', size=(70, 70), font=('Arial', 12, 'bold'))],
            [sg.Text('Qtd de Outros Anexos:', font=('Arial', 12, 'bold')),
             sg.Spin([i for i in range(0, 11)], initial_value=1, size=(5, 10), key=('qtd'),
                     font=(18))],
            [sg.Checkbox('Imprimir após enviar', key='check_impressao', size=(70, 70), font=('Arial', 12, 'bold'))],
            [sg.Button('Enviar Email', size=(52, 1), disabled=(False), font=('Arial', 14, 'bold')),
             sg.Button('Voltar', size=(20, 1), button_color=('gray'), font=('Arial', 14, 'bold'))],
        ]
    return sg.Window('Emails Diversos', layout=lay, size=(905, 480),  finalize=True)
   #("%s%s" % (abrev, codigo_email))






#-------------------------------------------------------
janela1, janela2 = janela_principal(), None

while True:
    window, event, values = sg.read_all_windows()

    #Eventos e ações da janela Principal
    if window == janela1 and event == sg.WINDOW_CLOSED:
        break

    elif window == janela1 and event == 'Solicitação de Parecer':
        janela1['tit1'].update('Modelo Escolhido', font = ('Arial', 18), text_color = ('red'))
        janela1['destinatario'].update(textos.get_email(1).__getitem__(0))
        janela1['assunt'].update(textos.get_email(1).__getitem__(1))
        janela1['texto_email'].update(textos.get_email(1).__getitem__(2))
        janela1['req1'].update('Informar número do processo', font = ('Arial', 12), text_color = ('red'))
        janela1['req2'].update('Informar fls. da Decisão', font = ('Arial', 12), text_color = ('red'))
        janela1['req3'].update('Selecionar o campo "Senha de acesso", previamente salva', font = ('Arial', 12), text_color = ('red'))
        codigo_email=1

    elif window == janela1 and event == 'Encaminhamento de Ofício':
        janela1['destinatario'].update(textos.get_email(2).__getitem__(0))
        janela1['assunt'].update(textos.get_email(2).__getitem__(1))
        janela1['texto_email'].update(textos.get_email(2).__getitem__(2))
        janela1['req1'].update('Informar número do processo')
        janela1['req2'].update('Selecionar o campo "Anexar Oficio", previamente salvo')
        janela1['req3'].update('')
        codigo_email=2
    elif window == janela1 and event == 'Distribuição de CP via Malote Digital':
        janela1['destinatario'].update(textos.get_email(3).__getitem__(0))
        janela1['assunt'].update(textos.get_email(3).__getitem__(1))
        janela1['texto_email'].update(textos.get_email(3).__getitem__(2))
        janela1['req1'].update('Informar número do processo')
        janela1['req2'].update('Selecionar o campo "Anexar Oficio", previamente salvo')
        janela1['req3'].update('')
        codigo_email=3
    elif window == janela1 and event == 'Devolução de CP via Malote Digital':
        janela1['destinatario'].update(textos.get_email(4).__getitem__(0))
        janela1['assunt'].update(textos.get_email(4).__getitem__(1))
        janela1['texto_email'].update(textos.get_email(4).__getitem__(2))
        janela1['req1'].update('Informar número do processo')
        janela1['req2'].update('Selecionar o campo "Anexar Oficio", previamente salvo')
        janela1['req3'].update('')
        codigo_email=4
    elif window == janela1 and event == 'INSS':
        janela1['destinatario'].update(textos.get_email(5).__getitem__(0))
        janela1['assunt'].update(textos.get_email(5).__getitem__(1))
        janela1['texto_email'].update(textos.get_email(5).__getitem__(2))
        janela1['req1'].update('Informar número do processo')
        janela1['req2'].update('Selecionar o campo "Anexar Oficio", previamente salvo')
        janela1['req3'].update('')
        codigo_email=5
    elif window == janela1 and event == 'Justiça Gratuita':
        janela1['destinatario'].update(textos.get_email(6).__getitem__(0))
        janela1['assunt'].update(textos.get_email(6).__getitem__(1))
        janela1['texto_email'].update(textos.get_email(6).__getitem__(2))
        janela1['req1'].update('Informar número do processo')
        janela1['req2'].update('Informar fls. da Decisão')
        janela1['req3'].update('Selecionar o campo "Anexar Senha de acesso", previamente salvo')
        codigo_email=6
    elif window == janela1 and event == 'Estimativa de Honorários':
        janela1['destinatario'].update(textos.get_email(7).__getitem__(0))
        janela1['assunt'].update(textos.get_email(7).__getitem__(1))
        janela1['texto_email'].update(textos.get_email(7).__getitem__(2))
        janela1['req1'].update('Informar número do processo')
        janela1['req2'].update('Informar fls. da Decisão')
        janela1['req3'].update('Selecionar o campo "Anexar Senha de acesso", previamente salvo')
        codigo_email=7

    elif window == janela1 and event == 'Folha de Rosto':
        para = "nao se aplica"
        assunto = "Nao se aplica"
        texto_modelo_email = "Não se aplica"
        janela1['assunt'].update(assunto)
        janela1['texto_email'].update(texto_modelo_email)
        janela1['destinatario'].update(para)



#------------------------------------------------------------------------------
    #Eventos e ações da Janela Email
    elif window == janela1 and event == 'Selecionar':
        janela2 = janela_scpc()
        janela1.hide()
    if window == janela2 and event == sg.WINDOW_CLOSED:
        break
    if window == janela2 and event =='Voltar':
        janela2.hide()
        janela1.un_hide()

    if window == janela2 and event == '+':
        if cursor.confirm('Deseja realmente inserir outro contrato?', 'Confirmação') == 'OK':
            #messagebox.askyesnocancel('pergunta', 'Deseja, realmente, inserir outro contrato?')
            num_contrato = values['num_contrato']
            num_contrato_bold = num_contrato
            valor_contrato = values['valor_contrato']
            data_contrato = values['data_contrato']
            contratos.insert(i,[num_contrato, valor_contrato, data_contrato])
            i += 1
            window['num_contrato'].update('')
            window['valor_contrato'].update('')
            window['data_contrato'].update('')
            window['num_contrato'].SetFocus()
    if window == janela2 and event == 'Enviar Email':
        num_proc = values['num_proc']
        fls_dec = values['fls_dec']
        nome_autor = values['nome_autor']
        rg_autor = values['rg_autor']
        docm_cpf = values['docm_cpf']
        docm_cnpj = values['docm_cnpj']
        cpf_autor = values['cpf_autor']
        nome_reu = values['nome_reu']
        doc_cpf = values['doc_cpf']
        doc_cnpj = values['doc_cnpj']
        rg_reu = values['rg_reu']
        cnpj_reu = values['cnpj_reu']
        num_contrato = values['num_contrato']
        valor_contrato = values['valor_contrato']
        data_contrato = values['data_contrato']
        qtd = values['qtd']
        qtd_string = str(qtd)
        imprimir = values['check_impressao']
        senha = values['check_senha']
        oficio = values['check_oficio']
        contratos.insert(i, [num_contrato, valor_contrato, data_contrato])
        janela2.hide()

        if diversos.get_capslock_state() == 1:
            cursor.press('capslock')


        diversos.get_image('nova_msg', 4, 5, 5, 250, 300)
        sleep(2.5)
        if (diversos.exists_image('enviar', 4, 10,100,800,300)) =='v':
            print('verdadeiro')
        else:
            print('falso')

        sleep(0.5)
        cursor.write(textos.get_email(codigo_email).__getitem__(0))
        sleep(0.5)
        #cursor.press("enter")
        sleep(0.1)
        cursor.hotkey("tab")
        sleep(0.1)
        cursor.hotkey("tab")
        sleep(0.1)
        diversos.get_image('campo_assunto', 4, 500, 250, 400, 350)
        #cursor.hotkey("tab")
        sleep(0.1)
        #cursor.hotkey("tab")
        sleep(0.5)
        #assunto
        pyperclip.copy(textos.get_email(codigo_email).__getitem__(1))
        sleep(0.2)
        cursor.hotkey('ctrl', 'v')
        sleep(0.2)
        cursor.write(num_proc)
        sleep(0.5)
        cursor.hotkey("tab")
        sleep(0.5)
        pyperclip.copy('Prezado(a) Senhor(a)!')
        sleep(0.2)
        cursor.hotkey('ctrl', 'v')
        sleep(0.2)
        cursor.press("enter")
        sleep(0.2)
        cursor.press("enter")
        sleep(0.2)
        if(codigo_email==1):
            pyperclip.copy('Com meus cumprimentos, encaminho a Vossa Senhoria, senha de acesso aos autos acima mencionados, solicitando parecer conforme Decisão de fls. ' +fls_dec)
        elif(codigo_email==2):
            pyperclip.copy('Com meus cumprimentos, encaminho cópia(s) de ofício expedido nos autos acima mencionados, solicitando as devidas providências.')
        elif (codigo_email == 3):
            pyperclip.copy('Com meus cumprimentos, encaminho Carta Precatória expedida nos autos '+num_proc+'(nosso), para encaminhamento via malote digital, à Comarca de...nome da Comarca.')
        elif (codigo_email == 4):
            pyperclip.copy('Com meus cumprimentos, encaminho cópias das peças produzidas nos autos de nº '+num_proc+' (nosso), para devolução, via malote digital, à Comarca de '+num_contrato+', referente à Carta Precatória nº origem - '+fls_dec)
        elif (codigo_email == 5):
            pyperclip.copy('Com meus cumprimentos, encaminho cópias da Petição inicial, Sentença, Acórdão e Decisão(ões) proferidas nos autos acima mencionados, para implantação do benefício concedido ao autor, Sr(a). '+nome_autor+', RG '+rg_autor+ ', CPF'+cpf_autor+'.')
            cursor.hotkey('ctrl', 'v')
            cursor.press('enter')
            pyperclip.copy('Solicitamos, ainda, a comunicação com este juízo quando cumprida a referida determinação anexa.')
        elif (codigo_email == 6):
            pyperclip.copy('Com meus cumprimentos, intimo Vossa Senhoria acerca de sua nomeação nos autos acima mencionados, para que manifeste se aceita o encargo, ciente de que os honorários periciais serão suportados exclusivamente pela Defensoria Pública conforme Decisão de fls. '+fls_dec)
        elif (codigo_email == 7):
            pyperclip.copy('Com meus cumprimentos, intimo Vossa Senhoria acerca de sua nomeação nos autos acima mencionados, para que estime seus honorários nos termos da Decisão de fls. '+fls_dec)
        cursor.hotkey('ctrl', 'v')
        sleep(0.3)

        cursor.press('enter')
        cursor.press('enter')
        cursor.write('Att,')

        #contratos.pop()
        if senha == 1:
            diversos.anexar_senha(num_proc)
        else:
            print('nao marcou anexar senha')
        if oficio == 1:
            diversos.anexar_oficio(num_proc)
        else:
            print('nao marcou anexar oficio')

        #diversos.anexar(textos.get_email(1).__getitem__(3))
        if(textos.get_email(1).__getitem__(3)==0):
            print('é igual a 0. Entao vou usar o selecionado')
            diversos.anexar(qtd)
        else:
            print('nao é 0, entao usei a referencia do textos')
            diversos.anexar(textos.get_email(1).__getitem__(3))

        #diversos.btn_enviar()
        #janela1.un_hide()

        if imprimir == 1:
            diversos.imp_email_enviado()
        else:
            print('nao marcou a impressao')
        sleep(2)
        diversos.digitalizar(num_proc, '724', '1')
    #janela1.un_hide()

exit()