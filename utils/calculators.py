def horizontal_circle_average(face1_reading, face2_reading):
    hcr_average = (face1_reading + (face2_reading - 180)) / 2
    return hcr_average


def explementary_horizontal_circle_average(face1_reading, face2_reading):
    if face2_reading > 180:
        exp_vcr_average = (face1_reading + (face2_reading - 180)) / 2
    else:
        exp_vcr_average = (face1_reading + (face2_reading + 180)) / 2
    return exp_vcr_average


def reduced_angle_horizontal_angle(average1, average2):
    reduced_angle = average2 - average1
    return reduced_angle


# returns corrected error
def calculate_total_angle_error(*reduced):
    hcr_error = -sum(reduced) - 360
    return hcr_error


# def distribute_error_to_reduced(hcr_error, *reduced):
#     distributed_error = hcr_error / reduced.count()
#     for i in reduced:
#         corrected_angle = reduced[i] + distributed_error
#     return corrected_angle


def vertical_circle_average(face1_reading, face2_reading):
    vcr_average = (face1_reading + (360 - face2_reading)) / 2
    return vcr_average
