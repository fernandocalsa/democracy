import time
from flask import Flask, request, jsonify
from py2neo import Graph, Node, Relationship
from models.political_party import PoliticalParty
from controllers.createPolitician import createPolitician
from controllers.getPoliticians import getPoliticians
from controllers.updatePolitician import updatePolitician
from controllers.importPoliticians import importPoliticians

app = Flask(__name__)
app.config.from_object('settings.Config')

neo4j = app.config['NEO4J'] if app.config['NEO4J'] else None
print(neo4j)
def get_db_connection():
  retries = 20
  while True:
    try:
      return Graph(neo4j)
    except Exception:
      print(retries)
      if retries == 0:
        raise Exception
      retries -= 1
      time.sleep(5)

graph = get_db_connection()

@app.route('/')
def index():
  return getPoliticians(request, graph)

@app.route('/create', methods=['POST'])
def createPoliticianRoute():
  return createPolitician(request, graph)

@app.route('/update', methods=['PUT'])
def update():
  return updatePolitician(request, graph)

@app.route('/import', methods=['POST'])
def importData():
  return importPoliticians(request, graph)