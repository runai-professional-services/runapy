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
        cluster_id=CLUSTER_ID
    )    

    # print(client.projects.all())

    # print(client.projects.test())
    # client.projects.create(
    #     name= "test-project",
    #     requestedNamespace="test",
    #     nodeTypes={
    #         "training": "s"
    #     })