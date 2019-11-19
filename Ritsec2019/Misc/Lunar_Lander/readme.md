## Ritsec 2019 - Lunar lander

**Category:** Misc
**Points:** 300
**Solves:** 39
**Solved by** Sondre

>We are trying to troubleshoot the guidance computer. You should already have the star tables, so we just need you to double check some of the distances for us. We aren't sure about the precision though so you may need to play with it
>Good luck, Houston
>[Distances.txt](distances.txt)

## Write-up

The first part of the job was finding the star tables. After some intenese googling (and a couple of hints from the autohor) i found [this](https://github.com/chrislgarry/Apollo-11/) repo which contained [this](https://github.com/chrislgarry/Apollo-11/blob/master/Comanche055/STAR_TABLES.agc) file. I found the distance between all of the different "stars" and converted the numbers into letters and voilá i got the flag: ritsec{leap_4_th3_stars}. [This](LunarLander.py) is the script i wrote for finding the distances