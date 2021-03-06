-   Velice
    -   Statistics
        -   Health
        -   Armor
        -   Body
        -   Mind

    -   Challenges
    -   Gameplay
        -   Starting a Game
        -   Turns
        -   Combat
        -   Winning the Game


Velice
======

***A universal miniature skirmish wargame ruleset.***

[![Creative Commons License](src/images/cc-by-sa.png "CC-By-SA")](http://creativecommons.org/licenses/by-sa/4.0/)

<span xmlns:dct="http://purl.org/dc/terms/" href="http://purl.org/dc/dcmitype/Text" property="dct:title" rel="dct:type"> Velice</span> by <a xmlns:cc="http://creativecommons.org/ns#" href="https://github.com/cnelsonsic/velice" property="cc:attributionName" rel="cc:attributionURL"> [Charles Nelson](https://github.com/cnelsonsic/velice)</a> is licensed under a [Creative Commons Attribution-ShareAlike 4.0 International License](http://creativecommons.org/licenses/by-sa/4.0/).

This ruleset has almost no fluff. At the moment, it is almost entirely statistics and numbers and so on. That being said, keep in mind that there will be additional content packs available in the future.

<!-- Add note about licensing, use, etc. -->

Statistics
----------

There are only a handful of statistics in Velice: Health, Armor, Body, and Mind.

The majority of differentiation between units is in their equipment and magic items. Some of which are “single-use”, or once per game.

### Health

Health is the amount of damage a unit can take before it is removed from play. When it reaches zero, it is removed from play.

### Armor

Armor represents a thick hide, or solid steel plating, and sometimes sheer evasiveness.

When a unit attacks another unit, its controller rolls 1d20 and adds the attacking unit’s Body statistic. If the result is greater than or equal to the target Unit’s Armor, the attack hits.

### Body

Body is representative of physical strength, fleetness of foot, and deftness of hand.

It is added to attack rolls; the higher the Body statistic, the easier it is to hit something with.

### Mind

Mind represents book smarts, street smarts, and social graces.

It is used for some magical spells and certain abilities.

Challenges
----------

Most challenges can be met with either Body or Mind. For instance, jumping a fence would be a Body challenge. Reading a scroll would be a Mind challenge.

To successfully complete a challenge, the unit’s controller needs to roll higher than or equal to the challenge’s difficulty. To roll for a challenge, the unit’s controller rolls 1d20, and adds the Body or Mind statistic, as appropriate for the challenge.

For example, leaping a waist-high stone wall in a single bound would need roughly a 10. Pat, the barbarian, has a 5 Body statistic. Their controlling player rolls a single twenty-sided die. It lands on a 6. Maybe Pat stumbles a little, or slips on the turf. However, Pat has a Body score of 5. Which, when added to the 6 from the twenty-sided die, becomes 11. With an 11, Pat is able to launch themself over the wall and land safely on the other side.

Gameplay
--------

### Starting a Game

Each player gets a set amount of “points” with which to “buy” units for use in this game. Usually this is 1000 for small skirmishes, but the only limit is the players’ imaginations.

A player’s army may not be worth more points than the agreed upon army value, because that would not be any fun at all.

Once both players have chosen the units they want to use, they place them on the table. These units are now considered to be “in play”, because they are. Players should place all their units in play at the same time, to frustrate attempts at tailoring ones’ army to subvert another’s.

All players should make sure that their opponents are okay with any additional rules and statistics that their units use. Not everyone wants to play against terrible eldritch horrors.

### Turns

Players take turns moving their units, one at a time. A unit may move and attack once per turn. A unit does not have to move or attack, both are optional.

A unit may move up to its Body statistic in centimeters.

A unit may only attack another unit if it is within range. All units are presumed to have a default attack ability:

<!-- See src/abilities.mkd -->
Attack  
Roll 1d20 and add this unit’s Body statistic. If the result is greater than or equal to the target’s Armor, the target takes 1d6+Body damage to its Health. This ability has a range of 3cm.

*Attack (range: 3cm, targets: 1): challenge vs. target Armor (1d20+Body), 1d6+Body damage to target Health*

### Combat

### Winning the Game
