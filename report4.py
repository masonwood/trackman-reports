from matplotlib import pyplot as plt
from matplotlib.patches import Rectangle
import matplotlib.lines as mlines
import os
from file import check_path, get_path

plt.style.use('seaborn')

pitch_colors = {
  'Fastball': '#D22D49',
  'Sinker': '#DE6A04',
  'Cutter': '#933F2C',
  'Slider': '#EEE716',
  'Curveball': '#00D1ED',
  'ChangeUp': '#1DBE3A',
  'Splitter': '#3BACAC',

}

pitch_result = {
  'StrikeCalled': 'X',
  'StrikeSwinging': '*',
  'FoulBall': 's',
  'BallCalled': 'o',
  'HitByPitch': '$HBP$',
  'InPlay': 'P',
}

pitch_alphas = {
  'Fastball': .95,
  'Sinker': .95,
  'Cutter': .95,
  'Slider': .95,
  'Curveball': .95,
  'ChangeUp': .95,
  'Splitter': .95,
}

# change function name here and import in main.py
def report4(data, save_path):
    data.boxplot(by ='TaggedPitchType',grid='True',column =['RelSpeed'], color='red', vert=False)

    plt.subplots_adjust(left=0.20)
    plt.suptitle('')

  # remains the same for every file
    check_path(save_path)

  # save image to folder
    plt.savefig(get_path(save_path, 'report4'))
    plt.close()