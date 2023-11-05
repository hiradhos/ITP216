import json
from typing import Tuple, Optional, Any

creds_db_file = r"C:\Users\hosse\Desktop\Github\ITP216\Week10Flask\ITP216_HW10_Hosseini_Hirad\ITP-216 H10 Starter Code\util\creds_db_file.json"
foods_db_file = r"C:\Users\hosse\Desktop\Github\ITP216\Week10Flask\ITP216_HW10_Hosseini_Hirad\ITP-216 H10 Starter Code\util\foods_db_file.json"


def save_dict_to_json_file(db_dict: dict[str, str], db_file: str) -> None:
    """
    Writes a python dictionary to a text file in JSON (Java Script Object Notation) format
    You will replace this w/ commit() and close() when working w/ an actual sqlite3 DB
    :param db_dict: the python dictionary to write to file
    :param db_file: the destination file name as a string
    :return: None
    Side Effects:
    """
    with open(db_file, 'w') as file:
        # use dumps() (with an s (for as string)) instead of dump()
        # to ensure human-readable text file instead of binary
        json_obj = json.dumps(db_dict)
        # write the in memory json object to file
        file.write(json_obj)


def load_json_file_to_dict(db_file: str) -> Any:
    """
    Reads a text file in JSON (Java Script Object Notation) format, created by save_dict_to_json_file()
    You will replace this w/ connect() when working w/ an actual sqlite3 DB
    and return it as a python dictionary
    :param db_file: the source text file in JSON file representing a python dictionary
    :return: a python dictionary representing the source text JSON file as a python dictionary object
    """
    with open(db_file, 'r') as file:
        # load from file into in-memory dict and return it
        return json.load(file)


def db_create_user(user_to_add: str, password_to_add: str) -> None:
    """
    Add provided user and password to the credentials table
    Add provided user to the userfoods table
    and sets their favorite food to "not set yet".
    Called from create_user() view function.

    :param user_to_add: username to create
    :param password_to_add: password to create
    :return: None
    """
    # load from file into in-memory dict
    cred_db_dict = load_json_file_to_dict(creds_db_file)
    # dict[key] = value  assigns value to key in dict
    cred_db_dict[user_to_add] = password_to_add
    # write in-memory dict back to file
    save_dict_to_json_file(cred_db_dict, creds_db_file)

    # Rinse and repeat for food db file/table
    foods_db_dict = load_json_file_to_dict(foods_db_file)
    foods_db_dict[user_to_add] = "not set yet"
    save_dict_to_json_file(foods_db_dict, foods_db_file)


def db_remove_user(user_to_remove: str) -> Tuple[Optional[str], Optional[str]]:
    """
    Removes provided user from all DB tables.
    Called from remove_user() view function.

    :param user_to_remove: username to remove from DB JSON files
    :return: tuple of 2 strings containing the credentials and foods db file user removed,
        or None if user doesn't exist in each respective db file
    """
    # load from file into in-memory dict
    cred_db_dict = load_json_file_to_dict(creds_db_file)
    # dict.pop() removes and returns what was removed, returns default of None otherwise
    cred_pop_return = cred_db_dict.pop(user_to_remove, None)
    # write in-memory dict back to file
    save_dict_to_json_file(cred_db_dict, creds_db_file)

    # Rinse and repeat for food db file/table
    food_db_dict = load_json_file_to_dict(foods_db_file)
    food_pop_return = food_db_dict.pop(user_to_remove, None)
    save_dict_to_json_file(food_db_dict, foods_db_file)

    return cred_pop_return, food_pop_return


def db_get_user_list(db_file: str) -> Any:
    """
    Returns the foods table to get a list of all the user and their corresponding favorite foods
    for display on admin.html.
    Called to render admin.html template.

    :param db_file: json db file as a string to read from (either creds or foods)

    :return: a dictionary with username as key and their favorite food as value
                NOTE: this is what populates the 'result' variable in the admin.html template
                which is passed as an argument to the result param when rendered in remove_user()
    """
    return load_json_file_to_dict(db_file)


def db_check_creds(db_dict: dict[str, str], user_to_check: str, password_to_check: str) -> bool:
    """
    Checks to see if supplied username and password are in the DB's credentials table.
    Called from login() view function.

    :param db_dict: file db dict to check against (simulates DB cred table)
    :param user_to_check: username to check
    :param password_to_check: password_to_check to check
    :return: True if both username and password are correct, False otherwise.
    """
    if user_to_check not in db_dict:
        return False
    else:
        # is password provided equal to correct password stored in "db" ?
        return db_dict[user_to_check] == password_to_check


