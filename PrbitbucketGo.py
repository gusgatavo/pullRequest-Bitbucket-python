import json
import requests
from requests.auth import HTTPBasicAuth
import datetime
from dotenv import load_dotenv, dotenv_values


class PrbitbucketGo:

    config = ""
    url = ""
    headers = {}
    APPLICATION_JSON = "application/json"

    def __init__(self, workspace, repositorio, source, destination):
        """
        method constructor.
        input workspace corresponds in the worspace of the project
        input repositorio corresponds in the name of the project
        input source corresponds in the branch source
        input destination in the branch destionation
        """
        self.source = source
        self.destination = destination

        self.__class__.url = f"https://api.bitbucket.org/2.0/repositories/{workspace}/{repositorio}/pullrequests"
        self.__class__.headers = {
            "Content-Type": self.__class__.APPLICATION_JSON,
            "Accept": self.__class__.APPLICATION_JSON,
        }
        load_dotenv()
        self.__class__.config = dotenv_values(".env")

    def get_title(self):
        """
        method for generate the title the PR
        """
        now = datetime.datetime.now()
        return f"AutomaticPullRequest{now.strftime("%Y%m%d_%H%M%S")}_{self.source}To{self.destination}"

    def prexist(self):
        """
        method valid yes, is exist pull reques
        """
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
                return pr["id"]

        return 0

    def gopr(self):
        """
        method for create pull request.
        """

        idpr = self.__class__.prexist(self)

        if idpr == 0:
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
                    "idpr": response.json()["id"],
                    "approve": response.json()["links"]["approve"]["href"],
                    "url": response.json()["links"]["html"]["href"],
                    "message": "",
                }
        else:
            return {
                "pull_request": "",
                "idpr": idpr,
                "approve": "",
                "url": "",
                "message": "Ya existe un Pull Request Pendiente de aprobación",
            }

    def approve_pr(self, idpr):
        """
        method car approve pull request
        input idpr, hat is the pull request identification
        """

        response = requests.post(
            f"{self.__class__.url}/{idpr}/approve",
            auth=HTTPBasicAuth(
                self.__class__.config["USERAPPROVE"],
                self.__class__.config["PASSWORDAPPROVE"],
            ),
            headers={"Accept": self.__class__.APPLICATION_JSON},
        )

        if response.status_code == 200:
            return {"status": 200, "idpr": idpr, "approve": response.json()["approved"]}
        else:
            return {"status": 400, "idpr": idpr, "approve": False}

    def merge_pr(self, idpr):
        """
        method car merge pull request, the branch source with branch destination
        input idpr, hat is the pull request identification
        """

        peyload = {
            "type": "user",
            "message": "merge test",
            "close_source_branch": self.__class__.config["CLOSEBRANCH"],
            "merge_strategy": "",
        }

        response = requests.post(
            f"{self.__class__.url}/{idpr}/merge",
            auth=HTTPBasicAuth(
                self.__class__.config["USERAPPROVE"],
                self.__class__.config["PASSWORDAPPROVE"],
            ),
            headers=self.__class__.headers,
            json=peyload,
        )

        if response.status_code == 200:
            return {
                "idpr": idpr,
                "type": response.json()["type"],
                "title": response.json()["title"],
                "state": response.json()["state"],
                "message": {
                    "type": "",
                    "error": {"message": "", "detail": "", "data": {}},
                },
            }
        elif response.status_code == 555:
            return {
                "idpr": idpr,
                "type": "",
                "title": "",
                "state": "",
                "message": {
                    "type": response.json()["type"],
                    "error": {
                        "message": response.json()["error"]["message"],
                        "detail": response.json()["error"]["detail"],
                        "data": response.json()["error"]["data"],
                    },
                },
            }
        else:
            return {
                "idpr": idpr,
                "type": "",
                "title": "",
                "state": "",
                "message": {
                    "type": "409",
                    "error": {
                        "message": "Conflicto en la ejecución",
                        "detail": "",
                        "data": "",
                    },
                },
            }
