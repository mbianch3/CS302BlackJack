class Hand():
  def __init__(self, user):
    self.user = user
    self.cardF = []
    self.cardV = []

  def get_user(self):
    return self.user
  
  def set_cardV(self, cards):
    self.cardV = cards

  def add_cardF(self, card):
    self.cardF.append(card)

  def add_cardV(self, card):
    self.cardV.append(card)

  def get_cardV(self):
    return self.cardV
  
  def get_cardF(self):
    return self.cardF

  def remove_last(self):
    cardF = self.cardF.pop()
    cardV = self.cardV.pop()
    return cardF, cardV
    