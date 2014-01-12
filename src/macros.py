
# ability
class attack(object):
    def __init__(self, name, range, targets, trigger, effect):
        self.name = name
        self.range = range
        self.targets = targets
        self.trigger = trigger
        self.effect = effect

    def short(self):
        return "{name} (range: {range}, targets: {targets}): {trigger}, {effect}".format(name=self.name, range=self.range, targets=self.targets, trigger=self.trigger.short(), effect=self.effect.short())

    def long(self):
        return '\n'.join(("{name}",
                ":    {trigger}",
                "     {effect}",
                "     This ability has a range of {range}.",
                ""
                )).format(name=self.name, trigger=self.trigger.long(),
                         effect=self.effect.long(), range=self.range)

# trigger
class challenge(object):
    def __init__(self, target, target_statistic, bonus_statistic):
        self.target = target
        self.target_statistic = target_statistic
        self.bonus_statistic = bonus_statistic

    def short(self):
        return "challenge vs. {target} {target_statistic} (1d20+{bonus_statistic})".format(target=self.target, target_statistic=self.target_statistic, bonus_statistic=self.bonus_statistic)

    def long(self):
        return '\n     '.join(("Roll 1d20 and add this unit's {bonus_statistic} statistic.",
                              "If the result is greater than or equal to the target's {target_statistic},",
                              )).format(bonus_statistic=self.bonus_statistic,
                                          target_statistic=self.target_statistic)

# effect
class change_stat(object):
    def __init__(self, target, statistic, verb, direction, number):
        self.target = target
        self.statistic = statistic
        self.verb = verb
        self.direction = direction
        self.number = number

    def short(self):
        return "{number} {direction} to {target} {statistic}".format(number=self.number, direction=self.direction, target=self.target, statistic=self.statistic)

    def long(self):
        return "the {target} {verb} {number} {direction} to its {statistic}.".format(target=self.target, number=self.number, verb=self.verb, direction=self.direction, statistic=self.statistic)
