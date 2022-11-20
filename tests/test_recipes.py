# test_reader.py
#
# Copyright 2022 Patrick Eschenbach
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
#
# SPDX-License-Identifier: GPL-3.0-or-later

import yuml

def test_recipes():
    recipe = yuml.recipe_from_file('data/Chili con Carne.yuml')
    assert len(recipe.quantities) == 1
    assert len(recipe.ingredients) == 11
    assert len(recipe.steps) == 11
    assert len(recipe.variants) == 2
    assert len(recipe.images) == 1