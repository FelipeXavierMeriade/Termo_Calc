import streamlit as st

# Configuração da aplicação (layout wide, título e favicon)
st.set_page_config(
    page_title="Oficina de Termodinâmica & Consumo Elétrico",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Inicialização da tarifa no session_state (único ponto de partida padrão: R$ 0,85/kWh)
if "tarifa_kwh" not in st.session_state:
    st.session_state.tarifa_kwh = 0.85

# Definição das páginas da aplicação usando st.navigation e st.Page
pages = [
    st.Page(
        "app_pages/home.py",
        title="Início & Tarifas",
        icon=":material/home:",
        default=True,
        help="Página principal da oficina com inserção da tarifa e os 4 cartões clicáveis.",
    ),
    st.Page(
        "app_pages/chaleira.py",
        title="1. Chaleira & Cafeteira",
        icon=":material/coffee_maker:",
        url_path="chaleira",
        help="Calculadora de calor, consumo e custo para aquecer 1 litro de água.",
    ),
    st.Page(
        "app_pages/chuveiro.py",
        title="2. Chuveiro Elétrico",
        icon=":material/shower:",
        url_path="chuveiro",
        help="Calculadora de consumo de banho com 3 classes de potência e temperatura.",
    ),
    st.Page(
        "app_pages/geladeira.py",
        title="3. Geladeira no Mês",
        icon=":material/kitchen:",
        url_path="geladeira",
        help="Calculadora do custo mensal e calor movimentado no ciclo de refrigeração.",
    ),
    st.Page(
        "app_pages/economia.py",
        title="4. Como Economizar",
        icon=":material/lightbulb:",
        url_path="economia",
        help="Instruções práticas para economizar dinheiro em cada situação.",
    ),
]

# Configura o sistema de navegação da barra lateral
nav = st.navigation(pages, position="sidebar")

# Barra lateral com resumo permanente da oficina (sem widgets conflitantes)
with st.sidebar:
    st.markdown("### ⚡ Oficina de Termodinâmica")
    st.caption("Consumo Energético & Custos Residenciais")
    st.divider()

    # Exibição da tarifa ativa em tempo real (atualizada instantaneamente por qualquer página)
    st.metric(
        label="Tarifa Ativa na Oficina",
        value=f"R$ {st.session_state.tarifa_kwh:.2f} / kWh",
        help="Defina ou altere este valor na página inicial ou em qualquer calculadora.",
    )

    st.divider()
    
    # Constantes Físicas Rápidas
    st.markdown("#### 🔬 Constantes Físicas")
    st.markdown(
        r"""
        - $c_{\text{água}} = 4,184\text{ kJ}/(\text{kg}\cdot^\circ\text{C})$
        - $\rho_{\text{água}} = 1,0\text{ kg/L}$
        - $1\text{ kWh} = 3.600\text{ kJ}$
        - $1\text{ W} = 1\text{ J/s} = 0,001\text{ kJ/s}$
        """
    )
    st.divider()
    st.caption("Projeto de Extensão Universitária • Engenharia & Física Aplicada")

# Executa a página selecionada
nav.run()
