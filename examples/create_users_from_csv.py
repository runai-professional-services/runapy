import os
import argparse

import pandas as pd
from dotenv import load_dotenv

from runai.client import RunaiClient

load_dotenv(override=True)

BASE_URL = os.environ.get("BASE_URL")
CLIENT_ID = os.environ.get("CLIENT_ID")
CLIENT_SECRET = os.environ.get("CLIENT_SECRET")
REALM = os.environ.get("REALM")
CLUSTER_ID = os.environ.get("CLUSTER_ID")

client = RunaiClient(
    realm=REALM,
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    runai_base_url=BASE_URL,
    cluster_id=CLUSTER_ID
)


def create_users_from_csv(csv_path):
    # Load the CSV file
    data = pd.read_csv(csv_path)

    # Initialize the client
    client = RunaiClient(
        realm=REALM,
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        runai_base_url=BASE_URL,
        cluster_id=CLUSTER_ID,
        debug=True
        )

    # Iterate through each row in the CSV and create users
    for index, row in data.iterrows():
        email = row['email']
        role_name = row['role']
        
        # Agonstic to failures in case user already exists
        try:
            resp = client.users.create(email=email)
        except Exception:
            continue
        username = resp["username"]
        password = resp["tempPassword"]
        print(f"Successfully created user: {username} with password: {password}\n)")
        
        # Get roles IDs
        roles_map = client.roles.get_roles_name_to_id_map()

        # Agonstic to failures in case access rule already exists
        try:
            client.access_rules.create(
                    subject_id=username,
                    subject_type="user",
                    role_id=roles_map[role_name],
                    scope_id=CLUSTER_ID,
                    scope_type="cluster"
                )
            print(f"Succesfully created access rule for: {username}, role: {role_name}\n")
        except Exception:
            continue


def main():
    parser = argparse.ArgumentParser(description='Create users from a CSV file.')
    parser.add_argument('csv_path', type=str, help='The path to the CSV file containing user data.')

    args = parser.parse_args()

    create_users_from_csv(args.csv_path)


if __name__ == '__main__':
    main()
