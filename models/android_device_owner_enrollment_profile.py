# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.mime_content import MimeContent
from datetime import datetime
from ..one_drive_object_base import OneDriveObjectBase


class AndroidDeviceOwnerEnrollmentProfile(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def account_id(self):
        """
        Gets and sets the accountId
        
        Returns:
            str:
                The accountId
        """
        if "accountId" in self._prop_dict:
            return self._prop_dict["accountId"]
        else:
            return None

    @account_id.setter
    def account_id(self, val):
        self._prop_dict["accountId"] = val

    @property
    def display_name(self):
        """
        Gets and sets the displayName
        
        Returns:
            str:
                The displayName
        """
        if "displayName" in self._prop_dict:
            return self._prop_dict["displayName"]
        else:
            return None

    @display_name.setter
    def display_name(self, val):
        self._prop_dict["displayName"] = val

    @property
    def description(self):
        """
        Gets and sets the description
        
        Returns:
            str:
                The description
        """
        if "description" in self._prop_dict:
            return self._prop_dict["description"]
        else:
            return None

    @description.setter
    def description(self, val):
        self._prop_dict["description"] = val

    @property
    def created_date_time(self):
        """
        Gets and sets the createdDateTime
        
        Returns:
            datetime:
                The createdDateTime
        """
        if "createdDateTime" in self._prop_dict:
            return datetime.strptime(self._prop_dict["createdDateTime"].replace("Z", ""), "%Y-%m-%dT%H:%M:%S.%f")
        else:
            return None

    @created_date_time.setter
    def created_date_time(self, val):
        self._prop_dict["createdDateTime"] = val.isoformat()+"Z"

    @property
    def last_modified_date_time(self):
        """
        Gets and sets the lastModifiedDateTime
        
        Returns:
            datetime:
                The lastModifiedDateTime
        """
        if "lastModifiedDateTime" in self._prop_dict:
            return datetime.strptime(self._prop_dict["lastModifiedDateTime"].replace("Z", ""), "%Y-%m-%dT%H:%M:%S.%f")
        else:
            return None

    @last_modified_date_time.setter
    def last_modified_date_time(self, val):
        self._prop_dict["lastModifiedDateTime"] = val.isoformat()+"Z"

    @property
    def token_value(self):
        """
        Gets and sets the tokenValue
        
        Returns:
            str:
                The tokenValue
        """
        if "tokenValue" in self._prop_dict:
            return self._prop_dict["tokenValue"]
        else:
            return None

    @token_value.setter
    def token_value(self, val):
        self._prop_dict["tokenValue"] = val

    @property
    def token_expiration_date_time(self):
        """
        Gets and sets the tokenExpirationDateTime
        
        Returns:
            datetime:
                The tokenExpirationDateTime
        """
        if "tokenExpirationDateTime" in self._prop_dict:
            return datetime.strptime(self._prop_dict["tokenExpirationDateTime"].replace("Z", ""), "%Y-%m-%dT%H:%M:%S.%f")
        else:
            return None

    @token_expiration_date_time.setter
    def token_expiration_date_time(self, val):
        self._prop_dict["tokenExpirationDateTime"] = val.isoformat()+"Z"

    @property
    def enrolled_device_count(self):
        """
        Gets and sets the enrolledDeviceCount
        
        Returns:
            int:
                The enrolledDeviceCount
        """
        if "enrolledDeviceCount" in self._prop_dict:
            return self._prop_dict["enrolledDeviceCount"]
        else:
            return None

    @enrolled_device_count.setter
    def enrolled_device_count(self, val):
        self._prop_dict["enrolledDeviceCount"] = val

    @property
    def qr_code_content(self):
        """
        Gets and sets the qrCodeContent
        
        Returns:
            str:
                The qrCodeContent
        """
        if "qrCodeContent" in self._prop_dict:
            return self._prop_dict["qrCodeContent"]
        else:
            return None

    @qr_code_content.setter
    def qr_code_content(self, val):
        self._prop_dict["qrCodeContent"] = val

    @property
    def qr_code_image(self):
        """
        Gets and sets the qrCodeImage
        
        Returns: 
            :class:`MimeContent<onedrivesdk.model.mime_content.MimeContent>`:
                The qrCodeImage
        """
        if "qrCodeImage" in self._prop_dict:
            if isinstance(self._prop_dict["qrCodeImage"], OneDriveObjectBase):
                return self._prop_dict["qrCodeImage"]
            else :
                self._prop_dict["qrCodeImage"] = MimeContent(self._prop_dict["qrCodeImage"])
                return self._prop_dict["qrCodeImage"]

        return None

    @qr_code_image.setter
    def qr_code_image(self, val):
        self._prop_dict["qrCodeImage"] = val

