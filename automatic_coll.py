# Copyright (C) 2020 Logan Bier. All rights reserved.

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.  
        
        def make_collision_from_model(input_model, world):
            # tristrip generation from static models
            # generic tri-strip collision generator begins
            geom_nodes = input_model.findAllMatches('**/+GeomNode')
            geom_nodes = geom_nodes.getPath(0).node()
            # print(geom_nodes)
            geom_target = geom_nodes.getGeom(0)
            # print(geom_target)
            output_bullet_mesh = BulletTriangleMesh()
            output_bullet_mesh.addGeom(geom_target)
            tri_shape = BulletTriangleMeshShape(output_bullet_mesh, dynamic=False)
            print(output_bullet_mesh)

            body = BulletRigidBodyNode('input_model_tri_mesh')
            np = self.render.attachNewNode(body)
            np.node().addShape(tri_shape)
            np.node().setMass(0)
            np.node().setFriction(0.5)
            np.setPos(-500, -500, 800)
            np.setR(90)
            np.setScale(1)
            np.setCollideMask(BitMask32.allOn())
            world.attachRigidBody(np.node())
        
        make_collision_from_model(access_deck_1, world)  # world = BulletWorld()
