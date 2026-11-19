import streamlit as st
import pandas as pd
from utils.thermo_calc import calcular_chaleira, CALOR_ESPECIFICO_AGUA

def render_chaleira_page():
    st.markdown(
    """
    <a href="/" target="_self" style="text-decoration: none; color: inherit;">
        <h1>⚡ Oficina de Termodinâmica Aplicada</h1>
    </a>
    """,
    unsafe_allow_html=True
)
    st.title("☕ 1. Chaleira & Cafeteira Elétrica")
    st.subheader("Custo e Energia para Aquecer 1 Litro de Água")
    
    st.markdown(
        r"""
        Nesta seção da oficina, analisamos o processo termodinâmico de aquecer água para chá ou café.
        O aquecimento baseia-se na transferência de calor sensível:
        
        $$Q = m \cdot c \cdot \Delta T$$
        
        onde $1\text{ L}$ de água líquida tem massa $m = 1\text{ kg}$, calor específico 
        $c = 4,184\text{ kJ}/(\text{kg}\cdot^\circ\text{C})$ e elevamos de $20^\circ\text{C}$ até a fervura a $100^\circ\text{C}$ ($\Delta T = 80^\circ\text{C}$).
        """
    )
    
    st.divider()

    # Painel de Parâmetros de Entrada
    st.markdown("### 📥 Parâmetros de Entrada")
    
    col_in1, col_in2 = st.columns(2, gap="medium")
    
    with col_in1:
        st.markdown("**a. Potência do Aparelho (em Watts):**")
        
        if "potencia_chaleira" not in st.session_state:
            st.session_state.potencia_chaleira = 1500

        # Input numérico direto via digitação livre
        potencia_digitada = st.number_input(
            "Digite a potência do equipamento (Watts):",
            min_value=100,
            max_value=5000,
            value=int(st.session_state.potencia_chaleira),
            step=50,
            help="Digite qualquer valor de potência em Watts indicado na etiqueta do aparelho.",
            key="input_potencia_chaleira_val",
        )
        st.session_state.potencia_chaleira = potencia_digitada
        potencia_watts = potencia_digitada

        # Sugestões rápidas de modelos comuns (apenas preenchem o campo quando clicadas)
        st.caption("Preenchimento rápido de potências comuns:")
        preset_cols = st.columns(5)
        presets = [("1000 W", 1000), ("1200 W", 1200), ("1500 W", 1500), ("1800 W", 1800), ("2000 W", 2000)]
        for p_col, (p_label, p_val) in zip(preset_cols, presets):
            if p_col.button(p_label, key=f"btn_p_ch_{p_val}", width="stretch"):
                st.session_state.potencia_chaleira = p_val
                st.rerun()

    with col_in2:
        st.markdown("**b. Tarifa de Energia Elétrica (em R$ / kWh):**")
        tarifa_kwh = st.number_input(
            "Tarifa aplicada (R$/kWh):",
            min_value=0.10,
            max_value=5.00,
            value=float(st.session_state.get("tarifa_kwh", 0.85)),
            step=0.05,
            format="%.2f",
            help="Sincronizada com o valor inserido na página inicial.",
            key="chaleira_tarifa_input",
        )
        # Sincroniza de volta no session state global
        st.session_state.tarifa_kwh = tarifa_kwh

    # Opções termodinâmicas adicionais (expansível para manter a interface simples e limpa)
    with st.expander("⚙️ Parâmetros Térmicos Adicionais (Volume, Temperaturas e Eficiência)", expanded=False):
        col_adv1, col_adv2, col_adv3 = st.columns(3)
        with col_adv1:
            volume_l = st.number_input(
                "Volume de água (Litros):",
                min_value=0.2,
                max_value=5.0,
                value=1.0,
                step=0.1,
                help="O padrão da oficina é 1 litro (1 kg de água).",
                key="chaleira_volume",
            )
        with col_adv2:
            t_ini = st.number_input("Temp. Inicial (°C):", value=20.0, step=1.0, key="chaleira_tini")
            t_fim = st.number_input("Temp. Final de Fervura (°C):", value=100.0, step=1.0, key="chaleira_tfim")
        with col_adv3:
            eficiencia_pct = st.slider(
                "Eficiência Térmica Estimada (%):",
                min_value=70,
                max_value=100,
                value=90,
                step=1,
                help="Chaleiras elétricas modernas têm eficiência de ~85% a 95% (perdas pequenas pelas paredes e vapor).",
                key="chaleira_eficiencia",
            )

    # Executa o cálculo termodinâmico com os valores digitados
    res = calcular_chaleira(
        potencia_watts=potencia_watts,
        tarifa_kwh=tarifa_kwh,
        volume_litros=volume_l if "volume_l" in locals() else 1.0,
        temp_inicial=t_ini if "t_ini" in locals() else 20.0,
        temp_final=t_fim if "t_fim" in locals() else 100.0,
        eficiencia=(eficiencia_pct / 100.0) if "eficiencia_pct" in locals() else 0.90,
    )

    st.divider()

    # SAÍDA OBRIGATÓRIA DOS DADOS
    st.markdown("### 📊 Resultados do Processo")
    
    card_col1, card_col2, card_col3 = st.columns(3)
    
    with card_col1:
        with st.container(border=True):
            st.metric(
                label="1. Quantidade de Calor no Processo",
                value=f"{res.calor_util_kj:.2f} kJ",
                help="Calor sensível útil absorvido pela água para atingir a fervura (Q = m * c * ΔT).",
            )
            st.caption(f"Calor total elétrico: **{res.calor_total_kj:.2f} kJ** (c/ {res.eficiencia_percent:.0f}% ef.)")

    with card_col2:
        with st.container(border=True):
            st.metric(
                label="2. Energia Elétrica Consumida",
                value=f"{res.energia_kwh:.4f} kWh",
                help="Energia elétrica retirada da rede elétrica (1 kWh = 3600 kJ).",
            )
            minutos = int(res.tempo_segundos // 60)
            segundos = int(res.tempo_segundos % 60)
            st.caption(f"⏱️ Tempo de aquecimento ({potencia_watts}W): **{minutos} min {segundos:02d} s**")

    with card_col3:
        with st.container(border=True):
            st.metric(
                label="3. Custo Total do Processo",
                value=f"R$ {res.custo_reais:.3f}",
                help=f"Custo total calculado com a tarifa de R$ {tarifa_kwh:.2f}/kWh.",
            )
            custo_30d = res.custo_reais * 30.0
            st.caption(f"Fervendo 1x ao dia no mês (30 dias): **R$ {custo_30d:.2f}**")

    # Insight pedagógico importante da Termodinâmica
    st.info(
        f"💡 **Insight da Oficina:** Fervendo **{res.volume_litros:.1f} L** de água com a potência digitada de **{potencia_watts} W**, "
        f"o processo leva **{res.tempo_minutos:.2f} minutos** e custa cerca de **R$ {res.custo_reais:.3f}** "
        f"(menos de 10 centavos!). Embora a potência seja alta, o tempo é curto, resultando em baixo consumo em kWh.",
        icon=":material/lightbulb:",
    )

    st.divider()

    # Visualização Didática: Gráfico Interativo de Potência vs Tempo vs Custo
    st.markdown("### 📈 Análise Didática: Potência x Tempo x Consumo")
    st.caption("Veja o que acontece quando variamos a potência do aparelho mantendo o mesmo volume de 1 litro:")

    # Gera dados de comparação de 600W a 2400W
    potencias_teste = [600, 800, 1000, 1200, 1500, 1800, 2000, 2200, 2500]
    dados_comp = []
    for p in potencias_teste:
        r = calcular_chaleira(
            potencia_watts=p,
            tarifa_kwh=tarifa_kwh,
            volume_litros=res.volume_litros,
            temp_inicial=res.temp_inicial,
            temp_final=res.temp_final,
            eficiencia=res.eficiencia_percent / 100.0,
        )
        dados_comp.append({
            "Potência (W)": p,
            "Tempo de Fervura (min)": round(r.tempo_minutos, 2),
            "Consumo (kWh)": round(r.energia_kwh, 4),
            "Custo (R$)": round(r.custo_reais, 3),
        })
    df_comp = pd.DataFrame(dados_comp)

    col_g1, col_g2 = st.columns([2, 1], gap="medium")
    with col_g1:
        st.line_chart(
            df_comp,
            x="Potência (W)",
            y="Tempo de Fervura (min)",
            color="#EA580C",
        )
    with col_g2:
        st.markdown(
            """
            **Conclusão Fundamental:**
            
            - **Maior Potência:** Reduz dramaticamente o tempo de fervura.
            - **Energia (kWh):** É praticamente a mesma (~0,10 kWh) para qualquer potência!
            - **Custo (R$):** Quase idêntico! Um aparelho de 2000W não gasta o dobro de dinheiro que um de 1000W para ferver a mesma água, pois ele opera pela metade do tempo!
            """
        )

    # Passo a passo da memória de cálculo
    with st.expander("📝 Memória de Cálculo Termodinâmica Detalhada", expanded=False):
        st.markdown(
            fr"""
            1. **Massa de água:** $m = {res.volume_litros:.1f}\text{{ L}} \times 1\text{{ kg/L}} = {res.massa_kg:.2f}\text{{ kg}}$
            2. **Variação de Temperatura:** $\Delta T = {res.temp_final:.1f}^\circ\text{{C}} - {res.temp_inicial:.1f}^\circ\text{{C}} = {res.delta_t:.1f}^\circ\text{{C}}$
            3. **Calor Útil Absorvido:**
               $$Q = m \cdot c \cdot \Delta T = {res.massa_kg:.2f} \times 4,184 \times {res.delta_t:.1f} = {res.calor_util_kj:.2f}\text{{ kJ}}$$
            4. **Energia Elétrica Requerida (com eficiência $\eta = {res.eficiencia_percent:.0f}\%$):**
               $$E_{{\text{{elétrica}}}} = \frac{{{res.calor_util_kj:.2f}\text{{ kJ}}}}{{{res.eficiencia_percent/100:.2f}}} = {res.calor_total_kj:.2f}\text{{ kJ}} = \frac{{{res.calor_total_kj:.2f}}}{{3600}} = {res.energia_kwh:.4f}\text{{ kWh}}$$
            5. **Tempo de Aquecimento:**
               $$t = \frac{{{res.calor_total_kj * 1000:.0f}\text{{ J}}}}{{{potencia_watts}\text{{ W}}}} = {res.tempo_segundos:.1f}\text{{ segundos}} = {res.tempo_minutos:.2f}\text{{ minutos}}$$
            6. **Custo Total:**
               $$\text{{Custo}} = {res.energia_kwh:.4f}\text{{ kWh}} \times \text{{R\$}} {tarifa_kwh:.2f} = \text{{R\$}} {res.custo_reais:.3f}$$
            """
        )

    # Botão para voltar à página inicial
    st.divider()
    st.page_link("app_pages/home.py", label="Voltar para a Página Inicial", icon=":material/arrow_back:")

render_chaleira_page()
