from flask import Flask, request
from py2neo import Graph, Node, Relationship
from models.political_party import PoliticalParty
from controllers.createPolitician import createPolitician
from controllers.getPoliticians import getPoliticians
from controllers.updatePolitician import updatePolitician
from controllers.importPoliticians import importPoliticians

app = Flask(__name__)
graph = Graph()

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