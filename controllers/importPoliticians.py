import csv
import io
from flask import jsonify
from models.politician import Politician

def importPoliticians(request, graph):
  f = request.files['file']
  if not f:
    return jsonify({
      'error': 'No file'
    })
  stream = io.StringIO(f.stream.read().decode("UTF8"), newline=None)
  csv_input = csv.reader(stream, delimiter=";")
  next(csv_input)
  politiciansNum = 0
  for row in csv_input:
    if (politiciansNum == 0):
      tx = graph.begin()
    politician_name = row[0]
    gender = 'male' if row[3] == 'Hombre' else 'female'
    political_party_name = row[1]
    charge = row[4]
    try:
      salary = float(row[8].replace(',', '.'))
    except ValueError:
      salary = 0.0
    institution_name = row[6]
    region_name = row[7]

    if (
      politician_name and
      political_party_name and
      region_name and
      institution_name and
      charge
    ):
      politician = Politician(
        politician_name,
        gender,
        political_party_name,
        region_name,
        institution_name,
        charge,
        salary
      )
      tx.create(politician)
      politiciansNum += 1

  tx.commit()
  return jsonify(f'Imported {politiciansNum} records')