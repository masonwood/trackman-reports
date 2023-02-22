from matplotlib import pyplot as plt
from matplotlib.patches import Rectangle
import matplotlib.lines as mlines
import os
import numpy as np
from file import check_path, get_path

plt.rcdefaults()
fig, ax = plt.subplots()

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
def report19(data, save_path):
    Pitcher = data['Pitcher'][1]
    Extension = data['Extension']
    TaggedPitchType = data['TaggedPitchType']

    fastball = []
    slider = []
    sinker = []
    cutter = []
    curveball = []
    changeup = []
    splitter = []

    for i, j in enumerate(Extension):
        if TaggedPitchType[i] == 'Fastball':
            fastball.append(j)
        elif TaggedPitchType[i] == 'Slider':
            slider.append(j)
        elif TaggedPitchType[i] == 'Sinker':
            sinker.append(j)
        elif TaggedPitchType[i] == 'Cutter':
            cutter.append(j)
        elif TaggedPitchType[i] == 'Curveball':
            curveball.append(j)
        elif TaggedPitchType[i] == 'ChangeUp':
            changeup.append(j)
        elif TaggedPitchType[i] == 'Splitter':
            splitter.append(j)

    labels = []
    count = 0

    if not len(fastball) == 0:
        fastball_bar = plt.barh(count, sum(fastball) / len(fastball), color = '#BA0C2F')
        ax.bar_label(fastball_bar, label_type='edge')
        labels.append('Fastball')
        count += 1

    if not len(sinker) == 0:
        sinker_bar = plt.barh(count, sum(sinker) / len(sinker), color = '#BA0C2F')
        ax.bar_label(sinker_bar, label_type='edge')
        labels.append('Sinker')
        count += 1

    if not len(cutter) == 0:
        cutter_bar = plt.barh(count, sum(cutter) / len(cutter), color = '#BA0C2F')
        ax.bar_label(cutter_bar, label_type='edge')
        labels.append('Cutter')
        count += 1

    if not len(slider) == 0:
        slider_bar = plt.barh(count, sum(slider) / len(slider), color = '#BA0C2F')
        ax.bar_label(slider_bar, label_type='edge')
        labels.append('Slider')
        count += 1

    if not len(curveball) == 0:
        curveball_bar = plt.barh(count, sum(curveball) / len(curveball), color = '#BA0C2F')
        ax.bar_label(curveball_bar, label_type='edge')
        labels.append('Curveball')
        count += 1

    if not len(changeup) == 0:
        changeup_bar = plt.barh(count, sum(changeup) / len(changeup), color = '#BA0C2F')
        ax.bar_label(changeup_bar, label_type='edge')
        labels.append('ChangeUp')
        count += 1

    if not len(splitter) == 0:
        splitter_bar = plt.barh(count, sum(splitter) / len(splitter), color = '#BA0C2F')
        ax.bar_label(splitter_bar, label_type='edge')
        labels.append('Splitter')
        count += 1

    ax.set_yticks(np.arange(len(labels)), labels=labels)

    plt.subplots_adjust(left=0.15)
    plt.ylabel('Pitch Types', fontsize=12)
    plt.title('Extension', fontsize=16)

    # remains the same for every file
    check_path(save_path)

    # save image to folder
    plt.savefig(get_path(save_path, 'report19'))
    plt.close()