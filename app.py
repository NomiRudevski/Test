from functions import *
from enum import Enum


class Questions(Enum):
    HIGHEST_PRICE = 1
    AVARAGE_PRICE = 2
    HOW_MENY_IDEAL = 3
    HOW_MENY_COLORS_AND_WHATTT = 4
    THE_MEDIAN_OF_PRIMIUM = 5
    AVARAGE_CARAT_BY_CUT = 6
    AVARAGE_PRICE_BY_COLOR = 7
    TEST_IS_DONE_EXIT = 8

if __name__ == '__main__':
     while True:
        print_all_actions(Questions)
        user_selection = Questions(validate_user_index_selection(Questions) + 1)

        if user_selection == Questions.TEST_IS_DONE_EXIT: exit()
        if user_selection == Questions.HIGHEST_PRICE: print_highst_price()
        if user_selection == Questions.AVARAGE_PRICE: print_avarage_price()
        if user_selection == Questions.HOW_MENY_IDEAL: print_sum_ideal()
        if user_selection == Questions.HOW_MENY_COLORS_AND_WHATTT: print_colors()
        if user_selection == Questions.THE_MEDIAN_OF_PRIMIUM: print_primium_median()
        if user_selection == Questions.AVARAGE_CARAT_BY_CUT: print_avarage_carat_cut()
        if user_selection == Questions.AVARAGE_PRICE_BY_COLOR: print_average_price_by_color()