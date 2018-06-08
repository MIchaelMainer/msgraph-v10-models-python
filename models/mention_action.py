# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.identity_set import IdentitySet
from ..one_drive_object_base import OneDriveObjectBase


class MentionAction(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def mentionees(self):
        """
        Gets and sets the mentionees
        
        Returns: 
            :class:`IdentitySet<onedrivesdk.model.identity_set.IdentitySet>`:
                The mentionees
        """
        if "mentionees" in self._prop_dict:
            if isinstance(self._prop_dict["mentionees"], OneDriveObjectBase):
                return self._prop_dict["mentionees"]
            else :
                self._prop_dict["mentionees"] = IdentitySet(self._prop_dict["mentionees"])
                return self._prop_dict["mentionees"]

        return None

    @mentionees.setter
    def mentionees(self, val):
        self._prop_dict["mentionees"] = val
