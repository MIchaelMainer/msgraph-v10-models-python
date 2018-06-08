# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.workbook_range_border import WorkbookRangeBorder
from ..model.workbook_range_fill import WorkbookRangeFill
from ..model.workbook_range_font import WorkbookRangeFont
from ..model.workbook_format_protection import WorkbookFormatProtection
from ..one_drive_object_base import OneDriveObjectBase


class WorkbookRangeFormat(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def column_width(self):
        """
        Gets and sets the columnWidth
        
        Returns:
            float:
                The columnWidth
        """
        if "columnWidth" in self._prop_dict:
            return self._prop_dict["columnWidth"]
        else:
            return None

    @column_width.setter
    def column_width(self, val):
        self._prop_dict["columnWidth"] = val

    @property
    def horizontal_alignment(self):
        """
        Gets and sets the horizontalAlignment
        
        Returns:
            str:
                The horizontalAlignment
        """
        if "horizontalAlignment" in self._prop_dict:
            return self._prop_dict["horizontalAlignment"]
        else:
            return None

    @horizontal_alignment.setter
    def horizontal_alignment(self, val):
        self._prop_dict["horizontalAlignment"] = val

    @property
    def row_height(self):
        """
        Gets and sets the rowHeight
        
        Returns:
            float:
                The rowHeight
        """
        if "rowHeight" in self._prop_dict:
            return self._prop_dict["rowHeight"]
        else:
            return None

    @row_height.setter
    def row_height(self, val):
        self._prop_dict["rowHeight"] = val

    @property
    def vertical_alignment(self):
        """
        Gets and sets the verticalAlignment
        
        Returns:
            str:
                The verticalAlignment
        """
        if "verticalAlignment" in self._prop_dict:
            return self._prop_dict["verticalAlignment"]
        else:
            return None

    @vertical_alignment.setter
    def vertical_alignment(self, val):
        self._prop_dict["verticalAlignment"] = val

    @property
    def wrap_text(self):
        """
        Gets and sets the wrapText
        
        Returns:
            bool:
                The wrapText
        """
        if "wrapText" in self._prop_dict:
            return self._prop_dict["wrapText"]
        else:
            return None

    @wrap_text.setter
    def wrap_text(self, val):
        self._prop_dict["wrapText"] = val

    @property
    def borders(self):
        """Gets and sets the borders
        
        Returns: 
            :class:`BordersCollectionPage<onedrivesdk.request.borders_collection.BordersCollectionPage>`:
                The borders
        """
        if "borders" in self._prop_dict:
            return BordersCollectionPage(self._prop_dict["borders"])
        else:
            return None

    @property
    def fill(self):
        """
        Gets and sets the fill
        
        Returns: 
            :class:`WorkbookRangeFill<onedrivesdk.model.workbook_range_fill.WorkbookRangeFill>`:
                The fill
        """
        if "fill" in self._prop_dict:
            if isinstance(self._prop_dict["fill"], OneDriveObjectBase):
                return self._prop_dict["fill"]
            else :
                self._prop_dict["fill"] = WorkbookRangeFill(self._prop_dict["fill"])
                return self._prop_dict["fill"]

        return None

    @fill.setter
    def fill(self, val):
        self._prop_dict["fill"] = val

    @property
    def font(self):
        """
        Gets and sets the font
        
        Returns: 
            :class:`WorkbookRangeFont<onedrivesdk.model.workbook_range_font.WorkbookRangeFont>`:
                The font
        """
        if "font" in self._prop_dict:
            if isinstance(self._prop_dict["font"], OneDriveObjectBase):
                return self._prop_dict["font"]
            else :
                self._prop_dict["font"] = WorkbookRangeFont(self._prop_dict["font"])
                return self._prop_dict["font"]

        return None

    @font.setter
    def font(self, val):
        self._prop_dict["font"] = val

    @property
    def protection(self):
        """
        Gets and sets the protection
        
        Returns: 
            :class:`WorkbookFormatProtection<onedrivesdk.model.workbook_format_protection.WorkbookFormatProtection>`:
                The protection
        """
        if "protection" in self._prop_dict:
            if isinstance(self._prop_dict["protection"], OneDriveObjectBase):
                return self._prop_dict["protection"]
            else :
                self._prop_dict["protection"] = WorkbookFormatProtection(self._prop_dict["protection"])
                return self._prop_dict["protection"]

        return None

    @protection.setter
    def protection(self, val):
        self._prop_dict["protection"] = val

