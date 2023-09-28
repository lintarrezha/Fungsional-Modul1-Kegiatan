# Fungsi tambah
def add(x, y):
    return x + y

# Fungsi pengurangan
def minus(x, y):
    return x - y

# Fungsi perkalian
def mult(x, y):
    return x * y

# Fungsi pembagian
def div(x, y):
    if y == 0:
        return "Tidak bisa dibagi oleh nol"
    return x / y

# Fungsi pohon ekspresi
def tree(node):
    if type(node) in (int, float):
        return node
    elif type(node) is tuple and len(node) == 3:
        operator, left_operand, right_operand = node
    
        if operator == '+':
            return tree(left_operand) + tree(right_operand)
        elif operator == '-':
            return tree(left_operand) - tree(right_operand)
        elif operator == '*':
            return tree(left_operand) * tree(right_operand)
        elif operator == '/':
            return tree(left_operand) / tree(right_operand)
    

# Contoh pohon ekspresi: (2 + 3) * (5 - 1)
expression_tree = ('*', ('+', 2, 3), ('-', 5, 1))

# Evaluasi pohon ekspresi dengan fungsi pada paradigma fungsional
result = tree(expression_tree)
print("Hasil evaluasi pohon ekspresi:", result)
