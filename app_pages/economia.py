import streamlit as st

def render_economia_page():
    st.markdown(
    """
    <a href="/" target="_self" style="text-decoration: none; color: inherit;">
        <h1>⚡ Oficina de Termodinâmica Aplicada</h1>
    </a>
    """,
    unsafe_allow_html=True
)
    st.title("💡 4. Instruções de Economia de Energia")
    st.subheader("Como Reduzir a Conta de Luz Aplicando Conceitos de Termodinâmica")
    
    st.markdown(
        r"""
        Economizar energia elétrica não significa passar frio ou abrir mão do conforto. 
        Compreendendo como a **física térmica** funciona, você pode aplicar pequenos ajustes 
        no dia a dia que geram reduções substanciais na fatura no final do mês.
        
        Confira abaixo as principais recomendações para cada um dos equipamentos analisados nesta oficina:
        """
    )
    
    st.divider()

    # 1. Chaleira & Cafeteira Elétrica
    with st.container(border=True):
        st.markdown("### ☕ 1. Economizando com a Chaleira e Cafeteira Elétrica")
        
        c1, c2 = st.columns([1.5, 1], gap="medium")
        with c1:
            st.markdown(
                r"""
                - **Aqueça estritamente o volume de água que vai consumir:**
                  Pela equação $Q = m \cdot c \cdot \Delta T$, o calor necessário é diretamente proporcional à **massa ($m$)**. 
                  Se você vai preparar uma xícara de chá (250 mL), não encha a chaleira com 1 litro. Fervendo 1 L em vez de 250 mL, você gasta **4 vezes mais energia e 4 vezes mais dinheiro**!
                
                - **Mantenha a chaleira sempre tampada durante o aquecimento:**
                  O calor latente de vaporização da água é altíssimo: $L_v \approx 2.257\text{ kJ/kg}$. 
                  Deixar a chaleira aberta dissipa calor continuamente por evaporação, aumentando o tempo e o gasto elétrico.
                
                - **Limpe o fundo da chaleira periodicamente:**
                  Resíduos de minerais e calcário criam uma camada isolante sobre a resistência térmica, reduzindo a eficiência $\eta$ e aumentando o tempo de fervura.
                """
            )
        with c2:
            st.success(
                "💰 **Potencial de Economia:**\n\n"
                "**Até 60% a 75%** de redução no gasto da chaleira apenas aquecendo o volume correto para o número de xícaras!",
                icon=":material/savings:",
            )

    # 2. Chuveiro Elétrico
    with st.container(border=True):
        st.markdown("### 🚿 2. Economizando com o Chuveiro Elétrico")
        
        c1, c2 = st.columns([1.5, 1], gap="medium")
        with c1:
            st.markdown(
                r"""
                - **Mude a chave para a posição Verão / Média nos dias amenos:**
                  A potência cai de ~5500W (ou 7500W) para ~3500W. Isso representa uma **economia imediata de 35% a 40%** na conta de luz daquele banho, mantendo uma temperatura agradável.
                
                - **Adote a 'Regra dos 5 Minutos a Menos':**
                  Diminuir o banho de 15 para 10 minutos economiza 33% da eletricidade do banho. Para uma família de 4 pessoas, isso representa mais de **R$ 40,00 a R$ 60,00 a menos todo mês**!
                
                - **Feche o registro ao se ensaboar e lavar o cabelo:**
                  Evita desperdício duplo: de água tratada e de eletricidade da rede.
                
                - **Limpe os orifícios (crivo) do chuveiro:**
                  Furos entupidos reduzem a vazão e concentram o calor, podendo queimar a resistência prematuramente.
                """
            )
        with c2:
            st.success(
                "💰 **Potencial de Economia:**\n\n"
                "**R$ 400 a R$ 800 por ano** para uma família média, apenas diminuindo 5 minutos por banho e usando a chave Verão nos meses quentes!",
                icon=":material/savings:",
            )

    # 3. Geladeira
    with st.container(border=True):
        st.markdown("### ❄️ 3. Economizando com a Geladeira")
        
        c1, c2 = st.columns([1.5, 1], gap="medium")
        with c1:
            st.markdown(
                r"""
                - **Faça o 'Teste da Folha de Papel' nas borrachas da porta:**
                  Feche a porta da geladeira prendendo uma folha de papel sulfite. Se a folha escorregar facilmente sem resistência, a vedação está gasta. 
                  O ar quente e úmido da cozinha entra continuamente, forçando o compressor a trabalhar o dobro do tempo (**+30% a 50% de consumo**).
                
                - **Nunca guarde alimentos quentes na geladeira:**
                  Uma panela de comida quente adiciona uma enorme carga térmica sensível e latente ($Q_C$). Espere atingir a temperatura ambiente antes de guardar.
                
                - **Jamais seque roupas na grade traseira do condensador:**
                  Cobrir o condensador impede a convecção natural de rejeitar calor ($Q_H$) para a cozinha. Isso superaquece o fluido refrigerante, sobrecarrega o compressor e aumenta o consumo em até **40%**, além do risco de incêndio!
                
                - **Mantenha espaço de ventilação de pelo menos 10 cm da parede:**
                  Garante o fluxo de ar livre para o resfriamento das serpentinas traseiras.
                
                - **Ajuste o termostato de acordo com a estação:**
                  No inverno ou em dias frios, diminua o nível do termostato interno para posições mais baixas (mínimo ou médio).
                """
            )
        with c2:
            st.success(
                "💰 **Potencial de Economia:**\n\n"
                "**Até 30%** de redução no consumo mensal da geladeira com borracha bem vedada, sem panela quente e condensador traseiro livre!",
                icon=":material/savings:",
            )

    # 4. Tabela Síntese do Impacto Anual
    st.divider()
    st.markdown("### 📊 Síntese do Impacto Financeiro Estimado no Ano")
    st.caption("Estimativa de economia anual para uma família de 3 a 4 pessoas:")

    dados_economia = [
        {
            "Aparelho": "Chuveiro Elétrico",
            "Ação Prática": "Reduzir 5 min no banho + usar chave Verão nos meses quentes",
            "Economia Mensal Estimada": "R$ 45,00 a R$ 70,00",
            "Economia Anual Estimada": "R$ 540,00 a R$ 840,00",
        },
        {
            "Aparelho": "Geladeira",
            "Ação Prática": "Trocar borracha gasta + não pôr panela quente + traseira ventilada",
            "Economia Mensal Estimada": "R$ 15,00 a R$ 25,00",
            "Economia Anual Estimada": "R$ 180,00 a R$ 300,00",
        },
        {
            "Aparelho": "Chaleira / Cafeteira",
            "Ação Prática": "Ferver somente a quantidade exata de água necessária para o preparo",
            "Economia Mensal Estimada": "R$ 5,00 a R$ 10,00",
            "Economia Anual Estimada": "R$ 60,00 a R$ 120,00",
        },
        {
            "Aparelho": "TOTAL CONJUNTO",
            "Ação Prática": "Aplicação de todas as boas práticas térmicas residenciais",
            "Economia Mensal Estimada": "R$ 65,00 a R$ 105,00 / mês",
            "Economia Anual Estimada": "R$ 780,00 a R$ 1.260,00 / ano",
        },
    ]
    st.table(dados_economia)

    # Botão de retorno
    st.divider()
    st.page_link("app_pages/home.py", label="Voltar para a Página Inicial", icon=":material/arrow_back:")

render_economia_page()
