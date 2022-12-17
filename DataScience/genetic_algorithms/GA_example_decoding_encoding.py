
def BinaryToString(bin_data):
        binary_int = int(bin_data, 2)
        byte_number = binary_int.bit_length() + 7 // 8
        binary_array = binary_int.to_bytes(byte_number, "big")
        ascii_text = binary_array.decode()
        return ascii_text

def StringToBinary(my_string):
        return ''.join(format(ord(i), '08b') for i in my_string)
        
        
        
if __name__ == "__main__":

        print('_'*60)
        print("ENCODING")

        my_string = 'HelloWorld'
        print("\nMy string is \t\t\t\t ->", my_string,"\nThe binary of that string is   \t\t->", StringToBinary(my_string))

        print('_'*60)
        print("DECODING")
        bin_data= '001001010100' # Random example
        str_data= BinaryToString(bin_data) 

        print("\nMy binary is \t\t\t\t ->", bin_data,"\nThe string of that binary is \t\t->", str_data)    

