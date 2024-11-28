import random
import string


# Algorithm 1: Basic Random Selection
def basic_random(length, char_pool):
    return ''.join(random.choices(char_pool, k=length))


# Algorithm 2: Markov Chain
def markov_chain(length, start_char='a'):
    char_pool = string.ascii_letters + string.digits + string.punctuation
    password = [start_char]
    for _ in range(length - 1):
        next_char = random.choice(char_pool)
        password.append(next_char)
    return ''.join(password)


# Algorithm 3: XOR-Based Password
def xor_based(length, base='password'):
    char_pool = string.ascii_letters + string.digits + string.punctuation
    password = ''
    for char in base[:length]:
        password += chr(ord(char) ^ random.randint(1, 255))
    return password[:length]


# Algorithm 4: Pattern-Based Password
def pattern_based(pattern):
    char_types = {
        'L': string.ascii_letters,   # Letters
        'N': string.digits,          # Numbers
        'S': string.punctuation      # Symbols
    }
    password = ''
    for p in pattern:
        if p in char_types:
            password += random.choice(char_types[p])
        else:
            password += p  # Add literal characters if not in the pattern keys
    return password


# Main function to generate passwords
def main():
    print("Password Generator with 4 Algorithms")
    print("1. Basic Random Selection")
    print("2. Markov Chain")
    print("3. XOR-Based Password")
    print("4. Pattern-Based Password")
    
    try:
        choice = int(input("Choose an algorithm (1-4): "))
        length = int(input("Enter desired password length: "))
        
        if choice == 1:
            char_pool = string.ascii_letters + string.digits + string.punctuation
            print("Generated Password:", basic_random(length, char_pool))
        
        elif choice == 2:
            start_char = input("Enter the starting character (default: 'a'): ") or 'a'
            print("Generated Password:", markov_chain(length, start_char))
        
        elif choice == 3:
            base = input("Enter a base string for XOR (default: 'password'): ") or 'password'
            print("Generated Password:", xor_based(length, base))
        
        elif choice == 4:
            pattern = input("Enter the pattern (e.g., LLNNSS): ")
            print("Generated Password:", pattern_based(pattern))
        
        else:
            print("Invalid choice! Please select a number between 1 and 4.")
    
    except ValueError:
        print("Invalid input! Please enter numbers where required.")
    except Exception as e:
        print(f"An error occurred: {e}")


# Run the program
if __name__ == "__main__":
    main()
