from py2neo.ogm import GraphObject, Property, RelatedFrom

class Region(GraphObject):
  __primarykey__ = "name"

  name = Property()

  located = RelatedFrom("Institution", "LOCATED")