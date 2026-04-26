import sys, Ice
import Demo

class PrinterI(Demo.Printer):
    def printString(self, s, current=None):
        print(f"Mensagem recebida: {s}")

    def toUpperCase(self, s, current=None):
        return s.upper()

    def countCharacters(self, s, current=None):
        return len(s)


class CalculatorI(Demo.Calculator):
    def add(self, a, b, current=None):
        return a + b

    def multiply(self, a, b, current=None):
        return a * b


with Ice.initialize(sys.argv) as communicator:
    adapter = communicator.createObjectAdapterWithEndpoints(
        "SimpleAdapter",
        "default -p 11000"
    )

    printer = PrinterI()
    calculator = CalculatorI()

    adapter.add(printer, communicator.stringToIdentity("SimplePrinter"))
    adapter.add(calculator, communicator.stringToIdentity("SimpleCalculator"))

    adapter.activate()

    print("Servidor Ice iniciado na porta 11000.")
    print("Objeto Printer registrado como SimplePrinter.")
    print("Objeto Calculator registrado como SimpleCalculator.")

    communicator.waitForShutdown()

