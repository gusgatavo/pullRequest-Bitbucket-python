import json
import requests
from requests.auth import HTTPBasicAuth
import datetime
from dotenv import load_dotenv, dotenv_values


class PrbitbucketGo:

    config = ""
    url = ""
    headers = {}

    def __init__(self, workspace, repositorio, source, destination):
        self.source = source
        self.destination = destination

        self.__class__.url = f"https://api.bitbucket.org/2.0/repositories/{workspace}/{repositorio}/pullrequests"
        self.__class__.headers = {"Content-Type": "application/json"}
        load_dotenv()
        self.__class__.config = dotenv_values(".env")

    def get_title(self):
        now = datetime.datetime.now()
        return f"AutomaticPullRequest{now.strftime("%Y%m%d_%H%M%S")}_{self.source}To{self.destination}"

    def prexist(self):
        response = requests.get(
            self.__class__.url,
            auth=HTTPBasicAuth(
                self.__class__.config["USER"], self.__class__.config["PASSWORD"]
            ),
            headers=self.__class__.headers,
        )

        for pr in response.json()["values"]:
            if (
                pr["destination"]["branch"]["name"] == self.destination
                and pr["source"]["branch"]["name"] == self.source
            ):
                return False

        return True

    def gopr(self):

        if self.__class__.prexist(self):
            payload = json.dumps(
                {
                    "title": self.__class__.get_title(self),
                    "source": {"branch": {"name": f"{self.source}"}},
                    "destination": {"branch": {"name": f"{self.destination}"}},
                }
            )

            response = requests.post(
                self.__class__.url,
                auth=HTTPBasicAuth(
                    self.__class__.config["USER"], self.__class__.config["PASSWORD"]
                ),
                data=payload,
                headers=self.__class__.headers,
            )

            if response.status_code == 200 or response.status_code == 201:
                return {
                    "pull_request": response.json()["title"],
                    "url": response.json()["links"]["html"]["href"],
                    "menssage": "",
                }
        else:
            return {
                "pull_request": "",
                "url": "",
                "menssage": "Ya existe un Pull Request Pendiente de aprobación",
            }
