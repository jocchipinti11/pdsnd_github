import time
import pandas as pd
import numpy as np
import sys

# Please refer to README.md for more information
# about the sources I referenced for this project.

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
              'washington': 'washington.csv' }

mo_names = ['january', 'february', 'march', 'april', 'may', 'june']

day_names = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday' ]

# Asks user to specify a city to analyze.
# Returns: (str) city - name of the city to analyze
def get_city():
    print('\n\nHello Welcome to Joe Occhipinti\'s Bikeshare Project. Let\'s explore some US bikeshare data!')
    print('\nChicago')
    print('New York')
    print('Washington')
    print('\nPlease choose one of the above cities to analyze by typing the city\'s first letter.')

    print('_'*10)

    c = input('>>>').lower().strip()
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

# Asks user to specify the time frame, the month, and day to analyze.
# Returns: (str) month - name of the month to filter by, or "all" to apply no month filter
#          (str) day - name of the day of week to filter by, or "all" to apply no day filter
def get_time():
    # get user input for month (all, january, february, ... , june)

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

    # get user input for day of week (all, monday, tuesday, ... sunday)


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

    #rename columns
    rider_data.rename(columns = {'Start Time':'start_time',
                         'End Time':'end_time',
                         'Trip Duration':'trip_duration',
                         'Start Station':'start_station',
                         'End Station':'end_station',
                         'User Type':'user_type'}, inplace = True)

    #convert date to match filter querie
    rider_data['start_time'] = pd.to_datetime(rider_data['start_time'])

    #get the filter data
        #create new columns
    rider_data['month'] = rider_data['start_time'].dt.month
    rider_data['day'] = rider_data['start_time'].dt.dayofweek
    rider_data['hour'] = rider_data['start_time'].dt.hour

         #apply filters
    if month != -1:
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


#displays time statistics
#nothing to return
def time_stats(rider_data):
    """Displays statistics on the most frequent times of travel."""
    print('='*60)
    print('\nCalculating The Most Frequent Times of Travel...\n')

    start_time = time.time()

    # display the most common month
    m = rider_data['month'].value_counts().idxmax()
    print('  ', mo_names[m-1].title(), 'was the month most traveled.')

    # display the most common day of week
    d = rider_data['day'].value_counts().idxmax()
    print('\n  ', day_names[d-1].title(), 'was the day most traveled.')

    # display the most common start hour
    h = rider_data['hour'].value_counts().idxmax()
    print('\n   {}:00 MT, was the hour of the day was the most traveled.'.format(h))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('='*60)

#displays stations statistics
#nothing to return
def station_stats(rider_data):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating the Most Popular Stations and most popular combination of stations or trips...\n')
    start_time = time.time()

   # create a trip column
    rider_data['trip'] = rider_data['start_station'] + ' -- ' + rider_data['end_station']

    # display most commonly used start station, end station and combination
    top_start_station = rider_data['start_station'].value_counts().idxmax()
    top_end_station = rider_data['end_station'].value_counts().idxmax()
    top_start_end_combo = rider_data['trip'].value_counts().idxmax()

    # display results
    print('   The most common start station is: {}'.format(top_start_station))
    print('   The most common end station is: {}'.format(top_end_station))
    print('   The most common combination or trip are: {}'.format(top_start_end_combo))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('='*60)

#displays trip statistics
#nothing to return
def trip_duration_stats(rider_data):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    #calculte the total, mean and max travel times
    tot_travel = rider_data['trip_duration'].sum()
    ave_travel = rider_data['trip_duration'].mean()

    #display the total, mean and max travel times
    print('The total travel time is: {}'.format(tot_travel))
    print('The average travel time is: {}'.format(ave_travel))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('='*60)

#displays user statistics
#nothing to return
def user_stats(metro_area, rider_data):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Calculate and display counts of user types and gender
    user_type_counts = rider_data['user_type'].value_counts()
    for i, types in enumerate(user_type_counts):
        print('There are {} {}s'.format(types, user_type_counts.index[i]))
    print()
    if metro_area != 'washington':
        gender_counts = rider_data['Gender'].value_counts()
        for i, sex in enumerate(gender_counts):
            print('There are {} {}s'.format(sex, gender_counts.index[i]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('='*60)

def main():

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
