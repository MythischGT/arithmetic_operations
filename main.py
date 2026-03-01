import argparse

# This script provides two main functionalities: calculating (base^exponent) mod modulus using the square-and-multiply algorithm, and finding the modular inverse of a number 'a' modulo 'm' using the Extended Euclidean Algorithm.
# The user can specify which operation to perform by providing the appropriate command-line arguments. The script is designed to be flexible and can handle both operations based on the user's input.
# Usage:
# To calculate (base^exponent) mod modulus:
# python main.py --operation square_and_multiply --base <base> --exponent <exponent> --modulus <modulus>
# Example:
# python main.py --operation square_and_multiply --base 5 --exponent 3
# To find the modular inverse of 'a' modulo 'm':
# python main.py --operation find_modular_inverse --a <a> --m <m
class ArithmeticOperations:
    def __init__(self,**kwargs):
        self.kwargs = kwargs

        # Determine which operation to perform based on the provided arguments
        # The user can specify the operation using the 'operation' argument, which can be either 'square_and_multiply' or 'find_modular_inverse'.
        # Depending on the operation, the appropriate parameters will be extracted from the arguments and the corresponding function will be called.
        # For 'square_and_multiply', the parameters are 'base', 'exponent', and 'modulus'.
        # For 'find_modular_inverse', the parameters are 'a' and 'm'.
        if self.kwargs.get('operation') == 'square_and_multiply':
            self.base = int(self.kwargs.get('base', 0))
            self.exponent = int(self.kwargs.get('exponent', 0))
            self.modulus = int(self.kwargs.get('modulus', 0))
            self.result = self.square_and_multiply(self.base, self.exponent, self.modulus)
        elif self.kwargs.get('operation') == 'find_modular_inverse':
            self.a = int(self.kwargs.get('a', 0))
            self.m = int(self.kwargs.get('m', 0))
            self.result = self.find_modular_inverse(self.a, self.m)

    # This script calculates (base^exponent) mod modulus using the square-and-multiply algorithm.
    # The algorithm is efficient for large exponents and is commonly used in cryptographic applications.
    # Usage:
    # python main.py <base> <exponent> <modulus>
    # Example:
    # python main.py 5 3 13
    # This will calculate (5^3) mod 13, which equals 8.
    def square_and_multiply(self, base, exponent, modulus):
        result = 1
        base = base % modulus
        
        while exponent > 0:
            if (exponent % 2) == 1:  # If exponent is odd
                result = (result * base) % modulus
            exponent = exponent >> 1  # Divide exponent by 2
            base = (base * base) % modulus
        
        return result

    # This function calculates the modular inverse of a number 'a' modulo 'm' using the Extended Euclidean Algorithm.
    # The modular inverse is the number 'x' such that (a * x) % m = 1.
    # Usage:
    # find_modular_inverse(a, m)
    # Example:
    # find_modular_inverse(3, 11)  # Returns 4, since (3 * 4) % 11 = 1
    def find_modular_inverse(self, a, m):
        m0, x0, x1 = m, 0, 1
        if m == 1:
            return 0
        while a > 1:
            # q is quotient
            q = a // m
            m, a = a % m, m
            x0, x1 = x1 - q * x0, x0
        if x1 < 0:
            x1 += m0
        return x1

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Perform arithmetic operations: square-and-multiply or find modular inverse.')
    parser.add_argument('--operation', type=str, required=True, help='The operation to perform: "square_and_multiply" or "find_modular_inverse".')
    parser.add_argument('--base', type=int, help='The base for the square-and-multiply operation.')
    parser.add_argument('--exponent', type=int, help='The exponent for the square-and-multiply operation.')
    parser.add_argument('--modulus', type=int, help='The modulus for the square-and-multiply operation.')
    parser.add_argument('--a', type=int, help='The number for which to find the modular inverse.')
    parser.add_argument('--m', type=int, help='The modulus for finding the modular inverse.')

    args = parser.parse_args()
    result = ArithmeticOperations(**vars(args)).result
    print("Result: ", result)