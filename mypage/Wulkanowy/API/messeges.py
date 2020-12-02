import os
import sys
import requests
from django import template
from django.utils.safestring import mark_safe
from django.shortcuts import render
import json
import requests
from django.shortcuts import redirect
from bs4 import BeautifulSoup

class GetMesseges():
    def __init__(self, register_id, register_r, oun, s, date):
        print(None)