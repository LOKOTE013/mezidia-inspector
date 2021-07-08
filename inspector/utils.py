from gidgethub import apps

from .config import GH_APP_ID, GH_PRIVATE_KEY


async def get_token(event, gh):
    if 'installation' in event.data:
        installation_id = event.data['installation']['id']
        token = await apps.get_installation_access_token(
            gh,
            installation_id=installation_id,
            app_id=GH_APP_ID,
            private_key=GH_PRIVATE_KEY
        )
        return token
    else:
        # For testing
        return None