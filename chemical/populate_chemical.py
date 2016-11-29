#run once to populate the database with nutritional information
import numpy as np
from pandas import Series,DataFrame
import pandas as pd
from chemical.models import Chemical, Specification, Attribute


# foods = pd.read_csv('food/static/food/FOOD_DES.txt',sep=',',  header=None,  usecols = [0,2,4])
# dbcol = pd.read_csv('food/static/food/nut_def.csv', sep = ',', header=None,  usecols = [1,2,4])
# nutrition = pd.read_csv('food/static/food/NUT_DAT.csv', sep = ',', header=None, usecols = [0,1,2])


def load_foods(cols):
    foods = pd.read_csv('food/static/food/FOOD_DES.txt',sep=',',  names = cols)
    return foods

def load_defs(cols):
    dbcol = pd.read_csv('food/static/food/NUTR_DEF.txt', sep = ',', names = cols)
    return dbcol
    
def load_nut(cols):
    nutrition = pd.read_csv('food/static/food/NUT_DAT.csv', sep = ',', names = cols)
    return nutrition

def get_values(food, test):
    nutrition = load_nut(['food','test','value'])
    content = nutrition.loc[nutrition['food'] == food]
    content = content.loc[content['test'] == test]
    return content['value']

    
def dict_food_codes():
    food_codes = load_foods(['code','group','name','desc0','desc1','desc2','desc3','desc4','desc5','desc6','desc7','desc8','desc9'])
    content = {}
    for index, food_code in food_codes.iterrows():
        desc = ""
        Y = False
        for i in range(10):
            desc_index = 'desc' + str(i)
            if food_code[desc_index] == 'Y' or Y:
                Y = True
            else:
                desc += str(food_code[desc_index]).lower() + " "
        content[food_code['code']] =  food_code['name'].lower() + ' (' + desc + ')'
    return content

def dict_test_codes():
    test_codes = load_defs(['code','unit','abrev','name'])
    content = {}
    for index, test_code in test_codes.iterrows():
        content[test_code['code']] =  str(test_code['abrev']) 
    return content

def add_all():
    foods = dict_food_codes()
    tests = dict_test_codes()
    nutrition = load_nut(['food','test','value'])
    context = {}
    last = nutrition['food'].iloc[0]
    # print(tests)
    for index, item in nutrition.iterrows():
        if item['food'] != last:
            food = Food(context)
            # food.save()
            print(context)
            context = {}
            break
        if context == {}:
            food_code = int(item['food'])
            context['name'] = foods[food_code]
        test_code = int(item['test'])
        test_name = tests[test_code]
        context[test_name] = round(item['value'], 3)
            
        
        last = item['food']
    #     print(test_code)
    # print(tests)
        
add_all()

def test_name():
    tests = load_defs(['code','unit','abrev','name'])
    for index, test in tests.iterrows():
        print(test['abrev'])