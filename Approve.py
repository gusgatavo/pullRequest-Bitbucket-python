import sys
from PrbitbucketGo import PrbitbucketGo

workspace = sys.argv[1]
repositorio = sys.argv[2]
source = sys.argv[3]
destination = sys.argv[4]
idpr = sys.argv[5]

object = PrbitbucketGo(workspace, repositorio, source, destination)
response = object.approve_pr(idpr)

print(response)