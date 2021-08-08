class Config:
    """
        Configure the required headers for the required URLs
    """

    def __init__(self):
        self.user_agent = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36"
    

    def shared_data(self) -> tuple:
        """
            GET data nedded for header login and etc.. 
            There is a lot of data here(current url) that you can use wherever you need it.

            Returns
            -------
            Tuple
                A tuple of shared data url and headers
        """

        url = "https://www.instagram.com/data/shared_data/"

        headers = {
            "user-agent":self.user_agent,
        }

        return url, headers


    def login(self, rollout_hash: str, csrf: str, username: str, password: str, version: int = 0, time: int = 0) -> tuple:
        """
            Headers neded for login 

            Returns
            -------
            Tuple
                A tuple of url, headers and data for login page
        """

        url = "https://www.instagram.com/accounts/login/ajax/"

        headers = {
            "accept-encoding":"gzip, deflate",
            "accept-language":"en-US,en;q=0.9",
            "origin":"https://www.instagram.com",
            "user-agent":self.user_agent,
            "referer":"https://www.instagram.com/accounts/login/",            
            "sec-fetch-site":"same-origin",
            "sec-fetch-mode":"cors",
            "x-instagram-ajax": rollout_hash,
            "X-CSRFToken":csrf,
            "x-requested-with":"XMLHttpRequest",
        }

        data = {
            "username":username,
            "enc_password":f"#PWD_INSTAGRAM_BROWSER:{version}:{time}:{password}",
            "queryParams":{},
            "optIntoOneTap":"false",
            "stopDeletionNonce":"",
            "trustedDeviceRecords":{}
        }

        return url, headers, data

