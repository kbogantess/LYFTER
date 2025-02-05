#Herencia múltiple

class WalkerMixin:
  def walk(self):
    print("I'm walking!")

class RunnerMixin:
  def run(self):
    print("I'm running!")

class FlyerMixin:
  def fly(self):
    print("I'm flying!")


class SuperMan(WalkerMixin, RunnerMixin, FlyerMixin):
  pass

clark_kent = SuperMan()
clark_kent.walk()
clark_kent.run()
clark_kent.fly()