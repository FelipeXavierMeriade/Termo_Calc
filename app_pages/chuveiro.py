import streamlit as st
import pandas as pd
from utils.thermo_calc import calcular_chuveiro, CALOR_ESPECIFICO_AGUA

def render_chuveiro_page():
    st.markdown(
    """
    <a href="/" target="_self" style="text-decoration: none; color: inherit;">
        <h1>⚡ Oficina de Termodinâmica Aplicada</h1>
    </a>
    """,
    unsafe_allow_html=True
)
    st.title("🚿 2. Chuveiro Elétrico")
    st.subheader("Consumo de Energia, Calor e Custo do Banho")
    
    st.markdown(
        r"""
        O chuveiro elétrico é tradicionalmente um dos maiores vilões da conta de luz devido à sua altíssima 
        potência instantânea (geralmente entre 5500W e 7500W). A resistência elétrica fica imersa diretamente no 
        fluxo de água contínuo transferindo calor instantaneamente:
        
        $$\dot{Q} = \dot{m} \cdot c \cdot \Delta T \approx P_{\text{efetiva}} \cdot \eta$$
        """
    )
    
    st.divider()

    # Painel de Parâmetros de Entrada
    st.markdown("### 📥 Parâmetros de Entrada")
    
    col_in1, col_in2 = st.columns(2, gap="medium")
    
    with col_in1:
        st.markdown("**a. Temperatura Final da Água (3 Classes de Potência):**")
        opcao_classe = st.radio(
            "Selecione o nível de aquecimento / chave seletora do chuveiro:",
            options=[
                "Potência Alta (Mais quente / Inverno - 100% da potência)",
                "Potência Média (Conforto / Morno / Verão - 65% da potência)",
                "Potência Mínima (Mais próxima do ambiente - 35% da potência)",
            ],
            index=0,
            key="chuveiro_classe_radio",
            help="Define a fração da potência nominal usada para aquecer o fluxo contínuo de água.",
        )
        
        # Mapeamento da classe para cálculo
        if "Alta" in opcao_classe:
            classe_key = "alta"
        elif "Média" in opcao_classe:
            classe_key = "media"
        else:
            classe_key = "minima"

        st.markdown("**b. Tempo Médio de Banho do Usuário (em minutos):**")
        tempo_min = st.number_input(
            "Digite o tempo médio de banho (minutos):",
            min_value=1,
            max_value=60,
            value=12,
            step=1,
            help="Tempo com o registro aberto e o chuveiro ligado.",
            key="input_tempo_chuveiro_val",
        )

    with col_in2:
        st.markdown("**c. Potência do Equipamento (em Watts):**")
        
        if "potencia_chuveiro" not in st.session_state:
            st.session_state.potencia_chuveiro = 5500

        potencia_digitada = st.number_input(
            "Digite a potência nominal do chuveiro (Watts):",
            min_value=1000,
            max_value=10000,
            value=int(st.session_state.potencia_chuveiro),
            step=250,
            help="Potência máxima do chuveiro indicada na embalagem (comuns no Brasil: 4500W, 5500W, 6800W e 7500W).",
            key="input_potencia_chuveiro_val",
        )
        st.session_state.potencia_chuveiro = potencia_digitada
        potencia_equip = potencia_digitada

        # Sugestões rápidas de preenchimento
        st.caption("Preenchimento rápido de modelos comuns:")
        p_cols = st.columns(4)
        for p_col, (p_label, p_val) in zip(p_cols, [("4500 W", 4500), ("5500 W", 5500), ("6800 W", 6800), ("7500 W", 7500)]):
            if p_col.button(p_label, key=f"btn_p_chuv_{p_val}", width="stretch"):
                st.session_state.potencia_chuveiro = p_val
                st.rerun()

        # Tarifa de Energia Elétrica
        tarifa_kwh = float(st.session_state.get("tarifa_kwh", 0.85))
        st.caption(f"💡 Tarifa ativa na oficina: **R$ {tarifa_kwh:.2f} / kWh** (herdada da página inicial)")

    # Parâmetros adicionais expansíveis
    with st.expander("⚙️ Parâmetros Hidráulicos e de Rede (Vazão e Temperatura Ambiente)", expanded=False):
        c_h1, c_h2 = st.columns(2)
        with c_h1:
            vazao = st.slider("Vazão de água do chuveiro (L/min):", 2.0, 10.0, 4.0, 0.5, key="chuveiro_vazao")
        with c_h2:
            temp_amb = st.number_input("Temperatura da água da caixa (°C):", 10.0, 35.0, 20.0, 1.0, key="chuveiro_tamb")

    # Realiza o cálculo para a classe selecionada
    res = calcular_chuveiro(
        potencia_watts=potencia_equip,
        classe_potencia=classe_key,
        tempo_minutos=tempo_min,
        tarifa_kwh=tarifa_kwh,
        temp_ambiente=temp_amb if "temp_amb" in locals() else 20.0,
        vazao_l_min=vazao if "vazao" in locals() else 4.0,
    )

    st.divider()

    # SAÍDA OBRIGATÓRIA DOS DADOS
    st.markdown("### 📊 Resultados do Banho")
    
    card_col1, card_col2, card_col3 = st.columns(3)
    
    with card_col1:
        with st.container(border=True):
            st.metric(
                label="1. Quantidade de Calor no Processo",
                value=f"{res.calor_processo_kj:.1f} kJ",
                help="Calor térmico transferido para a água durante o banho.",
            )
            st.caption(f"Potência efetiva em uso: **{res.potencia_efetiva_watts:.0f} W** ({res.fator_potencia*100:.0f}%)")

    with card_col2:
        with st.container(border=True):
            st.metric(
                label="2. Energia Elétrica Consumida",
                value=f"{res.energia_kwh:.3f} kWh",
                help="Energia elétrica consumida durante os minutos de banho.",
            )
            st.caption(f"💧 Volume de água aquecida: **{res.volume_total_litros:.0f} Litros** ({vazao:.1f} L/min)")

    with card_col3:
        with st.container(border=True):
            st.metric(
                label="3. Custo Total do Banho",
                value=f"R$ {res.custo_reais:.2f}",
                help=f"Custo financeiro por banho considerando a tarifa de R$ {tarifa_kwh:.2f}/kWh.",
            )
            st.caption(f"1 banho/dia no mês (30 dias): **R$ {res.custo_mensal_1pessoa:.2f}**")

    # Painel de impacto mensal e familiar
    st.info(
        f"💡 **Impacto no Orçamento Familiar:**\n\n"
        f"- Para **1 pessoa** tomando 1 banho diário de **{res.tempo_minutos:.0f} min**, o custo mensal é de **R$ {res.custo_mensal_1pessoa:.2f}** ({res.energia_kwh*30:.1f} kWh/mês).\n"
        f"- Para uma **família de 4 pessoas**, o custo mensal sobe para **R$ {res.custo_mensal_familia4:.2f}** ({res.energia_kwh*120:.1f} kWh/mês), "
        f"representando muitas vezes mais de 35% de toda a conta de luz da casa!",
        icon=":material/family_restroom:",
    )

    st.divider()

    # COMPARAÇÃO DIDÁTICA ENTRE AS 3 CLASSES DE POTÊNCIA
    st.markdown("### ⚖️ Comparativo entre as 3 Classes de Temperatura")
    st.caption(f"Comparação do mesmo banho de {res.tempo_minutos:.0f} minutos com chuveiro de {potencia_equip}W:")

    # Calcula os dados para as 3 classes
    classes_lista = [("alta", "Potência Alta (Inverno)"), ("media", "Potência Média (Verão)"), ("minima", "Potência Mínima (Ambiente)")]
    dados_tabela = []
    for c_k, c_nome in classes_lista:
        r_temp = calcular_chuveiro(
    potencia_watts=potencia_equip,
    classe_potencia=c_k,
    tempo_minutos=tempo_min,
    tarifa_kwh=tarifa_kwh,
    temp_ambiente=temp_amb if "temp_amb" in locals() else 20.0,
    vazao_l_min=vazao if "vazao" in locals() else 4.0,
)
        dados_tabela.append({
            "Classe de Temperatura": c_nome,
            "Potência Efetiva (W)": f"{r_temp.potencia_efetiva_watts:.0f} W",
            "Elevação Temp (ΔT)": f"+{r_temp.elevacao_temp_c:.1f} °C",
            "Calor (kJ)": f"{r_temp.calor_processo_kj:.1f} kJ",
            "Consumo (kWh)": f"{r_temp.energia_kwh:.3f} kWh",
            "Custo Banho (R$)": f"R$ {r_temp.custo_reais:.2f}",
            "Custo Mensal (R$)": f"R$ {r_temp.custo_mensal_1pessoa:.2f}",
        })

    st.dataframe(pd.DataFrame(dados_tabela), width="stretch", hide_index=True)

    # Gráfico de barras comparando os custos
    df_chart = pd.DataFrame([
        {"Classe": "Potência Alta", "Custo Mensal (R$)": calcular_chuveiro(potencia_equip, "alta", tempo_min, tarifa_kwh).custo_mensal_1pessoa},
        {"Classe": "Potência Média", "Custo Mensal (R$)": calcular_chuveiro(potencia_equip, "media", tempo_min, tarifa_kwh).custo_mensal_1pessoa},
        {"Classe": "Potência Mínima", "Custo Mensal (R$)": calcular_chuveiro(potencia_equip, "minima", tempo_min, tarifa_kwh).custo_mensal_1pessoa},
    ])
    st.bar_chart(df_chart, x="Classe", y="Custo Mensal (R$)", color="#0284C7")

    # Memória de cálculo
    with st.expander("📝 Memória de Cálculo Termodinâmica Detalhada", expanded=False):
        st.markdown(
            fr"""
            1. **Potência Efetiva Utilizada:**
               $$P_{{\text{{efetiva}}}} = {res.potencia_nominal_watts:.0f}\text{{ W}} \times {res.fator_potencia:.2f} = {res.potencia_efetiva_watts:.0f}\text{{ W}}$$
            2. **Tempo em Horas:**
               $$t = \frac{{{res.tempo_minutos:.0f}\text{{ min}}}}{{60}} = {res.tempo_minutos/60:.3f}\text{{ horas}}$$
            3. **Energia Elétrica Consumida:**
               $$E = \frac{{{res.potencia_efetiva_watts:.0f}\text{{ W}} \times {res.tempo_minutos/60:.3f}\text{{ h}}}}{{1000}} = {res.energia_kwh:.3f}\text{{ kWh}}$$
            4. **Quantidade de Calor Transferida (kJ):**
               $$Q = E_{{\text{{kWh}}}} \times 3600 \times \eta = {res.energia_kwh:.3f} \times 3600 \times 0,98 = {res.calor_processo_kj:.1f}\text{{ kJ}}$$
            5. **Elevação de Temperatura da Água:**
               Com vazão de {res.vazao_l_min:.1f} L/min, em {res.tempo_minutos:.0f} min passam {res.volume_total_litros:.0f} kg de água:
               $$\Delta T = \frac{{Q}}{{m \cdot c}} = \frac{{{res.calor_processo_kj:.1f}}}{{{res.volume_total_litros:.0f} \times 4,184}} \approx +{res.elevacao_temp_c:.1f}^\circ\text{{C}}$$
            6. **Custo Financeiro:**
               $$\text{{Custo}} = {res.energia_kwh:.3f}\text{{ kWh}} \times \text{{R\$}} {tarifa_kwh:.2f} = \text{{R\$}} {res.custo_reais:.2f}$$
            """
        )

    # Botão de retorno
    st.divider()
    st.page_link("app_pages/home.py", label="Voltar para a Página Inicial", icon=":material/arrow_back:")

render_chuveiro_page()
