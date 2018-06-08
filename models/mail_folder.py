# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.message import Message
from ..model.message_rule import MessageRule
from ..model.single_value_legacy_extended_property import SingleValueLegacyExtendedProperty
from ..model.multi_value_legacy_extended_property import MultiValueLegacyExtendedProperty
from ..one_drive_object_base import OneDriveObjectBase


class MailFolder(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

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
    def parent_folder_id(self):
        """
        Gets and sets the parentFolderId
        
        Returns:
            str:
                The parentFolderId
        """
        if "parentFolderId" in self._prop_dict:
            return self._prop_dict["parentFolderId"]
        else:
            return None

    @parent_folder_id.setter
    def parent_folder_id(self, val):
        self._prop_dict["parentFolderId"] = val

    @property
    def child_folder_count(self):
        """
        Gets and sets the childFolderCount
        
        Returns:
            int:
                The childFolderCount
        """
        if "childFolderCount" in self._prop_dict:
            return self._prop_dict["childFolderCount"]
        else:
            return None

    @child_folder_count.setter
    def child_folder_count(self, val):
        self._prop_dict["childFolderCount"] = val

    @property
    def unread_item_count(self):
        """
        Gets and sets the unreadItemCount
        
        Returns:
            int:
                The unreadItemCount
        """
        if "unreadItemCount" in self._prop_dict:
            return self._prop_dict["unreadItemCount"]
        else:
            return None

    @unread_item_count.setter
    def unread_item_count(self, val):
        self._prop_dict["unreadItemCount"] = val

    @property
    def total_item_count(self):
        """
        Gets and sets the totalItemCount
        
        Returns:
            int:
                The totalItemCount
        """
        if "totalItemCount" in self._prop_dict:
            return self._prop_dict["totalItemCount"]
        else:
            return None

    @total_item_count.setter
    def total_item_count(self, val):
        self._prop_dict["totalItemCount"] = val

    @property
    def messages(self):
        """Gets and sets the messages
        
        Returns: 
            :class:`MessagesCollectionPage<onedrivesdk.request.messages_collection.MessagesCollectionPage>`:
                The messages
        """
        if "messages" in self._prop_dict:
            return MessagesCollectionPage(self._prop_dict["messages"])
        else:
            return None

    @property
    def message_rules(self):
        """Gets and sets the messageRules
        
        Returns: 
            :class:`MessageRulesCollectionPage<onedrivesdk.request.message_rules_collection.MessageRulesCollectionPage>`:
                The messageRules
        """
        if "messageRules" in self._prop_dict:
            return MessageRulesCollectionPage(self._prop_dict["messageRules"])
        else:
            return None

    @property
    def child_folders(self):
        """Gets and sets the childFolders
        
        Returns: 
            :class:`ChildFoldersCollectionPage<onedrivesdk.request.child_folders_collection.ChildFoldersCollectionPage>`:
                The childFolders
        """
        if "childFolders" in self._prop_dict:
            return ChildFoldersCollectionPage(self._prop_dict["childFolders"])
        else:
            return None

    @property
    def single_value_extended_properties(self):
        """Gets and sets the singleValueExtendedProperties
        
        Returns: 
            :class:`SingleValueExtendedPropertiesCollectionPage<onedrivesdk.request.single_value_extended_properties_collection.SingleValueExtendedPropertiesCollectionPage>`:
                The singleValueExtendedProperties
        """
        if "singleValueExtendedProperties" in self._prop_dict:
            return SingleValueExtendedPropertiesCollectionPage(self._prop_dict["singleValueExtendedProperties"])
        else:
            return None

    @property
    def multi_value_extended_properties(self):
        """Gets and sets the multiValueExtendedProperties
        
        Returns: 
            :class:`MultiValueExtendedPropertiesCollectionPage<onedrivesdk.request.multi_value_extended_properties_collection.MultiValueExtendedPropertiesCollectionPage>`:
                The multiValueExtendedProperties
        """
        if "multiValueExtendedProperties" in self._prop_dict:
            return MultiValueExtendedPropertiesCollectionPage(self._prop_dict["multiValueExtendedProperties"])
        else:
            return None

