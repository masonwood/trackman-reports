from matplotlib import pyplot as plt
from matplotlib.patches import Rectangle
import matplotlib.lines as mlines
import os
from file import check_path,get_path

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

def report6(data, save_path):
  Pitcher = data['Pitcher'][1]
  PlateLocHeight = data['PlateLocHeight']
  PlateLocSide = data['PlateLocSide']
  TaggedPitchType = data['TaggedPitchType']
  PitchCall = data['PitchCall']

  rect = Rectangle((-1,1.4), 2, 1.7, fill=False, color='000000', alpha=1)
  plt.gca().add_patch(rect);

  rect = Rectangle((-0.9,1.5), 1.8, 1.5, fill=False, color='000000', alpha=1)
  plt.gca().add_patch(rect);

  rect = Rectangle((-.9,1.5), 3/5, .5, fill=False, color='000000', alpha=1)
  plt.gca().add_patch(rect);

  rect = Rectangle((-.9,1.5), 3/5, 1, fill=False, color='000000', alpha=1)
  plt.gca().add_patch(rect);

  rect = Rectangle((-.9,1.5), 3/5, 1.5, fill=False, color='000000', alpha=1)
  plt.gca().add_patch(rect);

  rect = Rectangle((-.3,1.5), 3/5, .5, fill=False, color='000000', alpha=1)
  plt.gca().add_patch(rect);

  rect = Rectangle((-.3,1.5), 3/5, 1, fill=False, color='000000', alpha=1)
  plt.gca().add_patch(rect);

  rect = Rectangle((-.3,1.5), 3/5, 1.5, fill=False, color='000000', alpha=1)
  plt.gca().add_patch(rect);

  rect = Rectangle((-.3,1.5), 3/5, 1, fill=False, color='000000', alpha=1)
  plt.gca().add_patch(rect);

  rect = Rectangle((.3,1.5), 3/5, .5, fill=False, color='000000', alpha=1)
  plt.gca().add_patch(rect);

  rect = Rectangle((.3,1.5), 3/5, 1, fill=False, color='000000', alpha=1)
  plt.gca().add_patch(rect);

  rect = Rectangle((.3,1.5), 3/5, 1.5, fill=False, color='000000', alpha=1)
  plt.gca().add_patch(rect);


  for i, j in enumerate(PlateLocSide):
    plt.scatter(
      [PlateLocSide [i]],
      [PlateLocHeight [i]], 
      s=100, 
      c=pitch_colors.get(TaggedPitchType[i], 'red'),
      marker=pitch_result.get(PitchCall[i], '*'),
      edgecolor='black', 
      alpha=pitch_alphas.get(TaggedPitchType[i], '1'),
    )  

  plt.title('All Pitches', fontsize=16)
  plt.xlabel('PlateLocSide', fontsize=12)
  plt.ylabel('PlateLocHeight', fontsize=12)

  pitch_colors_labels = []

  for key in pitch_colors:
    pitch_colors_labels.append(
      mlines.Line2D([], [], color=pitch_colors[key], marker='o', linestyle='None', markersize=10, label=key)
    )

  for key in pitch_result:
      pitch_colors_labels.append(
      mlines.Line2D([], [], color='black', marker=pitch_result[key], linestyle='None', markersize=10, label=key)
    )

  plt.grid(False)

  plt.text(-3.95, 3.92, Pitcher, fontsize = 4)
  plt.text(-3.95, 3.83, 'Pitcher POV', fontsize = 4)
  plt.legend(handles=pitch_colors_labels)
  plt.xlim([-4,4])
  plt.ylim([0,4])
  plt.tight_layout()

  check_path(save_path)
  plt.savefig(get_path(save_path, 'report6'))
  plt.close()