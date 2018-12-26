from flask import jsonify
from models.political_party import PoliticalParty
from models.politician import Politician
from models.institution import Institution
from models.region import Region

def createPolitician(request, graph):
  # Get required variables
  politician_name = request.form.get('name')
  political_party_name = request.form.get('political_party')
  gender = request.form.get('gender')
  charge = request.form.get('charge')
  salary = request.form.get('salary')
  salary = float(salary) if salary else 0.0
  institution_name = request.form.get('institution')
  region_name = request.form.get('region')
  if (
    not(politician_name) or
    not(political_party_name) or
    not(charge) or
    not(region_name) or
    not(institution_name)
  ):
    return jsonify({
      'error': 'name, political_party, institution and charge are required'
    })


  # Create politician
  politician = Politician(
    politician_name,
    gender,
    political_party_name,
    region_name,
    institution_name,
    charge,
    salary
  )
  
  graph.push(politician)

  return jsonify(politician.serialize())