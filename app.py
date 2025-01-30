import streamlit as st
from main_code import calculate_square

def main():
    # Title
    st.title("Square Calculator")

    # Input
    number = st.number_input("Enter a number:", value=0, step=1)

    # Calculate and display the square
    if st.button("Calculate"):
        square = calculate_square(number)
        st.write(f"The square of {number} is: {square}")

if __name__ == "__main__":
    main()