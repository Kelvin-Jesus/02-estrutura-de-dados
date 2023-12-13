from __future__ import annotations
import importlib

tad = importlib.import_module("01-TAD-ponto")
Ponto = tad.Ponto

ponto = Ponto(10, 20)
ponto2 = Ponto(20, 40)

print(ponto)

print(ponto.acessa())
ponto.atribui(10, 25)

print(round(ponto.distancia(ponto2), 2))