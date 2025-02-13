import streamlit as st
from geopy.geocoders import Nominatim
from geopy.distance import geodesic


# Listas fornecidas (simplificadas para exemplo)
bairros_fortaleza = [ "Álvaro Weyne", "Floresta", "Jacarecanga", "Jardim América", "Cidade 2000", "Bom Futuro", "Panamericano", "Demócrito Rocha", "Ellery", "Conjunto Ceará II", 
                     "Barra do Ceará", "Couto Fernandes", "Centro", "Farias Brito", "Carlito Pamplona", "Jardim Guanabara", "Conjunto Ceará I", "Mucuripe", "Parreão", "Cristo Redentor",
                      "Vila Peri", "Joaquim Távora", "Dionísio Torres", "Vila Velha", "Genibaú", "Parque Araxá", "Amadeu Furtado", "Monte Castelo", "Presidente Kennedy", "Antônio Bezerra",
                      "Vicente Pinzón", "José Bonifácio", "São Gerardo", "Quintino Cunha", "Cidade dos Funcionários", "Vila União", "Montese", "Dias Macedo", "Parangaba", "Pici",
                      "João XXIII", "Fátima", "Parque Manibura", "Manoel Sátiro", "Cocó", "Autran Nunes", "Serrinha", "Meireles", "Tauape", "Conjunto Esperança", "Bonsucesso",
                      "Jóquei Clube", "Barroso", "Damas", "Henrique Jorge", "Parque Dois Irmãos", "Olavo Oliveira", "Novo Mondubim", "Jardim das Oliveiras", "Messejana", "Praia de Iracema",
                      "Maraponga", "Alto da Balança", "Rodolfo Teófilo", "Aldeota", "Jardim Iracema", "Papicu", "Engenheiro Luciano Cavalcante", "Bom Jardim", "Itaperi", "Conjunto Palmeiras",
                      "Coaçu", "Guajeru", "Cais do Porto", "Benfica", "Edson Queiroz", "Jardim Cearense", "Varjota", "Passaré", "Boa Vista / Castelão", "Jangurussu", "Prefeito José Walter",
                      "Dom Lustosa", "Aeroporto", "Aracapé", "Sapiranga / Coité", "Curió", "Lagoa Redonda", "Aerolândia", "Cajazeiras", "José de Alencar", "Parque Santa Maria", "Salinas",
                      "Bela Vista", "Pirambu", "Cambeba", "Planalto Ayrton Senna", "Granja Portugal", "Ancuri", "Parquelândia", "Parque Santa Rosa", "Guararapes", "Mondubim", "Paupina",
                      "Itaoca", "Granja Lisboa", "Praia do Futuro II", "Parque Iracema", "Parque São José", "Canindezinho", "São Bento", "Padre Andrade", "Rachel de Queiroz", "Praia do Futuro I",
                      "Siqueira", "Manuel Dias Branco", "Parque Presidente Vargas", "Moura Brasil", "Pedras", "Sabiaguaba", "De Lourdes"

]

