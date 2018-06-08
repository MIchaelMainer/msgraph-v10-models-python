# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.importance import Importance
from ..model.recipient import Recipient
from ..one_drive_object_base import OneDriveObjectBase


class MessageRuleActions(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def move_to_folder(self):
        """Gets and sets the moveToFolder
        
        Returns: 
            str:
                The moveToFolder
        """
        if "moveToFolder" in self._prop_dict:
            return self._prop_dict["moveToFolder"]
        else:
            return None

    @move_to_folder.setter
    def move_to_folder(self, val):
        self._prop_dict["moveToFolder"] = val

    @property
    def copy_to_folder(self):
        """Gets and sets the copyToFolder
        
        Returns: 
            str:
                The copyToFolder
        """
        if "copyToFolder" in self._prop_dict:
            return self._prop_dict["copyToFolder"]
        else:
            return None

    @copy_to_folder.setter
    def copy_to_folder(self, val):
        self._prop_dict["copyToFolder"] = val

    @property
    def delete(self):
        """Gets and sets the delete
        
        Returns: 
            bool:
                The delete
        """
        if "delete" in self._prop_dict:
            return self._prop_dict["delete"]
        else:
            return None

    @delete.setter
    def delete(self, val):
        self._prop_dict["delete"] = val

    @property
    def permanent_delete(self):
        """Gets and sets the permanentDelete
        
        Returns: 
            bool:
                The permanentDelete
        """
        if "permanentDelete" in self._prop_dict:
            return self._prop_dict["permanentDelete"]
        else:
            return None

    @permanent_delete.setter
    def permanent_delete(self, val):
        self._prop_dict["permanentDelete"] = val

    @property
    def mark_as_read(self):
        """Gets and sets the markAsRead
        
        Returns: 
            bool:
                The markAsRead
        """
        if "markAsRead" in self._prop_dict:
            return self._prop_dict["markAsRead"]
        else:
            return None

    @mark_as_read.setter
    def mark_as_read(self, val):
        self._prop_dict["markAsRead"] = val

    @property
    def mark_importance(self):
        """
        Gets and sets the markImportance
        
        Returns: 
            :class:`Importance<onedrivesdk.model.importance.Importance>`:
                The markImportance
        """
        if "markImportance" in self._prop_dict:
            if isinstance(self._prop_dict["markImportance"], OneDriveObjectBase):
                return self._prop_dict["markImportance"]
            else :
                self._prop_dict["markImportance"] = Importance(self._prop_dict["markImportance"])
                return self._prop_dict["markImportance"]

        return None

    @mark_importance.setter
    def mark_importance(self, val):
        self._prop_dict["markImportance"] = val
    @property
    def forward_to(self):
        """
        Gets and sets the forwardTo
        
        Returns: 
            :class:`Recipient<onedrivesdk.model.recipient.Recipient>`:
                The forwardTo
        """
        if "forwardTo" in self._prop_dict:
            if isinstance(self._prop_dict["forwardTo"], OneDriveObjectBase):
                return self._prop_dict["forwardTo"]
            else :
                self._prop_dict["forwardTo"] = Recipient(self._prop_dict["forwardTo"])
                return self._prop_dict["forwardTo"]

        return None

    @forward_to.setter
    def forward_to(self, val):
        self._prop_dict["forwardTo"] = val
    @property
    def forward_as_attachment_to(self):
        """
        Gets and sets the forwardAsAttachmentTo
        
        Returns: 
            :class:`Recipient<onedrivesdk.model.recipient.Recipient>`:
                The forwardAsAttachmentTo
        """
        if "forwardAsAttachmentTo" in self._prop_dict:
            if isinstance(self._prop_dict["forwardAsAttachmentTo"], OneDriveObjectBase):
                return self._prop_dict["forwardAsAttachmentTo"]
            else :
                self._prop_dict["forwardAsAttachmentTo"] = Recipient(self._prop_dict["forwardAsAttachmentTo"])
                return self._prop_dict["forwardAsAttachmentTo"]

        return None

    @forward_as_attachment_to.setter
    def forward_as_attachment_to(self, val):
        self._prop_dict["forwardAsAttachmentTo"] = val
    @property
    def redirect_to(self):
        """
        Gets and sets the redirectTo
        
        Returns: 
            :class:`Recipient<onedrivesdk.model.recipient.Recipient>`:
                The redirectTo
        """
        if "redirectTo" in self._prop_dict:
            if isinstance(self._prop_dict["redirectTo"], OneDriveObjectBase):
                return self._prop_dict["redirectTo"]
            else :
                self._prop_dict["redirectTo"] = Recipient(self._prop_dict["redirectTo"])
                return self._prop_dict["redirectTo"]

        return None

    @redirect_to.setter
    def redirect_to(self, val):
        self._prop_dict["redirectTo"] = val
    @property
    def assign_categories(self):
        """Gets and sets the assignCategories
        
        Returns: 
            str:
                The assignCategories
        """
        if "assignCategories" in self._prop_dict:
            return self._prop_dict["assignCategories"]
        else:
            return None

    @assign_categories.setter
    def assign_categories(self, val):
        self._prop_dict["assignCategories"] = val

    @property
    def stop_processing_rules(self):
        """Gets and sets the stopProcessingRules
        
        Returns: 
            bool:
                The stopProcessingRules
        """
        if "stopProcessingRules" in self._prop_dict:
            return self._prop_dict["stopProcessingRules"]
        else:
            return None

    @stop_processing_rules.setter
    def stop_processing_rules(self, val):
        self._prop_dict["stopProcessingRules"] = val

