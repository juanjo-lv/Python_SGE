def sepagara(importe,iva=21,descuento=10):
    aux = importe + ((importe*21)/100)
    total = aux - ((aux*10)/100)
    return aux

print(sepagara(25))