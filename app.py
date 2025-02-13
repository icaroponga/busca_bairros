import streamlit as st
from geopy.geocoders import Nominatim
from geopy.distance import geodesic

# Lista de lojas com números e bairros
lojas = [
    {"numero": "01", "bairro": "Joaquim Távora", "endereco": "Ildefonso Albano - Joaquim Távora"},
    {"numero": "02", "bairro": "Serrinha", "endereco": "Av Paranjana - Serrinha"},
    {"numero": "03", "bairro": "Parque Manibura", "endereco": "Oliveira Paiva - Parque Manibura"},
    {"numero": "04", "bairro": "Genibaú", "endereco": "Henrique Jorge - Genibaú"},
    {"numero": "05", "bairro": "José Walter", "endereco": "José Walter"},
    {"numero": "06", "bairro": "Centro", "endereco": "Pinto Madeira - Centro"},
    {"numero": "07", "bairro": "Itapery", "endereco": "CD Itapery - Itapery"},
    {"numero": "08", "bairro": "Vila Velha", "endereco": "Vila Velha"},
    {"numero": "09", "bairro": "Maracanaú", "endereco": "Maracanaú"},
    {"numero": "10", "bairro": "Cidade dos Funcionários", "endereco": "Julio Lima - Cidade dos Funcionários"},
    {"numero": "11", "bairro": "Meireles", "endereco": "Virgílio Távora - Meireles"},
    {"numero": "12", "bairro": "Barra do Ceará", "endereco": "Castelo Branco - Barra do Ceará"},
    {"numero": "13", "bairro": "Centro", "endereco": "J da Penha - Centro"},
    # (adicione as outras lojas aqui)
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
        return None
    
    # Cria uma lista de lojas com suas distâncias e tempos em relação ao bairro consultado
    lojas_com_distancia = []
    for loja in lojas:
        coord_loja = obter_coordenadas(loja['bairro'])
        if coord_loja:
            distancia = calcular_distancia(coord_bairro, coord_loja)
            tempo = calcular_tempo(distancia, velocidade_kmh)
            lojas_com_distancia.append((loja, distancia, tempo))
    
    # Ordena as lojas pela distância e pega as 5 mais próximas
    lojas_com_distancia = sorted(lojas_com_distancia, key=lambda x: x[1])[:5]
    
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