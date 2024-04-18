def totalIva(cant, iva):
    iva = iva * .01
    if iva > 0:
        total = print((cant*iva)+cant)
    else:
        total = print((cant*.21)+cant)

  #  return total 

totalIva(100,16)