def horizontal_circle_average(face1_reading, face2_reading):
    hcr_average = (face1_reading + (face2_reading - 180)) / 2
    return hcr_average


def explementary_horizontal_circle_average(face1_reading, face2_reading):
    if face2_reading > 180:
        exp_vcr_average = (face1_reading + (face2_reading - 180)) / 2
    else:
        exp_vcr_average = (face1_reading + (face2_reading + 180)) / 2
    return exp_vcr_average


def reduce_horizontal_angle(average1, average2):
    reduced_angle = average2 - average1
    return reduced_angle


def vertical_circle_average(face1_reading, face2_reading):
    vcr_average = (face1_reading + (360 - face2_reading)) / 2
    return vcr_average
