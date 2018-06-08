# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..one_drive_object_base import OneDriveObjectBase


class FileSecurityState(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def authenticode_hash256(self):
        """Gets and sets the authenticodeHash256
        
        Returns: 
            str:
                The authenticodeHash256
        """
        if "authenticodeHash256" in self._prop_dict:
            return self._prop_dict["authenticodeHash256"]
        else:
            return None

    @authenticode_hash256.setter
    def authenticode_hash256(self, val):
        self._prop_dict["authenticodeHash256"] = val

    @property
    def name(self):
        """Gets and sets the name
        
        Returns: 
            str:
                The name
        """
        if "name" in self._prop_dict:
            return self._prop_dict["name"]
        else:
            return None

    @name.setter
    def name(self, val):
        self._prop_dict["name"] = val

    @property
    def path(self):
        """Gets and sets the path
        
        Returns: 
            str:
                The path
        """
        if "path" in self._prop_dict:
            return self._prop_dict["path"]
        else:
            return None

    @path.setter
    def path(self, val):
        self._prop_dict["path"] = val

    @property
    def risk_score(self):
        """Gets and sets the riskScore
        
        Returns: 
            str:
                The riskScore
        """
        if "riskScore" in self._prop_dict:
            return self._prop_dict["riskScore"]
        else:
            return None

    @risk_score.setter
    def risk_score(self, val):
        self._prop_dict["riskScore"] = val

    @property
    def sha256(self):
        """Gets and sets the sha256
        
        Returns: 
            str:
                The sha256
        """
        if "sha256" in self._prop_dict:
            return self._prop_dict["sha256"]
        else:
            return None

    @sha256.setter
    def sha256(self, val):
        self._prop_dict["sha256"] = val

