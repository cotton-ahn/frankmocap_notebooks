import os

# change this value as you want. Set this as -1 to process with original fps.
fps = 10
vid_height = 640

read_type = 'images'# 'videos' or 'images'

# Some Path Information
url_filePath = 'video_url.txt'
video_dir = 'videos'
image_dir = 'images'
mocap_dir = 'mocaps'
skeleton_pkl_dir = 'skeletons_pkl'
skeleton_npz_dir = 'skeletons_npz'

repo_abs_path = os.path.abspath('.')


# Joint Names (./eft/eft/cores/jointorders.py)
SPIN49_JOINT_NAMES = [
                    'OP_Nose', 'OP_Neck', 'OP_RShoulder',           #0,1,2
                    'OP_RElbow', 'OP_RWrist', 'OP_LShoulder',       #3,4,5
                    'OP_LElbow', 'OP_LWrist', 'OP_MidHip',          #6, 7,8
                    'OP_RHip', 'OP_RKnee', 'OP_RAnkle',             #9,10,11
                    'OP_LHip', 'OP_LKnee', 'OP_LAnkle',             #12,13,14
                    'OP_REye', 'OP_LEye', 'OP_REar',                #15,16,17
                    'OP_LEar', 'OP_LBigToe', 'OP_LSmallToe',        #18,19,20
                    'OP_LHeel', 'OP_RBigToe', 'OP_RSmallToe', 'OP_RHeel',  #21, 22, 23, 24  ##Total 25 joints  for openpose
                    'Right Ankle', 'Right Knee', 'Right Hip',               #0,1,2
                    'Left Hip', 'Left Knee', 'Left Ankle',                  #3, 4, 5
                    'Right Wrist', 'Right Elbow', 'Right Shoulder',     #6
                    'Left Shoulder', 'Left Elbow', 'Left Wrist',            #9
                    'Neck (LSP)', 'Top of Head (LSP)',                      #12, 13
                    'Pelvis (MPII)', 'Thorax (MPII)',                       #14, 15
                    'Spine (H36M)', 'Jaw (H36M)',                           #16, 17
                    'Head (H36M)', 'Nose', 'Left Eye',                      #18, 19, 20
                    'Right Eye', 'Left Ear', 'Right Ear'                    #21,22,23 (Total 24 joints)
                    ]


open_pose_dict = dict()
open_pose_dict['parent'] = [1, 0, 15, 0, 16,  1, 2, 3, 1, 5, 6, 1, 8, 9, 10, 11, 24, 24, 8, 12, 13, 14, 21, 21]
open_pose_dict['child'] =  [0, 15,17, 16,18, 2, 3, 4, 5, 6, 7, 8, 9,10, 11, 24, 22, 23, 12,13, 14, 21, 19, 20]
open_pose_dict['lr'] =     [0, 1, 1, 0, 0,   1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0]
open_pose_dict['joint_name'] = SPIN49_JOINT_NAMES[:25]

simple_pose_dict = dict()
simple_pose_dict['parent'] = [1, 1, 2, 3, 1, 5, 6, 1, 8, 9, 10, 8, 12, 13]
simple_pose_dict['child'] =  [0, 2, 3, 4, 5, 6, 7, 8, 9,10, 11, 12,13, 14]
simple_pose_dict['lr'] =     [0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1,  0, 0, 0]
simple_pose_dict['joint_name'] = SPIN49_JOINT_NAMES[:15]


aux_pose_dict = dict()
aux_pose_dict['parent'] = [12, 18, 19, 19, 21, 19, 20, 12, 8, 7, 12, 9, 10, 12, 15, 16, 14, 2, 1, 14, 3, 4]
aux_pose_dict['child'] =  [18, 13, 17, 21, 23, 20, 22, 8,  7, 6, 9, 10, 11, 15, 16, 14, 2, 1, 0,  3,  4, 5]
aux_pose_dict['lr'] =     [0,  0,  0,  1,  1,  0,  0,  1,  1, 1, 0,  0, 0, 0,   0,  0,  1, 1, 1, 0, 0, 0]
aux_pose_dict['joint_name'] = SPIN49_JOINT_NAMES[25:]

hand_dict = dict()
hand_dict['parent'] = [0, 1, 2, 3, 0, 5, 6, 7, 0, 9, 10, 11, 0, 13, 14, 15,0, 17, 18, 19]
hand_dict['child'] =  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,11, 12, 13,14,15, 16, 17,18, 19, 20]
hand_dict['joint_name'] = ['wrist', '5th_1', '5th_2', '5th_3', '5th_4',
                           '4th_1', '4th_2', '4th_3', '4th_4',
                           '3th_1', '3th_2', '3th_3', '3th_4',
                           '2th_1', '2th_2', '2th_3', '2th_4',
                           '1th_1', '1th_2', '1th_3', '1th_4']
# param and function for plot
lr_color = ['m', 'c']
