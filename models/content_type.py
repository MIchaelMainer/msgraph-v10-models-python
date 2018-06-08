# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.item_reference import ItemReference
from ..model.content_type_order import ContentTypeOrder
from ..model.column_link import ColumnLink
from ..one_drive_object_base import OneDriveObjectBase


class ContentType(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

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
    def group(self):
        """
        Gets and sets the group
        
        Returns:
            str:
                The group
        """
        if "group" in self._prop_dict:
            return self._prop_dict["group"]
        else:
            return None

    @group.setter
    def group(self, val):
        self._prop_dict["group"] = val

    @property
    def hidden(self):
        """
        Gets and sets the hidden
        
        Returns:
            bool:
                The hidden
        """
        if "hidden" in self._prop_dict:
            return self._prop_dict["hidden"]
        else:
            return None

    @hidden.setter
    def hidden(self, val):
        self._prop_dict["hidden"] = val

    @property
    def inherited_from(self):
        """
        Gets and sets the inheritedFrom
        
        Returns: 
            :class:`ItemReference<onedrivesdk.model.item_reference.ItemReference>`:
                The inheritedFrom
        """
        if "inheritedFrom" in self._prop_dict:
            if isinstance(self._prop_dict["inheritedFrom"], OneDriveObjectBase):
                return self._prop_dict["inheritedFrom"]
            else :
                self._prop_dict["inheritedFrom"] = ItemReference(self._prop_dict["inheritedFrom"])
                return self._prop_dict["inheritedFrom"]

        return None

    @inherited_from.setter
    def inherited_from(self, val):
        self._prop_dict["inheritedFrom"] = val

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
    def order(self):
        """
        Gets and sets the order
        
        Returns: 
            :class:`ContentTypeOrder<onedrivesdk.model.content_type_order.ContentTypeOrder>`:
                The order
        """
        if "order" in self._prop_dict:
            if isinstance(self._prop_dict["order"], OneDriveObjectBase):
                return self._prop_dict["order"]
            else :
                self._prop_dict["order"] = ContentTypeOrder(self._prop_dict["order"])
                return self._prop_dict["order"]

        return None

    @order.setter
    def order(self, val):
        self._prop_dict["order"] = val

    @property
    def parent_id(self):
        """
        Gets and sets the parentId
        
        Returns:
            str:
                The parentId
        """
        if "parentId" in self._prop_dict:
            return self._prop_dict["parentId"]
        else:
            return None

    @parent_id.setter
    def parent_id(self, val):
        self._prop_dict["parentId"] = val

    @property
    def read_only(self):
        """
        Gets and sets the readOnly
        
        Returns:
            bool:
                The readOnly
        """
        if "readOnly" in self._prop_dict:
            return self._prop_dict["readOnly"]
        else:
            return None

    @read_only.setter
    def read_only(self, val):
        self._prop_dict["readOnly"] = val

    @property
    def sealed(self):
        """
        Gets and sets the sealed
        
        Returns:
            bool:
                The sealed
        """
        if "sealed" in self._prop_dict:
            return self._prop_dict["sealed"]
        else:
            return None

    @sealed.setter
    def sealed(self, val):
        self._prop_dict["sealed"] = val

    @property
    def column_links(self):
        """Gets and sets the columnLinks
        
        Returns: 
            :class:`ColumnLinksCollectionPage<onedrivesdk.request.column_links_collection.ColumnLinksCollectionPage>`:
                The columnLinks
        """
        if "columnLinks" in self._prop_dict:
            return ColumnLinksCollectionPage(self._prop_dict["columnLinks"])
        else:
            return None

