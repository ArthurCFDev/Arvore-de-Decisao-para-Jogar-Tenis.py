def decidir_jogar_tenis(aspecto, umidade, vento):
    if aspecto == "Sol":
        if umidade == "Normal":
            return "S"
        else:
            return "N"
    elif aspecto == "Nuvens":
        return "S"
    elif aspecto == "Chuva":
        if vento == "Forte":
            return "N"
        else:
            return "S"
    else:
        return "N"

aspecto_input = input()
umidade_input = input()
vento_input = input()

decisao = decidir_jogar_tenis(aspecto_input, umidade_input, vento_input)
print(decisao)
