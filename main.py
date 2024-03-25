import os
from dotenv import load_dotenv

from client import RunaiClient

load_dotenv()

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
        runai_base_url=BASE_URL
    )
    clusters = client.clusters.all()
    
    # pprint.pprint("####################################### cluster #######################################")
    # pprint.pprint(clusters[0])
    # pprint.pprint("####################################### cluster #######################################")
    
    # departments = clusters[0].departments.all()

    # pprint.pprint("####################################### department #######################################")
    # pprint.pprint(departments[0])
    # pprint.pprint("####################################### department #######################################")
    
    # projects = departments[0].projects

    # pprint.pprint("####################################### project #######################################")
    # pprint.pprint(projects.all())
    # pprint.pprint("####################################### project #######################################")
    # print(client.projects.all(cluster_id=CLUSTER_ID))

    cluster = client.clusters.filter(name="cs-ofir-2-16-test-saas-1710667642")
    
    project = cluster[0].departments.filter(name="default")[0].projects.get(project_id=29953)
    print(project)