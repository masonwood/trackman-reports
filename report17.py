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
def report17(data, save_path):
    Pitcher = data['Pitcher'][1]
    RelHeight = data['RelHeight']
    RelSide = data['RelSide']
    TaggedPitchType = data['TaggedPitchType']

    # plt.scatter(HorzBreak, InducedVertBreak, s=100, c='red', edgecolor='black', linewidth=1, alpha=0.75)

    for i, j in enumerate(RelSide):
        plt.scatter(
            [RelSide [i]],
            [RelHeight [i]], 
            s=50, 
            c=pitch_colors.get(TaggedPitchType[i], 'Fastball'),
            edgecolor='black',
        )  

    # pitch_colors_labels = []

    # for key in pitch_colors:
    #   pitch_colors_labels.append(
    #     mlines.Line2D([], [], color=pitch_colors[key], marker='o', linestyle='None', markersize=10, label=key)
    #   )

    plt.title('Release Points', fontsize=16)
    plt.xlabel('Release Side(ft)', fontsize=12)
    plt.ylabel('(Release Height (ft)', fontsize=12)
    # plt.tight_layout()

    # remains the same for every file
    check_path(save_path)

    # save image to folder
    plt.savefig(get_path(save_path, 'report17'))
    plt.close()