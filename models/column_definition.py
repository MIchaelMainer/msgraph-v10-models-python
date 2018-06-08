# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.boolean_column import BooleanColumn
from ..model.calculated_column import CalculatedColumn
from ..model.choice_column import ChoiceColumn
from ..model.currency_column import CurrencyColumn
from ..model.date_time_column import DateTimeColumn
from ..model.default_column_value import DefaultColumnValue
from ..model.lookup_column import LookupColumn
from ..model.number_column import NumberColumn
from ..model.person_or_group_column import PersonOrGroupColumn
from ..model.text_column import TextColumn
from ..one_drive_object_base import OneDriveObjectBase


class ColumnDefinition(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def boolean(self):
        """
        Gets and sets the boolean
        
        Returns: 
            :class:`BooleanColumn<onedrivesdk.model.boolean_column.BooleanColumn>`:
                The boolean
        """
        if "boolean" in self._prop_dict:
            if isinstance(self._prop_dict["boolean"], OneDriveObjectBase):
                return self._prop_dict["boolean"]
            else :
                self._prop_dict["boolean"] = BooleanColumn(self._prop_dict["boolean"])
                return self._prop_dict["boolean"]

        return None

    @boolean.setter
    def boolean(self, val):
        self._prop_dict["boolean"] = val

    @property
    def calculated(self):
        """
        Gets and sets the calculated
        
        Returns: 
            :class:`CalculatedColumn<onedrivesdk.model.calculated_column.CalculatedColumn>`:
                The calculated
        """
        if "calculated" in self._prop_dict:
            if isinstance(self._prop_dict["calculated"], OneDriveObjectBase):
                return self._prop_dict["calculated"]
            else :
                self._prop_dict["calculated"] = CalculatedColumn(self._prop_dict["calculated"])
                return self._prop_dict["calculated"]

        return None

    @calculated.setter
    def calculated(self, val):
        self._prop_dict["calculated"] = val

    @property
    def choice(self):
        """
        Gets and sets the choice
        
        Returns: 
            :class:`ChoiceColumn<onedrivesdk.model.choice_column.ChoiceColumn>`:
                The choice
        """
        if "choice" in self._prop_dict:
            if isinstance(self._prop_dict["choice"], OneDriveObjectBase):
                return self._prop_dict["choice"]
            else :
                self._prop_dict["choice"] = ChoiceColumn(self._prop_dict["choice"])
                return self._prop_dict["choice"]

        return None

    @choice.setter
    def choice(self, val):
        self._prop_dict["choice"] = val

    @property
    def column_group(self):
        """
        Gets and sets the columnGroup
        
        Returns:
            str:
                The columnGroup
        """
        if "columnGroup" in self._prop_dict:
            return self._prop_dict["columnGroup"]
        else:
            return None

    @column_group.setter
    def column_group(self, val):
        self._prop_dict["columnGroup"] = val

    @property
    def currency(self):
        """
        Gets and sets the currency
        
        Returns: 
            :class:`CurrencyColumn<onedrivesdk.model.currency_column.CurrencyColumn>`:
                The currency
        """
        if "currency" in self._prop_dict:
            if isinstance(self._prop_dict["currency"], OneDriveObjectBase):
                return self._prop_dict["currency"]
            else :
                self._prop_dict["currency"] = CurrencyColumn(self._prop_dict["currency"])
                return self._prop_dict["currency"]

        return None

    @currency.setter
    def currency(self, val):
        self._prop_dict["currency"] = val

    @property
    def date_time(self):
        """
        Gets and sets the dateTime
        
        Returns: 
            :class:`DateTimeColumn<onedrivesdk.model.date_time_column.DateTimeColumn>`:
                The dateTime
        """
        if "dateTime" in self._prop_dict:
            if isinstance(self._prop_dict["dateTime"], OneDriveObjectBase):
                return self._prop_dict["dateTime"]
            else :
                self._prop_dict["dateTime"] = DateTimeColumn(self._prop_dict["dateTime"])
                return self._prop_dict["dateTime"]

        return None

    @date_time.setter
    def date_time(self, val):
        self._prop_dict["dateTime"] = val

    @property
    def default_value(self):
        """
        Gets and sets the defaultValue
        
        Returns: 
            :class:`DefaultColumnValue<onedrivesdk.model.default_column_value.DefaultColumnValue>`:
                The defaultValue
        """
        if "defaultValue" in self._prop_dict:
            if isinstance(self._prop_dict["defaultValue"], OneDriveObjectBase):
                return self._prop_dict["defaultValue"]
            else :
                self._prop_dict["defaultValue"] = DefaultColumnValue(self._prop_dict["defaultValue"])
                return self._prop_dict["defaultValue"]

        return None

    @default_value.setter
    def default_value(self, val):
        self._prop_dict["defaultValue"] = val

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
    def enforce_unique_values(self):
        """
        Gets and sets the enforceUniqueValues
        
        Returns:
            bool:
                The enforceUniqueValues
        """
        if "enforceUniqueValues" in self._prop_dict:
            return self._prop_dict["enforceUniqueValues"]
        else:
            return None

    @enforce_unique_values.setter
    def enforce_unique_values(self, val):
        self._prop_dict["enforceUniqueValues"] = val

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
    def indexed(self):
        """
        Gets and sets the indexed
        
        Returns:
            bool:
                The indexed
        """
        if "indexed" in self._prop_dict:
            return self._prop_dict["indexed"]
        else:
            return None

    @indexed.setter
    def indexed(self, val):
        self._prop_dict["indexed"] = val

    @property
    def lookup(self):
        """
        Gets and sets the lookup
        
        Returns: 
            :class:`LookupColumn<onedrivesdk.model.lookup_column.LookupColumn>`:
                The lookup
        """
        if "lookup" in self._prop_dict:
            if isinstance(self._prop_dict["lookup"], OneDriveObjectBase):
                return self._prop_dict["lookup"]
            else :
                self._prop_dict["lookup"] = LookupColumn(self._prop_dict["lookup"])
                return self._prop_dict["lookup"]

        return None

    @lookup.setter
    def lookup(self, val):
        self._prop_dict["lookup"] = val

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
    def number(self):
        """
        Gets and sets the number
        
        Returns: 
            :class:`NumberColumn<onedrivesdk.model.number_column.NumberColumn>`:
                The number
        """
        if "number" in self._prop_dict:
            if isinstance(self._prop_dict["number"], OneDriveObjectBase):
                return self._prop_dict["number"]
            else :
                self._prop_dict["number"] = NumberColumn(self._prop_dict["number"])
                return self._prop_dict["number"]

        return None

    @number.setter
    def number(self, val):
        self._prop_dict["number"] = val

    @property
    def person_or_group(self):
        """
        Gets and sets the personOrGroup
        
        Returns: 
            :class:`PersonOrGroupColumn<onedrivesdk.model.person_or_group_column.PersonOrGroupColumn>`:
                The personOrGroup
        """
        if "personOrGroup" in self._prop_dict:
            if isinstance(self._prop_dict["personOrGroup"], OneDriveObjectBase):
                return self._prop_dict["personOrGroup"]
            else :
                self._prop_dict["personOrGroup"] = PersonOrGroupColumn(self._prop_dict["personOrGroup"])
                return self._prop_dict["personOrGroup"]

        return None

    @person_or_group.setter
    def person_or_group(self, val):
        self._prop_dict["personOrGroup"] = val

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
    def required(self):
        """
        Gets and sets the required
        
        Returns:
            bool:
                The required
        """
        if "required" in self._prop_dict:
            return self._prop_dict["required"]
        else:
            return None

    @required.setter
    def required(self, val):
        self._prop_dict["required"] = val

    @property
    def text(self):
        """
        Gets and sets the text
        
        Returns: 
            :class:`TextColumn<onedrivesdk.model.text_column.TextColumn>`:
                The text
        """
        if "text" in self._prop_dict:
            if isinstance(self._prop_dict["text"], OneDriveObjectBase):
                return self._prop_dict["text"]
            else :
                self._prop_dict["text"] = TextColumn(self._prop_dict["text"])
                return self._prop_dict["text"]

        return None

    @text.setter
    def text(self, val):
        self._prop_dict["text"] = val

