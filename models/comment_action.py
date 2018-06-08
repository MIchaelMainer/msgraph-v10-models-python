# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.identity_set import IdentitySet
from ..one_drive_object_base import OneDriveObjectBase


class CommentAction(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def is_reply(self):
        """Gets and sets the isReply
        
        Returns: 
            bool:
                The isReply
        """
        if "isReply" in self._prop_dict:
            return self._prop_dict["isReply"]
        else:
            return None

    @is_reply.setter
    def is_reply(self, val):
        self._prop_dict["isReply"] = val

    @property
    def parent_author(self):
        """
        Gets and sets the parentAuthor
        
        Returns: 
            :class:`IdentitySet<onedrivesdk.model.identity_set.IdentitySet>`:
                The parentAuthor
        """
        if "parentAuthor" in self._prop_dict:
            if isinstance(self._prop_dict["parentAuthor"], OneDriveObjectBase):
                return self._prop_dict["parentAuthor"]
            else :
                self._prop_dict["parentAuthor"] = IdentitySet(self._prop_dict["parentAuthor"])
                return self._prop_dict["parentAuthor"]

        return None

    @parent_author.setter
    def parent_author(self, val):
        self._prop_dict["parentAuthor"] = val
    @property
    def participants(self):
        """
        Gets and sets the participants
        
        Returns: 
            :class:`IdentitySet<onedrivesdk.model.identity_set.IdentitySet>`:
                The participants
        """
        if "participants" in self._prop_dict:
            if isinstance(self._prop_dict["participants"], OneDriveObjectBase):
                return self._prop_dict["participants"]
            else :
                self._prop_dict["participants"] = IdentitySet(self._prop_dict["participants"])
                return self._prop_dict["participants"]

        return None

    @participants.setter
    def participants(self, val):
        self._prop_dict["participants"] = val
