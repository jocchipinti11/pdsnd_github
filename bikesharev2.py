import time
import pandas as pd
import numpy as np
import sys
<<<<<<< HEAD:occhipinti_bikeshare.py

# Please refer to README.md for more information
# about the sources I referenced for this project.
||||||| 74ad2ac:occhipinti_bikeshare.py

# I have included a readme.txt file with the sources I referenced for this project.

=======
"""
I have included a readme.txt file with the sources I referenced for this project.
"""
>>>>>>> refactoring:bikesharev2.py

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
              'washington': 'washington.csv' }

mo_names = ['january', 'february', 'march', 'april', 'may', 'june']

day_names = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday' ]

def get_city():
<<<<<<< HEAD:occhipinti_bikeshare.py
    print('\n\nHello Welcome to Joe Occhipinti\'s Bikeshare Project. Let\'s explore some US bikeshare data!')
||||||| 74ad2ac:occhipinti_bikeshare.py
    print('\n\nHello Welcome to Joe Occhipinti\'s Bikeshare Project. Let\'s explore some US bikeshare data!')    
=======
    """
    Asks user to specify a city to analyze.
    Returns:
        (str) city - name of the city to analyze
    """
    print('\n\nHello Welcome to Joe Occhipinti\'s Bikeshare Project. Let\'s explore some US bikeshare data!')
>>>>>>> refactoring:bikesharev2.py
    print('\nChicago')
    print('New York')
    print('Washington')
    print('\nPlease choose one of the above cities to analyze by typing the city\'s first letter.')
<<<<<<< HEAD:occhipinti_bikeshare.py

    print('_'*10)

||||||| 74ad2ac:occhipinti_bikeshare.py
    
    print('_'*10)
    
=======
>>>>>>> refactoring:bikesharev2.py
    c = input('>>>').lower().strip()
    print('_'*10)

    while c not in ['c', 'n', 'w']: c = input('try again, enter the first letter of a city on the list >>> ').lower().strip()
    if c == 'c':
        city = 'Chicago'
        print('\nYou chose {}\n'.format(city))
        return city.lower()
    if c == 'n':
        city = 'New York'
        print('\nYou chose {}\n'.format(city))
        return city.lower()
    if c == 'w':
        city = 'Washington'
        print('\nYou chose {}\n'.format(city))
        print('_'*10, '\n')
        return city.lower()

<<<<<<< HEAD:occhipinti_bikeshare.py
# Asks user to specify the time frame, the month, and day to analyze.
# Returns: (str) month - name of the month to filter by, or "all" to apply no month filter
#          (str) day - name of the day of week to filter by, or "all" to apply no day filter
||||||| 74ad2ac:occhipinti_bikeshare.py
# Asks user to specify the time frame, the month, and day to analyze.
# Returns: (str) month - name of the month to filter by, or "all" to apply no month filter
#          (str) day - name of the day of week to filter by, or "all" to apply no day filter         
=======


