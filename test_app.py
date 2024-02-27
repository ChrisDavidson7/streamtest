import streamlit as st

def square_number(number):
    return number ** 2

def main():
    st.title("Square Number App")
    
    # User input
    number = st.number_input("Enter a number:")
    
    # Process user input
    if st.button("Square"):
        squared = square_number(number)
        st.write(f"The square of {number} is {squared}")

if __name__ == "__main__":
    main()
