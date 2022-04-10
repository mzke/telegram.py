from enum import Enum


class EnumEmoji(str, Enum):
    falha = "falha"
    sucesso = "sucesso"
    alerta = "alerta"
    info = "info"
    bateria = "bateria"
    energia = "energia"
    feito = "feito"
    cancelado = "cancelado"
    on = "on"
    off = "off"
