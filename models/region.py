from py2neo.ogm import GraphObject, Property, RelatedFrom

class Region(GraphObject):
  __primarykey__ = "name"

  name = Property()

  def __init__(self, name):
    self.name = name

  located = RelatedFrom("Institution", "LOCATED")