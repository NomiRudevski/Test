import pandas as pd
from print_color import print

# Read CSV file into a DataFrame
csv_data = pd.read_csv('data.csv')       

def sort_by_column(data, column):       #sort data by spesific column highst first
    sorted_data = data.sort_values(by=column, ascending=False) 
    return sorted_data


def get_first_value_in_sorted_data_in_column(data, column):         # Get the highest of a pre sorted list(by column)
    highest = data[column].iloc[0]  
    return highest


def get_data_by_value_in_column(data,column, value):        #gets all data with a spesific value in a column
    type_data = data[data[column] == value]
    return type_data


def get_median(data, midian_parameter):         #returns midian of inputed data
    median = data[midian_parameter].median()
    return median

def get_average(data,colom):        # Calculate the average of a given data in a spesific column
    average = data[colom].mean() 
    rounded_average = round(average, 2)  # Roundup the averag
    return rounded_average

def get_uniqe_value_count(data, column):
    count = data[column].value_counts()
    return len(count)


def get_uniqe_values(data, column):
    values = data[column].value_counts().index.tolist()     #index with pandas and list them with a py function (.list())
    return values

def print_all_actions(array):
    for action in array:
        print(f'{action.value} - {action.name}', color='cyan')


def validate_user_index_selection(array):
    while True:
        user_input = input("Choose an option number: ")
        try:
            user_input = int(user_input)-1
            if 0 <= user_input < len(array):
                return user_input
            else:
                print('Input is invalid!', color='red')
        except:
            print('Input is invalid!', color='red')

def print_highst_price():
    highest_price = get_first_value_in_sorted_data_in_column(sort_by_column(csv_data, 'price'), 'price')
    print(f'the highst price is: {highest_price}', color='yellow')
    

def print_avarage_price():
    average = get_average(csv_data,'price')
    print(f'the average price of a diamond is: {average}', color='yellow')

def print_sum_ideal():
    ideal = get_data_by_value_in_column(csv_data, 'cut', 'Ideal')
    print(f'ther are {len(ideal)} ideal diamonds', color='yellow')

def print_colors():
    items = get_uniqe_values(csv_data, 'color')
    count = get_uniqe_value_count(csv_data, 'color')
    print(f'there are {count} colors, and they are: {items}')

def print_primium_median():
    median = get_median(get_data_by_value_in_column(csv_data,'cut', 'Premium'), 'carat')
    print(f'the midian carat of primin diamonds is {median}', color='yellow')

def print_avarage_carat_cut():
    cut_types = get_uniqe_values(csv_data, 'cut')
    for cut_type in cut_types:
        average_carat = get_average(get_data_by_value_in_column(csv_data, 'cut', cut_type), 'carat')
        print(f'The average carat of {cut_type} cut is {average_carat}', color='yellow')

def print_average_price_by_color():
    colors = get_uniqe_values(csv_data, 'color')
    for color in colors:
        average_price = get_average(get_data_by_value_in_column(csv_data, 'color', color), 'price')
        print(f'The average price of diamonds with color {color} is {average_price}', color='yellow')


