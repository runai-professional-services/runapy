from runai.client import RunaiClient

# Configure connectivity to your run:ai application
client = RunaiClient(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    runai_base_url=BASE_URL,
    cluster_id=CLUSTER_ID
)

# Get all templates
print(client.templates.all())

# Print all environments
print(client.environment.all())

# Get the jupyter-lab environment resource
jupyter_lab = client.environments.get_by_name(environment_name="jupyter-lab")
jupyter_lab_id = jupyter_lab['meta']['id']

# Get the cpu-only compute resource
cpu_only = client.compute.get_by_name(compute_name="cpu-only")
cpu_only_id = cpu_only['meta']['id']

# Create a template named my-template with the compute cpu-only and the jupyter_lab environment
print(client.templates.create(
    name="my-template",
    scope="cluster",
    assets = {
        "environment": jupyter_lab_id,
        "compute": cpu_only_id
    }
))

# Get template asset ID by name
my_template = client.templates.get_by_name(template_name="my-template")
my_template_id = my_template['meta']['id']

# Get the compute asset ID by name
half_gpu = client.compute.get_by_name(compute_name="half-gpu")
half_gpu_id = half_gpu['meta']['id']

# Update a template named my-template with the compute half-gpu and the jupyter_lab environment
print(client.templates.update(
    name="my-template",
    asset_id=my_template_id,
    assets = {
        "environment": jupyter_lab_id,
        "compute": half_gpu_id
    }
))

# Delete a template
print(client.templates.delete(
    asset_id=my_template_id
))