# Squid Game Simulator

As Netflix's second season of Squid Game came to a close, I could not help asking myself how truly difficult these games are to win.
And what are the odds of someone _actually_ surviving these series of kids' games?

This repo runs a sequence of simulation, going through each one of the 6 games tens of thousands of times.

I obviously cannot capture all the dynamics of the game, especially since it is fictional. Below are some of my assumptions.
* There is no fear involved, and everyone is completely rational.
* Players are independent of each other. This means one cannot positively/negatively impact the performance of other players.
* There are no votes in between games. It is hard to predict how players behave in reality anyway.
* There are no murders neither during nor in between games.

Without these assumptions, it is close to impossible to create a simulation. My goal is to get a rough idea of how 
difficult these games are to beat.
## Red Light Green Light
There are two ways to be eliminated from this game.
* Either you don't manage to reach the finish line in the allotted time.
* Or you move when you are not supposed to.

Based on the first season of Squid Game, the players had to stop exactly 20 times in a span on 5 minutes.
This actually leave the players around 2.5 minutes to run or walk a distance of 100 meters (as per the dimensions of the
actual set used during production). This means that a player must move at least at a pace of 0.67m/s. According to 
[this publication](https://www.researchgate.net/publication/286071735_Scenario_Analysis_of_Pedestrian_Flow_in_Public_Spaces),
the average walking pace is approximately normally distributed with an average and standard deviation of 1.34m/s and 0.37m/s respectively. 
This means an average person has ample time to walk the distance in time, without any need to hurry.

Modelling the time someone stands still is a bit trickier. According to [this article](https://revistapesquisa.fapesp.br/en/the-art-of-standing-still/), a person is able to stand still for an average of 30 seconds.
This is good enough as a start, and to model my ignorance, I place a Gamma distribution on the average value someone is able to stand still, with an average of 30 seconds.

With these two components in place, I can simulate the games, giving readings such as the figure below. 
![RLGL_Sim](https://github.com/DylanZammit/SquidGameSimulator/blob/master/src/img/rlgl.gif?raw=true)

## Sugar Honeycombs
The difficulty of this game greatly depends on the choice of cookie. Players are not aware of the game prior to this choice, so the assumption is that
players were allocated a cookie shape at random. We ignore the time components of this game, and place a beta distribution on the success rate of breaking the cookie.
The average success probabilities of each cookie were as follows:
Triangle: 80%
Circle: 60%
Star: 40%
Umbrella: 20%.
## Tug of War
Since there is no way to predict the ability of random player, and which they will be allocated to, we might as well
assign a 50% success probability.
## Marbles
For a similar reason as above, due to our ignorance of game played, and since no player has no inherit advantage of another,
we can simply allocate a success probability of 50%.
## Glass Stones

## Squid Game