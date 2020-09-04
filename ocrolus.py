from typing import Tuple, Optional, Union, List
import csv
from collections import namedtuple
import sys
# User phone data structure
UserPhoneData = namedtuple("UserPhoneData", ["first_name", "last_name", "number", "state"])

# Phone directory where data from csv will be loaded
phone_directory = {}


def is_valid_file_path(path: str)-> bool:
    """[Returns if the given file path is valid or not]

    Arguments:
        path {str}

    Returns:
        bool -- [description]
    """
    try:
        fp = open(path, "rb")
    except FileNotFoundError:
        return False
    return True


def process_input(data:Tuple) -> Union[bool, UserPhoneData]:
    """This method will take each row. And will validate the correctness of the
    row.

    This will return false
        - if not a valid data
    Else
        - It will return the data in the form of


    -- Valid formats are
    LastName, FirstName, State, Number
    FirstName, Lastname, Number, State
    FirstName, LastName, Number, State

    Arguments:
        data {Tuple} -- [description]

    Returns:
        [type] -- [description]
    """
    first_name, last_name = data[0], data[1]
    is_name_valid = isinstance(first_name,str) & isinstance(last_name, str)

    # If both first and last names are not string then not a valid format
    if not is_name_valid:
        return (False, UserPhoneData("", "", "", ""))

    # check if phone number is at last
    phone_number_at_last, phone_number_at_2nd =  False, False

    try:
        phone_number_at_last = isinstance(int(data[3][-1]), int)
    except ValueError:
        try:
            phone_number_at_2nd = isinstance(int(data[2][-1]), int)
        except ValueError:
            return (False, UserPhoneData("", "", "", ""))

    if not phone_number_at_last and not phone_number_at_2nd:
        return (False, UserPhoneData("", "", "", ""))

    if phone_number_at_2nd:
        # Then first name will be at 0th, last name will be at 1st
        user_phone_data = UserPhoneData(data[0], data[1], data[2], data[3])
    elif phone_number_at_last:
        # Then last name will be at 0th, first name will be at 1st
        user_phone_data = UserPhoneData(data[1], data[0], data[3], data[2])

    return (True, user_phone_data)

def load_data(user_phone_data: UserPhoneData) -> None:
    """[This function loads the data into phone directory]

    Arguments:
        user_phone_data {UserPhoneData}
    """
    last_name = user_phone_data.last_name

    if last_name.lower() in phone_directory:

        phone_directory[last_name.lower()].append(user_phone_data)
        phone_directory[last_name.lower()] =  sorted(
            phone_directory[last_name.lower()], key=lambda x: x.first_name.lower()
            )
    else:
        phone_directory[last_name.lower()] = [user_phone_data]


def process_csv(phone_dataset_filepath: str):
    """[This function extracts data from csv and loads into phone directory]

    Arguments:
        phone_dataset_filepath {str} -- [description]
    """
    with open(phone_dataset_filepath, "r") as fp:
        csv_reader = csv.reader(fp, delimiter=',')

        for row in csv_reader:
            is_valid, phone_data = process_input(row)
            if is_valid:
                load_data(phone_data)


def search_user_data(last_name: str) -> Optional[List[UserPhoneData]]:
    cleared_last_name = last_name.lower()

    try:
        return phone_directory[cleared_last_name]
    except Exception as e:
        return None



if __name__ == "__main__":
    argumentList = sys.argv
    # phone_dataset_filepath: str = input("Please enter phone dataset")
    # query_file_path: str = input()
    phone_dataset_filepath = argumentList[1]
    query_file_path = argumentList[2]

    is_valid_phone_data_path = is_valid_file_path(phone_dataset_filepath)
    is_valid_query_file_path = is_valid_file_path(query_file_path)

    assert is_valid_phone_data_path == True, "Invalid phone data set csv file"
    assert is_valid_query_file_path == True, "Invalid Query file path"

    # Process csv file to load all the phones
    process_csv(phone_dataset_filepath)

    # Now, Query from query.txt
    output_file = open("output.txt", "a")

    with open(query_file_path, "r") as fp:
        query_list = fp.readlines()
        for query in query_list:
            cleaned_query_text = query.strip("\n")
            output_file.write(f"Matches for: {cleaned_query_text}\n")
            searched_result = search_user_data(cleaned_query_text)
            if not searched_result:
                output_file.write("No results found\n")
                continue

            formatted_output = ""
            for idx, item in enumerate(searched_result):
                formatted_output += f"Result {idx+1}: {item.last_name}, {item.first_name}, {item.state}, {item.number}\n"

            output_file.write(formatted_output)



