# Note for the generation.py
You must change the os.rename fuction slightly to match whatever number of frames you are rendering.
50 frames? You'll change the "0001-0045.mkv" to "0001-0050.mkv"

# Generating Synthetic Data for use with Convolutional Neural Networks

The following program automates the process of 
importing a selection of models into Blender, 
appending a random motion capture sequence onto 
the mode, superimposing this on a background image,
then exporting the animation to a file 

# 1. Input your main directory here. Desktop was used.
`home_directory = "C:/Users/n10010319/Desktop"`

# 2. Navigate to your main directory 
`cd "C:/Users/n10010319/Desktop"`

# 3. Run the program through the command line
`blender.lnk C:/Users/n10010319/Desktop/gen_template.blend --python C:/Users/n10010319/Desktop/generation.py`

```
Desktop
│ README.md
│ gen_template.blend | generation.py
|
└───FinalVideos
│
└───Models
│ │ mademodel01.bvh
│ │ mademodel02.bvh
│ │ mademodel03.bvh
│ │ mademodel04.bvh
│ │ mademodel05.bvh
│ ...
│
└───Mocap
│ │ file00.bvh
│ │ file01.bvh
│ │ file02.bvh
│ │ file03.bvh
│ │ file04.bvh
│ ...
│
└───Images
│ pictureofgoats.jpg
│ randomname1.png
│ randomname2.png
│ randomname3.png
│ randomname4.png
│ randomname5.png
```
