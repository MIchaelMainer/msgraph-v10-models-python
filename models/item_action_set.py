# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.comment_action import CommentAction
from ..model.create_action import CreateAction
from ..model.delete_action import DeleteAction
from ..model.edit_action import EditAction
from ..model.mention_action import MentionAction
from ..model.move_action import MoveAction
from ..model.rename_action import RenameAction
from ..model.restore_action import RestoreAction
from ..model.share_action import ShareAction
from ..model.version_action import VersionAction
from ..one_drive_object_base import OneDriveObjectBase


class ItemActionSet(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def comment(self):
        """
        Gets and sets the comment
        
        Returns: 
            :class:`CommentAction<onedrivesdk.model.comment_action.CommentAction>`:
                The comment
        """
        if "comment" in self._prop_dict:
            if isinstance(self._prop_dict["comment"], OneDriveObjectBase):
                return self._prop_dict["comment"]
            else :
                self._prop_dict["comment"] = CommentAction(self._prop_dict["comment"])
                return self._prop_dict["comment"]

        return None

    @comment.setter
    def comment(self, val):
        self._prop_dict["comment"] = val
    @property
    def create(self):
        """
        Gets and sets the create
        
        Returns: 
            :class:`CreateAction<onedrivesdk.model.create_action.CreateAction>`:
                The create
        """
        if "create" in self._prop_dict:
            if isinstance(self._prop_dict["create"], OneDriveObjectBase):
                return self._prop_dict["create"]
            else :
                self._prop_dict["create"] = CreateAction(self._prop_dict["create"])
                return self._prop_dict["create"]

        return None

    @create.setter
    def create(self, val):
        self._prop_dict["create"] = val
    @property
    def delete(self):
        """
        Gets and sets the delete
        
        Returns: 
            :class:`DeleteAction<onedrivesdk.model.delete_action.DeleteAction>`:
                The delete
        """
        if "delete" in self._prop_dict:
            if isinstance(self._prop_dict["delete"], OneDriveObjectBase):
                return self._prop_dict["delete"]
            else :
                self._prop_dict["delete"] = DeleteAction(self._prop_dict["delete"])
                return self._prop_dict["delete"]

        return None

    @delete.setter
    def delete(self, val):
        self._prop_dict["delete"] = val
    @property
    def edit(self):
        """
        Gets and sets the edit
        
        Returns: 
            :class:`EditAction<onedrivesdk.model.edit_action.EditAction>`:
                The edit
        """
        if "edit" in self._prop_dict:
            if isinstance(self._prop_dict["edit"], OneDriveObjectBase):
                return self._prop_dict["edit"]
            else :
                self._prop_dict["edit"] = EditAction(self._prop_dict["edit"])
                return self._prop_dict["edit"]

        return None

    @edit.setter
    def edit(self, val):
        self._prop_dict["edit"] = val
    @property
    def mention(self):
        """
        Gets and sets the mention
        
        Returns: 
            :class:`MentionAction<onedrivesdk.model.mention_action.MentionAction>`:
                The mention
        """
        if "mention" in self._prop_dict:
            if isinstance(self._prop_dict["mention"], OneDriveObjectBase):
                return self._prop_dict["mention"]
            else :
                self._prop_dict["mention"] = MentionAction(self._prop_dict["mention"])
                return self._prop_dict["mention"]

        return None

    @mention.setter
    def mention(self, val):
        self._prop_dict["mention"] = val
    @property
    def move(self):
        """
        Gets and sets the move
        
        Returns: 
            :class:`MoveAction<onedrivesdk.model.move_action.MoveAction>`:
                The move
        """
        if "move" in self._prop_dict:
            if isinstance(self._prop_dict["move"], OneDriveObjectBase):
                return self._prop_dict["move"]
            else :
                self._prop_dict["move"] = MoveAction(self._prop_dict["move"])
                return self._prop_dict["move"]

        return None

    @move.setter
    def move(self, val):
        self._prop_dict["move"] = val
    @property
    def rename(self):
        """
        Gets and sets the rename
        
        Returns: 
            :class:`RenameAction<onedrivesdk.model.rename_action.RenameAction>`:
                The rename
        """
        if "rename" in self._prop_dict:
            if isinstance(self._prop_dict["rename"], OneDriveObjectBase):
                return self._prop_dict["rename"]
            else :
                self._prop_dict["rename"] = RenameAction(self._prop_dict["rename"])
                return self._prop_dict["rename"]

        return None

    @rename.setter
    def rename(self, val):
        self._prop_dict["rename"] = val
    @property
    def restore(self):
        """
        Gets and sets the restore
        
        Returns: 
            :class:`RestoreAction<onedrivesdk.model.restore_action.RestoreAction>`:
                The restore
        """
        if "restore" in self._prop_dict:
            if isinstance(self._prop_dict["restore"], OneDriveObjectBase):
                return self._prop_dict["restore"]
            else :
                self._prop_dict["restore"] = RestoreAction(self._prop_dict["restore"])
                return self._prop_dict["restore"]

        return None

    @restore.setter
    def restore(self, val):
        self._prop_dict["restore"] = val
    @property
    def share(self):
        """
        Gets and sets the share
        
        Returns: 
            :class:`ShareAction<onedrivesdk.model.share_action.ShareAction>`:
                The share
        """
        if "share" in self._prop_dict:
            if isinstance(self._prop_dict["share"], OneDriveObjectBase):
                return self._prop_dict["share"]
            else :
                self._prop_dict["share"] = ShareAction(self._prop_dict["share"])
                return self._prop_dict["share"]

        return None

    @share.setter
    def share(self, val):
        self._prop_dict["share"] = val
    @property
    def version(self):
        """
        Gets and sets the version
        
        Returns: 
            :class:`VersionAction<onedrivesdk.model.version_action.VersionAction>`:
                The version
        """
        if "version" in self._prop_dict:
            if isinstance(self._prop_dict["version"], OneDriveObjectBase):
                return self._prop_dict["version"]
            else :
                self._prop_dict["version"] = VersionAction(self._prop_dict["version"])
                return self._prop_dict["version"]

        return None

    @version.setter
    def version(self, val):
        self._prop_dict["version"] = val
