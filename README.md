# BanglaWriting: A multi-purpose Bangla offline-handwriting dataset

DOI Link: http://dx.doi.org/10.17632/r43wkvdk4w.1

Dataset Manual/Paper: https://arxiv.org/abs/2011.07499

The repository contains the python scripts to generate the converted images of the BanglaWriting dataset.

For more detailed information of the dataset, please see the [dataset manual](https://arxiv.org/abs/2011.07499).

### Description of the dataset

The BanglaWriting dataset contains single-page handwritings of 260 individuals of different personalities and ages. Each page includes bounding-boxes that bounds each word, along with the unicode representation of the writing. This dataset contains 21,234 words and 32,787 characters in total. Moreover, this dataset includes 5,470 unique words of Bangla vocabulary. Apart from the usual words, the dataset comprises 261 comprehensible overwriting and 450 incomprehensible overwriting. All of the bounding boxes and word labels are manually-generated. The dataset can be used for complex optical character/word recognition, writer identification, and handwritten word segmentation. Furthermore, this dataset is suitable for extracting age-based and gender-based variation of handwriting.

### Description of the code

The [convert_image](https://github.com/QuwsarOhi/BanglaWriting/blob/01be2bfe7ed30734affa8aae31f7ac256f0226a1/writingMod.py#L58) recieves an image path and returns an improved image.

An example of the input and output image is given.

![example](https://github.com/QuwsarOhi/BanglaWriting/blob/main/example.jpg)


## Cite the dataset

    @misc{https://doi.org/10.17632/r43wkvdk4w.1,
      doi = {10.17632/R43WKVDK4W.1},
      url = {https://data.mendeley.com/datasets/r43wkvdk4w/1},
      author = {{Mridha,  Dr. M. F.}},
      keywords = {Image Processing,  Optical Character Recognition,  Handwriting Recognition,  Handwriting,  Segmentation},
      title = {BanglaWriting: A multi-purpose offline Bangla handwriting dataset},
      publisher = {Mendeley},
      year = {2020}
    }


## Cite manual 

    @misc{2011.07499,
      Author = {M. F. Mridha and Abu Quwsar Ohi and M. Ameer Ali and Mazedul Islam Emon and Muhammad Mohsin Kabir},
      Title = {BanglaWriting: A multi-purpose offline Bangla handwriting dataset},
      Year = {2020},
      Eprint = {arXiv:2011.07499},
    }



## Cite this code

    @misc{banglawriting_script2020,
      author =       {Abu Quwsar Ohi},
      title =        {{BanglaWriting: A multi-purpose offline Bangla handwriting dataset (script)}},
      howpublished = {\url{https://github.com/QuwsarOhi/BanglaWriting}},
      year =         {2020}
    }
