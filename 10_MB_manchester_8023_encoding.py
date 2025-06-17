import matplotlib.pyplot as plt

# 4B/5B encoding table
FOURB_FIVEB_TABLE = {
    '0': '11110', '1': '01001', '2': '10100', '3': '10101',
    '4': '01010', '5': '01011', '6': '01110', '7': '01111',
    '8': '10010', '9': '10011', 'A': '10110', 'B': '10111',
    'C': '11010', 'D': '11011', 'E': '11100', 'F': '11101',
    # Optional control codes if needed later
}

def chunk_bits(bits, size=4):
    """Chunk bits into groups of `size`, pad last group with 0s if needed."""
    chunks = []
    for i in range(0, len(bits), size):
        chunk = bits[i:i+size]
        if len(chunk) < size:
            chunk += [0] * (size - len(chunk))  # zero-padding
        chunks.append(chunk)
    return chunks

def bits_to_hex_symbol(bits):
    """Convert list of 4 bits to hex symbol"""
    return hex(int(''.join(str(b) for b in bits), 2))[2:].upper()

def encode_4b5b_from_bits(bitstream):
    """Encode raw data bits using 4B/5B"""
    hex_symbols = [bits_to_hex_symbol(chunk) for chunk in chunk_bits(bitstream)]
    encoded_bits = []
    for symbol in hex_symbols:
        if symbol not in FOURB_FIVEB_TABLE:
            raise ValueError(f"Symbol '{symbol}' not in 4B/5B table.")
        encoded_bits.extend([int(b) for b in FOURB_FIVEB_TABLE[symbol]])
    return hex_symbols, encoded_bits

def data_line(bits):
    """Generate signal line for plotting"""
    time = []
    signal = []
    for i, bit in enumerate(bits):
        time += [i, i + 1]
        signal += [bit, bit]
    return time, signal

def plot_encoded(hex_symbols, encoded_bits):
    """Plot the encoded 4B/5B signal"""
    time, signal = data_line(encoded_bits)
    plt.figure(figsize=(12, 3))
    plt.step(time, signal, where='post', linewidth=2, color='blue')
    plt.title("4B/5B Encoded Output from Bitstream")
    plt.ylim(-0.5, 1.5)
    plt.xlabel("Time (bit periods)")
    plt.ylabel("Signal")
    plt.grid(True, alpha=0.3)

    for i, sym in enumerate(hex_symbols):
        plt.text(i * 5 + 2.5, 1.1, sym, ha='center', fontweight='bold')

    plt.tight_layout()
    plt.savefig("4b5b_from_bits.png", dpi=150, bbox_inches='tight')
    print("Plot saved as '4b5b_from_bits.png'")

# === MAIN EXECUTION ===

if __name__ == "__main__":
    data = [1, 1, 0, 1, 0, 0, 1, 1, 1, 0, 1]
    print("Original data bits:", data)

    symbols, encoded = encode_4b5b_from_bits(data)

    print("Grouped into hex symbols:", symbols)
    print("4B/5B Encoded bits:", encoded)

    plot_encoded(symbols, encoded)
