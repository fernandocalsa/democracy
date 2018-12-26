from py2neo.ogm import GraphObject, Property, RelatedTo, Label
from .political_party import PoliticalParty
from .institution import Institution

class Politician(GraphObject):
  name = Property()
  male = Label()
  female = Label()

  belongs = RelatedTo(PoliticalParty)
  mayor = RelatedTo(Institution)