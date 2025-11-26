def reloj_arena(m: int, s: str) -> str:
    if m <= 0:
        print("Error: La altura debe ser un entero positivo")
        return ""
    char = s[0]
    for i in range(m):
        print(" " * i + char * (2 * (m - i) - 1))
    for i in range(1, m):
        print(" " * (m - 1 - i) + char * (2 * i + 1))
    return ""
