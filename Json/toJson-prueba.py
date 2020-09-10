import json

class JsonRobot:
  
    def __init__(self):
        '''Constructor de JsonRobot'''
        self.__x = []
        self.__y = []
        self.__spriter = []
        self.__bx = []
        self.__by = []
        self.__spriteb = []
        self.__ex = []
        self.__ey = []
        self.__spritee = []
        self.__hp = []
        self.__rdir = []  
        self.__tdir = []    
        self.__tb = []
        self.__te = []


    def from_json(self, json_string):
        '''Recibe un JSON por parámetro y guarda en variables sus diferentes atributos.'''
        self.__json_dict = json_string
        #for x in range(len(self.__json_dict)): #recorre los diferentes frames
            #frame = self.__json_dict[x]
        for frame in self.__json_dict: #recorre los diferentes frames
            for r in range(len(frame["robots"])): #recorre "robots"
                self.__x.append(frame["robots"][str(r)]["posicion"][0])
                self.__y.append(frame["robots"][str(r)]["posicion"][1])
                self.__spriter.append("hull" + str(r) +".png")
                self.__rdir.append(frame["robots"][str(r)]["angulo"])
                self.__hp.append(frame["robots"][str(r)]["hp"])
                self.__tdir.append(frame["robots"][str(r)]["anguloarma"])
            for b in range(len(frame["balas"])): #recorre "balas"
                self.__tb.append(frame["balas"][b]["tipobala"])
                self.__bx.append(frame["balas"][b]["pos"][0])
                self.__by.append(frame["balas"][b]["pos"][1])
                self.__spriteb.append("bala" + str(b) + ".png")
            for e in range(len(frame["explosiones"])): #recorre "explosiones"
                self.__te.append(frame["explosiones"][str(e)]["tipo"])
                self.__ex.append(frame["explosiones"][str(e)]["pos"][0])
                self.__ey.append(frame["explosiones"][str(e)]["pos"][1])
                self.__spritee.append("explosion" + str(e) + ".png")
    
     
    def to_json(self):
        '''En base a los atributos obtenidos del JSON, elabora uno nuevo agregando
        datos según necesario y lo devuelve.'''
        lista_frames = []
        dicc = {}
        dicc["HEADER"] = "HEADER" #agrega el header para js
        dicc["robots"] = {}
        for x in range(2):
            dicc["robots"]["id_hull" + str(x)] = self.__spriter[x] #establece los sprites
        dicc["balas"] = {}
        dicc["explosiones"] = {}
        for tde in range(1): #establece los sprites según el tipo de bala/explosión.
            dicc["balas"]["id_bala" + str(tde)] = self.__spriteb[tde]
            dicc["explosiones"]["id_explosion" + str(tde)] = self.__spritee[tde]
        lista_frames.append(dicc) #agrega al JSON
        for frames in range(len(self.__json_dict)): #recorre los frames
            frame = {}
            frame["robots"] = {}
            for robt in range(len(self.__json_dict[frames]["robots"])): #agrega atributos a los dif. robots
                frame["robots"][str(robt)] = {}
                frame["robots"][str(robt)]["posicion"] = [self.__x[robt], self.__y[robt]]
                frame["robots"][str(robt)]["angulo"] = self.__rdir[robt]
                frame["robots"][str(robt)]["hp"] = self.__hp[robt]
                frame["robots"][str(robt)]["anguloarma"] = self.__tdir[robt]
            frame["balas"] = []
            diccionario_ = {}
            frame["balas"].append(diccionario_)
            for nbala in range(len(self.__json_dict[frames]["balas"])): #agrega atrib. a las dif. balas
                frame["balas"][nbala][str(nbala)] = {"tipobala" : self.__tb[nbala], 
                "pos" : [self.__bx[nbala], self.__by[nbala]] }   
            frame["explosiones"] = {}
            for exp in range(len(self.__json_dict[frames]["explosiones"])): #agrega atrib. a las dif. expl.
                frame["explosiones"][str(exp)] = {}
                frame["explosiones"][str(exp)]["tipo"] = self.__te[exp]
                frame["explosiones"][str(exp)]["pos"] = [self.__ex[exp], self.__by[exp]]
            lista_frames.append(frame)
        with open('data.json', 'w') as file: #abre el archivo "data.json" con permisos "w"
            json.dump(lista_frames, file, indent=4)  #dumpea el json en el archivo
        return json.dumps(lista_frames)

#testing
json_string = [{
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
        "0": {
            "tipo": 0,
            "pos": [
                100,
                100
            ]
        }
    }
    },
    {
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
        "0": {
            "tipo": 0,
            "pos": [
                100,
                100
            ]
        }
    }

}]

robot1 = JsonRobot()
JsonRobot.from_json(robot1, json_string)
robot1.to_json()

