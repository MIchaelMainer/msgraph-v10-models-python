# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.email_address import EmailAddress
from datetime import datetime
from ..one_drive_object_base import OneDriveObjectBase


class Mention(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def mentioned(self):
        """
        Gets and sets the mentioned
        
        Returns: 
            :class:`EmailAddress<onedrivesdk.model.email_address.EmailAddress>`:
                The mentioned
        """
        if "mentioned" in self._prop_dict:
            if isinstance(self._prop_dict["mentioned"], OneDriveObjectBase):
                return self._prop_dict["mentioned"]
            else :
                self._prop_dict["mentioned"] = EmailAddress(self._prop_dict["mentioned"])
                return self._prop_dict["mentioned"]

        return None

    @mentioned.setter
    def mentioned(self, val):
        self._prop_dict["mentioned"] = val

    @property
    def mention_text(self):
        """
        Gets and sets the mentionText
        
        Returns:
            str:
                The mentionText
        """
        if "mentionText" in self._prop_dict:
            return self._prop_dict["mentionText"]
        else:
            return None

    @mention_text.setter
    def mention_text(self, val):
        self._prop_dict["mentionText"] = val

    @property
    def client_reference(self):
        """
        Gets and sets the clientReference
        
        Returns:
            str:
                The clientReference
        """
        if "clientReference" in self._prop_dict:
            return self._prop_dict["clientReference"]
        else:
            return None

    @client_reference.setter
    def client_reference(self, val):
        self._prop_dict["clientReference"] = val

    @property
    def created_by(self):
        """
        Gets and sets the createdBy
        
        Returns: 
            :class:`EmailAddress<onedrivesdk.model.email_address.EmailAddress>`:
                The createdBy
        """
        if "createdBy" in self._prop_dict:
            if isinstance(self._prop_dict["createdBy"], OneDriveObjectBase):
                return self._prop_dict["createdBy"]
            else :
                self._prop_dict["createdBy"] = EmailAddress(self._prop_dict["createdBy"])
                return self._prop_dict["createdBy"]

        return None

    @created_by.setter
    def created_by(self, val):
        self._prop_dict["createdBy"] = val

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
    def server_created_date_time(self):
        """
        Gets and sets the serverCreatedDateTime
        
        Returns:
            datetime:
                The serverCreatedDateTime
        """
        if "serverCreatedDateTime" in self._prop_dict:
            return datetime.strptime(self._prop_dict["serverCreatedDateTime"].replace("Z", ""), "%Y-%m-%dT%H:%M:%S.%f")
        else:
            return None

    @server_created_date_time.setter
    def server_created_date_time(self, val):
        self._prop_dict["serverCreatedDateTime"] = val.isoformat()+"Z"

    @property
    def deep_link(self):
        """
        Gets and sets the deepLink
        
        Returns:
            str:
                The deepLink
        """
        if "deepLink" in self._prop_dict:
            return self._prop_dict["deepLink"]
        else:
            return None

    @deep_link.setter
    def deep_link(self, val):
        self._prop_dict["deepLink"] = val

    @property
    def application(self):
        """
        Gets and sets the application
        
        Returns:
            str:
                The application
        """
        if "application" in self._prop_dict:
            return self._prop_dict["application"]
        else:
            return None

    @application.setter
    def application(self, val):
        self._prop_dict["application"] = val

