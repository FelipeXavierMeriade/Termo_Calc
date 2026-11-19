"""Verificação detalhada das 3 correções solicitadas pelo usuário executando através de app.py."""
import sys
import os

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, ROOT_DIR)

from streamlit.testing.v1 import AppTest

def test_correcao_tarifa_digitada_home():
    at = AppTest.from_file(os.path.join(ROOT_DIR, "app.py"), default_timeout=15)
    at.run()
    assert not at.exception
    
    # 1. Altera a tarifa via digitação para 1.25 na Home
    tarifa_input = at.number_input(key="home_tarifa_input")
    assert tarifa_input.value == 0.85
    tarifa_input.set_value(1.25)
    at.run()
    assert not at.exception
    
    # Confirma que a tarifa permaneceu 1.25 e o session_state foi atualizado
    assert at.session_state.tarifa_kwh == 1.25
    assert at.number_input(key="home_tarifa_input").value == 1.25
    print("✓ Teste 1: Digitação da tarifa na Home OK (sem conflito/reset)!")

def test_navegacao_com_tarifa_alterada():
    at = AppTest.from_file(os.path.join(ROOT_DIR, "app.py"), default_timeout=15)
    at.run()
    
    # Altera a tarifa para 1.30
    at.number_input(key="home_tarifa_input").set_value(1.30)
    at.run()
    assert at.session_state.tarifa_kwh == 1.30
    
    # Navega para a página da chaleira
    at.switch_page("app_pages/chaleira.py")
    at.run()
    assert not at.exception
    
    # A tarifa de 1.30 deve estar preservada na página da chaleira!
    assert at.session_state.tarifa_kwh == 1.30
    assert at.number_input(key="chaleira_tarifa_input").value == 1.30
    print("✓ Teste 2: Navegação para a Chaleira mantendo a tarifa digitada (1.30) OK!")

def test_correcao_potencia_chaleira():
    at = AppTest.from_file(os.path.join(ROOT_DIR, "app.py"), default_timeout=15)
    at.run()
    at.switch_page("app_pages/chaleira.py")
    at.run()
    assert not at.exception
    
    # Digita potência personalizada de 1750 W
    pot_input = at.number_input(key="input_potencia_chaleira_val")
    pot_input.set_value(1750)
    at.run()
    assert not at.exception
    
    # Verifica que 1750 W NÃO foi sobrescrito por nenhum preset
    assert at.number_input(key="input_potencia_chaleira_val").value == 1750
    assert at.session_state.potencia_chaleira == 1750
    
    # As métricas devem refletir 1750 W (tempo ~3.54 min)
    assert len(at.metric) >= 3
    print("✓ Teste 3: Digitação livre da potência da Chaleira OK (1750W mantidos)!")

def test_correcao_potencia_chuveiro():
    at = AppTest.from_file(os.path.join(ROOT_DIR, "app.py"), default_timeout=15)
    at.run()
    at.switch_page("app_pages/chuveiro.py")
    at.run()
    assert not at.exception
    
    # Digita potência de 6200 W no chuveiro
    pot_input = at.number_input(key="input_potencia_chuveiro_val")
    pot_input.set_value(6200)
    # Digita tempo de 18 minutos
    tempo_input = at.number_input(key="input_tempo_chuveiro_val")
    tempo_input.set_value(18)
    at.run()
    assert not at.exception
    
    assert at.number_input(key="input_potencia_chuveiro_val").value == 6200
    assert at.number_input(key="input_tempo_chuveiro_val").value == 18
    print("✓ Teste 4: Digitação livre do Chuveiro OK (6200W e 18min mantidos)!")

def test_correcao_potencia_geladeira():
    at = AppTest.from_file(os.path.join(ROOT_DIR, "app.py"), default_timeout=15)
    at.run()
    at.switch_page("app_pages/geladeira.py")
    at.run()
    assert not at.exception
    
    # Digita potência de 185 W na geladeira
    pot_input = at.number_input(key="input_potencia_geladeira_val")
    pot_input.set_value(185)
    at.run()
    assert not at.exception
    
    assert at.number_input(key="input_potencia_geladeira_val").value == 185
    print("✓ Teste 5: Digitação livre da Geladeira OK (185W mantidos)!")

def test_imagens_todas_as_paginas():
    for page_path in ["app_pages/home.py", "app_pages/chaleira.py", "app_pages/chuveiro.py", "app_pages/geladeira.py", "app_pages/economia.py"]:
        at = AppTest.from_file(os.path.join(ROOT_DIR, "app.py"), default_timeout=15)
        at.run()
        if page_path != "app_pages/home.py":
            at.switch_page(page_path)
            at.run()
        assert not at.exception
        assert len(at.image) >= 1, f"Página {page_path} sem imagem!"
    print("✓ Teste 6: Todas as páginas possuem imagens exibidas com sucesso!")

if __name__ == "__main__":
    test_correcao_tarifa_digitada_home()
    test_navegacao_com_tarifa_alterada()
    test_correcao_potencia_chaleira()
    test_correcao_potencia_chuveiro()
    test_correcao_potencia_geladeira()
    test_imagens_todas_as_paginas()
    print("\nTODOS OS TESTES DE CORREÇÃO PASSARAM COM 100% DE SUCESSO! 🎯")
