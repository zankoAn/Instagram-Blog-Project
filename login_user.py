import aiohttp

import asyncio

from datetime import datetime

from config import Config      # ==> local config file


async def login_user(session, username: str, password: str) -> bool:

    url, headers = Config().shared_data()
    
    try:
        print("Start fetching data from Shard_data_url...\n")

        async with session.get(url=url, headers=headers) as resp:
            data = await resp.json()

            csrf_token = data.get("config").get("csrf_token")
            rollout_hash = data.get("rollout_hash")

            if csrf_token and rollout_hash:
                url, headers, data = Config().login(rollout_hash ,csrf_token, username, password, 0, int(datetime.now().timestamp()))

                print("Waiting for the response to the login request...\n")
                async with session.post(url=url, headers=headers, data=data) as r:
                    data = await r.json()

                    for k,v in data.items():
                        print(k,v)
    
                    if data.get("authenticated") == True:
                        return True
                    else:
                        return False   
    except Exception as err:
        print(f"New error: ==> {err}" )


async  def main():
    async with aiohttp.ClientSession() as session:
        login_task = asyncio.create_task(login_user(session, "Username", "Password"))
        response = await login_task
        if response:
            print("\nYou have successfully logged in")
        else:
            print("\nWrong username or password")

asyncio.run(main())
