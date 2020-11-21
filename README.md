# frankmocap_notebooks
- This repository is to use the [FrankMocap](https://github.com/facebookresearch/frankmocap) easier.. (MAYBE)

# Preparation
0. Prepare Ubuntu 18.04+ and Anaconda
1. Clone this Repository and [FrankMocap](https://github.com/facebookresearch/frankmocap)
  ```
  git clone https://github.com/cotton-ahn/frankmocap_notebooks
  cd frankmocap_notebooks
  git clone https://github.com/facebookresearch/frankmocap
  ```
2. Install the [FrankMocap](https://github.com/facebookresearch/frankmocap) as the official document says
* When training, you may face error related to "opendr" installation
- If ERRROR MSG goes like
  * Collect2: error: ld returned 1 exit status // Error: command ‘gcc’ failed with exit status 1
  * TRY below line : [source](https://github.com/openai/mujoco-py/issues/284)
  ```
  sudo apt-get install libosmesa6-dev
  ```
  
3. Try to run below to check whether the result is valid.
  ```
  cd ./frankmocap
  conda activate venv_frankmocap
  python -m demo.demo_bodymocap --input_path ./sample_data/han_short.mp4 --out_dir ./mocap_output
  ```
4. Replace ./copy_and_paste.py and ./demo_frankmocap.py
  ```
  cd $(THIS REPOSITORY)
  cp ./copy_and_paste.py ./frankmocap/integration
  cp ./demo_frankmocap ./frankmocap/demo
  ```
  
5. Prepare the jupyter notebook, and add the venv_frankmocap to the ipykernel
  ```
  pip install ipykernel jupyter
  python -m ipykernel install --user --name=venv_frankmocap
  ```
6. Install moviepy
  ```
  pip install moviepy
  ```
7. Run Jupyter Notebook in this repository
  ```
  cd $(THIS REPOSITORY)
  jupyter notebook
  ```
  
# How to Use
- Put videos that you want to process, to ./videos (config.video_dir)
  * Or, you can write down the YouTube Links on ./video_url.txt
  * Then, Run 00_process_youtube_videos.ipynb
  * Videos will be saved to ./videos, image frames will be saved to ./images (config.image_dir)
- Run 01_extract_mocap_results.
  * Results will be saved to ./mocaps (config.mocap_dir)
    - If config.read_type == 'videos', video files in ./videos will be used as inputs to the frankmocap
    - If config.read_type == 'images', images in ./images will be used as inputs to the frankmocap
  * In ./mocaps, folders with video's name will be generated, and results will be saved.
- Run 02_preprocess_mocap_result
  * This notebook organizes results into some .pkl and .npz files.
  * .pkl files will be saved to ./skeletons_pkl (config.skeletons_pkl_dir)
  * .npz files will be saved to ./skeletons_npz (config.skeletons_npz_dir)
- See the result with 03_visualize_processed_pkl_and_npz.
  * After loading pickle file, you will see the dictionary
    - KEY : 'open_pose', 'aux_pose', 'simple_pose', 'left_hand', 'right_hand', 'hand_info', 'heel_info', 'head_info'
    - Try to check the pickle file by yourself.
  * After loading .npz file, you will see an 87-dimensional array.
    - 0 ~ 45 (45) : 'simple_pose' in pickle file, the pose which size was 15 by 3
    - 45~ 51 (6)  : (3) head pose (3) head orientation
    - 51 ~ 63 (12): left hand thumb vector(3), index vector(3), palm vector(3), wrist pos(3)
    - 63 ~ 75 (12): right hand thumb vector(3), index vector(3), palm vector(3), wrist pos(3)
    - 75 ~ 87 (12): left heel pos (3), left foot vec (3), right heel pos (3), right foot vec (3)
