"""Módulo de cálculos termodinâmicos e elétricos para a oficina didática.

Contém fórmulas físicas para:
- Aquecimento de água em chaleira/cafeteira elétrica (Q = m * c * DeltaT)
- Consumo e aquecimento de água em chuveiro elétrico por classe de potência
- Ciclo de refrigeração e consumo mensal de geladeira doméstica
- Conversões de unidades (kJ <-> kWh, W <-> kW, etc.)
"""

from dataclasses import dataclass
from typing import Literal

# Constantes termodinâmicas fundamentais
CALOR_ESPECIFICO_AGUA = 4.184  # kJ / (kg * °C)
DENSIDADE_AGUA = 1.0  # kg / L (1 litro = 1 kg para água líquida padrão)
SEGUNDOS_POR_HORA = 3600
KJ_POR_KWH = 3600.0  # 1 kWh = 3.600 kJ

@dataclass
class ResultadoChaleira:
    """Resultados do aquecimento de água em chaleira/cafeteira elétrica."""
    volume_litros: float
    massa_kg: float
    temp_inicial: float
    temp_final: float
    delta_t: float
    potencia_watts: float
    eficiencia_percent: float
    calor_util_kj: float  # Calor absorvido pela água (m * c * deltaT)
    calor_total_kj: float  # Calor total fornecido pelo processo (Q_util / eta)
    tempo_segundos: float
    tempo_minutos: float
    energia_kwh: float  # Consumo elétrico em kWh
    custo_reais: float  # Custo em R$ de acordo com a tarifa

@dataclass
class ResultadoChuveiro:
    """Resultados do banho em chuveiro elétrico."""
    classe_potencia: str
    fator_potencia: float
    potencia_nominal_watts: float
    potencia_efetiva_watts: float
    tempo_minutos: float
    vazao_l_min: float
    volume_total_litros: float
    elevacao_temp_c: float
    temp_estimada_final_c: float
    calor_processo_kj: float  # Quantidade de calor gasta/transferida no processo
    energia_kwh: float  # Consumo elétrico em kWh
    custo_reais: float  # Custo do banho em R$
    custo_mensal_1pessoa: float
    custo_mensal_familia4: float

@dataclass
class ResultadoGeladeira:
    """Resultados do consumo e ciclo térmico da geladeira doméstica."""
    potencia_watts: float
    fator_ciclo: float  # % do tempo que o compressor fica ligado (~35%)
    horas_mes: int
    horas_operando: float
    cop: float  # Coeficiente de Performance do ciclo de refrigeração
    trabalho_eletrico_kj: float  # W = E_kwh * 3600
    calor_retirado_kj: float  # Q_frio = COP * W
    calor_rejeitado_kj: float  # Q_quente = (1 + COP) * W
    energia_kwh: float  # Consumo elétrico mensal em kWh
    custo_reais: float  # Custo total mensal em R$

def calcular_chaleira(
    potencia_watts: float,
    tarifa_kwh: float,
    volume_litros: float = 1.0,
    temp_inicial: float = 20.0,
    temp_final: float = 100.0,
    eficiencia: float = 0.90,
) -> ResultadoChaleira:
    """Calcula os parâmetros térmicos e financeiros para aquecer água na chaleira/cafeteira.
    
    Q_util = m * c * DeltaT
    Energia_eletrica = Q_util / eficiencia
    t = Energia_eletrica / Potencia
    """
    massa = volume_litros * DENSIDADE_AGUA
    delta_t = max(0.0, temp_final - temp_inicial)
    
    # Calor útil absorvido pela água em kJ
    calor_util_kj = massa * CALOR_ESPECIFICO_AGUA * delta_t
    
    # Calor total do processo levando em conta a eficiência
    eficiencia_valida = max(0.1, min(1.0, eficiencia))
    calor_total_kj = calor_util_kj / eficiencia_valida if calor_util_kj > 0 else 0.0
    
    # Consumo elétrico: 1 kWh = 3600 kJ
    energia_kwh = calor_total_kj / KJ_POR_KWH
    
    # Tempo em segundos = Energia em Joules / Potência em Watts
    # 1 kJ = 1000 J
    if potencia_watts > 0 and calor_total_kj > 0:
        tempo_seg = (calor_total_kj * 1000.0) / potencia_watts
    else:
        tempo_seg = 0.0
        
    tempo_min = tempo_seg / 60.0
    custo = energia_kwh * max(0.0, tarifa_kwh)
    
    return ResultadoChaleira(
        volume_litros=volume_litros,
        massa_kg=massa,
        temp_inicial=temp_inicial,
        temp_final=temp_final,
        delta_t=delta_t,
        potencia_watts=potencia_watts,
        eficiencia_percent=eficiencia_valida * 100.0,
        calor_util_kj=calor_util_kj,
        calor_total_kj=calor_total_kj,
        tempo_segundos=tempo_seg,
        tempo_minutos=tempo_min,
        energia_kwh=energia_kwh,
        custo_reais=custo,
    )

