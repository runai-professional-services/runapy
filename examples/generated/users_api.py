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


def example_create_group():
    """
    Example of using create_group

    Create a new group.
    Create a new group and assign it with roles. Deprecated endpoint. please reffer to Roles &amp; Access rules API.
    """
    try:
        # Prepare the request parameters

        # Create example data for GroupCreationRequest
        group_creation_request = models.GroupCreationRequest(
            username="group1",
            email="",
            roles=["viewer"],
            entity_type="sso-user",
            tenant_id=1001,
            permit_all_clusters=False,
            user_id="group1",
            permitted_clusters=["71f69d83-ba66-4822-adf5-55ce55efd210"],
            created_by="aaaaa-3333-4444-bbbbbb-111",
        )

        # Make the API call
        api_response = api_instance.create_group(
            group_creation_request=group_creation_request,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling create_group: {e}")


def example_create_user():
    """
    Example of using create_user

    Create a new user.
    Deprecated endpoint. Use the new endpoint api/v1/users instead and api/v1/authorization/access-rules to give user permissions.
    """
    try:
        # Prepare the request parameters

        # Create example data for UserCreationRequest
        user_creation_request = models.UserCreationRequest(
            email="user@email.com",
            roles=["viewer"],
            entity_type="regular-user",
            tenant_id=1001,
            password="secret!123",
            need_to_change_password=True,
            permit_all_clusters=False,
            user_id="4008188b-ab50-4aa5-a3f2-b78091ccf92d",
            permitted_clusters=["71f69d83-ba66-4822-adf5-55ce55efd210"],
        )

        # Make the API call
        api_response = api_instance.create_user(
            user_creation_request=user_creation_request,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling create_user: {e}")


def example_create_user_0():
    """
    Example of using create_user_0

    Create a local user.
    Use to create a local platform user.
    """
    try:
        # Prepare the request parameters

        # Create example data for UserCreationRequest1
        user_creation_request1 = models.UserCreationRequest1(
            email="A@9LCSLv1C1ylmgd0.Y2TA5TkIRHRRA401iz1CiIy.dNTRddzXYdswQltRTtwKQzBuNJxBelKTmfIQcBkWgeAShmXXoTaDzlkczbtHjkljEhQVqeWYqqMQZlEQb",
            reset_password=True,
        )

        # Make the API call
        api_response = api_instance.create_user_0(
            user_creation_request1=user_creation_request1,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling create_user_0: {e}")


def example_delete_group_by_name():
    """
    Example of using delete_group_by_name

    Delete a group.
    Delete the given group from the tenant. This endpoint requires ADMIN role. Deprecated endpoint. please reffer to Roles &amp; Access rules API.
    """
    try:
        # Prepare the request parameters
        group_name = "example_group_name"

        # Make the API call
        api_instance.delete_group_by_name(
            group_name=group_name,
        )

    except Exception as e:
        print(f"Exception when calling delete_group_by_name: {e}")


def example_delete_user_by_id():
    """
    Example of using delete_user_by_id

    Delete a user.
    Delete the given user from the tenant. This endpoint requires ADMIN role. Deprecated endpoint. Use the new endpoint api/v1/users/{userId} instead.
    """
    try:
        # Prepare the request parameters
        user_id = "example_user_id"

        users_type = ["example_item_1", "example_item_2"]

        # Make the API call
        api_instance.delete_user_by_id(
            user_id=user_id,
            users_type=users_type,
        )

    except Exception as e:
        print(f"Exception when calling delete_user_by_id: {e}")


def example_delete_user_by_id_0():
    """
    Example of using delete_user_by_id_0

    Delete a user by id.
    Use to delete a user by id.
    """
    try:
        # Prepare the request parameters
        user_id = "example_user_id"

        # Make the API call
        api_instance.delete_user_by_id_0(
            user_id=user_id,
        )

    except Exception as e:
        print(f"Exception when calling delete_user_by_id_0: {e}")


def example_ge_group_by_name():
    """
    Example of using ge_group_by_name

    Get group details.
    Get the details of a given group. This endpoint requires ADMIN, EDITOR or VIEWER role. Deprecated endpoint. please reffer to Roles &amp; Access rules API.
    """
    try:
        # Prepare the request parameters
        group_name = "example_group_name"

        # Make the API call
        api_response = api_instance.ge_group_by_name(
            group_name=group_name,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling ge_group_by_name: {e}")


def example_get_groups():
    """
    Example of using get_groups

    Get groups list.
    Return the list of groups of the tenant. Deprecated endpoint. please reffer to Roles &amp; Access rules API.
    """
    try:
        # Prepare the request parameters

        roles = ["example_item_1", "example_item_2"]

        only_created_by_me = True

        # Make the API call
        api_response = api_instance.get_groups(
            roles=roles,
            only_created_by_me=only_created_by_me,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling get_groups: {e}")


def example_get_roles():
    """
    Example of using get_roles

    Get all possible permissions.
    Get the complete set of permissions that a tenant can grant to users and applications. Deprecated endpoint. please refer to Roles &amp; Access rules API.
    """
    try:
        # Make the API call with no parameters
        api_response = api_instance.get_roles()
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling get_roles: {e}")


def example_get_user_by_id():
    """
    Example of using get_user_by_id

    Get user details.
    Get the details of a given user. This endpoint requires ADMIN, EDITOR or VIEWER role. Deprecated endpoint. Use the new endpoint api/v1/users/{userId} instead.
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


def example_get_user_by_id_0():
    """
    Example of using get_user_by_id_0

    Get a user by id.
    Retrieve a user&#39;s details by id.
    """
    try:
        # Prepare the request parameters
        user_id = "example_user_id"

        # Make the API call
        api_response = api_instance.get_user_by_id_0(
            user_id=user_id,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling get_user_by_id_0: {e}")


def example_get_user_roles():
    """
    Example of using get_user_roles

    Get user permissions.
    Return the set of permissions granted to a given user. Deprecated endpoint. please reffer to Roles &amp; Access rules API.
    """
    try:
        # Prepare the request parameters
        user_id = "example_user_id"

        # Make the API call
        api_response = api_instance.get_user_roles(
            user_id=user_id,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling get_user_roles: {e}")


def example_get_users():
    """
    Example of using get_users

    Get users list.
    Deprecated, use /api/v1/users instead.  Return the list of users of the tenant.
    """
    try:
        # Prepare the request parameters

        roles = ["example_item_1", "example_item_2"]

        only_created_by_me = True

        users_type = ["example_item_1", "example_item_2"]

        # Make the API call
        api_response = api_instance.get_users(
            roles=roles,
            only_created_by_me=only_created_by_me,
            users_type=users_type,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling get_users: {e}")


def example_get_users_0():
    """
    Example of using get_users_0

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
        api_response = api_instance.get_users_0(
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
        print(f"Exception when calling get_users_0: {e}")


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


def example_update_group_by_name():
    """
    Example of using update_group_by_name

    Update group details.
    Update the details of a given group. This endpoint requires ADMIN role. Deprecated endpoint. please reffer to Roles &amp; Access rules API.
    """
    try:
        # Prepare the request parameters
        group_name = "example_group_name"

        # Create example data for GroupWithName
        group_with_name = models.GroupWithName()

        # Make the API call
        api_response = api_instance.update_group_by_name(
            group_name=group_name,
            group_with_name=group_with_name,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling update_group_by_name: {e}")


def example_update_user_by_id():
    """
    Example of using update_user_by_id

    Update user details.
    Update the details of a given user. This endpoint requires ADMIN role. Deprecated endpoint. Use the new endpoint api/v1/users/{userId} instead.
    """
    try:
        # Prepare the request parameters
        user_id = "example_user_id"

        # Create example data for User1
        user1 = models.User1()

        # Make the API call
        api_response = api_instance.update_user_by_id(
            user_id=user_id,
            user1=user1,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling update_user_by_id: {e}")
