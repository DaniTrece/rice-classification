#!/usr/bin/env python
# coding: utf-8

import requests


url = 'http://localhost:9696/predict'

# Cammeo
rice_features = {
    'area': 15231.0,
    'perimeter': 525.5789795,
    'major_axis_length': 229.7498779,
    'minor_axis_length': 85.09378815,
    'eccentricity': 0.928882003,
    'convex_area': 15617.0,
    'extent': 0.572895527
}
# Osmancik
rice_features = {
    'area': 11434.0,
    'perimeter': 404.7099915,
    'major_axis_length': 161.0792694,
    'minor_axis_length': 90.86819458,
    'eccentricity': 0.825692177,
    'convex_area': 11591.0,
    'extent': 0.802949429
}


rice_features_arr = [list(rice_features.values())]

response = requests.post(url, json=rice_features_arr).json()
print(f"the variety of the rice is {response}")
