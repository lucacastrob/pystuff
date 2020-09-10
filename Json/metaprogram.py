import json

class jorge:
  
    def __init__(self, nx, ny, bullet_pos_x, bullet_pos_y, hp, turret_dir):
        self.__x = nx
        self.__y = ny 
        self.__bx = bullet_pos_x
        self.__by = bullet_pos_y
        self.__hp = hp
        self.__tdir = turret_dir
 
    def hacerJson(self):
        data = {}
        data['clients'] = []
        data['clients'].append({'pos_x' : self.__x, 'pos_y' : self.__y, 'pos_bullet_x' : self.__bx, 
        'pos_bullet_y' : self.__by, 'hp' : self.__hp, 'turret_dir' : self.__tdir}) #guardo un dicc en data
        print(data) #para testeo
        with open('data.json', 'w') as file:
            json.dump(data, file, indent=4)  
        return json.dumps(data['clients'])
        
        

robot1 = jorge(4, 3, 7, 4, 4000, 90)
robot1.hacerJson()

