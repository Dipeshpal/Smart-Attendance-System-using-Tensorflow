# Smart-Attendance-System

Smart Attendance System is the way to modernized the existing method of marking attendance on register. It helps to reduce complexity of management. Smart Attendance System not only provide record of attendance of student, it uses Machine Learning technique to identify person facial details to mark attendance on database and it can also perform statistical analysis of student data and provide recommendation to student. It is smart because it provide attendance record to student, teacher and admin in digitalize ways.

## Note: We have OpenCV version of this project also-
In OpenCV version we used OpenCV to train the model but due to less accuracy in real world implementation we used tensorflow.
If you want to just explore OpenCV version then just [click here](https://github.com/Dipeshpal/Smart-Attendance-System)

### What this project is all about?
 This project is all about attendance management sysetm in digitilize ways by using Facial Recognition with the help of Machine Learning.
 
## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

I am using [miniconda](https://conda.io/en/latest/miniconda.html) and [Python 3.6.6](https://www.python.org/). Make sure you have miniconda /  anaconda or Python installed.
Recommended Prerequisites- 
* Miniconda or
* Python 3.x

Install following (You can install latest versions)

* Django==2.1.7
* django-pagedown==1.0.6
* tensorflow==1.13.1
* numpy==1.16.3
* opencv-contrib-python==4.0.0.21
* opencv-python==3.4.0.14
* Pillow==5.4.1
* pytz==2018.9
* scikit-learn==0.20.2
* scipy==1.2.1
* xlrd==1.2.0

You can install all these with "requirements.txt" file.
Just Run following command in terminal-

```
pip install -r requirements.txt
```
You can install all these in your virtual environment or directly in your system interpreter.


### How to use this project?

Once you install these in your machine then just run project.

#### How to run project?
Just go to your project root folder "Toto-Smart-Attendance-System". Then change directory to "Toto_Smart_Attendance_System" folder and now open command prompt/Terminal and then run following command-

   ```
   python manage.py runserver
   ```
    
It will start server in your local  machine. Now just hit your local server ip provided by the project in you terminal and just start using project.
    
You may need to create superuser to explore all functionality.

#### How to create your own dataset for image training?
To train your own dataset or faces you need to upload excel sheet in this website. [You can subl=mit data in various ways but because we don't want to use any physical hardware to submit data or don't want to spent money on anything thats why we will submit excel file to train the model or create our own dataset]
1. <b>Just run the project and now login as admin (you need to create superuser first).</b>
2. <b/>Go to cpanel in website and upload excel sheet.</b>
   
   <p align="center">Cpanel-</p>
      <p align="center">
          <img src="(https://i.ibb.co/WkMd3jY/m-Screenshot.png" alt="Image" width="750px" height="350px" />
      </p>


3. <b>How to create excel sheet?</b>
 
   3.1 <b>Upload some videos to google drive and get links of all the videos (permission: anyone with the link)</b>
   
      <p align="center">Upload Videos-</p>
      <p align="center">
          <img src="https://i.ibb.co/z85q9M2/Screenshot-29.png" alt="Image" width="750px" height="350px" />
      </p>
      
      <p align="center">Set Permission-</p>
      <p align="center">
          <img src="https://i.ibb.co/2Kf48g0/Screenshot-30.png" alt="Image" width="750px" height="350px" />
      </p>
  
      <p align="center">Copy links of videos-</p>
      <p align="center">
          <img src="https://i.ibb.co/XJFHG8C/Screenshot-31.png" alt="Image" width="750px" height="350px" />
      </p>

   3.2 <b>Now paste these screenshot in excel file ([Downlaod Sample Excel File](https://github.com/Dipeshpal/Smart-Attendance-System-using-Tensorflow/blob/master/sv.xlsx))</b>
   
      In this sheet you have to enter Name, Roll Number and Video's Link. It conatains 3 Columns (Name,	Roll Number,	Video).

      <b style="color:red">DO NOT CHANGE ANY COLUMN NAME or DO NOT ADD ANY COLUMN</b>

      <b>You can add as many rows you want</b>

      Refer screenshot below-

      <p align="center">
          <img src="https://i.ibb.co/Vmzs9ky/Screenshot-32.png" alt="Image" width="750px" height="350px" />
      </p>

   3.3 <b>Once you create excel sheet now upload it. After uploading you will get button to start training. Just click on "Start Training". Your training will started, it may take some time depending on your video's length (20-30 second video is enough). Once training is done you will get success message. While training you can go to Command Prompt and see the status.</b>


#### How to check / recognize face-
You can click potos of face and upload it to website manually (If you upload single image at a time then their is less possibility of face detection) or you can directly capture images by using your webcamera (Recommended: Beacuse it capture multiple images at a time which increase possibility of marking attendance by recognize face in images).

1. Just go "Mark Attendance" and submit image or use camera to capture image.

   <p align="center">
          <img src="https://i.ibb.co/ssy30mC/Screenshot-33.png" alt="Image" width="750px" height="350px" />
   </p>

If you want to know backend of Tensorflow used in this project then just [click here](https://codelabs.developers.google.com/codelabs/tensorflow-for-poets/#0)
    

# Features of Smart Attendance System-
* It provide attendance management system.
* It use mark attendance with user captured photo/image only.
* Admin just have to provide excel sheet in this format ([Click Here](https://github.com/Dipeshpal/Toto-Smart-Attendance-System/blob/master/sv.xlsx) to see the format) to server [Upload excel to server].
* It will download videos and create dataset for training and testing, and create model for it.
* It provide roles to user. Admin, Teacher and Student. Admin can do anything, Teacher can mark attendance and check attendance, Student can check attendance only.
* It let admin to create/update/delete article also.

# Technology used-
1. Python
2. Machine Learning
3. Django
4. Tensorflow
5. OpenCV
6. Sklearn
7. Numpy
8. Sqlite
9. HTML, CSS, JavaScripts, Bootstrap, Jquery

# Any questions?
Feel free to contact me

# License-
You have to give me credit.

You can add following lines in your project/code/videos/document to give me credit.

```
Credit: Dipesh Pal
Project is originally developed by Dipesh Pal.
github.com/Dipeshpal
www.dipeshpal.com
www.youtube.com/DipeshPal17
```

You can thanks me by Subscribe me on YouTube: [Subscribe](www.youtube.com/DipeshPal17)
