"""
Copyright (C) 2019 Grant Wilk

This file is part of Atomic Data Manager.

Atomic Data Manager is free software: you can redistribute
it and/or modify it under the terms of the GNU General Public License
as published by the Free Software Foundation, either version 3 of the
License, or (at your option) any later version.

Atomic Data Manager is distributed in the hope that it will
be useful, but WITHOUT ANY WARRANTY; without even the implied warranty
of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
General Public License for more details.

You should have received a copy of the GNU General Public License along
with Atomic Data Manager.  If not, see <https://www.gnu.org/licenses/>.
"""

import bpy
from bpy.utils import register_class, unregister_class
from atomic_data_manager.ops.utils import clean, nuke
from atomic_data_manager.ui.utils import ui_layouts, blendstats


# Atomic Data Manager Nuke Operator
class DATAMGR_OT_nuke(bpy.types.Operator):
    """Removes all data from the selected categories"""
    bl_idname = "datamgr.nuke"
    bl_label = "CAUTION!"

    def draw(self, context):
        dmgr = bpy.context.scene.datamgr
        layout = self.layout

        col = layout.column()
        col.label(text="Remove the following data-blocks?")

        # No Data Section
        if not (dmgr.collections or dmgr.images or dmgr.lights or dmgr.materials
                or dmgr.node_groups or dmgr.particles or dmgr.textures or dmgr.worlds):

            ui_layouts.box_list(
                layout=layout,
            )

        # Collections Section
        if dmgr.collections and len(bpy.data.collections) != 0:
            collections = sorted(bpy.data.collections.keys())
            ui_layouts.box_list(
                layout=layout,
                title="Collections",
                items=collections,
                icon="OUTLINER_OB_GROUP_INSTANCE"
            )

        # Images Section
        if dmgr.images and len(bpy.data.images) != 0:
            images = sorted(bpy.data.images.keys())
            ui_layouts.box_list(
                layout=layout,
                title="Images",
                items=images,
                icon="IMAGE_DATA"
            )

        # Lights Section
        if dmgr.lights and len(bpy.data.lights) != 0:
            lights = sorted(bpy.data.lights.keys())
            ui_layouts.box_list(
                layout=layout,
                title="Lights",
                items=lights,
                icon="OUTLINER_OB_LIGHT"
            )

        # Materials Section
        if dmgr.materials and len(bpy.data.materials) != 0:
            materials = sorted(bpy.data.materials.keys())
            ui_layouts.box_list(
                layout=layout,
                title="Materials",
                items=materials,
                icon="MATERIAL"
            )

        # Node Group Section
        if dmgr.node_groups and len(bpy.data.node_groups) != 0:
            node_groups = sorted(bpy.data.node_groups.keys())
            ui_layouts.box_list(
                layout=layout,
                title="Node Groups",
                items=node_groups,
                icon="NODETREE"
            )

        # Particles Section
        if dmgr.particles and len(bpy.data.particles) != 0:
            particles = sorted(bpy.data.particles.keys())
            ui_layouts.box_list(
                layout=layout,
                title="Particle Systems",
                items=particles,
                icon="PARTICLES"
            )

        # Textures Section
        if dmgr.textures and len(bpy.data.textures) != 0:
            textures = sorted(bpy.data.textures.keys())
            ui_layouts.box_list(
                layout=layout,
                title="Textures",
                items=textures,
                icon="TEXTURE"
            )

        # Worlds Section
        if dmgr.worlds and len(bpy.data.worlds) != 0:
            worlds = sorted(bpy.data.worlds.keys())
            ui_layouts.box_list(
                layout=layout,
                title="Worlds",
                items=worlds,
                icon="WORLD"
            )

        row = layout.row()  # extra spacing

    def execute(self, context):
        dmgr = bpy.context.scene.datamgr

        if dmgr.collections:
            nuke.collections()
        if dmgr.images:
            nuke.images()
        if dmgr.lights:
            nuke.lights()
        if dmgr.materials:
            nuke.materials()
        if dmgr.node_groups:
            nuke.node_groups()
        if dmgr.particles:
            nuke.particles()
        if dmgr.textures:
            nuke.textures()
        if dmgr.worlds:
            nuke.worlds()

        bpy.ops.datamgr.deselect_all()

        return {'FINISHED'}

    def invoke(self, context, event):
        wm = context.window_manager
        return wm.invoke_props_dialog(self)


