#Cree las siguientes clases:
#Head
#Torso
#Arm
#Hand
#Leg
#Feet

#Ahora cree una clase de Human y conecte todas las clases de manera lógica por medio de atributos.
#Por ejemplo (este código esta incompleto, pero describe la idea):

#class Torso:
	#def __init__(self, head, right_arm, ...):
		#self.head = head
		#self.right_arm = right_arm
		#...

#class Arm:
	#def __init__(self, hand):
		#self.hand = hand


#right_hand = Hand()
#right_arm = Arm(right_hand)
#torso = (head, right_arm)
#"""


class Head:
    def __init__(self, eyes, mouth, nose, ears, hair_color):
        self.eyes = eyes
        self.mouth = mouth
        self.nose = nose
        self.ears = ears
        self.hair_color = hair_color

class Arm:
    def __init__(self, hand):
        self.hand = hand

class Hand:
    def __init__(self, fingers):
        self.fingers = fingers

class Leg:
    def __init__(self, foot):
        self.foot = foot

class Foot:
    def __init__(self, toes):
        self.toes = toes

class Torso:
    def __init__(self, head, left_arm, right_arm, left_leg, right_leg):
        self.head = head
        self.left_arm = left_arm
        self.right_arm = right_arm
        self.left_leg = left_leg
        self.right_leg = right_leg

class Human:
    def __init__(self):
        self.head = Head(eyes=2, mouth=1, nose=1, ears=2, hair_color="brown")
        self.left_hand = Hand(fingers=5)
        self.right_hand = Hand(fingers=5)
        self.left_arm = Arm(hand=self.left_hand)
        self.right_arm = Arm(hand=self.right_hand)
        self.left_foot = Foot(toes=5)
        self.right_foot = Foot(toes=5)
        self.left_leg = Leg(foot=self.left_foot)
        self.right_leg = Leg(foot=self.right_foot)
        self.torso = Torso(head=self.head, left_arm=self.left_arm, right_arm=self.right_arm, left_leg=self.left_leg, right_leg=self.right_leg)