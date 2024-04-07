from http.server import HTTPServer
from pysimplesoap.server import SOAPHandler, SoapDispatcher

def Saludar(nombre):
    return "¡Hola, {}!".format(nombre)

def Sumar(num1, num2):
    return "{} + {} = {}".format(num1,num2,num1+num2)
def Restar(num1, num2):
    return "{} - {} = {}".format(num1,num2,num1-num2)
def Multiplicar(num1, num2):
    return "{} * {} = {}".format(num1,num2,num1*num2)
def Dividir(num1, num2):
    return "{} / {} = {}".format(num1,num2,num1/num2)

dispatcher = SoapDispatcher(
    "ejemplo-soap-server",
    location="http://localhost:8000/",
    action="http://localhost:8000/",
    namespace="http://localhost:8000/",
    trace=True,
    ns=True,
)
dispatcher.register_function(
    "Saludar",
    Saludar,
    returns={"saludo":str},
    args={"nombre":str},
)
dispatcher.register_function(
    "Sumar",
    Sumar,
    returns={"res":str},
    args={"num1":int,"num2":int}
)
dispatcher.register_function(
    "Restar",
    Restar,
    returns={"res":str},
    args={"num1":int,"num2":int}
)
dispatcher.register_function(
    "Multiplicar",
    Multiplicar,
    returns={"res":str},
    args={"num1":int,"num2":int}
)
dispatcher.register_function(
    "Dividir",
    Dividir,
    returns={"res":str},
    args={"num1":int,"num2":int}
)

server = HTTPServer(("0.0.0.0",8000), SOAPHandler)
server.dispatcher = dispatcher
print("Servidor SOAP iniciando en http://localhost:8000")
server.serve_forever()