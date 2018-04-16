# Python-
用python语言把下载的数据可视化
＃从网站上下载一个JSON文件保存在蟒蛇文件下里
import json
from pygal_maps_world.maps import World
from get_countrycode import get_country_code
#添加可视化样式
from pygal.style import RotateStyle as RS, LightColorizedStyle as LCS,NeonStyle as NS
# 将数据加载到一个列表中
filename = 'population_data.json'
with open(filename) as f:
    pop_data = json.load(f)
    #print(pop_data)
#打印每个国家2010年的人口数量
cc_populations = {}
for pop_dict in pop_data:
    #print(pop_dict)
    if int(pop_dict['Year']) == 2010:
        country_name = pop_dict['Country Name']
        population = int(pop_dict['Value'])
        code = get_country_code(country_name)
        if code:
            cc_populations[code] = population
            #print(code + ": " + str(population))
        else:
            print('ERROR - ' + country_name)
#根据人口数量将所有的国家分成三组
cc_pops_1,cc_pops_2,cc_pops_3 = {},{},{}
for cc, pop in cc_populations.items():
    if pop < 100000000:
        cc_pops_1[cc] = pop
    elif pop < 100000000:
        cc_pops_2[cc] = pop
    else:
        cc_pops_3[cc] = pop
#看看每组包含了多少个国家
wm = World()
print(len(cc_pops_1),len(cc_pops_2),len(cc_pops_3))
wm_style = RS('#336699', base_style=NS)
wm = World(style = wm_style)
wm.title = 'World Population in 2010, by Country'
wm.add('0-10m', cc_pops_1)
wm.add('10m-1bn',cc_pops_2)
wm.add('>1bn', cc_pops_3)
wm.render_to_file('world_population.svg')
