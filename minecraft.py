from raytracer import *
from gl import *
from plane import *
from cube import *
from sphere import *

cuality = int(input("Ingrese el nivel de detalle (100 - 1000): "))

r = Raytracer(cuality, cuality)

r.light = Light(
    position=V3(-20, 20, 20),
    intensity=2
)

water = Material(diffuse=color(51, 83, 152), albedo=(
    0.6, 0.3, 0.1, 0), spec=50, refractive_index=2)
dirt = Material(diffuse=color(97, 51, 24), albedo=(
    0.9, 0.1, 0, 0), spec=50)
wood = Material(diffuse=color(202, 164, 114), albedo=(
    0.9, 0.1, 0, 0), spec=50)
darkWood = Material(diffuse=color(149, 69, 53), albedo=(
    0.9, 0.1, 0, 0), spec=50)
steel = Material(diffuse=color(50, 50, 50), albedo=(
    0.6, 0.3, 0.1, 0), spec=50, refractive_index=1.5)


r.scene.append(Cube(V3(0, -3, -2), 4, water))
r.scene.append(Cube(V3(0, -0.75, -4), 0.5, dirt))
r.scene.append(Cube(V3(0.5, -0.75, -4), 0.5, dirt))
r.scene.append(Cube(V3(1, -0.75, -4), 0.5, dirt))
r.scene.append(Cube(V3(1.5, -0.75, -4), 0.5, dirt))
r.scene.append(Cube(V3(2, -0.75, -4), 0.5, dirt))
r.scene.append(Cube(V3(2.5, -0.75, -4), 0.5, dirt))
r.scene.append(Cube(V3(-0.5, -0.75, -4), 0.5, dirt))
r.scene.append(Cube(V3(-1, -0.75, -4), 0.5, dirt))
r.scene.append(Cube(V3(-1.5, -0.75, -4), 0.5, dirt))
r.scene.append(Cube(V3(-2, -0.75, -4), 0.5, dirt))

r.scene.append(Cube(V3(0, -0.75, -4.25), 0.5, dirt))
r.scene.append(Cube(V3(0.5, -0.75, -4.25), 0.5, dirt))
r.scene.append(Cube(V3(1, -0.75, -4.25), 0.5, dirt))
r.scene.append(Cube(V3(1.5, -0.75, -4.25), 0.5, dirt))
r.scene.append(Cube(V3(2, -0.75, -4.25), 0.5, dirt))
r.scene.append(Cube(V3(2.5, -0.75, -4.25), 0.5, dirt))
r.scene.append(Cube(V3(-0.5, -0.75, -4.25), 0.5, dirt))
r.scene.append(Cube(V3(-1, -0.75, -4.25), 0.5, dirt))
r.scene.append(Cube(V3(-1.5, -0.75, -4.25), 0.5, dirt))
r.scene.append(Cube(V3(-2, -0.75, -4.25), 0.5, dirt))

r.scene.append(Cube(V3(-2.5, -0.75, -3.75), 0.5, dirt))
r.scene.append(Cube(V3(-2.5, -0.75, -3.5), 0.5, dirt))
r.scene.append(Cube(V3(-2.5, -0.75, -3.25), 0.5, dirt))
r.scene.append(Cube(V3(-2, -0.75, -3.75), 0.5, dirt))
r.scene.append(Cube(V3(-2, -0.75, -3.5), 0.5, dirt))
r.scene.append(Cube(V3(-1.5, -0.75, -3.75), 0.5, dirt))
r.scene.append(Cube(V3(2.5, -0.75, -3.75), 0.5, dirt))
r.scene.append(Cube(V3(2.5, -0.75, -3.5), 0.5, dirt))
r.scene.append(Cube(V3(2.5, -0.75, -3.25), 0.5, dirt))
r.scene.append(Cube(V3(2, -0.75, -3.75), 0.5, dirt))
r.scene.append(Cube(V3(2, -0.75, -3.5), 0.5, dirt))
r.scene.append(Cube(V3(1.5, -0.75, -3.75), 0.5, dirt))

r.scene.append(Cube(V3(-2.5, -1.25, -3.75), 0.5, dirt))
r.scene.append(Cube(V3(-2.5, -1.25, -3.5), 0.5, dirt))
r.scene.append(Cube(V3(-2.5, -1.25, -3.25), 0.5, dirt))
r.scene.append(Cube(V3(-2, -1.25, -3.75), 0.5, dirt))
r.scene.append(Cube(V3(-2, -1.25, -3.5), 0.5, dirt))
r.scene.append(Cube(V3(-1.5, -1.25, -3.75), 0.5, dirt))
r.scene.append(Cube(V3(2.5, -1.25, -3.75), 0.5, dirt))
r.scene.append(Cube(V3(2.5, -1.25, -3.5), 0.5, dirt))
r.scene.append(Cube(V3(2.5, -1.25, -3.25), 0.5, dirt))
r.scene.append(Cube(V3(2, -1.25, -3.75), 0.5, dirt))
r.scene.append(Cube(V3(2, -1.25, -3.5), 0.5, dirt))
r.scene.append(Cube(V3(1.5, -1.25, -3.75), 0.5, dirt))

# house
r.scene.append(Cube(V3(0.5, -0.25, -4.25), 0.5, wood))
r.scene.append(Cube(V3(-0.5, -0.25, -4.25), 0.5, wood))
r.scene.append(Cube(V3(0.5, 0.25, -4.25), 0.5, wood))
r.scene.append(Cube(V3(-0.5, 0.25, -4.25), 0.5, wood))
r.scene.append(Cube(V3(0.5, 0.75, -4.25), 0.5, wood))
r.scene.append(Cube(V3(-0.5, 0.75, -4.25), 0.5, wood))
r.scene.append(Cube(V3(0, 0.75, -4.25), 0.5, wood))
r.scene.append(Cube(V3(0.5, 1.25, -4.25), 0.5, darkWood))
r.scene.append(Cube(V3(1, 1.25, -4.25), 0.5, darkWood))
r.scene.append(Cube(V3(-0.5, 1.25, -4.25), 0.5, darkWood))
r.scene.append(Cube(V3(-1, 1.25, -4.25), 0.5, darkWood))
r.scene.append(Cube(V3(0, 1.25, -4.25), 0.5, darkWood))
r.scene.append(Cube(V3(0, 1.75, -4.25), 0.5, darkWood))
r.scene.append(Cube(V3(0.5, 1.75, -4.25), 0.5, darkWood))
r.scene.append(Cube(V3(-0.5, 1.75, -4.25), 0.5, darkWood))
r.scene.append(Cube(V3(0, 2.25, -4.25), 0.5, darkWood))
r.scene.append(Cube(V3(0, -0.25, -4.25), 0.5, darkWood))
r.scene.append(Cube(V3(0, 0.25, -4.25), 0.5, darkWood))
r.scene.append(Sphere(V3(0.1, 0, -3.5), 0.05, steel))


r.envmap = None
r.render()
r.write("Minecraft.bmp")
