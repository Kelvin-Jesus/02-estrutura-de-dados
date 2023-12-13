from Fracao import Fracao

f1 = Fracao(5, 7)
f2 = Fracao(3, 7)

print(f1, '=', round(f1.retornaValorReal(), 1))

print(f1, '*', f2, '=', f1.multiplicaFracao(f2))

print(f1, '-', f2, '=', f1.subtraiFracao(f2))

print(f1, '/', f2, '=', f1.divideFracao(f2))

print(Fracao(2, 3).somaFracao(Fracao(1, 3)))

print(Fracao(3, 3).subtraiFracao(Fracao(1, 3)))