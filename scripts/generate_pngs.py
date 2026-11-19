"""Gera imagens PNG de alta resolução para os 4 cards da página inicial."""
import os
from PIL import Image, ImageDraw, ImageFont

def hex_to_rgb(hex_str):
    hex_str = hex_str.lstrip('#')
    return tuple(int(hex_str[i:i+2], 16) for i in (0, 2, 4))

def create_gradient_card(
    filename: str,
    color_start: str,
    color_end: str,
    badge_text: str,
    title_line1: str,
    title_line2: str,
    description: str,
    detail: str,
    action_text: str,
    symbol: str,
):
    os.makedirs("assets", exist_ok=True)
    w, h = 800, 460
    img = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    r1, g1, b1 = hex_to_rgb(color_start)
    r2, g2, b2 = hex_to_rgb(color_end)

    # Cria fundo com gradiente vertical e cantos arredondados
    # Desenha gradiente em uma imagem base
    grad_img = Image.new("RGBA", (w, h))
    for y in range(h):
        ratio = y / float(h)
        r = int(r1 + (r2 - r1) * ratio)
        g = int(g1 + (g2 - g1) * ratio)
        b = int(b1 + (b2 - b1) * ratio)
        ImageDraw.Draw(grad_img).line([(0, y), (w, y)], fill=(r, g, b, 255))

    # Máscara para bordas suavizadas / arredondadas (radius = 32px)
    mask = Image.new("L", (w, h), 0)
    mask_draw = ImageDraw.Draw(mask)
    mask_draw.rounded_rectangle([(0, 0), (w, h)], radius=32, fill=255)
    
    img.paste(grad_img, (0, 0), mask)
    draw = ImageDraw.Draw(img)

    
    # Elementos decorativos (círculos suaves de brilho)
    overlay = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    ov_draw = ImageDraw.Draw(overlay)
    ov_draw.ellipse([(w - 280, -40), (w + 120, 320)], fill=(255, 255, 255, 25))
    ov_draw.ellipse([(w - 200, 180), (w + 100, 480)], fill=(255, 255, 255, 18))
    img = Image.alpha_composite(img, overlay)
    draw = ImageDraw.Draw(img)

    # Fontes: tenta carregar fontes do sistema ou padrão
    font_badge = ImageFont.load_default()
    font_title = ImageFont.load_default()
    font_desc = ImageFont.load_default()

    font_paths = [
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
        "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf",
        "/usr/share/fonts/truetype/freefont/FreeSansBold.ttf",
    ]
    font_regular_paths = [
        "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
        "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf",
        "/usr/share/fonts/truetype/freefont/FreeSans.ttf",
    ]

    for p in font_paths:
        if os.path.exists(p):
            try:
                font_title = ImageFont.truetype(p, 42)
                font_badge = ImageFont.truetype(p, 18)
                break
            except Exception:
                pass

    for p in font_regular_paths:
        if os.path.exists(p):
            try:
                font_desc = ImageFont.truetype(p, 22)
                font_detail = ImageFont.truetype(p, 18)
                font_btn = ImageFont.truetype(p, 20)
                font_sym = ImageFont.truetype(p, 110)
                break
            except Exception:
                pass
    else:
        font_detail = font_desc
        font_btn = font_desc
        font_sym = font_title

    # 2. Títulos
    draw.text((45, 110), title_line1, font=font_title, fill=(255, 255, 255, 255))
    draw.text((45, 160), title_line2, font=font_title, fill=(255, 240, 200, 255))

    # 3. Descrição
    draw.text((45, 230), description, font=font_desc, fill=(255, 255, 255, 230))
    draw.text((45, 265), detail, font=font_detail, fill=(255, 255, 255, 190))

    # 4. Símbolo temático à direita
    draw.text((w - 220, 140), symbol, font=font_sym, fill=(255, 255, 255, 180))

    # 5. Botão de Ação Visual
    btn_w = 280
    btn_h = 56
    btn_x = 45
    btn_y = 350
    draw.rounded_rectangle([(btn_x, btn_y), (btn_x + btn_w, btn_y + btn_h)], radius=28, fill=(255, 255, 255, 250))
    draw.text((btn_x + 32, btn_y + 16), action_text, font=font_btn, fill=(r2, g2, b2, 255))

    img.save(filename, "PNG")
    print(f"Salvo {filename}")

def generate_all_pngs():
    create_gradient_card(
        filename="assets/chaleira.png",
        color_start="#EA580C",
        color_end="#9A3412",
        badge_text="TERMODINÂMICA • 1 L DE ÁGUA",
        title_line1="Chaleira & Cafeteira",
        title_line2="Elétrica",
        description="Quanto custa para aquecer 1 litro de água?",
        detail="Calcule calor (kJ), tempo de fervura, kWh e custo.",
        action_text="Abrir Calculadora →",
        symbol="♨",
    )
    create_gradient_card(
        filename="assets/chuveiro.png",
        color_start="#0284C7",
        color_end="#0F172A",
        badge_text="BANHO DIÁRIO • 3 POTÊNCIAS",
        title_line1="Chuveiro Elétrico",
        title_line2="Consumo do Banho",
        description="Quantos reais e kWh se gasta no banho?",
        detail="Compare potência alta, média e mínima no tempo.",
        action_text="Abrir Calculadora →",
        symbol="⚡",
    )
    create_gradient_card(
        filename="assets/geladeira.png",
        color_start="#0D9488",
        color_end="#134E4A",
        badge_text="CICLO DE REFRIGERAÇÃO • 30 DIAS",
        title_line1="Geladeira Ligada",
        title_line2="Durante o Mês",
        description="Quanto custa manter a geladeira no mês?",
        detail="Entenda o calor retirado, consumo e custo mensal.",
        action_text="Abrir Calculadora →",
        symbol="❄",
    )
    create_gradient_card(
        filename="assets/economia.png",
        color_start="#059669",
        color_end="#064E3B",
        badge_text="GUIA PRÁTICO • EFICIÊNCIA",
        title_line1="Como Economizar",
        title_line2="Energia e Dinheiro",
        description="Dicas práticas para cada equipamento da oficina.",
        detail="Reduza a fatura aplicando conceitos de termodinâmica.",
        action_text="Ver Instruções →",
        symbol="$",
    )

if __name__ == "__main__":
    generate_all_pngs()
