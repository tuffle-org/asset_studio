# Asset Studio


## Setup for debian based destros
- Clone repo
```sh
git clone https://github.com/Tuffle-Org/asset_studio.git
```
- Install python, pip and venv
> Python 9+ may be available in you system
```sh
sudo apt update
sudo apt -y upgrade

python3 -v

# pip3
sudo apt install -y python3-pip

# if this is you first time using python I suggest these
sudo apt install build-essesntial libssl-dev libffi-dev python3-dev

# venv
sudo apt install python3-venv
```
- Create and Activate Virtual Env
```sh
#use python3 in virtual env and create .env directory
python3 -m venv .env | source .env/bin/activate
```
- You will need to install some dependencies for PySide6
```sh
# you can remove qtcreator qtchooser if you want
sudo apt install qtcreator qtbase5-dev qtchooser qt5-qmake qtbase5-dev-tools cmake

# these are important to run pyside6 application
sudo apt-get install '^libxcb.*-dev' libx11-xcb-dev libglu1-mesa-dev libxrender-dev libxi-dev libxkbcommon-dev libxkbcommon-x11-dev
```
- Install the requirements from `requirements.txt`
```sh
pip install -r  requirements.txt
```
- Run the application
```sh
python main.py
```


## Convert ui to py pyside6
```sh
pyside6-uic ui_file -o py_file
```