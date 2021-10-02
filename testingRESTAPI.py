#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 20 15:17:51 2021

@author: carolineskalla
"""
import requests
import json

theURL = "https://www.ncdc.noaa.gov/cdo-web/api/v2/{data?datasetid=FIPS:26}"
theToken = "YWUKdFcrfkZdNrrxSiTImkMtZYyrpyqW"
theHeader = {'token': '{}'.format(theToken)}
response = requests.get(theURL, headers=theHeader)
a = response.json()
print(a)


