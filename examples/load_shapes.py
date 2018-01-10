#!/usr/bin/env python
#-*- coding:utf-8 -*-
#
# This file is part of the PyNCulture project, which aims at providing tools to
# easily generate complex neuronal cultures.
# Copyright (C) 2017 SENeC Initiative
# 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

""" Loading shapes from an SVG file """

import matplotlib.pyplot as plt

import PyNCulture as nc


''' Choose a file and get the shapes '''
shapes_file = "areas.svg"

shapes = None

shapes = nc.shapes_from_file(shapes_file)

''' Plot the shapes '''
fig, ax = plt.subplots()
plt.title("shapes")

for shape in shapes:
    nc.plot_shape(shape, ax, show=False)

plt.show()
