# Arithmetic Operations

A Python utility providing efficient implementations of modular arithmetic operations commonly used in cryptography and number theory.

## Features

- **Square-and-Multiply Algorithm**: Efficiently computes (base^exponent) mod modulus using the binary exponentiation method
- **Modular Inverse**: Finds the modular inverse of a number using the Extended Euclidean Algorithm

## Requirements

- Python 3.6+

## Installation

Clone or download this repository:

\`\`\`bash
git clone <repository-url>
cd arithmetic_operations
\`\`\`

## Usage

### Square-and-Multiply Operation

Calculates (base^exponent) mod modulus efficiently.

\`\`\`bash
python main.py --operation square_and_multiply --base <base> --exponent <exponent> --modulus <modulus>
\`\`\`

**Example:**
\`\`\`bash
python main.py --operation square_and_multiply --base 5 --exponent 3 --modulus 13
# Output: Result: 8
\`\`\`

### Find Modular Inverse

Finds x such that (a * x) mod m = 1 using the Extended Euclidean Algorithm.

\`\`\`bash
python main.py --operation find_modular_inverse --a <a> --m <m>
\`\`\`

**Example:**
\`\`\`bash
python main.py --operation find_modular_inverse --a 3 --m 11
# Output: Result: 4 (since (3 * 4) % 11 = 1)
\`\`\`

## Command-line Arguments

| Argument | Description |
|----------|-------------|
| \`--operation\` | **Required**. The operation to perform: \`square_and_multiply\` or \`find_modular_inverse\` |
| \`--base\` | The base for square-and-multiply operation |
| \`--exponent\` | The exponent for square-and-multiply operation |
| \`--modulus\` | The modulus for square-and-multiply operation |
| \`--a\` | The number for which to find the modular inverse |
| \`--m\` | The modulus for finding the modular inverse |

## License

See LICENSE for details.