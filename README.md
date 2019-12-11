# hazard_lighting_optimization
### Analysis done for the Lake Lanier Association

<p>This repo was an independent research and analysis project performed for the <a href="https://lakelanier.org/">Lake Lanier Association</a> (LLA), all data was provided by the LLA. This repo contains two files. The first is a .csv with information on the locations of all hazard markers on Lake Lanier. The second file, solarLights.py, utilizes Gurobi to create an optimal model for installing hazard light monitoring devices. For information on why this problem is important, see <i>The Problem</i> and for information on the optimal model read <i>The Model</i>.</p> 

#### The Problem
<p>Lake Lanier has over 11 million visitors a year and over 30,000 registered vessels. In order to promote safety on the lake, the LLA began placing solar lights on top of hazard bouys to make them visible at night to boaters. Furthermore, the LLA commissioned a senior design group from Georgia Tech to engineer a device that monitors each solar light to ensure they are working properly. With the monitoring device in hand, the final step was for the LLA to install the device on every bouy. This leads to the question, what is the best way to install the monitoring devices?</p>

#### The Model
<p>The optimal model was a hub-and-spoke model that minimized installation and upkeep costs for the LLA by minimizing the total number of hazard light monitoring devices needed on the lake within the constraints (mainly connectivity distance between monitoring devices).</p>
