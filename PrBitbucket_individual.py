import sys
from PrbitbucketGo import PrbitbucketGo
from barprocess import barprocess

print(
    "El valor campo 1 es:", sys.argv[1], "El valor del argumento dos es :", sys.argv[2]
)

workspace = sys.argv[1]
repositorio = sys.argv[2]
source = sys.argv[3]
destination = sys.argv[4]

print("\nCreando Pull Request...\n")
barprocess()

object = PrbitbucketGo(workspace, repositorio, source, destination)
response = object.gopr()


if response["message"] == "":
    print(
        f"✅ Se ha creado el Pull Request con id {response['idpr']} y nombre '{response['pull_request']}' sin problemas.\n🔗 Link: {response['url']}"
    )
    print()
else:
    print(f"❌ Error: {response['message']}, con id {response['idpr']}")


pr_approved = (
    input("¿Sea realizar la aprobación del Pull Request creado? Si (Y) - No (N) ")
    .strip()
    .upper()
)

if pr_approved == "Y" or pr_approved == "y":
    print("Yes")
    print()
    barprocess()

    response_approved = object.approve_pr(response["idpr"])
    print(f"Se a aprobado el PR {response_approved['idpr']}")
    response_merge = object.merge_pr(response_approved["idpr"])
    print(f"Se a mergeado el PR {response_merge["idpr"]}")
    print("✅ finished process...")
elif pr_approved == "N" or pr_approved == "n":
    print("No")
else:
    print("Respuesta no valida")
