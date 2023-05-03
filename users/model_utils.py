from enum import Enum


class SecurityRuleCategories(Enum):
    Screen = 'Screen'
    Function = 'Function'

    @classmethod
    def all(cls):
        return [SecurityRuleCategories.Screen, SecurityRuleCategories.Function]
