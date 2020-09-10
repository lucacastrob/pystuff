import json

class JsonRobot:
  
    def __init__(self, nx, ny, sprite_robot, bullet_pos_x, bullet_pos_y, 
        sprite_bala, sprite_explosion, hp, robot_dir, turret_dir):
        '''Constructor de JsonRobot'''
        self.__x = nx
        self.__y = ny 
        self.__spriter = sprite_robot
        self.__bx = bullet_pos_x
        self.__by = bullet_pos_y
        self.__spriteb = sprite_bala
        self.__spritee = sprite_explosion
        self.__hp = hp
        self.__tdir = turret_dir
 
    def hacerJson(self):
        '''Recibe posicion x e y de un robot (por separado), sprite del robot (image), una lista con las balas en el mapa 
        (disparadas por el propio robot), cantidad de vida del robot, ángulo del robot, ángulo de la 
        torreta, etc. (seguimos agregando)'''
        data = {}
        data['robots'] = []
        data['robots'].append({'pos_x' : self.__x, 'pos_y' : self.__y, 'pos_bullet_x' : self.__bx, 
        'pos_bullet_y' : self.__by, 'hp' : self.__hp, 'turret_dir' : self.__tdir}) #guardo un dicc en data
        #print(data) 
        with open('data.json', 'w') as file:
            json.dump(data, file, indent=4)  
        return json.dumps(data['robots'])
        
        

#robot1 = JsonRobot(4, 3, 7, 4, 4000, 90)
#robot1.hacerJson()

