def analizar(Lista):
    menor = min (mixta);
    promedio = sum (mixta)/len(mixta)
    return {
        "Menor":menor,
        "Promedio":sum(Lista)
    }
    if __name__=="__Main__":
        numeros = [4,8,2,10]
        resultado = analizar(numeros)
        print(resultado)
