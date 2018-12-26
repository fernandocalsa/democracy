from py2neo.ogm import GraphObject, Property, RelatedFrom

class PoliticalParty(GraphObject):
  __primarykey__ = "name"

  name = Property()

  belongs = RelatedFrom("Politician", "BELONGS")

  def __init__(self, name):
    self.name = name

  def serialize(self):
    return {
      'name': self.name
    }