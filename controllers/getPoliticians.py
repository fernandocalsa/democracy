from flask import jsonify
from models.politician import Politician

def getPoliticians(request, graph):
  limit = int(request.args.get('limit', 50))
  politicians = list(Politician.match(graph).limit(limit))
  print(politicians)
  politiciansSerialize = list(map(lambda politician: politician.serialize(), politicians))
  return jsonify(politiciansSerialize)