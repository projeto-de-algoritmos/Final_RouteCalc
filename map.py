# -*- coding: utf-8 -*-
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import pandas as pd
import networkx
import itertools
    
def draw_map(m):
    m.fillcontinents(color="#0D9C28",lake_color="blue")
    m.drawmapboundary(fill_color="#5D9BFE")
    m.drawcountries(color='#585857',linewidth = 1)
    m.drawstates(linewidth = 0.2)
    m.drawcoastlines(linewidth=1)


def calculate(G, origin, destination):
    airports = networkx.dijkstra_path(G,source=origin,target=destination ,weight='Distance')
    
    airport_pairs = [(x,y) for x, y in itertools.izip_longest(airports, airports[1:])]
    airport_pairs = airport_pairs[:-1]

    
    for airport in airports:
        x0, y0 = m(G.nodes[airport]['Longitude'],G.nodes[airport]['Latitude'])
        m.scatter(x0, y0, marker='D',color="#FFFFFF", s=60,zorder=10)
        plt.text(x0,y0+100000,airport,fontsize=10,fontweight='bold',ha='center',va='bottom',color="white")
    
    distance = 0
    for airport in airport_pairs:
        d = networkx.dijkstra_path_length(G,airport[0],airport[1],weight="DISTANCE")
        distance += d
        x, y = m.gcpoints(G.nodes[airport[0]]['Longitude'],G.nodes[airport[0]]['Latitude'],
                        G.nodes[airport[1]]['Longitude'],G.nodes[airport[1]]['Latitude'],500)
        m.plot(x, y,color="#000000",linewidth=2, linestyle='dashed')
        x2, y2 = m([y['Longitude'] for x, y in G.nodes(data=True) if x in airport],
                [y['Latitude'] for x, y in G.nodes(data=True) if x in airport])
        m.scatter(x2, y2,color='#000000',s=50,zorder=4)
    title = "Distancia de {} para {}: {}km".format(origin, destination, distance)
    plt.title(title)
    plt.draw()  


if __name__ == '__main__':
    plt.figure(figsize = (60,40))
    m = Basemap(projection='gall')
    draw_map(m)
    airport = pd.read_csv("./data/airport.csv")
    routes = pd.read_csv('./data/route.csv')

    G = networkx.from_pandas_edgelist(routes,'SOURCE','DEST', edge_attr='DISTANCE',create_using=networkx.DiGraph())
    networkx.set_node_attributes(G,airport.Latitude.copy().rename(airport.IATA).to_dict(),'Latitude')
    networkx.set_node_attributes(G,airport.Longitude.copy().rename(airport.IATA).to_dict(),'Longitude')
    print("Grafo carregado")
    origin = raw_input("Insira o código IATA do aeroporto de origem(ex.: BSB): ").upper()
    destination = raw_input("Insira o código IATA do aeroporto de destino(ex.: JFK): ").upper()
    calculate(G, origin, destination)
    plt.show()

