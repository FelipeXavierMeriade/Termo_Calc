import os

def create_svg_assets():
    os.makedirs("assets", exist_ok=True)

    # 1. Chaleira / Cafeteira Elétrica
    svg_chaleira = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 340" width="100%" height="100%">
  <defs>
    <linearGradient id="bg-chaleira" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#EA580C"/>
      <stop offset="50%" stop-color="#C2410C"/>
      <stop offset="100%" stop-color="#7C2D12"/>
    </linearGradient>
    <linearGradient id="card-grad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#FFFFFF" stop-opacity="0.15"/>
      <stop offset="100%" stop-color="#000000" stop-opacity="0.35"/>
    </linearGradient>
    <filter id="shadow" x="-5%" y="-5%" width="110%" height="110%">
      <feDropShadow dx="0" dy="8" stdDeviation="12" flood-color="#000000" flood-opacity="0.3"/>
    </filter>
  </defs>
  
  <!-- Fundo com bordas arredondadas suaves -->
  <rect width="600" height="340" rx="24" ry="24" fill="url(#bg-chaleira)"/>
  <rect width="600" height="340" rx="24" ry="24" fill="url(#card-grad)"/>
  <rect x="1.5" y="1.5" width="597" height="337" rx="22.5" ry="22.5" fill="none" stroke="#FFFFFF" stroke-opacity="0.25" stroke-width="2"/>

  <!-- Elementos de fundo abstratos (ondas de calor) -->
  <circle cx="500" cy="80" r="140" fill="#F97316" fill-opacity="0.25"/>
  <circle cx="520" cy="260" r="100" fill="#FB923C" fill-opacity="0.15"/>

  <!-- Ilustração da Chaleira / Cafeteira -->
  <g transform="translate(410, 85)">
    <!-- Vapor saindo -->
    <path d="M 50,0 Q 40,-25 55,-45 T 45,-80" fill="none" stroke="#FED7AA" stroke-width="4" stroke-linecap="round" stroke-dasharray="6,4" opacity="0.8"/>
    <path d="M 70,5 Q 85,-20 70,-45 T 80,-80" fill="none" stroke="#FED7AA" stroke-width="4" stroke-linecap="round" stroke-dasharray="6,4" opacity="0.8"/>
    <!-- Corpo da chaleira -->
    <path d="M 20,40 L 100,40 L 115,120 L 10,120 Z" fill="#FFF7ED" opacity="0.95"/>
    <!-- Tampa -->
    <path d="M 30,40 Q 60,25 90,40 Z" fill="#FDBA74"/>
    <circle cx="60" cy="26" r="6" fill="#C2410C"/>
    <!-- Bico -->
    <path d="M 18,55 L -15,35 L -10,50 L 15,75 Z" fill="#FFEDD5"/>
    <!-- Alça -->
    <path d="M 105,50 Q 150,80 110,110" fill="none" stroke="#FED7AA" stroke-width="12" stroke-linecap="round"/>
    <!-- Base de aquecimento elétrica -->
    <rect x="5" y="123" width="115" height="12" rx="4" fill="#7C2D12"/>
    <line x1="20" y1="135" x2="35" y2="150" stroke="#F97316" stroke-width="4" stroke-linecap="round"/>
    <!-- Gotas d'água fervendo -->
    <circle cx="45" cy="85" r="4" fill="#F97316" opacity="0.7"/>
    <circle cx="65" cy="95" r="5" fill="#EA580C" opacity="0.7"/>
    <circle cx="85" cy="75" r="3" fill="#FB923C" opacity="0.7"/>
  </g>

  <!-- Tag / Badge -->
  <rect x="40" y="40" width="180" height="30" rx="15" fill="#FFFFFF" fill-opacity="0.2"/>
  <text x="52" y="60" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="13" font-weight="600" fill="#FFEDD5" letter-spacing="0.5">TERMODINÂMICA &bull; 1L ÁGUA</text>

  <!-- Título Principal -->
  <text x="40" y="115" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="28" font-weight="800" fill="#FFFFFF">Chaleira &amp; Cafeteira</text>
  <text x="40" y="150" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="28" font-weight="800" fill="#FED7AA">Elétrica</text>

  <!-- Descrição -->
  <text x="40" y="195" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="15" font-weight="400" fill="#FFEDD5">Quanto custa ferver 1 litro de água?</text>
  <text x="40" y="220" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="14" font-weight="400" fill="#FED7AA" opacity="0.9">Calcule calor (kJ), tempo, kWh e o custo exato.</text>

  <!-- Botão de Ação Visual -->
  <rect x="40" y="255" width="200" height="44" rx="22" fill="#FFFFFF" />
  <text x="65" y="282" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="14" font-weight="700" fill="#C2410C">Acessar Calculadora &rarr;</text>
