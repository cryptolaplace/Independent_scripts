'''
Official:

Think about spacing as you start to build your town. 
This game is all about minimizing travel time for your workers and maximizing efficiency. 
Pay attention to things like how far your Farmer needs to travel from house to field, and how often he needs to water the crops.

Your first milestone goal will always be to produce gasoline before you run out. 

Your town-building adventure will always start with the following items:
Farmhouse (including a Farmer)
Silo
2 Wheat Fields
Well
Wood Shed (with 9 Wood)
Some Dirt Roads
Builder House
Fuel Storage (filled with gasoline)
Trade Depot
$25,000 cash

Initial Wages - You’ll come into the game with three paid employees in your town.
Builder - $20/minute
Trade Depot - $20/minute
Farmer - $10/minute

Hopefully, you have built your town somewhere near a city. If not, you may want to consider starting over with a different location while it’s still early.

money-making strategy：
Natural value of the land - Make the most of the land you have chosen. If that land is a forest, you’ll want to focus first on the natural resources that are already plentiful there: Trees. For more information, check out the USING NATURAL RESOURCES page.
Ultimate production goals - Try to think ahead to the end of the competition, when you’ll be a contender for one of the top spots on the leaderboard. What will you be producing? How can you lay a groundwork now that will support this method of mass production in the future? For example, if you’re planning on making cakes, you’ll probably want to start with a solid system that produces and distributes flour, one of the most crucial ingredients in cake-making.
Proximity to a city - If you are in a location that is further away from a city, you’ll need to plan very carefully for either higher gasoline costs or longer travel time for your trade deliveries. Perhaps your goal is to eventually use a Freight Pier to deliver 100 goods at a time instead of 10. In this case, you’ll want to eventually build a system that puts even larger focus on storage than gasoline production.

Pick a Path
There are 2 main methods for increasing your value-per-trade early in the game. Once you have formulated a basic strategy based on the above considerations, it’s time to pick one to start. Eventually you will need a combination of both, but an initial focus must first be decided.
Ranching (Livestock raising)
Windmills (Milled production)


'''


init_resource = {'gas':40, 'wheat':10, 
                'wheat_f':2, 'silo':1, 'wood_s':1, 'fuel_s':1, 'pond':2, 'well':1,
                'farmer':1, 'builder':1,}

# human resource
cost_permin = {'farmer': 10, 'builder': 20, 'trader': 20, 'miller': 50, 'lumberjack': 50}

# storage
storage = {'silo': 20, 'fuel_s': 40, 'wood_s': 10}

# production
mature_time = {'wheat': 20, }
water_need = {'wheat': 3, 'cotton': 4, 'sugar': 8}  
miller = {'flour': {'wheat': 5, 'wood': 3}, 'sugar': {'sugarcane':6, 'wood':3}, 'salt':{'brine':6, 'wood':3}}

# economic 
city_score = {'blue_steel': [270950,6800], 'cake': [178050,4475], 'baguette': [91300,1472], 'pinot_noir': [57200,1008], 'pumpkin_pie': [49750,816], 
'batter': [48700,450], 'steel': [47000,768], 'cabernet_sauvignon': [42000,736], 'uniforms': [34450,560], 'dough': [29150,270], 'chardonnay': [27950,496], 
'candy_canes': [25700,183], 'wool_yarn': [24250,225], 'butter': [16250,153], 'bread': [15550,153], 'winebottle': [12800,126], 'oak_barrel': [5500,63], 'chromium': [4600,54], 
'iron': [4600,54], 'limestone': [4600,54], 'wool': [4550,24], 'milk': [4000,20], 'cotton_yarn': [3250,16], 'sugar': [3150,16], 'pinot_noir_grapes': [2670,20], 'salt': [2550,16], 
'flour': [2250,12], 'jet_fuel': [1900,27], 'cabernet_grapes': [1820,16], 'eggs': [1650,12], 'gasoline': [1450,8], 'lumber': [1350,8], 'pumpkin': [1000,2], 'silica': [1000,2], 
'chardonnay_grapes': [810,8], 'peppermint': [800,8], 'petroleum': [450,4], 'sugarcane': [400,1], 'cotton': [350,1], 'feed': [340,1], 'brine': [300,1], 'wheat': [300,1], 
'oak_wood': [250,1], 'wood': [250,1], 'water_drum': [150,1], 'energy': [50,1], 'crude_oil': [50,1], 'water': [50,1]}

