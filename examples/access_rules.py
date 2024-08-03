if __name__ == "__main__":

    client = RunaiClient(
        realm=REALM,
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        runai_base_url=BASE_URL,
        cluster_id=CLUSTER_ID
    )  

    # First, get roles map to know which type of role to put in accessrule.create (role_id)
    print(client.roles.get_roles_name_to_id_map())
    
    # List all access rules
    print(client.access_rules.all())
    
    # Create an access rule with L1 researcher permissions to cluster scope
    print(client.access_rules.create(
        subject_id="ofir.eldar@run.ai",
        subject_type="user",
        role_id=5,
        scope_id=CLUSTER_ID,
        scope_type="cluster"
    ))