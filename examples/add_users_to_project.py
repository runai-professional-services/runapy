"""
Given users emails list, project name, and a role.
Create access rules and assign all users to the project with the given role.

To run the script

1. Change the values for:
PROJECT_NAME -> the project name
ROLE_NAME -> role name, case sensitive, should match Run:ai roles per the docs
USER_NAME_MAP -> a map of emails to assign the permissions. The map also stores user ids for each user.
                 Keep values empty

2. Run the script

The script can be easily modified to on board users to different scope.
By switching the scope type and scope id in access rule API call
"""

from runai.configuration import Configuration
from runai.api_client import ApiClient
from runai.runai_client import RunaiClient

from runai import models

configuration = Configuration(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
    runai_base_url="https://org.run.ai",
)

api_client = ApiClient(configuration)
client = RunaiClient(api_client)

# Change the values according to requirements
PROJECT_NAME = "project-a"
ROLE_NAME = "L2 researcher"
USER_NAME_MAP = {
    "test@run.ai": "",
    "r-test@run.ai": "",
    "runai-testb@run.ai": "",
}

# Dynamically assigned from below API calls - Do not change manually
USER_ID_LIST = []
ROLE_ID = -1
PROJECT_ID = -1

# Get the role id by role name for access rules creation
response = client.authentication_and_authorization.roles.get_roles().data
for role in response:
    if role["name"] == ROLE_NAME:
        ROLE_ID = role["id"]

if ROLE_ID == -1:
    print(f"Could not find role id for role '{ROLE_NAME}' make sure there are no typos")
    exit(1)

# Get project ID by project name
response = client.organizations.projects.get_projects(
    filter_by=[f"name=={PROJECT_NAME}"]
).data["projects"][0]
PROJECT_ID = response["id"]

# Fetch user ids by user names for access rules creation
user_list = client.authentication_and_authorization.users.get_users_0().data
for user in user_list:
    if user["username"] in USER_NAME_MAP:
        USER_NAME_MAP[user["username"]] = user["id"]

# Create access rules for each user
for user_name, user_id in USER_NAME_MAP.items():
    response = client.authentication_and_authorization.access_rules.create_access_rule(
        access_rule_creation_fields=models.AccessRuleCreationFields(
            subject_type=models.SubjectType.USER,
            subject_id=user_id,
            role_id=ROLE_ID,
            scope_id=PROJECT_ID,
            scope_type=models.ScopeType.PROJECT,
        )
    )
    if response.status_code == 201:
        print(f"Succesfully created access rule for user: {user_name}")
    else:
        print(f"Failed to create access rule for user: {user_name}")
        print(response)
