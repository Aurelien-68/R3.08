def division(a: float, b: float) -> float:
    if b==0:
        raise ZeroDivisionError("on ne divise pas part 0")
    return a/b

if __name__=="__main__":
    try:
        res=division(2,0)
    except ZeroDivisionError as e:
        print(f"{e}")
    else:
        print(f"resultat {res}")