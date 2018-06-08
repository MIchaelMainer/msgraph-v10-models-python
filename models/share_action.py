# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.identity_set import IdentitySet
from ..one_drive_object_base import OneDriveObjectBase


class ShareAction(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def recipients(self):
        """
        Gets and sets the recipients
        
        Returns: 
            :class:`IdentitySet<onedrivesdk.model.identity_set.IdentitySet>`:
                The recipients
        """
        if "recipients" in self._prop_dict:
            if isinstance(self._prop_dict["recipients"], OneDriveObjectBase):
                return self._prop_dict["recipients"]
            else :
                self._prop_dict["recipients"] = IdentitySet(self._prop_dict["recipients"])
                return self._prop_dict["recipients"]

        return None

    @recipients.setter
    def recipients(self, val):
        self._prop_dict["recipients"] = val
