import sys
from solucion import reloj_arena
def main():
    if sys.stdin.isatty():
        data = []
        data.append(input("Ingresa la altura: ").strip())
        data.append(input("Ingresa el caracter: "))
    else:
        data = sys.stdin.read().strip().splitlines()
    if len(data) < 2:
        print("Error: Se esperan 2 lineas de entrada (altura, caracter)")
        return
    m_str = data[0].strip()
    s = data[1]
    try:
        m = int(m_str)
    except ValueError:
        print("Error: La altura debe ser un numero entero")
        return
    if len(s) == 0:
        print("Error: El caracter no puede ser vacío")
        return
    reloj_arena(m, s)
if __name__ == "__main__":
    main()