</svg>"""

    with open("assets/chaleira.svg", "w", encoding="utf-8") as f:
        f.write(svg_chaleira)

    # 2. Chuveiro Elétrico
    svg_chuveiro = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 340" width="100%" height="100%">
  <defs>
    <linearGradient id="bg-chuveiro" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0284C7"/>
      <stop offset="50%" stop-color="#0369A1"/>
      <stop offset="100%" stop-color="#0F172A"/>
    </linearGradient>
    <linearGradient id="card-grad2" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#FFFFFF" stop-opacity="0.15"/>
      <stop offset="100%" stop-color="#000000" stop-opacity="0.35"/>
    </linearGradient>
  </defs>
  
  <rect width="600" height="340" rx="24" ry="24" fill="url(#bg-chuveiro)"/>
  <rect width="600" height="340" rx="24" ry="24" fill="url(#card-grad2)"/>
  <rect x="1.5" y="1.5" width="597" height="337" rx="22.5" ry="22.5" fill="none" stroke="#FFFFFF" stroke-opacity="0.25" stroke-width="2"/>

  <!-- Elementos decorativos de água -->
  <circle cx="500" cy="70" r="130" fill="#38BDF8" fill-opacity="0.2"/>
  <circle cx="520" cy="270" r="100" fill="#0EA5E9" fill-opacity="0.15"/>

  <!-- Ilustração Chuveiro Elétrico -->
  <g transform="translate(420, 80)">
    <!-- Tubo de entrada de água -->
    <path d="M 0,-20 L 70,-20 L 70,30" fill="none" stroke="#E2E8F0" stroke-width="14" stroke-linecap="round"/>
    <!-- Cabeça do chuveiro -->
    <path d="M 30,30 L 110,30 L 130,55 L 10,55 Z" fill="#F8FAFC"/>
    <rect x="5" y="55" width="130" height="10" rx="3" fill="#38BDF8"/>
    <!-- Chave seletora de potência -->
    <circle cx="70" cy="25" r="8" fill="#EF4444"/>
    <!-- Jatos de água caindo -->
    <g stroke="#BAE6FD" stroke-width="3" stroke-linecap="round" stroke-dasharray="8,6" opacity="0.85">
      <line x1="25" y1="70" x2="15" y2="170"/>
      <line x1="45" y1="70" x2="40" y2="175"/>
      <line x1="70" y1="70" x2="70" y2="180"/>
      <line x1="95" y1="70" x2="100" y2="175"/>
      <line x1="115" y1="70" x2="125" y2="170"/>
    </g>
    <!-- Ondas térmicas vermelhas no chuveiro -->
    <path d="M 40,43 Q 70,35 100,43" fill="none" stroke="#F87171" stroke-width="3" opacity="0.9"/>
  </g>

  <!-- Tag / Badge -->
  <rect x="40" y="40" width="205" height="30" rx="15" fill="#FFFFFF" fill-opacity="0.2"/>
  <text x="52" y="60" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="13" font-weight="600" fill="#E0F2FE" letter-spacing="0.5">BANHO &bull; 3 NÍVEIS POTÊNCIA</text>

  <!-- Título Principal -->
  <text x="40" y="115" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="28" font-weight="800" fill="#FFFFFF">Chuveiro Elétrico</text>
  <text x="40" y="150" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="28" font-weight="800" fill="#7DD3FC">Consumo do Banho</text>

  <!-- Descrição -->
  <text x="40" y="195" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="15" font-weight="400" fill="#E0F2FE">Quantos reais e kWh você gasta por banho?</text>
  <text x="40" y="220" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="14" font-weight="400" fill="#BAE6FD" opacity="0.9">Compare potências alta, média e mínima no tempo.</text>

  <!-- Botão de Ação Visual -->
  <rect x="40" y="255" width="200" height="44" rx="22" fill="#FFFFFF" />
  <text x="65" y="282" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="14" font-weight="700" fill="#0369A1">Acessar Calculadora &rarr;</text>
</svg>"""

    with open("assets/chuveiro.svg", "w", encoding="utf-8") as f:
        f.write(svg_chuveiro)

    # 3. Geladeira
    svg_geladeira = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 340" width="100%" height="100%">
  <defs>
    <linearGradient id="bg-geladeira" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0D9488"/>
      <stop offset="50%" stop-color="#0F766E"/>
      <stop offset="100%" stop-color="#134E4A"/>
    </linearGradient>
    <linearGradient id="card-grad3" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#FFFFFF" stop-opacity="0.15"/>
      <stop offset="100%" stop-color="#000000" stop-opacity="0.35"/>
    </linearGradient>
  </defs>
  
  <rect width="600" height="340" rx="24" ry="24" fill="url(#bg-geladeira)"/>
  <rect width="600" height="340" rx="24" ry="24" fill="url(#card-grad3)"/>
  <rect x="1.5" y="1.5" width="597" height="337" rx="22.5" ry="22.5" fill="none" stroke="#FFFFFF" stroke-opacity="0.25" stroke-width="2"/>

  <!-- Elementos decorativos -->
  <circle cx="490" cy="80" r="130" fill="#2DD4BF" fill-opacity="0.2"/>
  <circle cx="510" cy="270" r="100" fill="#14B8A6" fill-opacity="0.15"/>

  <!-- Ilustração Geladeira -->
  <g transform="translate(425, 70)">
    <!-- Corpo da Geladeira Duplex -->
    <rect x="0" y="0" width="105" height="180" rx="10" fill="#F1F5F9" stroke="#CBD5E1" stroke-width="2"/>
    <!-- Divisão Freezer / Refrigerador -->
    <line x1="0" y1="55" x2="105" y2="55" stroke="#94A3B8" stroke-width="2"/>
    <!-- Puxadores -->
    <rect x="8" y="25" width="6" height="20" rx="3" fill="#64748B"/>
    <rect x="8" y="65" width="6" height="40" rx="3" fill="#64748B"/>
    <!-- Floco de neve no freezer -->
    <g transform="translate(52, 28) scale(0.65)" stroke="#38BDF8" stroke-width="2" stroke-linecap="round">
      <line x1="0" y1="-15" x2="0" y2="15"/>
      <line x1="-15" y1="0" x2="15" y2="0"/>
      <line x1="-10" y1="-10" x2="10" y2="10"/>
      <line x1="-10" y1="10" x2="10" y2="-10"/>
    </g>
    <!-- Serpentina traseira simbolizada ao lado -->
    <path d="M 115,30 Q 130,45 115,60 T 115,90 T 115,120 T 115,150" fill="none" stroke="#F87171" stroke-width="3" opacity="0.75"/>
    <text x="122" y="100" font-family="sans-serif" font-size="10" fill="#FECACA">Q_H</text>
  </g>

  <!-- Tag / Badge -->
  <rect x="40" y="40" width="220" height="30" rx="15" fill="#FFFFFF" fill-opacity="0.2"/>
  <text x="52" y="60" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="13" font-weight="600" fill="#CCFBF1" letter-spacing="0.5">REFRIGERAÇÃO &bull; CUSTO MENSAL</text>

  <!-- Título Principal -->
  <text x="40" y="115" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="28" font-weight="800" fill="#FFFFFF">Geladeira Ligada</text>
  <text x="40" y="150" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="28" font-weight="800" fill="#5EEAD4">Durante o Mês</text>

  <!-- Descrição -->
  <text x="40" y="195" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="15" font-weight="400" fill="#CCFBF1">Quanto custa manter a geladeira 24h por mês?</text>
  <text x="40" y="220" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="14" font-weight="400" fill="#99F6E4" opacity="0.9">Entenda o ciclo térmico, calor transferido e R$/mês.</text>

  <!-- Botão de Ação Visual -->
  <rect x="40" y="255" width="200" height="44" rx="22" fill="#FFFFFF" />
  <text x="65" y="282" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="14" font-weight="700" fill="#0F766E">Acessar Calculadora &rarr;</text>
