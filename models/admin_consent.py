# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.admin_consent_state import AdminConsentState
from ..one_drive_object_base import OneDriveObjectBase


class AdminConsent(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def share_apns_data(self):
        """
        Gets and sets the shareAPNSData
        
        Returns: 
            :class:`AdminConsentState<onedrivesdk.model.admin_consent_state.AdminConsentState>`:
                The shareAPNSData
        """
        if "shareAPNSData" in self._prop_dict:
            if isinstance(self._prop_dict["shareAPNSData"], OneDriveObjectBase):
                return self._prop_dict["shareAPNSData"]
            else :
                self._prop_dict["shareAPNSData"] = AdminConsentState(self._prop_dict["shareAPNSData"])
                return self._prop_dict["shareAPNSData"]

        return None

    @share_apns_data.setter
    def share_apns_data(self, val):
        self._prop_dict["shareAPNSData"] = val
