import streamlit as st
import random

def main():
    st.title("Press for a randomised list of last X digits in the user id")
    st.write("If there are any problems, you reach out to the analytics team and give them this URL which runs the code: https://github.com/eric-hb-carwow/crm_random_digits_regex")

    col1,_ = st.columns([1,2])
    
    with col1:
        num_digits = st.number_input("Number of digits to randomise", min_value=1, max_value=4, step=1, value=2)
    
    if st.button('Randomise!'):
        
        # Generate all possible combinations of the specified number of digits
        all_combinations = [str(i).zfill(num_digits) for i in range(10**num_digits)]
        
        # Randomize the list of combinations
        random.shuffle(all_combinations)
        
        # Divide the list into control and test groups
        mid_point = len(all_combinations) // 2
        control_group = all_combinations[:mid_point]
        test_group = all_combinations[mid_point:]
        
        # Display the results
        st.write('Group 1, note the copy button on the right side!')
        st.code(f".*{'|.*'.join(control_group)}")
        st.write('Group 2')
        st.code(f".*{'|.*'.join(test_group)}")

if __name__ == "__main__":
    main()
