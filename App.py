def analizar(Lista):
    suma=sum(Lista)
    mayor=max(Lista)
    return{"suma": suma ,
    "mayor": mayor }
    if __name__=="__Main__":
        numeros = [4,8,2,10]
        resultado = analizar(numeros)
        print(resultado)
