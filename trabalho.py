nomes = open('nome.txt','w')
idades = open('idade.txt','w')
enderecos = open('endereco.txt','w')
emails = open('email.txt','w')
telefones = open('telefone.txt','w')
nome = input("Nome:")
idade = input("Idade:")
endereco = input("Cidade :")
estado = input("Sigla do estado:")
email = input("Email:")
telefone = input("Telefone:")
nomes.write(nome + "\n")
idades.write(idade + "\n")
enderecos.write(endereco + " - " + estado + "\n")
emails.write(email + "\n")
telefones.write(telefone + "\n")
nomes.close()
idades.close()
enderecos.close()
emails.close()
telefones.close()

experiencia = open('experiencia.txt','w')
resposta = 'S'
while resposta.upper() == 'S':
    exp = input("Digite uma experiência profissional:")
    experiencia.write("<li>" + exp + "</li>\n")
    resposta = input("Deseja incluir mais experiências S/N?")
experiencia.close()

cursos = open('curso.txt','w')
cursandos = open('cursando.txt','w')
curso = input("Curso: ")
cursando = input("Ainda está cursando? (S/N): ")
if cursando.upper() == "S":
    period = input("Qual período você está cursando? ")
    situacao = "Cursando - " + period  + " período"
else:
    situacao = "Concluído"
cursos.write(curso + "\n")
cursandos.write(situacao + "\n")
cursos.close()
cursandos.close()

idiomas = open('idiomas.txt','w')
resposta = 'S'
while resposta.upper() == 'S':
    idioma = input("Digite o idioma que você fala:")
    nivel = input("Digite o nível de proficiência (Básico, Intermediário, Avançado): ")
    idiomas.write("<li>" + idioma + " - " + nivel + "</li>\n")
    resposta = input("Deseja incluir mais idiomas S/N?")
idiomas.close()


nomess = open('nome.txt', 'r')
idadess = open('idade.txt', 'r')
endereçoss = open('endereco.txt', 'r')
emailss = open('email.txt', 'r')
telefoness = open('telefone.txt', 'r')
cursoss = open('curso.txt','r')
cursandoss = open('cursando.txt','r')
experienciass = open('experiencia.txt', 'r')
idiomass = open('idiomas.txt','r')

html = """
<!DOCTYPE html>
<html lang="pt-br">
<head>
<meta charset="UTF-8">
<title>Currículo</title>
<style>
    body {
        font-family: 'Trebuchet MS', sans-serif;
        background-color: #f0f2f5;
        margin: 0;
        padding: 0;
    }
    .container {
        max-width: 700px;
        margin: 30px auto;
        background-color: #ffffff;
        border-radius: 10px;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.267);
        overflow: hidden;
    }
    .cabecalho {
        background-color: #27ae5f69;
        color: #000000;
        padding: 25px;
        display: flex;
        align-items: center;
    }
    .cabecalho img {
        width: 110px;
        height: 110px;
        border-radius: 50%;
        border: 3px solid #000000;
        object-fit: cover;
        margin-right: 20px;
        background-color: #eaeaea;
    }
    .cabecalho h1 {
        margin: 0;
        font-size: 26px;
    }
    .cabecalho p {
        margin: 4px 0 0 0;
        font-size: 14px;
        color: #000000;
    }
    .secao {
        padding: 20px 25px;
        border-bottom: 1px solid #e9e9e9;
    }
    .secao h2 {
        color: #2c3e50;
        border-left: 5px solid #27ae60;
        padding-left: 10px;
        font-size: 18px;
    }
    ul {
        padding-left: 20px;
    }
    li {
        margin-bottom: 6px;
    }
    .secao ul {
    list-style-type: none;
    padding: 0;
    }

    .secao li {
        background-color: rgba(0, 0, 0, 0.047);
        padding: 12px 15px;
        margin-bottom: 10px;
        border-radius: 8px;
        border-left: 4px solid #27ae60;
    }
</style>
</head>
<body>

<div class="container">

    <div class="cabecalho">
        <img src="fotocr.avif" alt="Foto de perfil">
        <div>
            <h1>""" + nomess.read() + """</h1>
            <p>Idade: """ + idadess.read() + """ | Cidade: """ + endereçoss.read() + """</p>
            <p>Email: """ + emailss.read() + """ | Telefone: """ + telefoness.read() + """</p>
        </div>
    </div>

    <div class="secao">
        <h2>Informações Profissionais</h2>
        <p><strong>Curso:</strong> """ + cursoss.read() + """ (""" + cursandoss.read() +""")</p>
        <p><strong>Experiências:</strong></p>
        <ul>
            """ + experienciass.read() + """
        </ul>
    </div>

    <div class="secao">
        <h2>Idiomas</h2>
        <ul>
""" + idiomass.read() + """
        </ul>
    </div>

</div>

</body>
</html>
"""

nomess.close()
idadess.close()
endereçoss.close()
emailss.close()
telefoness.close()
cursoss.close()
cursandoss.close()
experienciass.close()
idiomass.close()

arquivo = open("curriculo.html", "w", encoding="utf-8")
arquivo.write(html)
arquivo.close()