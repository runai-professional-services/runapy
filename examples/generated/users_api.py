"""
Examples for using the UsersApi
"""

from runai.configuration import Configuration
from runai.api_client import ApiClient
from runai.api import UsersApi
from runai import models

# Configure API key authorization
configuration = Configuration(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
    runai_base_url="https://org.run.ai",
)

api_client = ApiClient(configuration)
api_instance = UsersApi(api_client)


def example_change_user_password():
    """
    Example of using change_user_password

    change user password

    """
    try:
        # Prepare the request parameters

        # Create example data for UserChangePasswordRequest
        user_change_password_request = models.UserChangePasswordRequest(
            current_password="", new_password=""
        )

        # Make the API call
        api_response = api_instance.change_user_password(
            user_change_password_request=user_change_password_request,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling change_user_password: {e}")


def example_count_users():
    """
    Example of using count_users

    Count users
    count users
    """
    try:
        # Prepare the request parameters

        filter_by = ["example_item_1", "example_item_2"]

        search = "example_search"

        # Make the API call
        api_response = api_instance.count_users(
            filter_by=filter_by,
            search=search,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling count_users: {e}")


def example_create_user():
    """
    Example of using create_user

    Create a local user.
    Use to create a local platform user.
    """
    try:
        # Prepare the request parameters

        # Create example data for UserCreationRequest1
        user_creation_request1 = models.UserCreationRequest1(
            email="A@9LCSLv1C1ylmgd0.Y2TA5TkIRHRRA401iz1CiIy.dNTRddzXYdswQltRTtwKQzBuNJxBelKTmfIQcBkWgeAShmXXoTaDzlkczbtHjkljEhQVqeWYqqMQZlEQb",
            reset_password=True,
            notify=True,
        )

        # Make the API call
        api_response = api_instance.create_user(
            user_creation_request1=user_creation_request1,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling create_user: {e}")


def example_delete_user_by_id():
    """
    Example of using delete_user_by_id

    Delete a user by id.
    Use to delete a user by id.
    """
    try:
        # Prepare the request parameters
        user_id = "example_user_id"

        # Make the API call
        api_instance.delete_user_by_id(
            user_id=user_id,
        )

    except Exception as e:
        print(f"Exception when calling delete_user_by_id: {e}")


def example_get_user_by_id():
    """
    Example of using get_user_by_id

    Get a user by id.
    Retrieve a user&#39;s details by id.
    """
    try:
        # Prepare the request parameters
        user_id = "example_user_id"

        # Make the API call
        api_response = api_instance.get_user_by_id(
            user_id=user_id,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling get_user_by_id: {e}")


def example_get_users():
    """
    Example of using get_users

    Get users.
    Retrieve a list of platform users.
    """
    try:
        # Prepare the request parameters
        filter = "example_filter"

        filter_by = ["example_item_1", "example_item_2"]

        sort_order = "example_sort_order"

        offset = 42

        limit = 42

        search = "example_search"

        # Make the API call
        api_response = api_instance.get_users(
            filter=filter,
            filter_by=filter_by,
            sort_by=sort_by,
            sort_order=sort_order,
            offset=offset,
            limit=limit,
            search=search,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling get_users: {e}")


def example_logout_user():
    """
    Example of using logout_user

    Logout a user.
    Use to force a user to logout.
    """
    try:
        # Prepare the request parameters
        user_id = "example_user_id"

        # Make the API call
        api_instance.logout_user(
            user_id=user_id,
        )

    except Exception as e:
        print(f"Exception when calling logout_user: {e}")


def example_reset_user_password():
    """
    Example of using reset_user_password

    Reset a user&#39;s password.
    Use to to reset a user&#39;s password.
    """
    try:
        # Prepare the request parameters
        user_id = "example_user_id"

        # Make the API call
        api_response = api_instance.reset_user_password(
            user_id=user_id,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling reset_user_password: {e}")
