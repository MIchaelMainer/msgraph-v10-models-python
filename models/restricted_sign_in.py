# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..one_drive_object_base import OneDriveObjectBase


class RestrictedSignIn(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def target_tenant_id(self):
        """
        Gets and sets the targetTenantId
        
        Returns:
            UUID:
                The targetTenantId
        """
        if "targetTenantId" in self._prop_dict:
            return self._prop_dict["targetTenantId"]
        else:
            return None

    @target_tenant_id.setter
    def target_tenant_id(self, val):
        self._prop_dict["targetTenantId"] = val

