# Replace the "ANSWER HERE" for your answer

def number_to_month(month):
    numb = month
    match numb:
        case 1:
            return "enero"
        case 2:
            return "febrero"
        case 3:
            return "marzo"
        case 4:
            return "abril"
        case 5:
            return "mayo"
        case 6:
            return "junio"
        case 7:
            return "julio"
        case 8:
            return "agosto"
        case 9:
            return "septiembre"
        case 10:
            return "octubre"
        case 11:
            return "noviembre"
        case 12:
            return "diciembre"
        case _:
            return "error"
