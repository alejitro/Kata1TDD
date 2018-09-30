

class Calculadora:
    def sumar(self,cadena):
        if cadena=="":
            return 0
        elif "," in cadena or ":" in cadena or "&" in cadena:
            cadena=cadena.replace(":",",")
            cadena=cadena.replace("&",",")
            numeros=cadena.split(",")
            print(numeros)
            suma=0
            num: object
            for num in numeros:
                suma+=int(num)
                print(suma)
            return suma
        else:
            return int(cadena)