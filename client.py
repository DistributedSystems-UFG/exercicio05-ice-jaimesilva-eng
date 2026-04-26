import sys, Ice
import Demo

SERVER_IP = "172.31.44.131"

with Ice.initialize(sys.argv) as communicator:
    printer_base = communicator.stringToProxy(
            f"SimplePrinter:tcp -h {SERVER_IP} -p 11000"
    )

    calculator_base = communicator.stringToProxy(
            f"SimpleCalculator:tcp -h {SERVER_IP} -p 11000"
    )

    printer = Demo.PrinterPrx.checkedCast(printer_base)
    calculator = Demo.CalculatorPrx.checkedCast(calculator_base)

    if not printer:
        raise RuntimeError("Proxy inválido para Printer")

    if not calculator:
        raise RuntimeError("Proxy inválido para Calculator")

    printer.printString("Hello World!")

    upper = printer.toUpperCase("sistemas distribuidos com ice")
    count = printer.countCharacters("sistemas distribuidos com ice")

    print(f"Texto em maiúsculas: {upper}")
    print(f"Quantidade de caracteres: {count}")

    soma = calculator.add(10, 5)
    multiplicacao = calculator.multiply(10, 5)

    print(f"Soma: {soma}")
    print(f"Multiplicação: {multiplicacao}")

