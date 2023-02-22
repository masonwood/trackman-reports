import os

def check_path(save_path):
  folder_path = os.path.expanduser(f'~/Desktop/Testing/{save_path}')
  exists = os.path.exists(folder_path)
  if not exists:
    os.mkdir(folder_path)

def get_path(save_path,plot_name):
    return os.path.expanduser(f'~/Desktop/Testing/{save_path}/{plot_name}.png')
