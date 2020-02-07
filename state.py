#!/usr/bin/python
# -*- coding: utf-8 -*-

from PyQt5.QtCore import QObject, pyqtSignal
import time_tracker_cli as tt

class State(QObject):

    class __State:
        def __init__(self, data_path):
            super(State).__init__()
            self.data_path = data_path
            self.data = tt.load_data(data_path)
            self.listeners = []

        def update_data_path(self, data_path):
            # Update data path and notify listeners
            self.data_path = data_path
            self.data = tt.load_data(data_path)
            self.notify_update()

        def add_listener(self, listener):
            # Adds a new listener and triggers an update.
            self.listeners.append(listener)
            self.notify_update()

        def add_project(self, project_name):
            # To add a new project
            self.data = tt.create_project(project_name, self.data)
            tt.save_data(self.data, self.data_path)
            self.notify_update()

        def update_project(self, old_name, new_name):
            # To update/edit a project
            idx = tt.get_project_index(old_name, self.data)
            if idx >= 0:
                project_data = self.data.get("projects")[idx]
                project_data.update({"project_name": new_name})
                self.data.get("projects").pop(idx)
                self.data.get("projects").insert(idx, project_data)
                tt.save_data(self.data, self.data_path)
                self.notify_update()

        def remove_project(self, project_name):
            # To remove a project
            idx = tt.get_project_index(project_name, self.data)
            if idx >= 0:
                self.data.get("projects").pop(idx)
                tt.save_data(self.data, self.data_path)
                self.notify_update()

        def add_timestamp(self, project_name):
            # To add a timestamp (start/end) to the last working session of a project 
            p = tt.get_project(project_name, self.data)
            p = tt.add_timestamp(p)
            self.data = tt.update_project(p, self.data)
            tt.save_data(self.data, self.data_path)
            self.notify_update()

        def notify_update(self):
            # Notifies data changes to every state listener
            if len(self.data_path) > 0:
                for l in self.listeners:
                    l.update_data(self.data)

        # time-tracker wrapper methods
        def has_ongoing_sessions(self, project_name):
            return tt.has_ongoing_sessions(project_name, self.data)

        def get_last_session_timedelta(self, project_name):
            return tt.get_last_session_timedelta(project_name, self.data)

        def get_project_names(self):
            return tt.get_project_names(self.data)

        def get_total_timedelta(self, project_name):
            return tt.get_total_timedelta(project_name, self.data)

    instance = None
    def __init__(self, data_path):
        if not State.instance:
            State.instance = State.__State(data_path)

    def __getattr__(self, name):
        return getattr(self.instance, name)