def reloj_arena(m: int, s: str) -> str:
    if m <= 0:
        print("Error: La altura debe ser un entero positivo")
        return ""
    for i in range(m):
        print(" " * i + s * (2 * (m - i) - 1))
    for i in range(1, m):
        print(" " * (m - 1 - i) + s * (2 * i + 1))
    return ""
