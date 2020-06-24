# StackGAN - Text to Photo-realistic Image Synthesis with Stacked Generative Adversarial Networks
## Dataset
* Image: [Caltech-UCSD Birds-200-2011](http://www.vision.caltech.edu/visipedia/CUB-200-2011.html)
* Text: [char-CNN-RNN text embedding](https://drive.google.com/file/d/0B3y_msrWZaXLT1BZdVdycDY5TEE/view)

## Usage
├─ project_folder (thư mục chứa dự án)<br>
&nbsp;&nbsp;&nbsp;&nbsp;├─ dataset<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ birds<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├─ images<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├─ domain1 (thư mục 1 loài chim)<br>
          ├─ aaa.jpg (hình ảnh loài chim)<br>
          ├─ bbb.jpg<br>
          ├─ ... <br>
        ├─ domain2<br>
          ├─ ccc.jpg (hình ảnh loài chim)<br>
          ├─ ddd.jpg<br>
          ├─ ... <br>
        ├─ domain3<br>
        ├─ ... <br>
      ├─ text<br>
        ├─ filename.pickle<br>
        ├─ class_infor.pickle<br>
  ├─ checkpoint<br>
    ├─ StackGAN_birds_gan_1adv_2kl<br>
      ├─ checkpoint<br>
      ├─ StackGAN.model.data-00000-of-00001<br>
      ├─ StackGAN.model.index<br>
      ├─ StackGAN.model.meta<br>
  ├─ imageSource<br>
    ├─ openfile.png<br>
    ├─ save.png<br>
    ├─ ... <br>
  ├─ buildGUI.py (chạy tệp tin này để chạy phần mềm)<br>
  ├─ utils.py<br>
  ├─ ops.py<br>
  ├─ StackGAN.py<br>
