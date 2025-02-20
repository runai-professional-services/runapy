import asyncio

from runai.configuration import Configuration
from runai.api_client import AsyncApiClient
from runai.runai_client import RunaiClient


async def list_projects() -> None:
    config = Configuration(
        client_id="YOUR_CLIENT_ID",
        client_secret="YOUR_CLIENT_SECRET",
        runai_base_url="https://org.run.ai",
    )

    # Create async client
    async with RunaiClient(AsyncApiClient(config)) as client:
        try:
            # List projects with pagination
            offset = 0
            limit = 10
            while True:
                # Get projects page
                response = await client.organizations.projects.get_projects()

                # Print projects in this page
                print(response.status_code)
                print(response.data)
                projects = response.data["projects"]
                if not projects:
                    break

                print(f"\nProjects (offset={offset}, limit={limit}):")
                for project in projects:
                    print(f"- {project['name']} (ID: {project['id']})")
                    if project["description"]:
                        print(f"  Description: {project['description']}")

                # Move to next page
                offset += limit
                if len(projects) < limit:
                    break

        except Exception as e:
            print(f"Failed to list projects: {e}")
            raise


async def main():
    await list_projects()


if __name__ == "__main__":
    asyncio.run(main())
