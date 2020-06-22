# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####


# ----------------------------------------------------------
#
# External Utilities to be accessed by BlenderBIM, Archipack and other Addons
# Author:  Kevan Cress
#
# ----------------------------------------------------------


def blenderBIM_get_coords (context):
    dim_coords_list = []
   
    scene = context.scene
    sceneProps = scene.MeasureItArchProps

    # Display selected or all
    if scene.measureit_arch_gl_ghost is False:
        objlist = context.selected_objects
    else:
        objlist = context.view_layer.objects

    # ---------------------------------------
    # Generate all OpenGL calls
    # ---------------------------------------
    for myobj in objlist:
    
        #Stash Object Vertices for use in Draw functions
          
        if myobj.visible_get() is True:
            mat = myobj.matrix_world

            #if 'LineGenerator' in myobj and myobj.LineGenerator[0].line_num != 0:
            #    lineGen = myobj.LineGenerator[0]
            #    draw_line_group(context,myobj,lineGen,mat)

            #if 'AnnotationGenerator' in myobj and myobj.AnnotationGenerator[0].num_annotations != 0:
            #    annotationGen = myobj.AnnotationGenerator[0]
            #    draw_annotation(context,myobj,annotationGen,mat)

            if 'DimensionGenerator' in myobj:
                DimGen = myobj.DimensionGenerator[0]
                
                for alignedDim in DimGen.alignedDimensions:
                    dim_coords_list.append(get_dim_coords(context, myobj, DimGen, alignedDim, mat))

            #    for angleDim in DimGen.angleDimensions:
            #        draw_angleDimension(context, myobj, DimGen, angleDim,mat)
            #
            #    for axisDim in DimGen.axisDimensions:
            #        draw_axisDimension(context,myobj,DimGen,axisDim,mat)
                
            #    for boundsDim in DimGen.boundsDimensions:
            #        draw_boundsDimension(context,myobj,DimGen,boundsDim,mat)
                
            #    for arcDim in DimGen.arcDimensions:
            #        draw_arcDimension(context,myobj,DimGen,arcDim,mat)

            #    for areaDim in DimGen.areaDimensions:
            #        draw_areaDimension(context,myobj,DimGen,areaDim,mat)

def get_dim_coords(context, myobj, DimGen, dim, mat):
    pass