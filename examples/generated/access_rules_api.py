"""
Examples for using the AccessRulesApi
"""

from runai.configuration import Configuration
from runai.api_client import ApiClient
from runai.api import AccessRulesApi
from runai import models

# Configure API key authorization
configuration = Configuration(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
    runai_base_url="https://org.run.ai",
)

api_client = ApiClient(configuration)
api_instance = AccessRulesApi(api_client)


def example_count_access_rules():
    """
    Example of using count_access_rules

    Count access rules.
    Use to retrieve the number of access rules.
    """
    try:
        # Prepare the request parameters

        include_deleted = True

        filter_by = ["example_item_1", "example_item_2"]

        search = "example_search"

        # Make the API call
        api_response = api_instance.count_access_rules(
            include_deleted=include_deleted,
            filter_by=filter_by,
            search=search,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling count_access_rules: {e}")


def example_create_access_rule():
    """
    Example of using create_access_rule

    Create an access rule.
    Use to bind a predefined role to a subject (user, group or application) in a scope.
    """
    try:
        # Prepare the request parameters

        # Create example data for AccessRuleCreationFields
        access_rule_creation_fields = models.AccessRuleCreationFields(
            subject_id="user@run.ai",
            subject_type="user",
            role_id=53142648,
            scope_id="a418ed33-9399-48c0-a890-122cadd13bfd",
            scope_type="system",
            cluster_id="71f69d83-ba66-4822-adf5-55ce55efd210",
        )

        # Make the API call
        api_response = api_instance.create_access_rule(
            access_rule_creation_fields=access_rule_creation_fields,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling create_access_rule: {e}")


def example_delete_access_rule():
    """
    Example of using delete_access_rule

    Delete an access rule.
    Use to delete the subject permissions assigned by access rule id.
    """
    try:
        # Prepare the request parameters

        access_rule_id = 42

        # Make the API call
        api_instance.delete_access_rule(
            access_rule_id=access_rule_id,
        )

    except Exception as e:
        print(f"Exception when calling delete_access_rule: {e}")


def example_get_access_rule():
    """
    Example of using get_access_rule

    Get an access rule.
    Use to retrieve the details of an access rule by id.
    """
    try:
        # Prepare the request parameters

        access_rule_id = 42

        # Make the API call
        api_response = api_instance.get_access_rule(
            access_rule_id=access_rule_id,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling get_access_rule: {e}")


def example_get_access_rules():
    """
    Example of using get_access_rules

    List the access rules.
    Retrieve a list of access rules.
    """
    try:
        # Prepare the request parameters
        subject_type = "example_subject_type"

        subject_id_filter = "example_subject_id_filter"

        subject_ids = ["example_item_1", "example_item_2"]

        limit = 42

        offset = 42

        last_updated = "example_last_updated"

        include_deleted = True

        cluster_id = "example_cluster_id"

        scope_type = "example_scope_type"

        scope_id = "example_scope_id"

        role_id = 42

        sort_order = "example_sort_order"

        filter_by = ["example_item_1", "example_item_2"]

        search = "example_search"

        # Make the API call
        api_response = api_instance.get_access_rules(
            subject_type=subject_type,
            subject_id_filter=subject_id_filter,
            subject_ids=subject_ids,
            limit=limit,
            offset=offset,
            last_updated=last_updated,
            include_deleted=include_deleted,
            cluster_id=cluster_id,
            scope_type=scope_type,
            scope_id=scope_id,
            role_id=role_id,
            sort_order=sort_order,
            sort_by=sort_by,
            filter_by=filter_by,
            search=search,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling get_access_rules: {e}")
