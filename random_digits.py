import streamlit as st
import random

def main():
    st.title("Press for a randomised list of last X digits in the user id")
    st.write("If there are any problems, you reach out to the analytics team and give them this URL which runs the code: https://github.com/eric-hb-carwow/crm_random_digits_regex")

    col1,col2,_ = st.columns([1,1,1])
    
    with col1:
        num_digits = st.number_input("Number of digits to randomise", min_value=1, max_value=4, step=1, value=2)
    with col2:
        num_groups = st.number_input("Number of groups", min_value=1, step=1, value=2)
    
    if st.button('Randomise!'):
        
        # Generate all possible combinations of the specified number of digits
        all_combinations = [str(i).zfill(num_digits) for i in range(10**num_digits)]
        
        # Randomize the list of combinations
        random.shuffle(all_combinations)
        
        # Divide the list into control and test groups
        start = 0
        mid_point = len(all_combinations) // num_groups
        for i in range(num_groups-1):
            group = all_combinations[start:mid_point]
            start += mid_point
            mid_point += mid_point
            
            if i == 0:
                st.write(f'Group 1, note the copy button on the right side!')
            else:
                st.write(f"Group %s" % (i+1))

        # Display the results
        st.code(f".*{'|.*'.join(group)}")
        

if __name__ == "__main__":
    main()
