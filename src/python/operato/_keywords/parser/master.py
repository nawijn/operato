@dataclass
class $NAME(Keyword):
$ATTRIBUTES

    @property
    def keyword(self):
        return f"$KEYWORD/{self.id}"

    @property
    def pre_conditions(self):
        return ["NOT yet implemented"
        ]

    @property
    def structure(self,$VARIABLE):
        structure=[
$FORMAT
            ]

        return structure
