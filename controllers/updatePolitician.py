from flask import jsonify
from models.politician import Politician
from models.political_party import PoliticalParty

def updatePolitician(request, graph):
  politician_id = request.form.get('id')
  politician = Politician.match(graph).where(f"ID(_) = {politician_id}").first()
  if (not(politician)):
    return jsonify({
      'error': 'Politician not found'
    })
  political_party_name = request.form.get('political_party')
  politician.belongs.clear()
  political_party = PoliticalParty(political_party_name)
  politician.belongs.add(political_party)
  graph.push(politician)
  return jsonify(politician.serialize())