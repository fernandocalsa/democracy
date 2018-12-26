from py2neo.ogm import GraphObject, Property, RelatedTo, Label
from .political_party import PoliticalParty
from .institution import Institution

class Politician(GraphObject):
  name = Property()
  male = Label()
  female = Label()

  belongs = RelatedTo(PoliticalParty)
  mayor = RelatedTo(Institution)

  def __init__(self, name, gender, political_party_name, region_name, institution_name, charge, salary):
    self.name = name
    if (gender == 'female'):
      self.female = True
    else:
      self.male = True

    if (political_party_name):
      political_party = PoliticalParty(political_party_name)
      self.belongs.add(political_party)

    if (institution_name and charge):
      institution = Institution(institution_name, region_name)
      if (charge == 'Alcalde'):
        self.mayor.add(institution, salary=salary)

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