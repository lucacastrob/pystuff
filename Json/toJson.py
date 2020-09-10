import json

class JsonRobot:
  
    def __init__(self, posicion_r, sprite_robot, posicion_b, 
        sprite_bala, tipo_bala, posicion_e, sprite_explosion, tipo_exp, hp, robot_dir, turret_dir):
        '''Constructor de JsonRobot'''
        self.__x = []
        self.__x.append(posicion_r[0])
        self.__y = []
        self.__y.append(posicion_r[1])
        self.__spriter = sprite_robot
        self.__bx = posicion_b[0]
        self.__by = posicion_b[1]
        self.__spriteb = sprite_bala
        self.__ex = posicion_e[0]
        self.__ey = posicion_e[1]
        self.__spritee = sprite_explosion
        self.__hp = hp
        self.__rdir = robot_dir
        self.__tdir = turret_dir
        self.__tb = tipo_bala
        self.__te = tipo_exp

    def from_json(self, json_string):
        json_dict = json.loads(json_string)

    

    def to_json(self):
        '''Recibe posicion x e y de un robot (por separado), sprite del robot (image), una lista con las balas en el mapa 
        (disparadas por el propio robot), cantidad de vida del robot, ángulo del robot, ángulo de la 
        torreta, etc. (seguimos agregando)'''
        data = {}
        data_frame = {}
        for x in range(3):
            frame = str(x)
            data_frame[frame] = {'posicion_r' : [self.__x, self.__y], 'sprite_robot' : self.__spriter,
            'hp' : self.__hp, 'robot_dir' : self.__rdir, 'turret_dir' : self.__tdir} #guardo un dicc en data
            #print(data) 
        data['robots'] = data_frame
        data['balas'] = [{'tipo_bala' : self.__tb, 'posicion_b' : [self.__bx, self.__by], 
        'sprite_bullet' : self.__spriteb }]
        data['explosiones'] = {"tipo_explosion" : self.__te, 'posicion_e' : [self.__ex, self.__ey], 
        'sprite_explosion' : self.__spritee, }
        with open('data.json', 'w') as file:
            json.dump(data, file, indent=4)  
        return json.dumps(data)


json_string = {
    "robots": {
        "0": {
            "posicion": [
                100,
                200
            ],
            "angulo": 90,
            "hp": 100,
            "anguloarma": 90
        },
        "1": {
            "posicion": [
                500,
                500
            ],
            "angulo": 90,
            "hp": 100,
            "anguloarma": 90
        }
    },
    "balas": [
        {
            "tipobala": 0,
            "pos": [
                100,
                100
            ]
        }
    ],
    "explosiones": {
        "tipo": 0,
        "pos": [
            100,
            100
        ]
    }
},
{
    "robots": {}
},
{
    "robots": {}
},
{
    "robots": {}
},
{
    "robots": {}
},
{
    "robots": {}
}

JsonRobot.from_json(json_string)
robot1 = JsonRobot([4, 3], 'sprite_robot(ejemplo).png', [7, 10], 0, 'sprite_bala.png', [8, 11], 'sprite_explosion', 4000, 0, 90, 180)
robot1.to_json()

