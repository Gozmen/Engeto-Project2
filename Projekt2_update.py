"""
projekt_2.py: Bulls & Cows projekt do Engeto Online Python Akademie

author: Jakub Dostál
email: gozo.jakub@gmail.com
discord: gozo197, Gozo#2494
"""

import random
import time

def add_line():
    print("-" * 20)
    
def generate_unique_random():
    numbers = []
    first_digit = random.randint(1, 9)
    numbers.append(first_digit)
    while len(numbers) < 4:
        new_number = random.randint(0, 9)
        if new_number not in numbers:
            numbers.append(new_number)
    return ''.join(map(str, numbers))

def is_valid(guess):
    if len(guess) != 4:
        return "Cislo musi byt presne 4 cislice dlouhe."
    if not guess.isdigit():
        return "Cislo musi obsahovat pouze cislice."
    if guess[0] == '0':
        return "Cislo nesmi zacinat nulou."
    if len(set(guess)) != 4:
        return "Vsechny cislice musi byt unikatni."
    return "valid"

def evaluate_guess(secret, guess):
    bulls = 0
    cows = 0
    for i in range(4):
        if guess[i] == secret[i]:
            bulls += 1
    for i in range(4):
        if guess[i] in secret and guess[i] != secret[i]:
            cows += 1
    bull_text = f"{bulls} bull{'s' if bulls != 1 else ''}"
    cow_text = f"{cows} cow{'s' if cows != 1 else ''}"
    return f"{bull_text}, {cow_text}"

def results(attempts):
    #print(attempts)
    if attempts < 10:
        result = "vyborny"
    if attempts >= 10 and attempts <= 17:
        result = "prumerny"
    if attempts > 17:
        result = "nic moc"
    print(f"To je {result} vysledek.")         

secret_number = generate_unique_random()
print(secret_number)
#print(secret_number)
print("Vitej, zahrajeme si hru Cows & Bulls.")
print("Nyni vygeneruji nahodne 4 mistne cislo. Tvym ukolem je cislo postupne uhodnout.")
add_line()
print("Tajne cislo bylo vygenerovano. Zacnete hadat...")
attempts = 0
start_time = time.time()

add_line()

while True:
    guess = input("Zadejte svuj tip (4 unikatni cislice od 0 do 9): ")
    valid = is_valid(guess)
    if valid != "valid":
        print(valid)
        continue
    
    attempts += 1
    if guess == secret_number:
        end_time = time.time()
        total_time = round(end_time - start_time)
        print(f"Presne tak! Uhodli jste cislo. Hledane cislo bylo: {secret_number}")
        print(f"K uhodnuti jsi potreboval {attempts} pokusu a trvalo to {total_time} sekund")
        results(attempts)
        break
    
    print(evaluate_guess(secret_number, guess))
