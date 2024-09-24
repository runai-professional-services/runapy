from runai.client import RunaiClient

client = RunaiClient(
    client_id="api-client",
    client_secret="SECRET",
    runai_base_url="https://ps.runailabs-cs.com",
    cluster_id="162fbc44-b3de-4719-8107-15f5a880b13b"
)

###### S3 and access keys ######

print(client.assets.credentials.access_key.create(
    name="s3-creds",
    scope="tenant",
    access_key_id="ACIVJXLQQTGRRXKNPAI3",
    access_key_secret="tBb7gR3zQcgZ184eTNETxXFyytEPXu3ewWTXTdSb"
))

print(client.assets.s3.create(
    name="test-bucket",
    scope="tenant",
    spec={"bucket": "bucket",
          "url": "https://bucket.s3.us-east-1.amazonaws.com",
          "path": "/home/jovyan/work",
          "accessKeyAssetId": "6bb6cdf4-08e7-4df0-abe7-d8400bc891b2"
          }
))


###### PVCs ######

print(
    client.assets.pvc.create(
        "first-pvc",
        scope="tenant",
        spec={
            "path": "/container/my-claim",
            "existingPvc": False,
            "claimName": "my-claim",
            "readOnly": False,
            "ephemeral": False,
            "claimInfo": {
                "size": "1G",
                "storageClass": "my-storage-class",
                "accessModes": {
                    "readWriteOnce": True,
                    "readOnlyMany": False,
                    "readWriteMany": False,
                },
                "volumeMode": "Filesystem",
            },
        },
    )
)

# Create PVC datasource from existing pvc
print(client.assets.pvc.create(
    name="claim-from-existing",
    scope="tenant",
    spec={
        "path": "/host/local/data",
        "existingPvc": True,
        "claimName": "my-claim"
    }
))


##### Git #####
print(client.assets.credentials.password.create(
    name="git-creds",
    scope="tenant",
    user="git-username",
    password="secret-password"
))

print(client.assets.git.create(
    name="git-datasource",
    scope="tenant",
    repository="github.com/my-org/my-repo",
    path="/container/my-repository",
    password_asset_id="ca484ab7-5555-41d8-8ddc-f4a4de2b6d91"
))


#### docker-registry #####
print(client.assets.credentials.docker_registry_secret.create(
    name="registry-test",
    scope="tenant",
    url="https://hub.docker.com",
    user="docker-user",
    password="dckr_pat_R-r_vWF6Y3rH-XwXDTBeK0do6c7"
))


#### Secret ####
print(client.assets.nfs.create(
    name="new-secret-from-docker-registry-secret",
    scope="tenant",
    path="/container/nfs",
    server="10.54.30.12",
    mount_path="/home/local/data"
))

# List assets
client.assets.git.all()
client.assets.s3.all()
client.assets.nfs.all()
client.assets.pvc.all()

client.assets.credentials.access_key.all()
client.assets.credentials.docker_registry_secret.all()
client.assets.credentials.password.all()
