# Password Generator 🔐

This project is a Python-based **Password Generator** that uses **four different algorithms** to create secure and customizable passwords. It's designed to help users generate strong passwords tailored to their needs, ensuring both security and flexibility.

---
## Table of Contents 📖
- [Features ✨](#features✨)
- [Getting Started 🚀](#getting-started🚀)
- [Usage 🛠️](#usage-🛠️)
- [Algorithms Explained 🧠](#algorithms-explained🧠)
- [Example Interaction 🖥️](#example-interaction🖥️)
- [License 📝](#license📝)


## Features ✨

- **Four Algorithms**:
  1. **Basic Random Selection**: Randomly selects characters from a specified pool.
  2. **Markov Chain**: Generates passwords using character transition logic.
  3. **XOR-Based Password**: Uses XOR operation with a base string for randomness.
  4. **Pattern-Based Password**: Creates passwords following a user-defined pattern.

- Customizable password length.
- User-friendly CLI interface.
- Supports letters, digits, symbols, or user-defined patterns.

---

## Getting Started 🚀

### Prerequisites
- **Python 3.x** installed on your system.
- A code editor like **VS Code** (optional).

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/threathawk05/password-generator.git
   cd password-generator
   ```

2. Open the project in your code editor or terminal.

## Usage 🛠️
1. Run Script
    ```bash
     python password_generator.py
   ```

2. Follow the prompts:

- Choose the algorithm.
- Enter the password length and other details (e.g., base string or pattern).
- Get your generated password!

## Algorithms Explained 🧠

### 1. Basic Random Selection
  Randomly generates a password by selecting characters from:

- Uppercase letters
- Lowercase letters
- Digits
- Symbols

Example: A8@lR2q!

## 2. Markov Chain
Uses a starting character and generates a password based on a random sequence of transitions.

Example: aPwL12!e

## 3. XOR-Based Password
Generates a password using the XOR operation between a base string and random integers for added randomness.

Example: 7z@f&Ui9

## 4. Pattern-Based Password
Follows a user-defined pattern to generate passwords.

- L: Letters
- N: Numbers
- S: Symbols
  
Example: Pattern LLNNSS → Password: Ab12@#

### Example Interaction 🖥️
<img width="559" alt="image" src="https://github.com/user-attachments/assets/56c42a67-a93f-437b-96b0-b82ad477fc45">

### 📝 License
This project is open source and available under the MIT License.

[MIT](https://choosealicense.com/licenses/mit/)