def db_get_food(user_to_get: str) -> Any:
    """
    Gets the provided user's favorite food from the DB file.
    Called to render user.html fav_food template variable.

    :param user_to_get: username to get favorite food of
    :return: the favorite food of the provided user as a string,
        or 'Not Found!' if user not in db file
    """
    food_db_dict = load_json_file_to_dict(foods_db_file)
    # long form get() allows to specify 'Not Found' as a string default if the user is not in db file
    # whereas using the short form dict[key] to get value throws an error on not found
    return food_db_dict.get(user_to_get, 'Not Found!')


def db_set_food(user_to_update: str, new_fav_food: str) -> None:
    """
    Sets the favorite food of user param, to new favorite food param.
    Called from set_food() view function.

    :param user_to_update: username to update favorite food of
    :param new_fav_food: user's new favorite food
    :return: None
    """
    food_db_dict = load_json_file_to_dict(foods_db_file)
    # dict[key] = value  assigns value to key
    food_db_dict[user_to_update] = new_fav_food
    save_dict_to_json_file(food_db_dict, foods_db_file)


def main() -> None:
    """
    Example Usage / Unit Tests
    :return: None
    """
    # Initialize python dicts
    cred_db_dict = {"user1": "pass1", "user2": "pass2", "user3": "pass3"}
    food_db_dict = {"user1": "cake", "user2": "popcorn", "user3": "pie"}

    # Save python dicts to their respective json db files
    save_dict_to_json_file(cred_db_dict, creds_db_file)
    save_dict_to_json_file(food_db_dict, foods_db_file)

    # Load json db files back to python dicts
    cred_db_dict = load_json_file_to_dict(creds_db_file)
    food_db_dict = load_json_file_to_dict(foods_db_file)
    assert cred_db_dict == {'user1': 'pass1', 'user2': 'pass2', 'user3': 'pass3'}
    assert food_db_dict == {'user1': 'cake', 'user2': 'popcorn', 'user3': 'pie'}

    # Make sure a new user is created successfully in both tables w/ the proper initial values everywhere
    db_create_user('newUser', 'newPassword')
    creds_db_dict = load_json_file_to_dict(creds_db_file)
    foods_db_dict = load_json_file_to_dict(foods_db_file)
    assert creds_db_dict == {'user1': 'pass1', 'user2': 'pass2', 'user3': 'pass3', 'newUser': 'newPassword'}
    assert foods_db_dict == {'user1': 'cake', 'user2': 'popcorn', 'user3': 'pie', 'newUser': 'not set yet'}

    # Make sure a user is actually removed from the DB
    db_remove_user('user3')
    db_dict = load_json_file_to_dict(creds_db_file)
    foods_db_dict = load_json_file_to_dict(foods_db_file)
    assert db_dict == {'user1': 'pass1', 'user2': 'pass2', 'newUser': 'newPassword'}
    assert food_db_dict == {'user1': 'cake', 'user2': 'popcorn', 'user3': 'pie'}

    # Make sure removing a user that doesn't exist behaves properly (no effect on DB)
    db_remove_user('user doesnt exist')
    db_dict = load_json_file_to_dict(creds_db_file)
    assert db_dict == {'user1': 'pass1', 'user2': 'pass2', 'newUser': 'newPassword'}
    assert food_db_dict == {'user1': 'cake', 'user2': 'popcorn', 'user3': 'pie'}

    # Make sure get user list function works
    assert db_get_user_list(foods_db_file) == {'user1': 'cake', 'user2': 'popcorn', 'newUser': 'not set yet'}

    # Correct username and password (green case)
    assert db_check_creds(cred_db_dict, 'user1', 'pass1') is True
    # Wrong username but right password
    assert db_check_creds(cred_db_dict, 'wrong user', 'pass1') is False
    # Right username but wrong password
    assert db_check_creds(cred_db_dict, 'user1', 'wrong password') is False
    # Wrong everyhing
    assert db_check_creds(cred_db_dict, 'wrong user', 'wrong password') is False

    # Spot check values
    assert db_get_food('user1') == 'cake'
    assert db_get_food('newUser') == 'not set yet'
    assert db_get_food('user doesnt exist') == 'Not Found!'

    # Update existing user 
    db_set_food('user1', 'oreos')
    assert db_get_user_list(foods_db_file) == {'user1': 'oreos', 'user2': 'popcorn', 'newUser': 'not set yet'}


if __name__ == '__main__':
    main()
