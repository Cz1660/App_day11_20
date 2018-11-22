import yaml,os

class Read_Data:
  def __init__(self,file_name):
    self.file_path = os.getcwd() + os.sep + 'Yaml' + os.sep + file_name
  def return_data(self):
    with open(self.file_path,'r',encoding='utf-8') as f:
      data = yaml.load(f)
    return data
