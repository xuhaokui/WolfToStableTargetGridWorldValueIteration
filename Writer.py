#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-12-14 17:25:44
# @Author  : xuhaokui (haokuixu.psy@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import pickle
import os 

def savePolicyToPkl(policy,filename):
	output=open(filename,'wb')
	pickle.dump(policy, output)
	output.close()
	return
