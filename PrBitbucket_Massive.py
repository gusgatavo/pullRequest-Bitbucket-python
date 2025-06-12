from PrbitbucketGo import PrbitbucketGo
from tqdm.rich import tqdm
import sys

withMerge = "" if (len(sys.argv) - 1) == 0 else sys.argv[1]
arrayResult = []


def statusmergestr(code):
    if code == 200:
        return "Approved"
    elif code == 400:
        return "Error Approved"
    elif code == "":
        return "Merge"
    else:
        return "Error Merge"


with open("./pullRequest.txt") as file:
    lines = file.readlines()
    countbar = len(lines) * 3 if withMerge == "merge" else len(lines)

    with tqdm(total=countbar, desc="Procesando Pull Requests", unit="PR") as pbar:

        for line in lines:

            value = line.strip().split(",")
            execName = value[0] + "/" + value[1] + "/" + value[2] + "/" + value[3]
            pbar.set_postfix(current=execName)

            object = PrbitbucketGo(value[0], value[1], value[2], value[3])
            response = object.gopr()

            if withMerge == "merge":
                statusMerge = ""
                responseAppove = object.approve_pr(response["idpr"])
                statusMerge = statusmergestr(responseAppove["status"])
                pbar.update(1)

                if statusMerge == "Approved":
                    responseMerge = object.merge_pr(responseAppove["idpr"])
                    statusMerge = statusmergestr(responseMerge["message"]["type"])
                    pbar.update(1)

            else:
                statusMerge = "Created"

            stringResult = f"{execName} -- {response["idpr"]} -- {statusMerge} -- {response["pull_request"]} -- {response["url"]} -- {response["message"]}"
            arrayResult.append(stringResult)

            pbar.update(1)


with open("result.txt", "w") as fileResult:
    for line in arrayResult:
        fileResult.writelines(line + "\n")

print()
print("✅ finished processd...")
