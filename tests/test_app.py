"""Testes funcionais e de validação da aplicação Streamlit usando AppTest."""
import sys
import os

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, ROOT_DIR)

from streamlit.testing.v1 import AppTest
from utils.thermo_calc import calcular_chaleira, calcular_chuveiro, calcular_geladeira

def test_calculos_termodinamicos_chaleira():
    # 1 litro de água de 20°C a 100°C: Q = 1 * 4.184 * 80 = 334.72 kJ
    # Com 90% de eficiência: Q_total = 371.91 kJ -> E = 371.91 / 3600 = 0.1033 kWh
    res = calcular_chaleira(potencia_watts=1500, tarifa_kwh=0.85)
    assert round(res.calor_util_kj, 2) == 334.72
    assert round(res.energia_kwh, 4) == 0.1033
    assert round(res.custo_reais, 3) == round(0.1033086 * 0.85, 3)
    assert res.tempo_minutos > 3.0 and res.tempo_minutos < 5.0

def test_calculos_termodinamicos_chuveiro():
    # Chuveiro 5500W a 100% (alta) por 12 min (0.2 h): E = 5.5 * 0.2 = 1.100 kWh
    res_alta = calcular_chuveiro(5500, "alta", 12, 0.85)
    assert round(res_alta.energia_kwh, 3) == 1.100
    assert round(res_alta.custo_reais, 2) == round(1.1 * 0.85, 2)
    assert res_alta.calor_processo_kj > 3800

    # Chuveiro 5500W a 65% (média): E = 5.5 * 0.65 * 0.2 = 0.715 kWh
    res_media = calcular_chuveiro(5500, "media", 12, 0.85)
    assert round(res_media.energia_kwh, 3) == 0.715
    assert res_media.energia_kwh < res_alta.energia_kwh

    # Chuveiro 5500W a 35% (mínima): E = 5.5 * 0.35 * 0.2 = 0.385 kWh
    res_minima = calcular_chuveiro(5500, "minima", 12, 0.85)
    assert round(res_minima.energia_kwh, 3) == 0.385
    assert res_minima.energia_kwh < res_media.energia_kwh

def test_calculos_termodinamicos_geladeira():
    # Geladeira 150W com 35% de ciclo no mês (720h * 0.35 = 252h): E = 150 * 252 / 1000 = 37.8 kWh
    res = calcular_geladeira(150, 0.85, fator_ciclo=0.35)
    assert round(res.energia_kwh, 1) == 37.8
    assert round(res.custo_reais, 2) == round(37.8 * 0.85, 2)
    assert res.calor_retirado_kj == res.trabalho_eletrico_kj * 2.5

def test_app_home_page():
    at = AppTest.from_file(os.path.join(ROOT_DIR, "app.py"), default_timeout=15)
    at.run()
    assert not at.exception
    # Verifica presença do input da tarifa na home
    assert len(at.number_input) >= 1
    tarifa_input = at.number_input(key="home_tarifa_input")
    assert tarifa_input.value == 0.85
    # Verifica presença dos links/imagens
    assert len(at.image) >= 4

def test_pagina_chaleira_direta():
    at = AppTest.from_file(os.path.join(ROOT_DIR, "app.py"), default_timeout=15)
    at.run()
    at.switch_page("app_pages/chaleira.py")
    at.run()
    assert not at.exception
    metric_labels = [m.label for m in at.metric]
    assert any("Quantidade de Calor" in lbl for lbl in metric_labels)
    assert any("Energia Elétrica" in lbl for lbl in metric_labels)
    assert any("Custo Total" in lbl for lbl in metric_labels)

def test_pagina_chuveiro_direta():
    at = AppTest.from_file(os.path.join(ROOT_DIR, "app.py"), default_timeout=15)
    at.run()
    at.switch_page("app_pages/chuveiro.py")
    at.run()
    assert not at.exception
    metric_labels = [m.label for m in at.metric]
    assert any("Quantidade de Calor" in lbl for lbl in metric_labels)
    assert any("Energia Elétrica" in lbl for lbl in metric_labels)
    assert any("Custo Total" in lbl for lbl in metric_labels)

def test_pagina_geladeira_direta():
    at = AppTest.from_file(os.path.join(ROOT_DIR, "app.py"), default_timeout=15)
    at.run()
    at.switch_page("app_pages/geladeira.py")
    at.run()
    assert not at.exception
    metric_labels = [m.label for m in at.metric]
    assert any("Quantidade de Calor" in lbl for lbl in metric_labels)
    assert any("Energia Elétrica" in lbl for lbl in metric_labels)
    assert any("Custo Total" in lbl for lbl in metric_labels)

def test_pagina_economia_direta():
    at = AppTest.from_file(os.path.join(ROOT_DIR, "app.py"), default_timeout=15)
    at.run()
    at.switch_page("app_pages/economia.py")
    at.run()
    assert not at.exception

if __name__ == "__main__":
    test_calculos_termodinamicos_chaleira()
    test_calculos_termodinamicos_chuveiro()
    test_calculos_termodinamicos_geladeira()
    test_app_home_page()
    test_pagina_chaleira_direta()
    test_pagina_chuveiro_direta()
    test_pagina_geladeira_direta()
    test_pagina_economia_direta()
    print("ALL TESTS PASSED SUCCESSFULLY! 🚀")
