def division_par_2(a: float, b: float) -> float:
    try:
        return a/b
    except TypeError:
        print("a ou b ne sont pas des nombre réel")
    except ZeroDivisionError:
        print("ATTENTION b est egal a zero, la division est imposilble")


print(division_par_2(10, 2))   # 5.0
print(division_par_2(10, 0))   # message d'erreur + None
print(division_par_2(10, "a")) # message d'erreur + None
