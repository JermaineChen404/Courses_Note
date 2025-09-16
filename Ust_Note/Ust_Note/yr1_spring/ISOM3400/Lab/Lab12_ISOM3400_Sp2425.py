from bs4 import BeautifulSoup
import requests 
import streamlit as st
import pandas as pd

st.set_page_config('Taiko No Tatsujin Data', '🥁', layout='wide')
st.title('Taiko No Tatsujin!')

# Caching: prevents Streamlit from re-executing the function and return the cached value instead.
# Recall that Streamlit re-runs the script from top to bottom after user interaction.
# It takes some time for the web scraping code to load - thus cache to prevent reruns every time we choose a different option.
@st.cache_data
def scrape_website():

    base_url='https://taiko.namco-ch.net/taiko/en/songlist/'
    res = requests.get(base_url)
    soup = BeautifulSoup(res.content, 'html.parser')
    
    # Data for different categories are stored in different pages - get the links so we can scrape from all of them.
    music_categories = [category_anchor.get('href') for category_anchor in soup.select_one('nav#sgnavi').select('a')]
    # First, select the nav element where the links are stored (id: 'sgnavi')
    # Then select all anchor elements (<a>). (-> obtain list of anchor elements)
    # Finally, for each anchor in the list of obtained anchors: get the href attribute (links).
    
    # music_categories[0] looks like this: 'pops.php#sgnavi'
    
    song_titles = []
    categories = []
    artists = []
    easy_lv = []
    normal_lv = []
    hard_lv = []
    extreme_lv = []
    inner_extreme_lv = []

    # For each category in the list of music categories (8 in total), we access the relevant page and scrape data from it.
    for category in music_categories:
        
        # Access the category's page (requests.get) and create a BeautifulSoup object from its content
        category_soup = BeautifulSoup(requests.get(base_url + category).content, 'html.parser')
        category_name = category.split('.')[0].title()
        
        # Select the table on the page.
        # The first two rows are table headers, not the data we want, so we skip them by slicing. (Similar to prev. scraping lab)
        song_rows = category_soup.select_one('table').select('tr')[2:]
        
        # For each subsequent row:
        for row in song_rows:
            
            # The song title and artist name (if it exists) are stored in a header cell. Process to obtain title and artist.
            song_info = row.select_one('th').get_text(strip=True, separator='|').split('|')
            
            if len(song_info) > 1:
                title, *others, artist = song_info
            else:
                title = song_info[0]
                artist = '-'
                
            
            # difficulty ratings are stored in td cells.
            # Note that there is a "papa mama support" option for certain songs (one column).
            # Under Namco Original, there is also a column for YouTube videos. we can use packing to handle it.
            #   If we do not use the asterisk, then it must take in one value (which may not exist in other pages).
            #   By using the asterisk (packing), we can take in 0 values as well (if that column does not exist)
            papamama, easy, normal, hard, extreme, inner_extreme, *vid = row.select('td')
            
            # Append data to relevant lists. For difficulty ratings, we can convert them back into ints.
            song_titles.append(title)
            categories.append(category_name)
            artists.append(artist)
            easy_lv.append(int(easy.text))
            normal_lv.append(int(normal.text))
            hard_lv.append(int(hard.text))
            extreme_lv.append(int(extreme.text))
            
            # Not all songs have an Extreme (Inner) level. Since int() cannot be called on a string, we need to handle it.
            inner_extreme_lv.append(None if inner_extreme.text == '-' else int(inner_extreme.text))
    
    # Outside the for-loop (After going through all rows in all categories):
    #   Create a dataframe with the lists we have appended to        
    df = pd.DataFrame({
        'Song Title': song_titles,
        'Category': categories,
        'Artist': artists,
        'Easy': easy_lv,
        'Normal': normal_lv,
        'Hard': hard_lv,
        'Extreme': extreme_lv,
        'Extreme (Inner)': inner_extreme_lv
        
    })
    
    # Since this is a function, we need to return the dataframe to pass it to variables outside of the function.
    return df

###########################
# Outside of the function:
# We get the dataframe by calling the scrape_website() function we have just defined.
df = scrape_website()

diff_colors = ['#FF2703', '#8CB852', '#435935', '#DB1885', '#7135DB']
cat_list = df.groupby('Category').groups.keys()
diff_list = ['Easy', 'Normal', 'Hard', 'Extreme', 'Extreme (Inner)']


# Create two columns to show the charts and pills selection widgets side by side
col1, col2= st.columns(2)

# One method to write into columns: using dot notation

# Display dataframe
col1.dataframe(df, height=400)

# Display bar chart: No. of songs per category
col2.write("Number of songs per category")
col2.bar_chart(df['Category'].value_counts(), horizontal=True, height=356)

# Display input widgets for user to modify data displayed
chosen_diff = col1.pills('View difficulty distribution for levels:', diff_list, default='Easy')
chosen_category = col2.pills('View difficulty distribution for categories:', cat_list, selection_mode = 'multi', default=cat_list)
stacked = col2.checkbox('Stack bars?', value=True)

# pills will return the chosen option (by default) / a list of chosen options (if selection_mode is 'multi').
# checkbox will return either True (if checked) or False (if unchecked).

# Generated charts depend below on the difficulty chosen above (chosen_diff).
# If no difficulty is chosen (chosen_diff is None), an error will occur.
# We can display an error message to remind the user to choose a difficulty.

if not chosen_diff: # Equivalent to if chosen_diff == None
    st.error('Please choose a difficulty to view charts.')
    
else: # If a difficulty is chosen, we will be able to display the charts.

    # Another method to write into columns: using with notation.
    with col1:
        st.subheader("Rating distribution of all songs")
        
        # Display the rating distribution of the chosen difficulty in the form of a bar chart.
        st.bar_chart(df[chosen_diff].value_counts(),\
                    x_label=chosen_diff + ' rating', y_label='No. of Songs',\
                    color=diff_colors[diff_list.index(chosen_diff)])
                    # You can modify the labels on the chart!
                    # The color is dependent on the difficulty chosen. They are defined in diff_colors.

    with col2:
        st.subheader("Rating distribution according to categories")
        
        # If no category is chosen, no data will be shown.
        # We can display a warning message to ask the user to choose at least one category.
        if not chosen_category:
            st.warning("Please choose at least one category.")
        else:
            # Grouping by Category, then counting according to difficulty rating.
            difficulty_df = pd.DataFrame(df.groupby(['Category', chosen_diff]).count().reset_index())
    
            # Further filtering: only include selected categories from the chosen_category pills widget
            difficulty_df = difficulty_df[difficulty_df['Category'].isin(chosen_category)]
            
            # Display the bar chart:
            st.bar_chart(difficulty_df,\
                        x=chosen_diff, y='Song Title',\
                        x_label = chosen_diff + ' rating', y_label='No. of Songs',\
                        color='Category', stack=stacked)
                        # Color is dependent on the Category value.
                        # You can choose to display the different categories stacked or separated.
                        #   This is controlled by the stacked checkbox above.



