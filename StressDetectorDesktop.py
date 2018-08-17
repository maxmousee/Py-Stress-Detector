"""
For information on how to run, check README file
@author: MaxMouse
"""

import sys
import utils_stress_detector


def main(argv):
    input_file = utils_stress_detector.get_input_file_from_argv(argv)
    sample_rate, the_data = utils_stress_detector.get_audio_data_from_file_absolute_path(input_file)
    stress_tremor_average = utils_stress_detector.get_stress_tremor_average_from_data(the_data, sample_rate)
    under_stress = utils_stress_detector.is_under_stress(stress_tremor_average)
    print('under stress {}'.format(under_stress))
    print('stress microtremor avg freq is {}'.format(stress_tremor_average))


if __name__ == "__main__":
   main(sys.argv[1:])