def calcular_chuveiro(
    potencia_watts: float,
    classe_potencia: Literal["alta", "media", "minima"],
    tempo_minutos: float,
    tarifa_kwh: float,
    temp_ambiente: float = 20.0,
    vazao_l_min: float = 4.0,
    eficiencia: float = 0.98,
) -> ResultadoChaveiro if False else ResultadoChuveiro:
    """Calcula os parâmetros térmicos e financeiros do banho em chuveiro elétrico.
    
    Classes:
    - Alta (Inverno): 100% da potência nominal
    - Média (Verão / Conforto): 65% da potência nominal
    - Mínima (Econômica / Ambiente): 35% da potência nominal
    """
    fatores = {
        "alta": (1.00, "Potência Alta (Inverno / Mais Quente)"),
        "media": (0.65, "Potência Média (Verão / Conforto)"),
        "minima": (0.35, "Potência Mínima (Econômico / Próxima ao Ambiente)"),
    }
    fator, nome_classe = fatores.get(classe_potencia, (1.0, "Potência Alta"))
    
    potencia_efetiva = potencia_watts * fator
    tempo_horas = max(0.0, tempo_minutos) / 60.0
    tempo_seg = max(0.0, tempo_minutos) * 60.0
    
    # Energia elétrica consumida em kWh
    energia_kwh = (potencia_efetiva * tempo_horas) / 1000.0
    
    # Quantidade de calor gasta/transferida para a água no processo em kJ
    # Eficiência de imersão de aprox. 98%
    calor_processo_kj = energia_kwh * KJ_POR_KWH * eficiencia
    
    # Volume total de água do banho
    volume_total = vazao_l_min * tempo_minutos
    massa_total = volume_total * DENSIDADE_AGUA
    
    # Elevação de temperatura estimada: DeltaT = Q / (m * c)
    if massa_total > 0:
        elevacao_temp = calor_processo_kj / (massa_total * CALOR_ESPECIFICO_AGUA)
    else:
        elevacao_temp = 0.0
    temp_final = temp_ambiente + elevacao_temp
    
    # Custo em R$
    custo_banho = energia_kwh * max(0.0, tarifa_kwh)
    custo_mensal_1p = custo_banho * 30.0  # 1 banho por dia
    custo_mensal_f4 = custo_mensal_1p * 4.0  # 4 pessoas
    
    return ResultadoChuveiro(
        classe_potencia=nome_classe,
        fator_potencia=fator,
        potencia_nominal_watts=potencia_watts,
        potencia_efetiva_watts=potencia_efetiva,
        tempo_minutos=tempo_minutos,
        vazao_l_min=vazao_l_min,
        volume_total_litros=volume_total,
        elevacao_temp_c=elevacao_temp,
        temp_estimada_final_c=temp_final,
        calor_processo_kj=calor_processo_kj,
        energia_kwh=energia_kwh,
        custo_reais=custo_banho,
        custo_mensal_1pessoa=custo_mensal_1p,
        custo_mensal_familia4=custo_mensal_f4,
    )

def calcular_geladeira(
    potencia_watts: float,
    tarifa_kwh: float,
    fator_ciclo: float = 0.35,
    dias_mes: int = 30,
    cop: float = 2.5,
) -> ResultadoGeladeira:
    """Calcula o consumo mensal e balanço térmico da geladeira doméstica.
    
    O compressor da geladeira não opera continuamente 24h. Ele liga e desliga
    mantendo a temperatura do evaporador (ciclo de trabalho típico ~30% a 40%).
    COP = Q_frio / Trabalho_eletrico
    Q_quente (rejeitado no condensador) = Q_frio + Trabalho_eletrico
    """
    horas_mes = dias_mes * 24
    horas_operando = horas_mes * max(0.05, min(1.0, fator_ciclo))
    
    # Energia elétrica consumida no mês em kWh
    energia_kwh = (potencia_watts * horas_operando) / 1000.0
    
    # Trabalho elétrico em kJ
    trabalho_kj = energia_kwh * KJ_POR_KWH
    
    # Calor retirado do interior (alimentos / freezer)
    calor_retirado_kj = trabalho_kj * cop
    
    # Calor rejeitado na cozinha pelo condensador traseiro
    calor_rejeitado_kj = trabalho_kj + calor_retirado_kj
    
    # Custo mensal
    custo = energia_kwh * max(0.0, tarifa_kwh)
    
    return ResultadoGeladeira(
        potencia_watts=potencia_watts,
        fator_ciclo=fator_ciclo,
        horas_mes=horas_mes,
        horas_operando=horas_operando,
        cop=cop,
        trabalho_eletrico_kj=trabalho_kj,
        calor_retirado_kj=calor_retirado_kj,
        calor_rejeitado_kj=calor_rejeitado_kj,
        energia_kwh=energia_kwh,
        custo_reais=custo,
    )
