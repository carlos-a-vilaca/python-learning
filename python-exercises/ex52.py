'''Cria um programa com um tuplo com os 20 primeiros classificados do Campeonato Espanhol de Futebol.
Depois mostra:
a) Os primeiros 5 classificados
b) Os últimos 4 classificados
c) Uma lista com as equipas por ordem alfabética
d) A posição da equipa Espanhol'''

classificados = ('Alavés','Athletic Bilbao','Atlético de Madrid','Celta de Vigo','Deportivo','Elche CF',
                 'Espanyol','FC Barcelona','Getafe CF','Levante','Málaga CF','Osasuna','Racing Santander',
                 'Rayo Vallecano','Real Betis','Real Madrid','Real Sociedad','Sevilla FC','Valencia CF',
                 'Villarreal CF')

print(classificados[:5])
print(classificados[-4])
print(sorted(classificados))
print(classificados[6])
