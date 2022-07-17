class init:
    def create_db(self,config_f):
        self.config_f = config_f
        with open(self.config_f) as data:
            self.config = json.loads(data)
