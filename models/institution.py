from py2neo.ogm import GraphObject, Property, RelatedFrom, RelatedTo
from .region import Region

class Institution(GraphObject):
  __primarykey__ = "name"

  name = Property()
  
  mayor = RelatedFrom("Politician", "MAYOR")
  located = RelatedTo(Region)

  def __init__(self, name, region_name):
    self.name = name
    if (region_name):
      region = Region(region_name)
      self.located.add(region)

  def serialize(self):
    return {
      'name': self.name
    }