# products
products = {
        'blue_steel' : {'steel':5,'energy':10,'uniforms':1},
        'cake' : {'batter':3, 'sugar':10, 'energy':3},
        'baguette' : {'dough':2,'butter':2,'wood':2},
        'pinot_noir' : {'pinot_noir_grapes':6, 'winebottle':1, 'oak_barrel':1},
        'pumpkin_pie':{'pumpkin':10,'sugar':10,'eggs':5},
        'batter' : {'flour':5,'eggs':3,'butter':2},
        'steel' : {'iron':10,'energy':5, 'water_drum':5},
        'cabernet_sauvignon':{'cabernet_grapes':5,'winebottle':1,'oak_barrel':1},
        'uniforms':{'cotton_yarn':3,'wool_yarn':1,'energy':3},
        'dough':{'flour':5,'eggs':1,'butter':1},
        'chardonnay':{'chardonnay_grapes':3,'winebottle':1,'oak_barrel':1},
        'candy_canes':{'peppermint':4,'sugar':6,'energy':10},
        'wool_yarn':{'wool':5,'lumber':1,'energy':1},
        'butter':{'milk':2,'salt':2,'sugar':1},
        'bread':{'flour':4,'milk':1,'salt':1},
        'winebottle':{'silica':3,'chromium':1,'limestone':1},
        'oak_barrel':{'oak_wood':3,'iron':1,'energy':1},
        'chromium':{'lumber':3,'energy':3,'water_drum':2},
        'iron':{'lumber':3,'energy':3,'water_drum':2},
        'limestone':{'lumber':3,'energy':3,'water_drum':2},
        'wool':{'feed':9,'wood':1,'water':5},
        'milk':{'feed':8,'wood':1,'water':3},
        'cotton_yarn':{'cotton':5,'lumber':1,'energy':1},
        'sugar':{'sugarcane':6,'wood':3},
        'pinot_noir_grapes':{'water':2,'wood':1},
        'salt':{'brine':6,'wood':3},
        'flour':{'wheat':5,'wood':3},
        'jet_fuel':{'petroleum':3,'water_drum':2,'energy':3},
        'cabernet_grapes':{'water':2,'wood':1},
        'eggs':{'feed':3,'wood':1,'water':1},
        'gasoline':{'petroleum':1,'water_drum':2,'energy':6},
        'lumber':{'wood':4,'energy':2,'water_drum':1},
        'pumpkin':{'water':20},
        'silica':{'energy':2},
        'chardonnay_grapes':{'water':2,'wood':1},
        'peppermint':{'water':3,'wood':1},
        'petroleum':{'crude_oil':2,'water_drum':1,'energy':2},
        'sugarcane':{'water':8},
        'cotton':{'water':4},
        'feed':{'wheat':1},
        'brine':{'water':3},
        'wheat':{'water':5},
        'oak_wood':{'water':5},
        'wood':{'water':7},
        'water_drum':{'water':3},
        'energy':{'crude_oil':2,'water_drum':1},
        'crude_oil':{'crude_oil':1},
        'water':{'water':1}
}



def product_cost(prd):

    lst_a = []
    for k,v in products[prd].items():
        for i in range (v):
            lst_a.append(k)

    lst_b = []
    for i in lst_a:
        for k,v in products[i].items():
            for j in range(v):
                lst_b.append(k)

    lst_c = []
    for i in lst_b:
        for k,v in products[i].items():
            for j in range(v):
                lst_c.append(k)

    lst_d = []
    for i in lst_c:
        for k,v in products[i].items():
            for j in range(v):
                lst_d.append(k)

    lst_e = []
    for i in lst_d:
        for k,v in products[i].items():
            for j in range(v):
                lst_e.append(k)

    lst_f = []
    for i in lst_e:
        for k,v in products[i].items():
            for j in range(v):
                lst_f.append(k)

    lst_g = []
    for i in lst_f:
        for k,v in products[i].items():
            for j in range(v):
                lst_g.append(k)

    # for x in [lst_a,lst_b,lst_c,lst_d,lst_g]:
    #     n = set(x)
    #     new_dict = {}
    #     for i in n:
    #         new_dict[i] = x.count(i)
    #     print(new_dict)

    n = set(lst_g)
    new_dict = {}
    for i in n:
        new_dict[i] = lst_g.count(i)

    # print('\n')
    # print(prd, 'total cost: ', new_dict)

    return new_dict

def revenue_ratio():
    reve_ratio_dic = {}
    for prd in products.keys():
        rst = product_cost(prd)
        reve_ratio = city_score[prd][0]/(sum(rst.values()))
        reve_ratio_dic[prd] = round(reve_ratio,2)
    reve_ratio_dic = {k: v for k, v in sorted(reve_ratio_dic.items(), key=lambda item: item[1])}
    return reve_ratio_dic

def points_ratio():
    points_ratio_dic = {}
    for prd in products.keys():
        rst = product_cost(prd)
        points_ratio = city_score[prd][1]/(sum(rst.values()))
        points_ratio_dic[prd] = round(points_ratio,2)
    points_ratio_dic = {k: v for k, v in sorted(points_ratio_dic.items(), key=lambda item: item[1])}
    return points_ratio_dic


if __name__ == '__main__':

    # for prd in products.keys():
    #     rst = product_cost(prd)
    
    print('\n')
    rst = revenue_ratio()
    print('revenue ratio: ', rst)
    print('\n')
    rst = points_ratio()
    print('points ratio: ', rst)