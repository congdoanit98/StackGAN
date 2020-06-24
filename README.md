# StackGAN - Text to Photo-realistic Image Synthesis with Stacked Generative Adversarial Networks
## Dataset
* Image: [Caltech-UCSD Birds-200-2011](http://www.vision.caltech.edu/visipedia/CUB-200-2011.html)
* Text: [char-CNN-RNN text embedding](https://drive.google.com/file/d/0B3y_msrWZaXLT1BZdVdycDY5TEE/view)

## Usage
├─ project_folder (thư mục chứa dự án)
  ├─ dataset
    └─ birds
      ├─ images
        ├─ domain1 (thư mục 1 loài chim)
          ├─ aaa.jpg (hình ảnh loài chim)
          ├─ bbb.jpg
          ├─ ...
        ├─ domain2
          ├─ ccc.jpg (hình ảnh loài chim)
          ├─ ddd.jpg
          ├─ ...
        ├─ domain3
        ├─ ...
      ├─ text
        ├─ filename.pickle
        ├─ class_infor.pickle
  ├─ checkpoint
    ├─ StackGAN_birds_gan_1adv_2kl
      ├─ checkpoint
      ├─ StackGAN.model.data-00000-of-00001
      ├─ StackGAN.model.index
      ├─ StackGAN.model.meta
  ├─ imageSource
    ├─ openfile.png
    ├─ save.png
    ├─ ...
  ├─ buildGUI.py (chạy tệp tin này để chạy phần mềm)
  ├─ utils.py
  ├─ ops.py
  ├─ StackGAN.py
