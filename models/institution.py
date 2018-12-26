from py2neo.ogm import GraphObject, Property, RelatedFrom, RelatedTo
from .region import Region

class Institution(GraphObject):
  __primarykey__ = "name"

  name = Property()
  
  mayor = RelatedFrom("Politician", "MAYOR")
  located = RelatedTo(Region)

  def __init__(self, name):
    self.name = name

  def serialize(self):
    return {
      'name': self.name
    }