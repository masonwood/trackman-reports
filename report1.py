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
def report1(data, save_path):
    group_by_diag = data.groupby(["TaggedPitchType"]).count().reset_index()
    pitch_types = data['TaggedPitchType'].value_counts()
    labels = []
    colors = []

    for pitch_type, count in pitch_types.items():
        labels.append(pitch_type)
        colors.append(pitch_colors.get(pitch_type))
    
    # myexplode = [0.1, 0.1, 0.1, 0.1, 0.1, 0.1]

    # print(pitch_types[0])
    # print(labels)
    # print(group_by_diag)

    plt.title('Pitch Breakdown', fontsize=16)
    plt.pie(pitch_types, labels = labels, colors = colors, wedgeprops = {'linewidth': 30}, autopct='%1.1f%%')


    # remains the same for every file
    check_path(save_path)

    # save image to folder
    plt.savefig(get_path(save_path, 'report1'))
    plt.close()