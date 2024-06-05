# Feige-Fiat-Shamir (FFS) Authentication Protocol

This project implements the Feige-Fiat-Shamir (FFS) identification protocol in Python. The protocol is designed for secure user authentication, where a prover (Alice) convinces a verifier (Bob) of her identity without revealing her secret key. This implementation also includes a simulation of a hacker attempting to falsely authenticate.

## Project Structure

The project consists of the following files:

- `alice_and_hacker.py`: Contains classes for selecting user secrets and simulating a hacker.
- `round.py`: Manages the protocol messages and the steps involved in each round of the identification process.
- `trusted_center.py`: Contains the logic for generating system parameters, including prime numbers and security parameters.
- `main.py`: The main script that ties everything together, executing the authentication process and interacting with the user.

## Usage

### 1. Clone the repository

```bash
git clone <repository-url>
cd <repository-directory>
```

### 2. Run the Main Script

```bash
python main.py
```

### 3. Follow the Prompts

- The trusted center will generate the system parameters.
- Alice (or a hacker) will generate the public and private keys.
- The identification process will run for a specified number of rounds.

## Classes and Methods

### `trusted_center.py`

- **SelectingSystemParameters**
  - `__init__(self, p, q, k, t)`: Initializes the system parameters.
  - `is_prime(l)`: Checks if a number is prime.
  - `generate_prime()`: Generates a prime number.
  - `generate_n()`: Generates `n` as the product of two prime numbers.
  - `generate_security_params()`: Generates the security parameters `k` and `t`.

### `alice_and_hacker.py`

- **SelectingUserSecrets**
  - `__init__(self, n, k)`: Initializes the user secrets.
  - `select_user_secrets()`: Selects the user secrets `s` and `b`.
  - `extended_gcd(a, b)`: Computes the greatest common divisor using the extended Euclidean algorithm.
  - `mod_inverse(a, m)`: Finds the modular inverse.
  - `v_calculation()`: Calculates the public values `v`.
  - `keys()`: Forms the public and private keys.

- **Hacker**
  - `__init__(self, n, k, v)`: Initializes the hacker's parameters.
  - `hacker_generates_s()`: Generates the hacker's secret values.
  - `keys()`: Forms the public and private keys for the hacker.

### `round.py`

- **ProtocolMessages**
  - `x_calculation(n, b)`: Calculates the value `x` and a random value `r`.
  - `random_vector_generation(k)`: Generates a random vector `e`.
  - `y_calculation(r, e, s, n)`: Calculates the value `y`.
  - `z_calculation(y, v, e, n)`: Calculates the value `z`.
  - `identification(x, z, n)`: Performs the identification check.

### `main.py`

- `identify_user()`: Prompts the user to identify as Alice or a hacker.
- `perform_identification(n, k, t, s, b, v)`: Executes the identification process for `t` rounds.
- Main script flow:
  - Generates system parameters.
  - Alice or a hacker generates keys.
  - Sends the public key to the verifier.
  - Performs the identification process and prints the result.

## Feige-Fiat-Shamir (FFS) Protocol

The Feige-Fiat-Shamir identification protocol is a zero-knowledge proof system used for authentication. It allows one party (the prover) to prove to another party (the verifier) that they know a value, without conveying any information apart from the fact that they know the value.