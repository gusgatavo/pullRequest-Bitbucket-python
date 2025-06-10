import sys
from PrbitbucketGo import PrbitbucketGo
import time
from tqdm.rich import tqdm

print(
    "El valor campo 1 es:", sys.argv[1], "El valor del argumento dos es :", sys.argv[2]
)

workspace = sys.argv[1]
repositorio = sys.argv[2]
source = sys.argv[3]
destination = sys.argv[4]

print("\nCreando Pull Request...\n")
for _ in tqdm(range(30), desc="Procesando", bar_format="{l_bar}{bar}| {n_fmt}/{total_fmt}", ncols=60):
    time.sleep(0.05)  # Simula actividad

object = PrbitbucketGo(workspace, repositorio, source, destination)
response = object.gopr()

print()
if response["menssage"] == "":
    print(
        f"✅ Se ha creado el Pull Request '{response['pull_request']}' sin problemas.\n🔗 Link: {response['url']}"
    )
else:
    print(f"❌ Error: {response['menssage']}")
