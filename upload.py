class upload:
    def __init__(self, cloud, creds, id, params=None):
        #PARAMS CONTAINS PATH AND OTHER MODIFICATION
        self.cloud = cloud
        self.creds = creds
        self.params = params
        self.id = id
        call_cloud()
    
    def call_cloud(self):
        config() - fenerator
        self.params = params generator
        match self.cloud:
            case s3:
                self.s3()
            case default:
                return "something"
        
    def s3(self):

        
        
    #HERE ADD AND ALLOW TO CUSTOMIZE PATH BASED ON DATE and other PARAMS
    
    #ALSO MAINLY HERE LOGIC FOR FILE UPLOAD CUSTOMIZATION AND THAT INCLUDES INTERACTING FOR ITS STATUS AND DB LOGGING
        