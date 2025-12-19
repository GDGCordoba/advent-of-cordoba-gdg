# Week 3: Discovering Cordoba 

Welcome to this week’s challenge! Get ready to explore the engineering behind Córdoba’s historic layout as you calculate the shortest path between its iconic landmarks.

## 📜 Story:
The Mezquita Server contains a map with the main tourist attractions of Córdoba and the pedestrian connections between them (distances in meters). Your task is to help a visitor find the minimum distance between two landmarks (for example, from Calleja de las Flores to the Torre de la Calahorra). If no path exists, print INF.

## Input format
First line: an integer N (number of nodes).
Next N lines: names of the locations (each name may contain spaces; the entire line is the name).
Next line: an integer M (number of edges).
Next M lines: A|B|W — a connection between locations A and B with weight W (an integer, meters). Nodes A and B will appear exactly as written in the list of N names. (The | character is used as a separator on each line.)
Last line: START|END — names of the start and destination locations (exact matches).

## Output
A single integer: the minimum distance in meters between START and END, or the string INF if no route exists.

## ✍🏼 Data
12
Mezquita-Catedral
Puente Romano
Alcazar de los Reyes Cristianos
Plaza de la Corredera
Calleja de las Flores
Torre de la Calahorra
Medina Azahara
Palacio de Viana
Plaza de las Tendillas
Templo Romano
Museo Julio Romero de Torres
Patios de San Basilio
16
Mezquita-Catedral|Puente Romano|450
Mezquita-Catedral|Alcazar de los Reyes Cristianos|300
Mezquita-Catedral|Calleja de las Flores|80
Calleja de las Flores|Plaza de la Corredera|120
Plaza de la Corredera|Plaza de las Tendillas|250
Plaza de las Tendillas|Templo Romano|150
Templo Romano|Museo Julio Romero de Torres|200
Museo Julio Romero de Torres|Puente Romano|600
Alcazar de los Reyes Cristianos|Puente Romano|600
Puente Romano|Torre de la Calahorra|200
Alcazar de los Reyes Cristianos|Patios de San Basilio|400
Patios de San Basilio|Calleja de las Flores|250
Palacio de Viana|Plaza de las Tendillas|350
Plaza de la Corredera|Museo Julio Romero de Torres|300
Torre de la Calahorra|Medina Azahara|5000
Alcazar de los Reyes Cristianos|Medina Azahara|4800
Calleja de las Flores Torre de la Calahorra