</svg>"""

    with open("assets/geladeira.svg", "w", encoding="utf-8") as f:
        f.write(svg_geladeira)

    # 4. Economia de Energia
    svg_economia = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 340" width="100%" height="100%">
  <defs>
    <linearGradient id="bg-economia" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#059669"/>
      <stop offset="50%" stop-color="#047857"/>
      <stop offset="100%" stop-color="#064E3B"/>
    </linearGradient>
    <linearGradient id="card-grad4" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#FFFFFF" stop-opacity="0.15"/>
      <stop offset="100%" stop-color="#000000" stop-opacity="0.35"/>
    </linearGradient>
  </defs>
  
  <rect width="600" height="340" rx="24" ry="24" fill="url(#bg-economia)"/>
  <rect width="600" height="340" rx="24" ry="24" fill="url(#card-grad4)"/>
  <rect x="1.5" y="1.5" width="597" height="337" rx="22.5" ry="22.5" fill="none" stroke="#FFFFFF" stroke-opacity="0.25" stroke-width="2"/>

  <!-- Elementos decorativos -->
  <circle cx="500" cy="80" r="130" fill="#34D399" fill-opacity="0.2"/>
  <circle cx="520" cy="270" r="100" fill="#10B981" fill-opacity="0.15"/>

  <!-- Ilustração Lâmpada Eficiência / Economia -->
  <g transform="translate(435, 75)">
    <!-- Lâmpada bulbo -->
    <path d="M 40,20 C 15,20 0,45 0,70 C 0,90 20,105 25,125 L 55,125 C 60,105 80,90 80,70 C 80,45 65,20 40,20 Z" fill="#FEF08A"/>
    <!-- Base de rosca -->
    <rect x="25" y="125" width="30" height="15" rx="3" fill="#94A3B8"/>
    <path d="M 30,140 Q 40,150 50,140" fill="#64748B"/>
    <!-- Filamento interno em folha/coração verde -->
    <path d="M 40,50 Q 25,70 40,95 Q 55,70 40,50 Z" fill="#10B981"/>
    <!-- Cifrão / Moeda de economia -->
    <circle cx="75" cy="120" r="22" fill="#F59E0B" stroke="#FDE68A" stroke-width="3"/>
    <text x="68" y="127" font-family="sans-serif" font-size="20" font-weight="bold" fill="#FFFFFF">R$</text>
    <!-- Raios de luz -->
    <g stroke="#FDE047" stroke-width="3" stroke-linecap="round" opacity="0.8">
      <line x1="40" y1="5" x2="40" y2="-8"/>
      <line x1="0" y1="20" x2="-10" y2="10"/>
      <line x1="80" y1="20" x2="90" y2="10"/>
      <line x1="-15" y1="65" x2="-25" y2="65"/>
      <line x1="95" y1="65" x2="105" y2="65"/>
    </g>
  </g>

  <!-- Tag / Badge -->
  <rect x="40" y="40" width="220" height="30" rx="15" fill="#FFFFFF" fill-opacity="0.2"/>
  <text x="52" y="60" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="13" font-weight="600" fill="#D1FAE5" letter-spacing="0.5">GUIA PRÁTICO &bull; EFICIÊNCIA</text>

  <!-- Título Principal -->
  <text x="40" y="115" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="28" font-weight="800" fill="#FFFFFF">Como Economizar</text>
  <text x="40" y="150" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="28" font-weight="800" fill="#6EE7B7">Energia &amp; Dinheiro</text>

  <!-- Descrição -->
  <text x="40" y="195" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="15" font-weight="400" fill="#D1FAE5">Instruções para economizar em cada aparelho.</text>
  <text x="40" y="220" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="14" font-weight="400" fill="#A7F3D0" opacity="0.9">Dicas termodinâmicas práticas para reduzir a fatura.</text>

  <!-- Botão de Ação Visual -->
  <rect x="40" y="255" width="200" height="44" rx="22" fill="#FFFFFF" />
  <text x="65" y="282" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="14" font-weight="700" fill="#047857">Acessar Instruções &rarr;</text>
</svg>"""

    with open("assets/economia.svg", "w", encoding="utf-8") as f:
        f.write(svg_economia)

    print("SVG assets created successfully!")

if __name__ == "__main__":
    create_svg_assets()
