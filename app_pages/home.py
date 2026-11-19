import streamlit as st

def render_home_page():
    # Título principal e descrição da oficina
    st.title("⚡ Oficina de Termodinâmica Aplicada")
    st.subheader("Relação entre Temperatura, Quantidade de Água, Potência, Tempo, Consumo e Custo")
    
    st.markdown(
        r"""
        Esta oficina didática e interativa foi desenvolvida para demonstrar de forma clara e prática
        como a **Termodinâmica** se manifesta no consumo diário de energia elétrica residencial.
        
        Descubra como variáveis fundamentais da física — **massa de água ($m$)**, **variação de temperatura ($\Delta T$)**, 
        **calor sensível ($Q$)**, **potência dos aparelhos ($P$)**, **tempo de operação ($t$)** e **eficiência energética ($\eta$)** — 
        determinam diretamente o consumo em **kWh** e o **valor em reais (R$)** na sua fatura de energia.
        """
    )
    
    st.divider()

    # Input da Tarifa de Energia Elétrica logo abaixo do título e descrição
    st.markdown("### 🏷️ 1. Defina a Tarifa de Energia Elétrica")
    st.caption("Insira abaixo o valor da tarifa em R$ / kWh. Qualquer valor digitado aqui será aplicado imediatamente em todas as calculadoras:")
    
    col_t1, col_t2 = st.columns([1.5, 2], vertical_alignment="center")
    
    with col_t1:
        tarifa_digitada = st.number_input(
            "Tarifa de Energia Elétrica (em R$ / kWh):",
            min_value=0.10,
            max_value=5.00,
            value=float(st.session_state.get("tarifa_kwh", 0.85)),
            step=0.05,
            format="%.2f",
            key="home_tarifa_input",
            help="Consulte a sua conta de luz para o valor do kWh com impostos (ICMS, PIS, COFINS) e bandeira tarifária.",
        )
        # Salva o valor digitado no estado global compartilhado
        st.session_state.tarifa_kwh = tarifa_digitada

    with col_t2:
        st.info(
            f"💡 **Tarifa ativa na oficina:** **R$ {st.session_state.tarifa_kwh:.2f} / kWh**\n\n"
            "*(Referência ANEEL média Brasil: ~R$ 0,75 a R$ 1,15 por kWh dependendo da distribuidora e da bandeira tarifária)*",
            icon=":material/info:",
        )

    st.divider()

    # Seção com os 4 cards de imagem retangulares com cantos arredondados
    st.markdown("### 🧮 2. Escolha o Equipamento para Calcular")
    st.write("Clique em qualquer um dos cartões abaixo para acessar a calculadora correspondente:")

    # CSS para suavizar as bordas das imagens com efeito visual moderno
    st.html(
        """
        <style>
        .stImage img {
            border-radius: 14px !important;
            object-fit: cover !important;
            aspect-ratio: 16 / 9 !important;
            width: 100% !important;
            box-shadow: 0 4px 14px rgba(0, 0, 0, 0.12);
            transition: transform 0.25s ease, box-shadow 0.25s ease;
        }
        .stImage img:hover {
            transform: scale(1.02);
            box-shadow: 0 8px 24px rgba(0, 0, 0, 0.2);
        }
        </style>
        """
    )

    # Grid 2x2 para os 4 módulos
    row1_col1, row1_col2 = st.columns(2, gap="medium")

     # 1. Chaleira / Cafeteira Elétrica
    with row1_col1:
        with st.container(border=True):
            st.image(
                "assets/chaleira.png",
                link="chaleira",
                width="stretch",
                alt="Quanto custa para aquecer água usando uma chaleira elétrica ou cafeteira",
            )
            st.markdown("#### ☕ 1. Chaleira & Cafeteira Elétrica")
            st.write(
                "Descubra quanto custa aquecer 1 litro de água até a fervura, "
                "o tempo necessário conforme a potência e a quantidade de calor em kJ."
            )
            if st.button(
                "Acessar Calculadora da Chaleira",
                key="btn_nav_chaleira",
                width="stretch",
                type="primary",
            ):
                st.switch_page("app_pages/chaleira.py")

    # 2. Chuveiro Elétrico
    with row1_col2:
        with st.container(border=True):
            st.image(
                "assets/chuveiro.png",
                link="chuveiro",
                width="stretch",
                alt="Quantos reais se gasta e quanta energia elétrica é gasta para tomar um banho usando um chuveiro elétrico",
            )
            st.markdown("#### 🚿 2. Chuveiro Elétrico")
            st.write(
                "Calcule os reais e o consumo em kWh gastos por banho comparando as 3 classes "
                "de temperatura: potência alta (inverno), média (conforto) e mínima (ambiente)."
            )
            if st.button(
                "Acessar Calculadora do Chuveiro",
                key="btn_nav_chuveiro",
                width="stretch",
                type="primary",
            ):
                st.switch_page("app_pages/chuveiro.py")

    row2_col1, row2_col2 = st.columns(2, gap="medium")

    # 3. Geladeira
    with row2_col1:
        with st.container(border=True):
            st.image(
                "assets/geladeira.png",
                link="geladeira",
                width="stretch",
                alt="Quanto custa para manter a geladeira ligada por mês",
            )
            st.markdown("#### ❄️ 3. Geladeira no Mês")
            st.write(
                "Calcule o custo mensal para manter a geladeira funcionando 24h por dia, "
                "compreendendo o ciclo de compressão a vapor e o calor retirado dos alimentos."
            )
            if st.button(
                "Acessar Calculadora da Geladeira",
                key="btn_nav_geladeira",
                width="stretch",
                type="primary",
            ):
                st.switch_page("app_pages/geladeira.py")

    # 4. Instruções de Economia
    with row2_col2:
        with st.container(border=True):
            st.image(
                "assets/economia.png",
                link="economia",
                width="stretch",
                alt="Instruções de como economizar dinheiro em cada uma das situações",
            )
            st.markdown("#### 💡 4. Instruções de Economia")
            st.write(
                "Aprenda estratégias práticas e termodinâmicas para reduzir significativamente "
                "o gasto com chuveiro, chaleira, geladeira e outros eletrodomésticos da casa."
            )
            if st.button(
                "Acessar Guia de Economia",
                key="btn_nav_economia",
                width="stretch",
            ):
                st.switch_page("app_pages/economia.py")

    st.divider()

    # Painel didático de física termodinâmica da oficina
    with st.expander("📚 Fundamentos Teóricos da Oficina: Relação entre Grandezas Físicas", expanded=False):
        fcol1, fcol2 = st.columns(2)
        with fcol1:
            st.markdown(
                r"""
                **1. Calor Sensível ($Q$ em kJ):**
                $$Q = m \cdot c \cdot \Delta T$$
                - $m$: massa da água em kg ($1\text{ L} \approx 1\text{ kg}$)
                - $c$: calor específico da água ($4,184\text{ kJ}/(\text{kg}\cdot^\circ\text{C})$)
                - $\Delta T$: variação de temperatura ($T_{\text{final}} - T_{\text{inicial}}$)
                
                **2. Potência, Energia e Tempo:**
                $$E = P \cdot t \quad \iff \quad P = \frac{E}{t}$$
                - $P$ em Watts (W) = Joules por segundo (J/s)
                - $t$ em segundos ou horas
                - $1\text{ kWh} = 3.600\text{ kJ} = 3.600.000\text{ J}$
                """
            )
        with fcol2:
            st.markdown(
                r"""
                **3. Eficiência Energética ($\eta$):**
                $$\eta = \frac{Q_{\text{útil}}}{E_{\text{elétrica}}}$$
                Nem toda a energia elétrica consumida vira calor no líquido; uma parcela é perdida para o ar ou para as paredes do recipiente.
                
                **4. Custo Financeiro (R$):**
                $$\text{Custo (R\$)} = E_{\text{kWh}} \times \text{Tarifa (R\$/kWh)}$$
                O valor financeiro é proporcional direto aos kWh consumidos.
                """
            )

render_home_page()
