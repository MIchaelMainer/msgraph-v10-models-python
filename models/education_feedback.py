# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.education_item_body import EducationItemBody
from ..model.identity_set import IdentitySet
from datetime import datetime
from ..one_drive_object_base import OneDriveObjectBase


class EducationFeedback(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def text(self):
        """
        Gets and sets the text
        
        Returns: 
            :class:`EducationItemBody<onedrivesdk.model.education_item_body.EducationItemBody>`:
                The text
        """
        if "text" in self._prop_dict:
            if isinstance(self._prop_dict["text"], OneDriveObjectBase):
                return self._prop_dict["text"]
            else :
                self._prop_dict["text"] = EducationItemBody(self._prop_dict["text"])
                return self._prop_dict["text"]

        return None

    @text.setter
    def text(self, val):
        self._prop_dict["text"] = val
    @property
    def feedback_date_time(self):
        """Gets and sets the feedbackDateTime
        
        Returns: 
            datetime:
                The feedbackDateTime
        """
        if "feedbackDateTime" in self._prop_dict:
            return datetime.strptime(self._prop_dict["feedbackDateTime"].replace("Z", ""), "%Y-%m-%dT%H:%M:%S.%f")
        else:
            return None

    @feedback_date_time.setter
    def feedback_date_time(self, val):
        self._prop_dict["feedbackDateTime"] = val.isoformat()+"Z"

    @property
    def feedback_by(self):
        """
        Gets and sets the feedbackBy
        
        Returns: 
            :class:`IdentitySet<onedrivesdk.model.identity_set.IdentitySet>`:
                The feedbackBy
        """
        if "feedbackBy" in self._prop_dict:
            if isinstance(self._prop_dict["feedbackBy"], OneDriveObjectBase):
                return self._prop_dict["feedbackBy"]
            else :
                self._prop_dict["feedbackBy"] = IdentitySet(self._prop_dict["feedbackBy"])
                return self._prop_dict["feedbackBy"]

        return None

    @feedback_by.setter
    def feedback_by(self, val):
        self._prop_dict["feedbackBy"] = val
