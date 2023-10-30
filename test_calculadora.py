import calculadora

def test_somar():
    assert calculadora.somar(2, 3) == 5
    assert calculadora.somar(-1, 1) == 0

def test_subtrair():
    assert calculadora.subtrair(5, 3) == 2
    assert calculadora.subtrair(1, 5) == -4

def test_multiplicar():
    assert calculadora.multiplicar(2, 3) == 6
    assert calculadora.multiplicar(4, 0) == 0

def test_dividir():
    assert calculadora.dividir(6, 3) == 2
    assert calculadora.dividir(5, 2) == 2.5

    # Teste para divisão por zero
    try:
        calculadora.dividir(1, 0)
        assert False, "A divisão por zero não levantou uma exceção"
    except ValueError:
        pass
