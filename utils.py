import config
import numpy as np

import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.patches as patches

def plot_3D(body, left_hand, right_hand, body_dict, hand_dict, ax, draw_hand=True):
    body = body.reshape(-1, 3)
    for ii, p_idx in enumerate(body_dict['parent']):
        ax.plot([body[p_idx, 0], body[body_dict['child'][ii], 0]],
                [body[p_idx, 1], body[body_dict['child'][ii], 1]],
                [body[p_idx, 2], body[body_dict['child'][ii], 2]],
                color=config.lr_color[body_dict['lr'][ii]])
        
    for j_i, joint in enumerate(body):
        ax.plot(joint[0], joint[1], joint[2], 'k.')
        ax.text(joint[0]-0.1, joint[1]-0.05, joint[2]-0.1, str(j_i), color='b', fontsize=10)

    if draw_hand:
        for ii, p_idx in enumerate(hand_dict['parent']):
            ax.plot([left_hand[p_idx, 0], left_hand[hand_dict['child'][ii], 0]],
                    [left_hand[p_idx, 1], left_hand[hand_dict['child'][ii], 1]],
                    [left_hand[p_idx, 2], left_hand[hand_dict['child'][ii], 2]],
                    color=config.lr_color[0], linewidth=2)

            ax.plot([right_hand[p_idx, 0], right_hand[hand_dict['child'][ii], 0]],
                    [right_hand[p_idx, 1], right_hand[hand_dict['child'][ii], 1]],
                    [right_hand[p_idx, 2], right_hand[hand_dict['child'][ii], 2]],
                    color=config.lr_color[1], linewidth=2)
        
    ax.view_init(-90, -90)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    

def plot_2D(body, body_dict, 
            left_hand, right_hand, hand_dict,
            bbox, ax, draw_hand=True):  
    body = body.reshape(-1, 3)
    for ii, p_idx in enumerate(body_dict['parent']):
        ax.plot([body[p_idx, 0], body[body_dict['child'][ii], 0]],
                [body[p_idx, 1], body[body_dict['child'][ii], 1]],
                color=config.lr_color[body_dict['lr'][ii]], linewidth=2)
        
    if draw_hand:
        for ii, p_idx in enumerate(hand_dict['parent']):
            ax.plot([left_hand[p_idx, 0], left_hand[hand_dict['child'][ii], 0]],
                    [left_hand[p_idx, 1], left_hand[hand_dict['child'][ii], 1]],
                    color=config.lr_color[0], linewidth=2)

            ax.plot([right_hand[p_idx, 0], right_hand[hand_dict['child'][ii], 0]],
                    [right_hand[p_idx, 1], right_hand[hand_dict['child'][ii], 1]],
                    color=config.lr_color[1], linewidth=2)
            
    # Create a Rectangle patch
    rect = patches.Rectangle((bbox[0], bbox[1]), bbox[2], bbox[3],
                             linewidth=2, edgecolor='r', facecolor='none')

    # Add the patch to the Axes
    ax.add_patch(rect)
    
    
def plot_vector(pos, vec, ax, length=50):
    ax.plot([pos[0], pos[0]+length*vec[0]], [pos[1], pos[1]+length*vec[1]], linewidth=4)
    

def get_head_info(open_pose):
    head_info = dict()
    head_info['pos'] = open_pose[0]
    head_info['vec'] = open_pose[0] - (open_pose[17] + open_pose[18])/2
    head_info['vec'] /= np.linalg.norm(head_info['vec'])
    
    info_array = np.concatenate([head_info['pos'], head_info['vec']])
    return head_info, info_array

def plot_head_info(head_info, ax):
    plot_vector(head_info['pos'], head_info['vec'], ax)


def get_hand_info(hand, direction):
    hand_info = dict()
    
    index_vector = hand[9] - hand[0]
    index_vector /= np.linalg.norm(index_vector)

    pinky_vector = hand[17] - hand[0]
    pinky_vector /= np.linalg.norm(pinky_vector)

    if direction=='left':    
        palm_vector = np.cross(pinky_vector, index_vector)
        palm_vector /= np.linalg.norm(palm_vector)

        new_thumb_vector = np.cross(palm_vector, index_vector)
        new_thumb_vector /= np.linalg.norm(new_thumb_vector)
        
    elif direction=='right':
        palm_vector = np.cross(index_vector, pinky_vector)
        palm_vector /= np.linalg.norm(palm_vector)

        new_thumb_vector = np.cross(index_vector, palm_vector)
        new_thumb_vector /= np.linalg.norm(new_thumb_vector)
    
    hand_info['thumb'] = new_thumb_vector
    hand_info['index'] = index_vector
    hand_info['palm'] = palm_vector
    hand_info['pos'] = hand[0]
    
    info_array = [new_thumb_vector, index_vector, palm_vector, hand[0]]
    info_array = np.concatenate(info_array)
    
    return hand_info, info_array

def plot_hand_info(hand_info, ax):
    plot_vector(hand_info['pos'], hand_info['palm'], ax)

    
def get_heel_info(open_pose):
    left_heel = open_pose[21]
    right_heel = open_pose[24]
    
    left_foot_vector = (open_pose[19] + open_pose[20])/2 - open_pose[21]
    left_foot_vector /= np.linalg.norm(left_foot_vector)

    right_foot_vector = (open_pose[22] + open_pose[23])/2 - open_pose[24]
    right_foot_vector /= np.linalg.norm(right_foot_vector)

    left = {'pos':left_heel, 'vec':left_foot_vector}
    right = {'pos':right_heel, 'vec':right_foot_vector}
    
    info_array = [left_heel, left_foot_vector, right_heel, right_foot_vector]
    info_array = np.concatenate(info_array)
    
    return left, right, info_array
    
def plot_heel_info(left, right, ax): 
    plot_vector(left['pos'], left['vec'], ax)
    plot_vector(right['pos'], right['vec'], ax)
    