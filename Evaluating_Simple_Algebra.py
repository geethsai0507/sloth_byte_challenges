def evalAlgebra(a: str) -> int:
    if not a:
        return 0
    else:
        data = a.split(" = ")
        lhs = data[0].replace(" ","")
        rhs = int(data[1])
        for i in range(len(lhs)):
            if lhs[i] == "x" and i == 0:
                lhs = int(lhs.replace("x",""))
                if lhs < rhs:
                    return(rhs + (-lhs))
                else:
                    return(rhs - lhs)
            elif lhs[i] == "x" and i != 0 and lhs[i-1] == "-":
                lhs = int(lhs.replace("-x",""))
                return(lhs - rhs)
            elif lhs[i] == "x" and i != 0 and lhs[i-1] == "+":
                lhs = int(lhs.replace("+x",""))
                return(rhs - lhs)
            else:
                continue


expr = evalAlgebra(input("enter equation: "))
print("x =", expr)