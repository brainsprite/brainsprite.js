"""
Statistical map viewer
======================
Generate a brainsprite viewer for an activation map with an anatomical
background, by populating an html template.
"""

#%%
# First fetch the MNI high-resolution template and a functional statistical map.
from nilearn import datasets
anat = datasets.MNI152_FILE_PATH

# one motor contrast map from NeuroVault
motor_images = datasets.fetch_neurovault_motor_task()
stat_img = motor_images.images[0]

#%%
# We are going to use the same template and instruction as in the
# `plot_anat <plot_anat.html>`_ tutorial. The defaults are set for a functional
# map, so there is not much to do. We still tweak a couple parameters to get a
# clean map:
#
#  * apply a threshold to get rid of small activation (:code:`threshold`),
#  * reduce the opacity of the overlay to see the underlying anatomy (:code:`opacity`)
#  * Put a title inside the figure (:code:`title`)
#  * manually specify the cut coordinates (:code:`cut_coords`)
from brainsprite import brainsprite_viewer

viewer = brainsprite_viewer(stat_img, bg_img=anat, threshold=3,
                         opacity=0.5, title="plot_stat_map",
                         cut_coords=[36, -27, 66])

# In a Jupyter notebook, if ``view`` is the output of a cell, it will
# be displayed below the cell
viewer

#%%
# There are a lot more control one can use to modify the appearance of the
# brain viewer. Check the Python API for more information.
