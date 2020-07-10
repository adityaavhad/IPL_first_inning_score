import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
#%%
app = Flask(__name__)
model = pickle.load(open('ipl_score_lin_reg.pkl','rb'))

#%%
import os
os.getcwd()
os.chdir()