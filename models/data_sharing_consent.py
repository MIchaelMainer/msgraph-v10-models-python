# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from datetime import datetime
from ..one_drive_object_base import OneDriveObjectBase


class DataSharingConsent(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def service_display_name(self):
        """
        Gets and sets the serviceDisplayName
        
        Returns:
            str:
                The serviceDisplayName
        """
        if "serviceDisplayName" in self._prop_dict:
            return self._prop_dict["serviceDisplayName"]
        else:
            return None

    @service_display_name.setter
    def service_display_name(self, val):
        self._prop_dict["serviceDisplayName"] = val

    @property
    def terms_url(self):
        """
        Gets and sets the termsUrl
        
        Returns:
            str:
                The termsUrl
        """
        if "termsUrl" in self._prop_dict:
            return self._prop_dict["termsUrl"]
        else:
            return None

    @terms_url.setter
    def terms_url(self, val):
        self._prop_dict["termsUrl"] = val

    @property
    def granted(self):
        """
        Gets and sets the granted
        
        Returns:
            bool:
                The granted
        """
        if "granted" in self._prop_dict:
            return self._prop_dict["granted"]
        else:
            return None

    @granted.setter
    def granted(self, val):
        self._prop_dict["granted"] = val

    @property
    def grant_date_time(self):
        """
        Gets and sets the grantDateTime
        
        Returns:
            datetime:
                The grantDateTime
        """
        if "grantDateTime" in self._prop_dict:
            return datetime.strptime(self._prop_dict["grantDateTime"].replace("Z", ""), "%Y-%m-%dT%H:%M:%S.%f")
        else:
            return None

    @grant_date_time.setter
    def grant_date_time(self, val):
        self._prop_dict["grantDateTime"] = val.isoformat()+"Z"

    @property
    def granted_by_upn(self):
        """
        Gets and sets the grantedByUpn
        
        Returns:
            str:
                The grantedByUpn
        """
        if "grantedByUpn" in self._prop_dict:
            return self._prop_dict["grantedByUpn"]
        else:
            return None

    @granted_by_upn.setter
    def granted_by_upn(self, val):
        self._prop_dict["grantedByUpn"] = val

    @property
    def granted_by_user_id(self):
        """
        Gets and sets the grantedByUserId
        
        Returns:
            str:
                The grantedByUserId
        """
        if "grantedByUserId" in self._prop_dict:
            return self._prop_dict["grantedByUserId"]
        else:
            return None

    @granted_by_user_id.setter
    def granted_by_user_id(self, val):
        self._prop_dict["grantedByUserId"] = val

