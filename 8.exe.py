import pandas  as pd 
from openpyxl import load_workbook

def calcular_imc(Peso,Altura ):
    """calcula o imc dado Peso (kg) e Altura (m)"""
    return round (Peso /(Altura **2), 2)    

def classifcar_imc(imc):
   """classica o IMC  de acordo com as faixas padrão"""
   if imc <18.5:
       return "abaixo do peso"
   elif 18.5 <=imc < 24.9:
       return "peso normal"
   elif 25 <= imc <29.9:
       return "sobrepeso"
   elif 30 <= imc < 34.9:
       return "obesidade grau 1"
   elif 35 <= imc <39.9:
       return "obesidade grau 2"
   else:
       return"obesidade grau 3"
   
   #Nome dos arquivo da planilha 
arquivo = "dados_pessoas.xlsx"

try:

    #ler a planilha e remover espaços extras nos nomes das colunas 
    dados =pd.read_excel(arquivo)
    dados.columns = dados.columns.astype(str).str.strip()
    
    #Verificar se as colunas necessarias existem 

    if not{'Nome', 'Peso' , 'Altura'}.issubset (dados.columns):
        print("o arquivo excel deve conter as colunas: Nome , Peso e Altura.")
    else:

    #coverter para valores numéricos invalidos 
        dados['Peso'] = pd.to_numeric(dados['Peso'], errors='coerce')
        dados['Altura'] = pd.to_numeric(dados['Altura'], errors='coerce')

        #Removewr linhas com valores invalidos 
        dados= dados.dropna(subset=['Peso' , 'Altura'])


        #Calcular o IMC e classificação 
        dados['IMC'] = dados.apply(lambda x: calcular_imc(x['Peso'] , x['Altura']), axis=1)
        dados['Classificação'] = dados['IMC'].apply (classifcar_imc)

        #sobrescrever a planilha original mantendo os dados e adicionando as colunas novas 

        with pd.ExcelWriter (arquivo, engine ='openpyxl' , mode='w')as writer:
            dados.to_excel(writer, sheet_name="pessoas", index=False)

            print(f"Resultados adicionados ao arquivo '{arquivo}',")
except FileNotFoundError:

    print(f"Erro: O arquivo'{arquivo}' não foi encontrado.")
except Exception as e:
    print(f"ocorreu um erro: {e}")


