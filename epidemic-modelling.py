#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# modelling response/policy


# In[122]:


get_ipython().run_line_magic('matplotlib', 'widget')
import matplotlib.pyplot as plt
import numpy as np
import random
import base64


# In[449]:


class Pathogen:
    def __init__(self, **kwargs):
        defaults = dict(
            infectiousness=0.01,
            virulence=0.1,
            symptomaticity=0.8,
            incubation_period=14/365,
            disease_period=7/365,
        )
#         period of communicability
        defaults |= kwargs
        for k, v in defaults.items():
            setattr(self, k, v)
