from flask import Flask, request
from py2neo import Graph, Node, Relationship
from models.political_party import PoliticalParty
from controllers.createPolitician import createPolitician
app = Flask(__name__)
graph = Graph()

@app.route('/create', methods=['POST'])
def createPoliticianRoute():
  return createPolitician(request, graph)