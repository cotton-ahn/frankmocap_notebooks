# frankmocap_notebooks
- This repository is to use the [FrankMocap](https://github.com/facebookresearch/frankmocap) easier.. (MAYBE)

# How to use
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
  4. Prepare the jupyter notebook, and add the venv_frankmocap to the ipykernel
  ```
  pip install ipykernel jupyter
  python -m ipykernel install --user --name=venv_frankmocap
  ```
  5. Install moviepy
  ```
  pip install moviepy
  ```
  6. Run Jupyter Notebook in this repository
  ```
  cd $(THIS REPOSITORY)
  jupyter notebook
  ```
  
  