>>>>>>> refactoring:bikesharev2.py
def get_time():
    """
    Asks user to specify the time frame, the month, and day to analyze.
    Returns:
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    # get user input for month (all, january, february, ... , june)
<<<<<<< HEAD:occhipinti_bikeshare.py

||||||| 74ad2ac:occhipinti_bikeshare.py
    
=======
>>>>>>> refactoring:bikesharev2.py
    for mo in mo_names:
        print('{} for {}'.format(mo_names.index(mo), mo))
    print('Enter \'all\' to analyze all the months together.\n')
    print('\nPlease type \'all\' or type the number for the month you are interested in analyzing.')
    month = input('>>>')

    while month not in ['0','1','2','3','4','5','all']: month = input('Try again >>> ').lower().strip()
    if month == 'all':
        print('\nYou chose no month filter')
        print('_'*10, '\n')
        month = -1
    else:
        month =int(month)
        print('\nYou chose {}'.format(mo_names[month]).title())
        print('_'*10, '\n')
<<<<<<< HEAD:occhipinti_bikeshare.py

    # get user input for day of week (all, monday, tuesday, ... sunday)


||||||| 74ad2ac:occhipinti_bikeshare.py
        
    # get user input for day of week (all, monday, tuesday, ... sunday)         
    
    
=======

    # get user input for day of week (all, monday, tuesday, ... sunday)
>>>>>>> refactoring:bikesharev2.py
    for day in day_names:
        print('{} for {}'.format(day_names.index(day), day))
    print('enter \'all\' to analyze all days of the week together.')
    print('\nPlease type \'all\' or type a number for the day of the week you are interested in analyzing.\n')
    day = input('>>>')

    while day not in ['0','1','2','3','4','5','6','all']: month = input('Try again >>> ').lower().strip()
    if day == 'all':
        print('\nYou chose no day filter')
        print('_'*10, '\n')
        day = -1
    else:
        day =int(day)
        print('\nYou chose {}'.format(day_names[day]).title())

    return month, day

#modifies the data to make it usable for analysis
#returns a modified dataframe, with added columns
def load_data(city, month, day):
    """
    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        rider_data - Pandas DataFrame containing city data filtered by month and day
    """

    #Loads data for the specified city
    rider_data = pd.read_csv(CITY_DATA[city])
<<<<<<< HEAD:occhipinti_bikeshare.py

    #rename columns
    rider_data.rename(columns = {'Start Time':'start_time',
                         'End Time':'end_time',
                         'Trip Duration':'trip_duration',
                         'Start Station':'start_station',
                         'End Station':'end_station',
                         'User Type':'user_type'}, inplace = True)

||||||| 74ad2ac:occhipinti_bikeshare.py
        
    #rename columns
    rider_data.rename(columns = {'Start Time':'start_time', 
                         'End Time':'end_time', 
                         'Trip Duration':'trip_duration',
                         'Start Station':'start_station',
                         'End Station':'end_station',
                         'User Type':'user_type'}, inplace = True)
    
=======

>>>>>>> refactoring:bikesharev2.py
    #convert date to match filter querie
<<<<<<< HEAD:occhipinti_bikeshare.py
    rider_data['start_time'] = pd.to_datetime(rider_data['start_time'])

    #get the filter data
||||||| 74ad2ac:occhipinti_bikeshare.py
    rider_data['start_time'] = pd.to_datetime(rider_data['start_time'])
    
    #get the filter data 
=======
    rider_data['Start Time'] = pd.to_datetime(rider_data['Start Time'])

    #get the filter data
>>>>>>> refactoring:bikesharev2.py
        #create new columns
<<<<<<< HEAD:occhipinti_bikeshare.py
    rider_data['month'] = rider_data['start_time'].dt.month
    rider_data['day'] = rider_data['start_time'].dt.dayofweek
    rider_data['hour'] = rider_data['start_time'].dt.hour

         #apply filters
    if month != -1:
||||||| 74ad2ac:occhipinti_bikeshare.py
    rider_data['month'] = rider_data['start_time'].dt.month 
    rider_data['day'] = rider_data['start_time'].dt.dayofweek
    rider_data['hour'] = rider_data['start_time'].dt.hour
  
         #apply filters         
    if month != -1:        
=======
    rider_data['month'] = rider_data['Start Time'].dt.month
    rider_data['day'] = rider_data['Start Time'].dt.dayofweek
    rider_data['hour'] = rider_data['Start Time'].dt.hour

         #apply filters
    if month != -1:
>>>>>>> refactoring:bikesharev2.py
        rider_data = rider_data[rider_data['month'] == month]
    if day != -1:
        rider_data = rider_data[rider_data['day'] == day]

    # show raw data if user wants to see it
    start_row, end_row = 0, 5
    while True:
        view_raw = input('To see 5 rows of raw data click enter or type \'any key\' to skip to the analysis. \n>>> ').lower().strip()
        if view_raw != '': break
        print(rider_data.iloc[start_row:end_row])
        start_row += 5
        end_row += 5
    return rider_data

def time_stats(rider_data):
    """
    #displays time statistics on the most frequent times of travel.
    Args:
        dataframe - contains city filtered data
    #nothing to return
    """
    print('='*60)
    print('\nCalculating The Most Frequent Times of Travel...\n')
<<<<<<< HEAD:occhipinti_bikeshare.py

    start_time = time.time()

||||||| 74ad2ac:occhipinti_bikeshare.py
    
    start_time = time.time()
 
=======

>>>>>>> refactoring:bikesharev2.py
    # display the most common month
    m = rider_data['month'].value_counts().idxmax()
    print('  ', mo_names[m-1].title(), 'was the month most traveled.')

    # display the most common day of week
    d = rider_data['day'].value_counts().idxmax()
    print('\n  ', day_names[d-1].title(), 'was the day most traveled.')

    # display the most common start hour
    h = rider_data['hour'].value_counts().idxmax()
    print('\n   {}:00 MT, was the hour of the day was the most traveled.'.format(h))
    print('='*60)

<<<<<<< HEAD:occhipinti_bikeshare.py
#displays stations statistics
#nothing to return
||||||| 74ad2ac:occhipinti_bikeshare.py
#displays stations statistics
#nothing to return       
=======
>>>>>>> refactoring:bikesharev2.py
def station_stats(rider_data):
<<<<<<< HEAD:occhipinti_bikeshare.py
    """Displays statistics on the most popular stations and trip."""

||||||| 74ad2ac:occhipinti_bikeshare.py
    """Displays statistics on the most popular stations and trip."""
    
=======
    """
    #displays stations statistics on the most popular stations and trip.
    Args:
        dataframe - contains city filtered data
    #nothing to return
    """
>>>>>>> refactoring:bikesharev2.py
    print('\nCalculating the Most Popular Stations and most popular combination of stations or trips...\n')
<<<<<<< HEAD:occhipinti_bikeshare.py
    start_time = time.time()

||||||| 74ad2ac:occhipinti_bikeshare.py
    start_time = time.time()    
    
=======

>>>>>>> refactoring:bikesharev2.py
   # create a trip column
    rider_data['trip'] = rider_data['Start Station'] + ' -- ' + rider_data['End Station']

    # display most commonly used start station, end station and combination
<<<<<<< HEAD:occhipinti_bikeshare.py
    top_start_station = rider_data['start_station'].value_counts().idxmax()
    top_end_station = rider_data['end_station'].value_counts().idxmax()
    top_start_end_combo = rider_data['trip'].value_counts().idxmax()

||||||| 74ad2ac:occhipinti_bikeshare.py
    top_start_station = rider_data['start_station'].value_counts().idxmax()
    top_end_station = rider_data['end_station'].value_counts().idxmax()
    top_start_end_combo = rider_data['trip'].value_counts().idxmax()
    
=======
    Top_Start_Station = rider_data['Start Station'].value_counts().idxmax()
    Top_End_Station = rider_data['End Station'].value_counts().idxmax()
    Top_Start_end_Combo = rider_data['trip'].value_counts().idxmax()

>>>>>>> refactoring:bikesharev2.py
    # display results
    print('   The most common start station is: {}'.format(Top_Start_Station))
    print('   The most common end station is: {}'.format(Top_End_Station))
    print('   The most common combination or trip are: {}'.format(Top_Start_end_Combo))
    print('='*60)

<<<<<<< HEAD:occhipinti_bikeshare.py
#displays trip statistics
#nothing to return
||||||| 74ad2ac:occhipinti_bikeshare.py
#displays trip statistics
#nothing to return    
=======
>>>>>>> refactoring:bikesharev2.py
def trip_duration_stats(rider_data):
<<<<<<< HEAD:occhipinti_bikeshare.py
    """Displays statistics on the total and average trip duration."""

||||||| 74ad2ac:occhipinti_bikeshare.py
    """Displays statistics on the total and average trip duration."""
    
=======
    """
    Displays statistics on the total and average trip duration.
    Args:
        dataframe - contains city filtered data
    nothing to return
    """

>>>>>>> refactoring:bikesharev2.py
    print('\nCalculating Trip Duration...\n')
<<<<<<< HEAD:occhipinti_bikeshare.py
    start_time = time.time()

||||||| 74ad2ac:occhipinti_bikeshare.py
    start_time = time.time()
    
=======

>>>>>>> refactoring:bikesharev2.py
    #calculte the total, mean and max travel times
<<<<<<< HEAD:occhipinti_bikeshare.py
    tot_travel = rider_data['trip_duration'].sum()
    ave_travel = rider_data['trip_duration'].mean()

||||||| 74ad2ac:occhipinti_bikeshare.py
    tot_travel = rider_data['trip_duration'].sum()
    ave_travel = rider_data['trip_duration'].mean()
       
=======
    tot_travel = rider_data['Trip Duration'].sum()
    ave_travel = rider_data['Trip Duration'].mean()

>>>>>>> refactoring:bikesharev2.py
    #display the total, mean and max travel times
    print('The total travel time is: {}'.format(tot_travel))
    print('The average travel time is: {}'.format(ave_travel))
<<<<<<< HEAD:occhipinti_bikeshare.py

    print("\nThis took %s seconds." % (time.time() - start_time))
||||||| 74ad2ac:occhipinti_bikeshare.py
    
    print("\nThis took %s seconds." % (time.time() - start_time))
=======
>>>>>>> refactoring:bikesharev2.py
    print('='*60)

<<<<<<< HEAD:occhipinti_bikeshare.py
#displays user statistics
#nothing to return
||||||| 74ad2ac:occhipinti_bikeshare.py
#displays user statistics
#nothing to return    
=======
>>>>>>> refactoring:bikesharev2.py
def user_stats(metro_area, rider_data):
<<<<<<< HEAD:occhipinti_bikeshare.py
    """Displays statistics on bikeshare users."""

||||||| 74ad2ac:occhipinti_bikeshare.py
    """Displays statistics on bikeshare users."""
    
=======
    """
    Displays statistics on bikeshare users.
    Args:
        dataframe - contains city filtered data
    nothing to return
    """
>>>>>>> refactoring:bikesharev2.py
    print('\nCalculating User Stats...\n')

    # Calculate and display counts of user types and gender
    user_type_counts = rider_data['User Type'].value_counts()
    for i, types in enumerate(user_type_counts):
        print('There are {} {}s'.format(types, user_type_counts.index[i]))
    print()
    if metro_area != 'washington':
        gender_counts = rider_data['Gender'].value_counts()
        for i, sex in enumerate(gender_counts):
            print('There are {} {}s'.format(sex, gender_counts.index[i]))
    print('='*60)

def main():
<<<<<<< HEAD:occhipinti_bikeshare.py

||||||| 74ad2ac:occhipinti_bikeshare.py
    
=======
    """Main"""
>>>>>>> refactoring:bikesharev2.py
    while True:
        city = get_city()
        month, day = get_time()
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(city, df)

        restart = input('\nType <enter> to end the analysis. To continue type \'c\' and enter.\n')
        if restart.lower() != 'c':
            break
if __name__ == "__main__":
	main()
