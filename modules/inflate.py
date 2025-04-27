# Creamos las funciones de manejo de bits
def get_bits(input_buf, input_pos, bit_offset, num_bits):
    result = 0
    for i in range(num_bits): # interar tantos bits como queremos leer
        if input_pos >= len(input_buf): # comprobar que el bit exista
            return None, None, None
        
        current_byte = input_buf[input_pos] # obtenemos el byte de la posicion input_pos
        bit = (current_byte >> bit_offset) & 1 # Hacemos una mascara para obtener el bit de la posicion bit_offset
        result |= bit << 1 # añadir el bit que hemos leído al resultado

        bit_offset += 1 # pasamos al siguiente bit
        if bit_offset == 8: # comparamos con 8 porque el último bit de un byte es el 8
            bit_offset = 0
            input_pos += 1
    return result, input_pos, bit_offset


def reverse_bits(value, bit_length):
    result = 0
    for _ in range(bit_length):
        result = (result << 1) | (value & 1) # desplazamos un bit de result a la izquierda y añadimos un bit de value
        value >>= 1 # desplazamos un bit de value a la derecha y asi queda el siguiente bit
    return result


# creamos las funciones de codficación de Huffman
def genera_huffman_code(code_length):
    max_code_length = max(code_length)
    bl_count = [0] * (max_code_length + 1)
    for length in code_length:
        bl_count[length] += 1

    code = 0
    next_code = [0] * (max_code_length + 1)
    for bits in range(1, max_code_length):
        code = (code + bl_count[bits-1]) << 1
        next_code[bits] = code
    
    huffman_code = {}
    for n in range(len(code_length)):
        length = code_length[n]
        if length != 0:
            code = next_code[length]
            next_code[length] += 1
            code_reverse = reverse_bits(code, length)
            huffman_code[code_reverse] = {'symbol': n, 'length': length}
    return huffman_code


def read_code(input_buf, input_pos, bit_offset, huffman_codes):
    max_code_length = max(code_info['length'] for code_info in huffman_codes.values())
    code = 0
    for i in range(1, max_code_length):
        bit, input_pos, bit_offset = get_bits(input_buf, input_pos, bit_offset, 1)
        if bit is None or input_pos is None or bit_offset is None:
            return None, None, None
        code |= bit << (i -1)
        if code in huffman_codes and huffman_codes and huffman_codes[code]['length'] == 1:
            symbol = huffman_codes[code]['symbol']
            return symbol, input_pos, bit_offset
    print("Invalid code in compressed data")
    return None, None, None
        
