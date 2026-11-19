import streamlit as st
import pandas as pd
from utils.thermo_calc import calcular_geladeira

def render_geladeira_page():
    st.markdown(
    """
    <a href="/" target="_self" style="text-decoration: none; color: inherit;">
        <h1>⚡ Oficina de Termodinâmica Aplicada</h1>
    </a>
    """,
    unsafe_allow_html=True
)
    st.title("❄️ 3. Geladeira Doméstica")
    st.subheader("Custo Mensal e Ciclo de Refrigeração a Vapor")
    
    st.markdown(
        r"""
        Diferente de aquecedores resistivos (como chaleira e chuveiro), a geladeira é uma **máquina térmica reversa** 
        (bomba de calor / ciclo de compressão de vapor).
        
        Pela **2ª Lei da Termodinâmica**, o calor não flui espontaneamente de um corpo frio (alimentos no interior) 
        para um corpo quente (ar da cozinha). Para que isso ocorra, o compressor elétrico realiza trabalho mecânico ($W$), 
        extraindo calor $Q_C$ do congelador e rejeitando calor $Q_H = Q_C + W$ pelo condensador traseiro.
        """
    )
    
    st.divider()

    # Painel de Parâmetros de Entrada
    st.markdown("### 📥 Parâmetros de Entrada")
    
    col_in1, col_in2 = st.columns(2, gap="medium")
    
    with col_in1:
        st.markdown("**a. Potência do Equipamento (em Watts):**")
        
        if "potencia_geladeira" not in st.session_state:
            st.session_state.potencia_geladeira = 150

        potencia_digitada = st.number_input(
            "Digite a potência do compressor (Watts):",
            min_value=40,
            max_value=1000,
            value=int(st.session_state.potencia_geladeira),
            step=10,
            help="Potência do motor compressor quando em funcionamento (etiqueta traseira do motor, ex: 100W a 250W).",
            key="input_potencia_geladeira_val",
        )
        st.session_state.potencia_geladeira = potencia_digitada
        potencia_watts = potencia_digitada

        # Sugestões rápidas de modelos comuns no Brasil
        st.caption("Preenchimento rápido de modelos comuns:")
        p_cols = st.columns(5)
        modelos = [("90 W", 90), ("120 W", 120), ("150 W", 150), ("200 W", 200), ("250 W", 250)]
        for p_col, (p_label, p_val) in zip(p_cols, modelos):
            if p_col.button(p_label, key=f"btn_p_gel_{p_val}", width="stretch"):
                st.session_state.potencia_geladeira = p_val
                st.rerun()

    with col_in2:
        st.markdown("**Fator de Ciclo de Funcionamento (Duty Cycle):**")
        st.caption("A geladeira fica na tomada 24h, mas o compressor liga e desliga via termostato:")
        
        perfil_uso = st.radio(
            "Regime de funcionamento do compressor ao longo do dia:",
            options=[
                "Uso Econômico / Inverno (~25% do tempo ativo - 6 horas/dia)",
                "Uso Moderado / Padrão (~35% do tempo ativo - 8,4 horas/dia)",
                "Uso Intenso / Verão (~45% do tempo ativo - 10,8 horas/dia)",
            ],
            index=1,
            key="radio_perfil_geladeira",
        )
        
        if "25%" in perfil_uso:
            fator_ciclo = 0.25
        elif "45%" in perfil_uso:
            fator_ciclo = 0.45
        else:
            fator_ciclo = 0.35

        tarifa_kwh = float(st.session_state.get("tarifa_kwh", 0.85))
        st.caption(f"💡 Tarifa ativa na oficina: **R$ {tarifa_kwh:.2f} / kWh** (herdada da página inicial)")

    # Parâmetros avançados expansíveis
    with st.expander("⚙️ Parâmetros Termodinâmicos do Ciclo de Refrigeração", expanded=False):
        c_adv1, c_adv2 = st.columns(2)
        with c_adv1:
            cop = st.slider(
                "Coeficiente de Performance (COP = Q_frio / Trabalho):",
                min_value=1.5,
                max_value=4.0,
                value=2.5,
                step=0.1,
                help="Refrigeradores domésticos modernos têm COP típico entre 2,2 e 3,0.",
                key="geladeira_cop",
            )
        with c_adv2:
            dias_mes = st.number_input("Dias de cálculo no mês:", min_value=1, max_value=31, value=30, key="geladeira_dias")

    # Realiza os cálculos termodinâmicos
    res = calcular_geladeira(
        potencia_watts=potencia_watts,
        tarifa_kwh=tarifa_kwh,
        fator_ciclo=fator_ciclo,
        dias_mes=dias_mes if "dias_mes" in locals() else 30,
        cop=cop if "cop" in locals() else 2.5,
    )

    st.divider()

    # SAÍDA OBRIGATÓRIA DOS DADOS
    st.markdown("### 📊 Resultados do Consumo Mensal")
    
    card_col1, card_col2, card_col3 = st.columns(3)
    
    with card_col1:
        with st.container(border=True):
            st.metric(
                label="1. Quantidade de Calor no Processo",
                value=f"{res.calor_retirado_kj / 1000.0:.2f} MJ",
                help="Calor térmico total retirado dos alimentos no mês para mantê-los refrigerados.",
            )
            st.caption(f"Em kJ: **{res.calor_retirado_kj:,.0f} kJ** retirados | Rejeitado: **{res.calor_rejeitado_kj:,.0f} kJ**")

    with card_col2:
        with st.container(border=True):
            st.metric(
                label="2. Energia Elétrica Consumida no Mês",
                value=f"{res.energia_kwh:.1f} kWh / mês",
                help=f"Consumo elétrico acumulado no mês ({res.horas_mes} horas com ciclo de {fator_ciclo*100:.0f}%).",
            )
            st.caption(f"Horas ativas do compressor: **{res.horas_operando:.0f} h** no mês (~{res.horas_operando/30:.1f} h/dia)")

    with card_col3:
        with st.container(border=True):
            st.metric(
                label="3. Custo Total no Mês",
                value=f"R$ {res.custo_reais:.2f} / mês",
                help=f"Custo mensal considerando a tarifa de R$ {tarifa_kwh:.2f}/kWh.",
            )
            custo_dia = res.custo_reais / 30.0
            st.caption(f"Custo diário médio: **R$ {custo_dia:.2f} / dia**")

    # Insight didático
    st.info(
        f"💡 **Insight da Oficina:** Mesmo com uma potência relativamente modesta ({potencia_watts} W), "
        f"a geladeira consome **{res.energia_kwh:.1f} kWh/mês** porque opera dia e noite ininterruptamente. "
        f"No acumulado de 30 dias ({res.horas_operando:.0f} horas ativas), ela custa **R$ {res.custo_reais:.2f}**, "
        f"sendo responsável por uma fatia constante da conta de luz.",
        icon=":material/lightbulb:",
    )

    st.divider()

    # Visualização Didática: Gráfico do Consumo Acumulado nos 30 Dias
    st.markdown("### 📈 Evolução do Gasto Acumulado ao Longo do Mês")
    st.caption("Acompanhe o consumo e custo da geladeira crescendo dia após dia:")

    dias = list(range(1, 31))
    consumo_dia = res.energia_kwh / 30.0
    custo_dia = res.custo_reais / 30.0
    df_mes = pd.DataFrame({
        "Dia do Mês": dias,
        "Custo Acumulado (R$)": [round(d * custo_dia, 2) for d in dias],
        "Consumo Acumulado (kWh)": [round(d * consumo_dia, 2) for d in dias],
    })

    col_g1, col_g2 = st.columns([2, 1], gap="medium")
    with col_g1:
        st.line_chart(df_mes, x="Dia do Mês", y="Custo Acumulado (R$)", color="#0D9488")
    with col_g2:
        st.markdown(
            f"""
            **Balanço do Ciclo Térmico:**
            
            - **Trabalho elétrico ($W$):** {res.trabalho_eletrico_kj/1000.0:.1f} MJ
            - **Calor frio absorvido ($Q_C$):** {res.calor_retirado_kj/1000.0:.1f} MJ
            - **Calor quente rejeitado ($Q_H$):** {res.calor_rejeitado_kj/1000.0:.1f} MJ
            
            Como $COP = {res.cop:.1f}$, para cada **1 kJ** de eletricidade que entra no motor, a geladeira retira **{res.cop:.1f} kJ** de calor de dentro dos alimentos!
            """
        )

    # Memória de cálculo
    with st.expander("📝 Memória de Cálculo Termodinâmica Detalhada", expanded=False):
        st.markdown(
            fr"""
            1. **Horas Ativas do Compressor:**
               $$t_{{\text{{ativo}}}} = 30\text{{ dias}} \times 24\text{{ h}} \times {res.fator_ciclo:.2f} = {res.horas_operando:.1f}\text{{ horas}}$$
            2. **Energia Elétrica Mensal Consumida:**
               $$E = \frac{{{potencia_watts}\text{{ W}} \times {res.horas_operando:.1f}\text{{ h}}}}{{1000}} = {res.energia_kwh:.2f}\text{{ kWh/mês}}$$
            3. **Trabalho Elétrico Fornecido ao Ciclo ($W$ em kJ):**
               $$W = {res.energia_kwh:.2f} \times 3600 = {res.trabalho_eletrico_kj:,.0f}\text{{ kJ}}$$
            4. **Calor Retirado dos Alimentos ($Q_C$ em kJ):**
               $$Q_C = COP \times W = {res.cop:.1f} \times {res.trabalho_eletrico_kj:,.0f} = {res.calor_retirado_kj:,.0f}\text{{ kJ}}$$
            5. **Calor Rejeitado pelo Condensador Traseiro ($Q_H$ em kJ):**
               $$Q_H = Q_C + W = {res.calor_rejeitado_kj:,.0f}\text{{ kJ}}$$
            6. **Custo Mensal Total:**
               $$\text{{Custo}} = {res.energia_kwh:.2f}\text{{ kWh}} \times \text{{R\$}} {tarifa_kwh:.2f} = \text{{R\$}} {res.custo_reais:.2f}$$
            """
        )

    # Botão de retorno
    st.divider()
    st.page_link("app_pages/home.py", label="Voltar para a Página Inicial", icon=":material/arrow_back:")

render_geladeira_page()
