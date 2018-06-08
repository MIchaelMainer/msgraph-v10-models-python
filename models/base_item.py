# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.identity_set import IdentitySet
from ..model.item_reference import ItemReference
from ..model.user import User
from datetime import datetime
from ..one_drive_object_base import OneDriveObjectBase


class BaseItem(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def created_by(self):
        """
        Gets and sets the createdBy
        
        Returns: 
            :class:`IdentitySet<onedrivesdk.model.identity_set.IdentitySet>`:
                The createdBy
        """
        if "createdBy" in self._prop_dict:
            if isinstance(self._prop_dict["createdBy"], OneDriveObjectBase):
                return self._prop_dict["createdBy"]
            else :
                self._prop_dict["createdBy"] = IdentitySet(self._prop_dict["createdBy"])
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
    def e_tag(self):
        """
        Gets and sets the eTag
        
        Returns:
            str:
                The eTag
        """
        if "eTag" in self._prop_dict:
            return self._prop_dict["eTag"]
        else:
            return None

    @e_tag.setter
    def e_tag(self, val):
        self._prop_dict["eTag"] = val

    @property
    def last_modified_by(self):
        """
        Gets and sets the lastModifiedBy
        
        Returns: 
            :class:`IdentitySet<onedrivesdk.model.identity_set.IdentitySet>`:
                The lastModifiedBy
        """
        if "lastModifiedBy" in self._prop_dict:
            if isinstance(self._prop_dict["lastModifiedBy"], OneDriveObjectBase):
                return self._prop_dict["lastModifiedBy"]
            else :
                self._prop_dict["lastModifiedBy"] = IdentitySet(self._prop_dict["lastModifiedBy"])
                return self._prop_dict["lastModifiedBy"]

        return None

    @last_modified_by.setter
    def last_modified_by(self, val):
        self._prop_dict["lastModifiedBy"] = val

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
    def name(self):
        """
        Gets and sets the name
        
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
    def parent_reference(self):
        """
        Gets and sets the parentReference
        
        Returns: 
            :class:`ItemReference<onedrivesdk.model.item_reference.ItemReference>`:
                The parentReference
        """
        if "parentReference" in self._prop_dict:
            if isinstance(self._prop_dict["parentReference"], OneDriveObjectBase):
                return self._prop_dict["parentReference"]
            else :
                self._prop_dict["parentReference"] = ItemReference(self._prop_dict["parentReference"])
                return self._prop_dict["parentReference"]

        return None

    @parent_reference.setter
    def parent_reference(self, val):
        self._prop_dict["parentReference"] = val

    @property
    def web_url(self):
        """
        Gets and sets the webUrl
        
        Returns:
            str:
                The webUrl
        """
        if "webUrl" in self._prop_dict:
            return self._prop_dict["webUrl"]
        else:
            return None

    @web_url.setter
    def web_url(self, val):
        self._prop_dict["webUrl"] = val

    @property
    def created_by_user(self):
        """
        Gets and sets the createdByUser
        
        Returns: 
            :class:`User<onedrivesdk.model.user.User>`:
                The createdByUser
        """
        if "createdByUser" in self._prop_dict:
            if isinstance(self._prop_dict["createdByUser"], OneDriveObjectBase):
                return self._prop_dict["createdByUser"]
            else :
                self._prop_dict["createdByUser"] = User(self._prop_dict["createdByUser"])
                return self._prop_dict["createdByUser"]

        return None

    @created_by_user.setter
    def created_by_user(self, val):
        self._prop_dict["createdByUser"] = val

    @property
    def last_modified_by_user(self):
        """
        Gets and sets the lastModifiedByUser
        
        Returns: 
            :class:`User<onedrivesdk.model.user.User>`:
                The lastModifiedByUser
        """
        if "lastModifiedByUser" in self._prop_dict:
            if isinstance(self._prop_dict["lastModifiedByUser"], OneDriveObjectBase):
                return self._prop_dict["lastModifiedByUser"]
            else :
                self._prop_dict["lastModifiedByUser"] = User(self._prop_dict["lastModifiedByUser"])
                return self._prop_dict["lastModifiedByUser"]

        return None

    @last_modified_by_user.setter
    def last_modified_by_user(self, val):
        self._prop_dict["lastModifiedByUser"] = val

