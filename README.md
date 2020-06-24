# StackGAN - Text to Photo-realistic Image Synthesis with Stacked Generative Adversarial Networks
## Processing
![processing](/imageSource/procesStackGans.jpg)
## Demo
[Video on youtube](https://youtu.be/ItSQF6OB5Ig)
## Dataset
* Image: [Caltech-UCSD Birds-200-2011](http://www.vision.caltech.edu/visipedia/CUB-200-2011.html)
* Text: [char-CNN-RNN text embedding](https://drive.google.com/file/d/0B3y_msrWZaXLT1BZdVdycDY5TEE/view)

## Usage
├─ project_folder (thư mục chứa dự án)<br>
&emsp;├─ dataset<br>
&emsp;&emsp;└─ birds<br>
&emsp;&emsp;&emsp;├─ images<br>
&emsp;&emsp;&emsp;&emsp;├─ domain1 (thư mục 1 loài chim)<br>
&emsp;&emsp;&emsp;&emsp;&emsp;├─ aaa.jpg (hình ảnh loài chim)<br>
&emsp;&emsp;&emsp;&emsp;&emsp;├─ bbb.jpg<br>
&emsp;&emsp;&emsp;&emsp;&emsp;├─ ... <br>
&emsp;&emsp;&emsp;&emsp;├─ domain2<br>
&emsp;&emsp;&emsp;&emsp;&emsp;├─ ccc.jpg (hình ảnh loài chim)<br>
&emsp;&emsp;&emsp;&emsp;&emsp;├─ ddd.jpg<br>
&emsp;&emsp;&emsp;&emsp;&emsp;├─ ... <br>
&emsp;&emsp;&emsp;&emsp;├─ domain3<br>
&emsp;&emsp;&emsp;&emsp;&emsp;├─ ... <br>
&emsp;&emsp;&emsp;├─ text<br>
&emsp;&emsp;&emsp;&emsp;├─ filename.pickle<br>
&emsp;&emsp;&emsp;&emsp;├─ class_infor.pickle<br>
&emsp;├─ checkpoint<br>
&emsp;&emsp;├─ StackGAN_birds_gan_1adv_2kl<br>
&emsp;&emsp;&emsp;├─ checkpoint<br>
&emsp;&emsp;&emsp;├─ StackGAN.model.data-00000-of-00001<br>
&emsp;&emsp;&emsp;├─ StackGAN.model.index<br>
&emsp;&emsp;&emsp;├─ StackGAN.model.meta<br>
&emsp;├─ imageSource<br>
&emsp;&emsp;├─ openfile.png<br>
&emsp;&emsp;├─ save.png<br>
&emsp;&emsp;├─ ... <br>
&emsp;├─ buildGUI.py (chạy tệp tin này để chạy phần mềm)<br>
&emsp;├─ utils.py<br>
&emsp;├─ ops.py<br>
&emsp;├─ StackGAN.py<br>


## Result
![bird1](/kq/chim1.png)
![bird2](/kq/chim2.png)
![bird3](/kq/ketqua.png)
