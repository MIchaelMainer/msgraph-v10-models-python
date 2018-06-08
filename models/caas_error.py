# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.caas_child_error import CaasChildError
from ..one_drive_object_base import OneDriveObjectBase


class CaasError(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def details(self):
        """
        Gets and sets the details
        
        Returns: 
            :class:`CaasChildError<onedrivesdk.model.caas_child_error.CaasChildError>`:
                The details
        """
        if "details" in self._prop_dict:
            if isinstance(self._prop_dict["details"], OneDriveObjectBase):
                return self._prop_dict["details"]
            else :
                self._prop_dict["details"] = CaasChildError(self._prop_dict["details"])
                return self._prop_dict["details"]

        return None

    @details.setter
    def details(self, val):
        self._prop_dict["details"] = val
