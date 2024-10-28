# Análisis de Redes: Representación y Cálculo de Caminos Más Cortos Usando Grafos
This script represents and calculates the shortest path between two nodes using Dijkstra
- [Requirements](#requirements)
- [Installation](#installation)
- [Use](#use)
- [Unit Tests](#UnitTests)
- [License](#license)

### Requirements
This is a list of the libraries used in this code:
- contourpy==1.3.0
- cycler==0.12.1
- fonttools==4.54.1
- kiwisolver==1.4.7
- matplotlib==3.9.2
- networkx==3.4.2
- numpy==2.1.2
- packaging==24.1
- pillow==11.0.0
- pyparsing==3.2.0
- python-dateutil==2.9.0.post0
- six==1.16.0

### Installation
Below is the process installation for each package and the Python script, for this you must have already installed git [Click here to install git](https://git-scm.com/downloads) and Python [Click here to install Python](https://www.python.org/downloads/).
|Steps|Description|
|-|-|
Step 1|Open your code editor and open up a new terminal
Step 2|Install graphs library (networkx), therefore, copy and paste the below command:<br>```pip install networkx```
Step 3|Install the library for visualization (matplotlib), therefore, copy and paste the below command:<br>```pip install matplotlib```
Step 4|Pull the Python Script into your folder, please copy and paste this command:<br>```git clone https://github.com/luisca12/Proyecto-Investigacion.git```

NOTE: If step 4 fails, please check that you have Git installed.

### Use
Once the Python script is loaded into your code editor program you will notice the following Python files:
- functions.py
- graphDef.py
- utils.py
- log.py
- main.py
- strings.py

To run the program you will need to go to main.py and run it from there.
#### Instructions to use it
1. You will be prompted to the following menu where you have to first choose option #1 to choose the number of images to download.
```
        --------------------------------------------------
          Welcome to the automatic modify images program
        --------------------------------------------------
  --------------------------------------------------------------
                Menu - Please choose an option
                  Only numbers are accepted
  --------------------------------------------------------------
  >             Paso #1. Escoger la cantidad de imagenes       <
  >             Paso #2. Modificar las imagenes                <
  >             Paso #3. Ingresar el correo destinatario       <
  >             Paso #4. Salir                                 <
  --------------------------------------------------------------

Please choose a number from 1 to 4:
```
2. Once you have chosen the number of images to download, choose option number 2 to modify each individual image.
```
  -------------------------------------------------------------- 
                Menu - Please choose an option
                  Only numbers are accepted
  -------------------------------------------------------------- 
  >             Paso #1. Escoger la cantidad de imagenes       <
  >             Paso #2. Modificar las imagenes                <
  >             Paso #3. Ingresar el correo destinatario       <
  >             Paso #4. Salir                                 <
  --------------------------------------------------------------

Please choose a number from 1 to 4: 2
Do you want to modify the image number 1? (y/n):y
Do you want to make the image black and white? (y/n):y
Do you want to transpose the image? (y/n):y
Do you want to blur the image? (y/n):y
Do you want to rotate 90 degress the image? (y/n):y
```
3. Once you have modified all the images, please choose option number 3 to input the destination email to send the final images.
```
  --------------------------------------------------------------
                Menu - Please choose an option
                  Only numbers are accepted
  --------------------------------------------------------------
  >             Paso #1. Escoger la cantidad de imagenes       <
  >             Paso #2. Modificar las imagenes                <
  >             Paso #3. Ingresar el correo destinatario       <
  >             Paso #4. Salir                                 <
  --------------------------------------------------------------

Please choose a number from 1 to 4: 3
Please enter your email:example@gmail.com
```
4. Please repeat this process to download/modify more images, otherwise, please choose option 4 to exit the program.

### UnitTests
To run the unit tests inside this Python script please follow these steps:
|Steps|Description|
|-|-|
Step 1|Search and open CMD
Step 2|Using the command "cd" please navigate to where your code is, for example:<br><p align="center"><img src="https://www.wikihow.com/images/thumb/0/08/Change-Directories-in-Command-Prompt-Step-7-Version-2.jpg/v4-460px-Change-Directories-in-Command-Prompt-Step-7-Version-2.jpg.webp" alt="dir-image"></p><br>You may also use the command "dir" to view all the files inside the current directory<br><p align="center"><img src="https://upload.wikimedia.org/wikipedia/commons/5/52/Comando_Dir_no_Prompt_do_Windows.png" alt="dir-image"></p>
Step 3|Once you are inside the Python Script folder please copy and paste the following command <br>```python -m unittest discover -s tests```

### License
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.