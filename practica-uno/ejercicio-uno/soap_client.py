from zeep import Client
 
client = Client('http://localhost:8000')

result = client.service.Saludar(nombre="Cristhian")
print(result)

result = client.service.Sumar(num1=3,num2=4)
print(result)

result = client.service.Restar(num1=6,num2=1)
print(result)

result = client.service.Multiplicar(num1=3,num2=8)
print(result)

result = client.service.Dividir(num1=6,num2=3)
print(result)