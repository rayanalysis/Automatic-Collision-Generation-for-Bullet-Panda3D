'''
BSD 3-Clause License

Copyright (c) 2019, Logan Bier.
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

* Redistributions of source code must retain the above copyright notice, this
  list of conditions and the following disclaimer.

* Redistributions in binary form must reproduce the above copyright notice,
  this list of conditions and the following disclaimer in the documentation
  and/or other materials provided with the distribution.

* Neither the name of the copyright holder nor the names of its
  contributors may be used to endorse or promote products derived from
  this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
'''
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