# Lista de lojas com números e bairros
lojas = [
    {"numero": "01", "bairro": "Joaquim Távora"},
    {"numero": "02", "bairro": "Serrinha"},
    {"numero": "03", "bairro": "Parque Manibura"},
    {"numero": "04", "bairro": "Genibaú"},
    {"numero": "05", "bairro": "José Walter"},
    {"numero": "06", "bairro": "Centro"},
    {"numero": "07", "bairro": "Itapery"},
    {"numero": "08", "bairro": "Vila Velha"},
    {"numero": "09", "bairro": "Maracanaú"},
    {"numero": "10", "bairro": "Cidade dos Funcionários"},
    {"numero": "11", "bairro": "Meireles"},
    {"numero": "12", "bairro": "Barra do Ceará"},
    {"numero": "13", "bairro": "Centro"},
    {"numero": "14", "bairro": "Fátima"},
    {"numero": "15", "bairro": "Siqueira"},
    {"numero": "16", "bairro": "Messejana"},
    {"numero": "17", "bairro": "Messejana"},
    {"numero": "18", "bairro": "Novo Mondubim"},
    {"numero": "19", "bairro": "Serrinha"},
    {"numero": "20", "bairro": "Cidade dos Funcionários"},
    {"numero": "21", "bairro": "Dom Lustosa"},
    {"numero": "22", "bairro": "Dionísio Torres"},
    {"numero": "23", "bairro": "Siqueira"},
    {"numero": "24", "bairro": "Papicu"},
    {"numero": "25", "bairro": "Centro"},
    {"numero": "26", "bairro": "Aldeota"},
    {"numero": "27", "bairro": "Aldeota"},
    {"numero": "28", "bairro": "Parquelândia"},
    {"numero": "29", "bairro": "Fátima"},
    {"numero": "30", "bairro": "Aldeota"},
    {"numero": "31", "bairro": "Mondubim"},
    {"numero": "32", "bairro": "Maraponga"},
    {"numero": "33", "bairro": "Presidente Kennedy"},
    {"numero": "34", "bairro": "Sapiranga"},
    {"numero": "35", "bairro": "Jacarecanga"},
    {"numero": "36", "bairro": "Eusébio"},
    {"numero": "37", "bairro": "Serrinha"},
    {"numero": "38", "bairro": "Messejana"},
    {"numero": "39", "bairro": "Mondubim"},
    {"numero": "40", "bairro": "Damas"},
    {"numero": "41", "bairro": "Luciano Cavalcante"},
    {"numero": "42", "bairro": "Joaquei Clube"},
    {"numero": "43", "bairro": "Fátima"},
    {"numero": "44", "bairro": "Montese"},
    {"numero": "45", "bairro": "Cidade dos Funcionários"},
    {"numero": "46", "bairro": "José Walter"},
    {"numero": "47", "bairro": "Montese"},
    {"numero": "48", "bairro": "Distrito Industrial 1 - Maracanau"}
]

# Função para obter as coordenadas geográficas de um bairro
def obter_coordenadas(bairro):
    geolocator = Nominatim(user_agent="bairro_locator")
    location = geolocator.geocode(bairro + ", Fortaleza, Ceará")
    if location:
        return (location.latitude, location.longitude)
    return None

# Função para calcular a distância entre duas coordenadas
def calcular_distancia(coord1, coord2):
    return geodesic(coord1, coord2).km

def calcular_tempo(distancia_km, velocidade_kmh):
    # Tempo em horas = Distância / Velocidade
    tempo_horas = distancia_km / velocidade_kmh
    # Convertendo o tempo para minutos
    tempo_minutos = tempo_horas * 60
    return tempo_minutos

# Função para encontrar as lojas mais próximas ao bairro consultado
def encontrar_lojas_proximas(bairro_query, lojas, velocidade_kmh=40):
    # Obtém as coordenadas do bairro consultado
    coord_bairro = obter_coordenadas(bairro_query)
    
    if not coord_bairro:
        print("Bairro não encontrado.")
        return []
    
    # Cria uma lista de lojas com suas distâncias e tempos em relação ao bairro consultado
    lojas_com_distancia = []
    for loja in lojas:
        coord_loja = obter_coordenadas(loja['bairro'])
        if coord_loja:
            distancia = calcular_distancia(coord_bairro, coord_loja)
            tempo = calcular_tempo(distancia, velocidade_kmh)
            lojas_com_distancia.append((loja, distancia, tempo))
    
    # Ordena as lojas pela distância e pega as 5 mais próximas
    lojas_com_distancia = sorted(lojas_com_distancia, key=lambda x: x[1])[:30]
    
    return lojas_com_distancia


# Streamlit app
st.title("Busca de Lojas mais Próximas")
st.markdown("""
    ## Encontre as 5 lojas mais próximas do bairro de Fortaleza!
""")

# Entrada do usuário para o bairro
bairro_consultado = st.text_input("Digite o nome do bairro:", "Messejana")

# Botão para buscar
if st.button("Buscar Lojas"):
    # Chamando a função para encontrar as lojas
    lojas_encontradas = encontrar_lojas_proximas(bairro_consultado, lojas)

    if lojas_encontradas:
        st.write(f"As 5 lojas mais próximas de **{bairro_consultado}**:")
        for loja, distancia, tempo in lojas_encontradas:
            st.write(f"**{loja['numero']} - {loja['bairro']}** | Distância: {distancia:.2f} km | Tempo estimado: {tempo:.2f} minutos")
    else:
        st.write(f"Nenhuma loja encontrada próxima ao bairro **{bairro_consultado}**.")