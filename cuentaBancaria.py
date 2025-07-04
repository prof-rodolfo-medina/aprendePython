class CuentaBancaria:
    """
    Clase que representa una cuenta bancaria simple.
    Permite depositar, retirar y consultar el saldo.
    """

    def __init__(self, titular: str, saldo_inicial: float = 0.0):
        self.titular = titular
        self.saldo = saldo_inicial

    def depositar(self, monto: float) -> None:
        """Agrega dinero a la cuenta."""
        if monto > 0:
            self.saldo += monto

    def retirar(self, monto: float) -> bool:
        """Retira dinero de la cuenta si hay saldo suficiente."""
        if 0 < monto <= self.saldo:
            self.saldo -= monto
            return True
        return False

    def consultar_saldo(self) -> float:
        """Devuelve el saldo actual de la cuenta."""
        return self.saldo

    def __str__(self):
        return f"Cuenta de {self.titular}, Saldo: {self.saldo:.2f}"

# Ejemplo de uso:
if __name__ == "__main__":
    cuenta = CuentaBancaria("Juan", 1000)
    print(cuenta)
    cuenta.depositar(500)
    print(f"Después de depositar 500: {cuenta.consultar_saldo()}")
    exito = cuenta.retirar(300)
    print(f"Retiro de 300 exitoso: {exito}")
    print(f"Saldo final: {cuenta.consultar_saldo()}")
    print(cuenta)