# Atomic Data Manager Clean Operator
class DATAMGR_OT_clean(bpy.types.Operator):
    """Automatically removes all user-less data from the selected categories"""
    bl_idname = "datamgr.clean"
    bl_label = "Clean"

    def draw(self, context):
        dmgr = bpy.context.scene.datamgr
        layout = self.layout

        col = layout.column()
        col.label(text="Remove the following data-blocks?")

        # No Data Section
        if not (dmgr.collections or dmgr.images or dmgr.lights or dmgr.materials
                or dmgr.node_groups or dmgr.particles or dmgr.textures or dmgr.worlds):

            ui_layouts.box_list(
                layout=layout,
            )

        # Collections Section
        if dmgr.collections and len(blendstats.get_unused_collections()) != 0:
            collections = sorted(blendstats.get_unused_collections())
            ui_layouts.box_list(
                layout=layout,
                title="Collections",
                items=collections,
                icon="OUTLINER_OB_GROUP_INSTANCE"
            )

        # Images Section
        if dmgr.images and len(blendstats.get_unused_images()) != 0:
            images = sorted(blendstats.get_unused_images())
            ui_layouts.box_list(
                layout=layout,
                title="Images",
                items=images,
                icon="IMAGE_DATA"
            )

        # Lights Section
        if dmgr.lights and len(blendstats.get_unused_lights()) != 0:
            lights = sorted(blendstats.get_unused_lights())
            ui_layouts.box_list(
                layout=layout,
                title="Lights",
                items=lights,
                icon="OUTLINER_OB_LIGHT"
            )

        # Materials Section
        if dmgr.materials and len(blendstats.get_unused_materials()) != 0:
            materials = sorted(blendstats.get_unused_materials())
            ui_layouts.box_list(
                layout=layout,
                title="Materials",
                items=materials,
                icon="MATERIAL"
            )

        # Node Group Section
        if dmgr.node_groups and len(blendstats.get_unused_node_groups()) != 0:
            node_groups = sorted(blendstats.get_unused_node_groups())
            ui_layouts.box_list(
                layout=layout,
                title="Node Groups",
                items=node_groups,
                icon="NODETREE"
            )

        # Particles Section
        if dmgr.particles and len(blendstats.get_unused_particles()) != 0:
            particles = sorted(blendstats.get_unused_particles())
            ui_layouts.box_list(
                layout=layout,
                title="Particle Systems",
                items=particles,
                icon="PARTICLES"
            )

        # Textures Section
        if dmgr.textures and len(blendstats.get_unused_textures()) != 0:
            textures = sorted(blendstats.get_unused_textures())
            ui_layouts.box_list(
                layout=layout,
                title="Textures",
                items=textures,
                icon="TEXTURE"
            )

        # Worlds Section
        if dmgr.worlds and len(blendstats.get_unused_worlds()) != 0:
            worlds = sorted(blendstats.get_unused_worlds())
            ui_layouts.box_list(
                layout=layout,
                title="Worlds",
                items=worlds,
                icon="WORLD"
            )

        row = layout.row()  # extra spacing

    def execute(self, context):
        dmgr = bpy.context.scene.datamgr

        if dmgr.collections:
            clean.collections()
        if dmgr.images:
            clean.images()
        if dmgr.lights:
            clean.lights()
        if dmgr.materials:
            clean.materials()
        if dmgr.node_groups:
            clean.node_groups()
        if dmgr.particles:
            clean.particles()
        if dmgr.textures:
            clean.textures()
        if dmgr.worlds:
            clean.worlds()

        bpy.ops.datamgr.deselect_all()

        return {'FINISHED'}

    def invoke(self, context, event):
        wm = context.window_manager
        return wm.invoke_props_dialog(self)


# Atomic Data Manager Undo Operator
class DATAMGR_OT_undo(bpy.types.Operator):
    """Undoes the previous action"""
    bl_idname = "datamgr.undo"
    bl_label = "Undo"

    def execute(self, context):
        bpy.ops.ed.undo()
        return {'FINISHED'}


# Atomic Data Manager Smart Select Operator
class DATAMGR_OT_smart_select(bpy.types.Operator):
    """Auto-select categories with user-less data"""
    bl_idname = "datamgr.smart_select"
    bl_label = "Smart Select"

    def execute(self, context):
        data = bpy.data

        bpy.context.scene.datamgr.collections = any(len(collection.all_objects.values()) == 0 for collection in data.collections)
        bpy.context.scene.datamgr.images = any(image.users == 0 for image in data.images)
        bpy.context.scene.datamgr.lights = any(lights.users == 0 for lights in data.lights)
        bpy.context.scene.datamgr.materials = any(material.users == 0 for material in data.materials)
        bpy.context.scene.datamgr.node_groups = any(node_group.users == 0 for node_group in data.node_groups)
        bpy.context.scene.datamgr.particles = any(particle.users == 0 for particle in data.particles)
        bpy.context.scene.datamgr.textures = any(texture.users == 0 for texture in data.textures)
        bpy.context.scene.datamgr.worlds = any(world.users == 0 for world in data.worlds)

        return {'FINISHED'}


# Atomic Data Manager Select All Operator
class DATAMGR_OT_select_all(bpy.types.Operator):
    """Selects all categories"""
    bl_idname = "datamgr.select_all"
    bl_label = "Select All"

    def execute(self, context):
        bpy.context.scene.datamgr.collections = True
        bpy.context.scene.datamgr.images = True
        bpy.context.scene.datamgr.lights = True
        bpy.context.scene.datamgr.materials = True
        bpy.context.scene.datamgr.node_groups = True
        bpy.context.scene.datamgr.particles = True
        bpy.context.scene.datamgr.textures = True
        bpy.context.scene.datamgr.worlds = True
        return {'FINISHED'}


# Atomic Data Manager Deselect All Operator
class DATAMGR_OT_deselect_all(bpy.types.Operator):
    """Deselects all categories"""
    bl_idname = "datamgr.deselect_all"
    bl_label = "Deselect All"

    def execute(self, context):
        bpy.context.scene.datamgr.collections = False
        bpy.context.scene.datamgr.images = False
        bpy.context.scene.datamgr.lights = False
        bpy.context.scene.datamgr.materials = False
        bpy.context.scene.datamgr.node_groups = False
        bpy.context.scene.datamgr.particles = False
        bpy.context.scene.datamgr.textures = False
        bpy.context.scene.datamgr.worlds = False

        return {'FINISHED'}


reg_list = [DATAMGR_OT_nuke,
            DATAMGR_OT_clean,
            DATAMGR_OT_undo,
            DATAMGR_OT_smart_select,
            DATAMGR_OT_select_all,
            DATAMGR_OT_deselect_all]


def register():
    for item in reg_list:
        register_class(item)


def unregister():
    for item in reg_list:
        unregister_class(item)
