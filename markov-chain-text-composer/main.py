import random
import re

def preprocess_text(text):
    text = re.sub(r'[^\w\s]', '', text.lower()) 
    words = text.split() 
    return words

def build_markov_chain(words):
    markov_chain = {}

    for i in range(len(words) - 1):
        current_word = words[i]
        next_word = words[i + 1]

        if current_word in markov_chain:
            markov_chain[current_word].append(next_word)
        else:
            markov_chain[current_word] = [next_word]

    return markov_chain

def generate_text(markov_chain, length=100):
    current_word = random.choice(list(markov_chain.keys()))
    generated_text = current_word

    for _ in range(length - 1):
        if current_word in markov_chain:
            next_word = random.choice(markov_chain[current_word])
            generated_text += " " + next_word
            current_word = next_word
        else:
            break

    return generated_text

input_text = "The sun sets behind the mountains, casting a warm glow over the peaceful meadow."
words = preprocess_text(input_text)
markov_chain = build_markov_chain(words)
generated_text = generate_text(markov_chain, length=20)
print(generated_text)
