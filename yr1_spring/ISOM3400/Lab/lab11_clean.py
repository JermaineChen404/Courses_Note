import streamlit as st

grading = {
    'Labs': 5,
    'Assignment 1': 15,
    'Assignment 2': 15,
    'Final Exam': 65
}

# TODO 1: Setup
# 1.1: Give the page a title (and optionally an icon) using set_page_config~
st.set_page_config("title")

# You can also change the title displayed on the app if you want!
st.title("ISOM3400 Grade Calculator")
st.write("Let's see if you will pass this course~")


# TODO 1.2: Create a form to group the input together.
#           You can choose to use the 'with' notation (given) or directly call methods on the form object.
with st.form("input form"):

    # TODO 2: Ask for user input by creating number inputs/sliders. (Please remove the None values!)
    # You may define max/min values to restrict the valid range.
    labs_attended = None
    asm1_score = None
    asm2_score = None
    final_score = None


    # Don't forget the submit button! You can also pass in text to display on the button.
    click_submit = st.form_submit_button() 


# TODO 3: Calculate scores
if click_submit: 
    # When the click_submit button returns True, all obtained values will be sent to the Streamlit server.
    # Process the obtained values and calculate the total (weighted) score!
    # (You can refer to the grading dictionary at the top for the weights.)






    # You should then display the calculated score on the web app. (e.g. with st.write()/st.markdown()...)

    # TODO 4: Display result
    # Once the total score has been calculated, let the user know if they are likely to pass the course or not.
    # Note that we stay in the indented block under if click_submit.
    # We do not want anything to be displayed if the user has not submitted yet.






    pass
