class Plants():
    name = ''
    def flower(self):
        return True
    def thorns(self):
        return ''
    
class Rose_plant(Plants):
    def flower(self):
        return self.name + ' has flower'
    def thorns(self):
        return self.name + ' has thorns'
    
class Hibiscus_plant(Plants):
    def flower(self):
        return self.name + ' has flower'
    def thorns(self):
        return self.name + ' has no thorns'
    
class Grass(Plants):
    def flower(self):
        return self.name + ' has no flower'
    def thorns(self):
        return self.name + ' has no thorns'
    
    
    
def show_details(plant):
    print(plant.name)
    print(plant.flower())
    print(plant.thorns())
    
rose = Rose_plant()
rose.name = 'rose'
show_details(rose)

print()

hibiscus = Hibiscus_plant()
hibiscus.name = 'hibiscus'
show_details(hibiscus)

print()

grass = Grass()
grass.name = 'grass'
show_details(grass)