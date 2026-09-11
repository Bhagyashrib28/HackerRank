import string

def print_rangoli(size):
    alphabet = string.ascii_lowercase
    lines = []
    
    for i in range(size):
        # Slice letters up to the current row index and reverse
        s = "-".join(alphabet[i:size])
        row = s[::-1] + s[1:]
        # Center the row with hyphens
        lines.append(row.center(4 * size - 3, "-"))
    
    # Bottom half (including center row) reversed + top half
    rangoli = lines[::-1] + lines[1:]
    print("\n".join(rangoli))


    
if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
