#Define enemy data
enemies = [
    #[hp, armour, armourThreshold, Name]
    (150, 70, 0.5, "Light Swat"),
    (150, 170, 0.5, "Heavy Swat"),
    (150, 140, 0.5, "Taser/Nader"),
    (150, 0, 0, "Cloaker"),
    (160, 180, 1, "Shield")
    ]


# Functions
def damageCalc(shots, HP, AP, APMult, damage, critMult):
    while True:
        if (HP <= 0):
            break
        elif (AP <= 0):
            HP -= damage * critMult
            #print ('Shot {}. HP: {}'.format(shots,HP))
        elif (AP > 0):
            AP -= damage
            HP -= APMult * damage * critMult
            #print('Shot {}. AP: {}. HP: {}'.format(shots,AP,HP))
        shots += 1
    return shots
        
def NoEdge(HP, AP, APThreshold, enemy):
    shots = 0
    APMult = APen - APThreshold
    APMult = max([0, APMult])

    shots = damageCalc(shots, HP, AP, APMult, damage, critMult)
    
    print ("{} killed without Edge in {} shots.".format(enemy,shots))

def Edge(HP, AP, APThreshold, enemy):
    shots = 0
    APMult = APen - APThreshold
    APMult = max([0, APMult])
        
    shots = damageCalc(shots, HP, AP, APMult, damage * 1.1, critMult)
    
    print ("{} killed with Edge in {} shots.".format(enemy,shots))

def CuttingShot(HP, AP, APThreshold, enemy):
    shots = 0
    APMult = APen - APThreshold + 0.1
    APMult = max([0, APMult])
    
    shots = damageCalc(shots, HP, AP, APMult, damage * 1.1, critMult)
    
    print ("{} killed with Cutting Shot in {} shots.".format(enemy,shots))

while True:
    print("-----------------------------------------")
    try:
        #Gather weapon data
        damage = float(input('Weapon damage: '))
        critMult = float(input('Crit multiplier: '))
        APen = float(input('AP Value: '))
        print("")
        
        for enemy in enemies:
            NoEdge(*enemy)
            Edge(*enemy)
            CuttingShot(*enemy)
            print("")

    except Exception as e:
        print(e)
