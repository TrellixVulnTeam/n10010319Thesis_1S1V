# The following program automates the process of 
# importing a selection of models into Blender, 
# appending a random motion capture sequence onto 
# the mode, superimposing this on a background image,
# then exporting the animation to a file 

# Input your main directory here. Desktop was used.
home_directory = "C:/Users/n10010319/Desktop"

# Navigate to your main directory 
# cd "C:/Users/n10010319/Desktop"

# Run the program through the command line
# blender.lnk C:/Users/n10010319/Desktop/gen_template.blend --python C:/Users/n10010319/Desktop/generation.py


# Desktop
# │   README.md
# │   gen_template.blend  
# |   generation.py  
# |
# └───FinalVideos
# │
# └───Models
# │   │   mademodel01.bvh
# │   │   mademodel02.bvh
# │   │   mademodel03.bvh
# │   │   mademodel04.bvh
# │   │   mademodel05.bvh
# │       ...
# │
# └───Mocap
# │   │   file00.bvh
# │   │   file01.bvh
# │   │   file02.bvh
# │   │   file03.bvh
# │   │   file04.bvh
# │       ...
# │   
# └───Images
#     │   pictureofgoats.jpg
#     │   randomname1.png
#     │   randomname2.png
#     │   randomname3.png
#     │   randomname4.png
#     │   randomname5.png
#         ...
# ```

import random
import os, bpy
import time

# Following the directories specified above
model_directory = home_directory + "/ModelsLite"
mocap_directory = home_directory + "/Mocap"
image_directory = home_directory + "/Images"
video_directory = home_directory + "/FinalVideos"


def modelling(file_name, placeholder):
    # For debugging purposes
    # bpy.app.debug_wm = True

    # SELECT RANDOM MODEL===================================================================================
    # A random model is selected from the options
    # If the textures file is selected, the program
    # is ran again from the ground, and the randomised
    # values generated again.
    selected_model = random.choice(os.listdir(model_directory))
    print("RANDOM MODEL============" + selected_model)

    if selected_model == "textures":
        selected_model = random.choice(os.listdir(model_directory))
    print("SELECTED MODEL============" + selected_model)
    
    # To modify the generated model, the .mxh must be removed.
    capital_selected_model = selected_model[:-5].capitalize()
    print("OBJECT============" + capital_selected_model)

    # The random model is imported into the Blender workspace.
    bpy.ops.import_scene.makehuman_mhx2(filepath=model_directory+"/"+selected_model, useOverride=True)

    # Set the model as an active object
    bpy.ops.object.mode_set(mode='OBJECT')
    bpy.context.scene.objects.active = bpy.data.objects[capital_selected_model]

    # GRAFT ANIMATION ONTO MODEL===========================================================================
    # A random bvh file is selected from the directory
    selected_mocap = random.choice(os.listdir(mocap_directory))


    # The file is loaded and retargeted onto the model
    bpy.ops.mcp.load_and_retarget(filepath=mocap_directory+"/"+selected_mocap)


    # APPEND BACKGROUND TO VIDEO===========================================================================
    
    img_path = image_directory + "/" + random.choice(os.listdir(image_directory))

    img = bpy.data.images.load(img_path, check_existing=True)  # Load the image in data
    node_tree = bpy.context.scene.node_tree  # Get the current scene's compositor node tree
    img_comp_node = node_tree.nodes.get('Image')
    if img_comp_node:
        img_comp_node.image = img

    # ANIMATE==============================================================================================
    # Changes can be made in the template file. These 
    # change will be applied across the entire database.
    bpy.ops.render.render(animation=True)

    # The name of the file is changed from the general output 
    # to the name of the model + its mocap sequence
    os.rename(video_directory+"/0001-0045.mkv", video_directory+"/"+capital_selected_model + "mocap"+ selected_mocap[:-4]+".mkv")


    # The model object is then delete to allow for the nect one
    # to be made in its place
    bpy.ops.object.mode_set(mode='OBJECT')
    bpy.data.objects[capital_selected_model].select = True
    for child in bpy.data.objects[capital_selected_model].children:
        child.select = True
    bpy.ops.object.delete()


# # Testing Purposes
# modelling(model_directory+"/blending0001.mhx2", model_directory+"/blending0001.mhx2")


for filename in os.listdir(model_directory):
    placeholder = filename 
    modelling(filename, placeholder)

#  Close Blender 
bpy.ops.wm.quit_blender()
