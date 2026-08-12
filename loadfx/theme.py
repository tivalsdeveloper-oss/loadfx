class Theme:
    _themes={
      "default":{"primary":"cyan","secondary":"white","success":"green","warning":"yellow","error":"red"},
      "cyberpunk":{"primary":"magenta","secondary":"cyan","success":"green","warning":"yellow","error":"red"},
      "matrix":{"primary":"green","secondary":"green","success":"green","warning":"yellow","error":"red"},
      "retro":{"primary":"yellow","secondary":"white","success":"green","warning":"yellow","error":"red"},
      "minimal":{"primary":"white","secondary":"gray","success":"green","warning":"yellow","error":"red"},
    }
    current="default"
    @classmethod
    def use(cls,name):
        if name not in cls._themes: raise ValueError(f"Unknown theme: {name}")
        cls.current=name; return cls
    @classmethod
    def create(cls,name,**values): cls._themes[name]=values; return cls
    @classmethod
    def get(cls): return dict(cls._themes[cls.current])
    @classmethod
    def names(cls): return sorted(cls._themes)
