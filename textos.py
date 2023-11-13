import diversos

#para=''
#assunto=''
#conteudo=''
saudacao='Prezado(a) Senhor(a)!'

def get_email(codigo):
    if(codigo==1):
        #para='cartorioriitaqua@terra.com.br'
        para = 'qualquercoisa@terra.com.br'
        assunto='Solicitação de Parecer - Autos: '
        conteudo='Com meus cumprimentos, encaminho a Vossa Senhoria, senha de acesso aos autos acima mencionados, solicitando parecer conforme Decisão de fls. '
        qtd_anexos=0
    elif (codigo == 2):
        para = 'unidade_mogicruzes@defensoria.sp.def.br'
        assunto = 'Encaminhamento de Ofício - Autos: '
        conteudo = 'Com meus cumprimentos, encaminho cópia(s) de ofício expedido nos autos acima mencionados, solicitando as devidas providências.'
        qtd_anexos = 0
    elif (codigo == 2):
        para = 'unidade_mogicruzes@defensoria.sp.def.br'
        assunto = 'Encaminhamento de Ofício - Autos: '
        conteudo = 'Com meus cumprimentos, encaminho cópia(s) de ofício expedido nos autos acima mencionados, solicitando as devidas providências.'
        qtd_anexos = 0
    elif (codigo == 3):
        para = 'itaquaquecetubaggg'
        assunto = 'Carta Precatória para distribuição via Malote Digital - Autos: '
        conteudo = 'Com meus cumprimentos, encaminho cópia(s) de carta precatória expedida nos autos acima mencionados(nosso), para envio/distribuição junto à Comarca de '
        qtd_anexos = 0
    elif (codigo == 4):
        para = 'itaquaquecetubacp'
        assunto = 'Devolução de Carta Precatória via malote digital - Autos: '
        conteudo = 'Com meus cumprimentos, encaminho cópias das peças produzidas nos autos de nº XXXXXXXXX(nosso)  para devolução via  Malote Digital à 2ª Vara Cível de Paranavaí -PROJUDI - TJPR - Referente ao processo de  origem nº XXXXXXXXX'
        qtd_anexos = 0
    elif (codigo == 5):
        para = 'elabgexgru'
        assunto = 'Implantação de Benefício - Autos: '
        conteudo = 'Com meus cumprimentos, encaminho cópias da petição inicial, Sentença, Acórdão e Decisão(ões) proferidas nos autos acima mencionados, para implantação do benefício concedido aos autor, Sr(a). XXXXX, RG XXXX, CPF XXXX. Solicitamos, ainda, a comunicação com este juízo quando cumprida a referida determinação anexa.'
        qtd_anexos = 0
    elif (codigo == 6):
        para = 'jairdsmg@gmail.com'
        assunto = 'Intimação de Nomeação - Autos: '
        conteudo = 'Com meus cumprimentos, intimo Vossa Senhoria acerca de sua nomeação nos autos acima mencionados, para que manifeste se aceita o encargo, ciente de que os honorários periciais serão suportados exclusivamente pela Defensoria Pública conforme Decisão de fls. '
        qtd_anexos = 0
    elif (codigo == 7):
        para = 'jairdsmg@gmail.com'
        assunto = 'Intimação de Nomeação - Autos: '
        conteudo = 'Com meus cumprimentos, intimo Vossa Senhoria acerca de sua nomeação nos autos acima mencionados, para que estime seus honorários nos termos da Decisão de fls. '
        qtd_anexos = 0

    return(para,assunto,conteudo,qtd_anexos)