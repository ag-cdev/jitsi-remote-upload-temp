#CONFIG IN GLOBAL
class call:
  def __init__(self, file_name, id, type=user):
    self.file_name = file_name
    self.id = id
    self.type = type
    start()

  def start(self, type):
    if(self.type == admin):
        self.admin()
    if(self.type == user):
        self.user()

  def admin(self):
    #here call config and upload parameters
    #so mainly for auth creds----
    admin_upload = upload(config_v['admin']['cloud']['name'], config_v['admin']['cloud'], self.params)
    if(admin_upload == True):
        #Upload Done
    else:
        #Upload Failed
    
    
  def user():
    #here upload paramers and creds call