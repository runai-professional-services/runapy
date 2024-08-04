import os
from dotenv import load_dotenv

from client import RunaiClient

load_dotenv(override=True)

BASE_URL = os.environ.get("BASE_URL")
CLIENT_ID = os.environ.get("CLIENT_ID")
CLIENT_SECRET = os.environ.get("CLIENT_SECRET")
REALM = os.environ.get("REALM")
CLUSTER_ID = os.environ.get("CLUSTER_ID")

if __name__ == "__main__":

    client = RunaiClient(
        realm=REALM,
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        runai_base_url=BASE_URL,
        cluster_id=CLUSTER_ID,
        retries=3,
    )

    # print(client.roles.get_roles_name_to_id_map())
    
    # print(client.access_rules.all())
    
    # print(client.access_rules.create(
    #     subject_id="ofir.eldar@run.ai",
    #     subject_type="user",
    #     role_id=2,
    #     scope_id=CLUSTER_ID,
    #     scope_type="cluster"
    # ))

    # print(client.access_rules.all())