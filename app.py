import streamlit as st
import random

# List of quotes
quotes = [
    "The only way to do great work is to love what you do. - Steve Jobs",
    "Success is not final, failure is not fatal: It is the courage to continue that counts. - Winston Churchill",
    "Life is what happens when you're busy making other plans. - John Lennon",
    "In the end, it's not the years in your life that count. It's the life in your years. - Abraham Lincoln"
]

def main():
    
    random_quote = random.choice(quotes)
    st.write(random_quote)

if __name__ == "__main__":
    main()
