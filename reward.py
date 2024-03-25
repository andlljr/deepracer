def reward_function(params):
    '''
    Example of rewarding the agent to follow center line
    '''
    
    # Read input parameters
    track_width = params['track_width']
    distance_from_center = params['distance_from_center']
    all_wheels_on_track = params['all_wheels_on_track']
    speed = params['speed']
    
    # Calculate 3 markers that are at varying distances away from the center line
    marker_1 = 0.1 * track_width
    marker_2 = 0.25 * track_width
    marker_3 = 0.5 * track_width

    # Declare reward
    reward = 0

    # Add bonus reward as fast the car go
    if speed == 1:
        reward += 0.05
    elif speed > 1 and speed <= 2.5:
        reward += 0.1
    # I made a mistake that not to change the value to > 2.5 and < 4.0
    # I did a model fixing this mistake and the result was wrost
    elif speed > 1 and speed <= 2.5:
        reward += 0.2
    
    # Penalty if car is out of track
    if not all_wheels_on_track:
        reward = 1e-5
    else:
        # Give higher reward if the car is closer to center line and vice versa
        if distance_from_center <= marker_1:
            reward += 0.8
        elif distance_from_center <= marker_2:
            reward += 0.3
        elif distance_from_center <= marker_3:
            reward += 0.1
        else:
            reward = 1e-5  # likely crashed/ close to off track
    
    return float(reward)
