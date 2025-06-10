from PrbitbucketGo import PrbitbucketGo
from tqdm.rich import tqdm

arrayResult = []

with open("./pullRequest.txt") as file:
    lines = file.readlines()
    with tqdm(total=len(lines), desc="Procesando Pull Requests", unit="PR") as pbar:

        for line in lines:

            value = line.strip().split(",")
            execName = value[0] + "/" + value[1] + "/" + value[2] + "/" + value[3]
            pbar.set_postfix(current=execName)

            object = PrbitbucketGo(value[0], value[1], value[2], value[3])
            response = object.gopr()
            
            stringResult = f"{execName} -- {response["pull_request"]} -- {response["url"]} -- {response["menssage"]}"
            arrayResult.append(stringResult)
            
            pbar.update(1)


with open("result.txt", "w") as fileResult:
    for line in arrayResult:
        fileResult.writelines(line + "\n")

print("✅ Process finished...")
