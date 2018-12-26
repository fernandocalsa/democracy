from py2neo.ogm import GraphObject, Property, RelatedTo, Label
from .political_party import PoliticalParty
from .institution import Institution

class Politician(GraphObject):
  name = Property()
  male = Label()
  female = Label()

  belongs = RelatedTo(PoliticalParty)
  mayor = RelatedTo(Institution)

  def __init__(self, name, gender):
    self.name = name
    if (gender == 'female'):
      self.female = True
    else:
      self.male = True

  def getPoliticalParty(self):
    politicalPartyRelationship = self.belongs._related_objects[0]
    return politicalPartyRelationship[0]

  def getInstitution(self):
    institution = self.mayor._related_objects[0]
    return institution[0]

  def getSalary(self):
    institution = self.mayor._related_objects[0]
    return institution[1]['salary']

  def serialize(self):
    institution = self.getInstitution()
    return {
      'id': self.__node__.identity,
      'name': self.name,
      'gender': 'male' if self.male else 'female',
      'politicalParty': self.getPoliticalParty().serialize(),
      'mayor': {
        'institution': institution.serialize(),
        'salary': self.getSalary()
      }
    }