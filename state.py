from PyQt5.QtCore import QObject, pyqtSignal
from datetime import datetime
from time_tracker import *
from utils import get_project_index

class State(QObject):

    class __State:
        def __init__(self, data_path):
            super(State).__init__()
            self.data_path = data_path
            self.data = load_data(data_path)
            self.listeners = []

        def update_data_path(self, data_path):
            #Update data path and notify listeners
            self.data_path = data_path
            self.data = load_data(data_path)
            self.notify_update()

        def add_listener(self, listener):
            #Adds a new listener and triggers an update.
            self.listeners.append(listener)
            self.notify_update()

        def add_project(self, project_name):
            #To add a new project
            self.data = create_project(project_name, self.data)
            #TODO: when creating project, save_data is done automatically
            self.notify_update()

        def update_project(self, old_name, new_name):
            #To edit a project
            idx = get_project_index(self.data, old_name)
            if idx >= 0:
                project_data = self.data.get("projects")[idx]
                project_data.update({"project_name": new_name})
                self.data.get("projects").pop(idx)
                self.data.get("projects").insert(idx, project_data)
                save_data(self.data, self.data_path)
                self.notify_update()

        def remove_project(self, project_name):
            #To remove a project
            idx = get_project_index(self.data, project_name)
            if idx >= 0:
                self.data.get("projects").pop(idx)
                save_data(self.data, self.data_path)
                self.notify_update()

        ## Move to time-tracker
        def are_there_ongoing_sessions(self, project_name):
            # Returns True if is there an ongoing working session for a given project. 
            # Otherwise, returns False.
            ongoing = False
            for p in self.data.get("projects"):
                if p.get("project_name") == project_name:
                    for s in p.get("sessions"):
                        if s.get("end") is None:
                            ongoing = True
            return ongoing

        def get_last_session_timedelta(self, project_name):
            #Return timedelta and True if the last session is ongoing otherwise, False
            p = get_project(project_name, self.data)
            last_session = p.get("sessions")[-1]
            start = format_date(last_session.get("start"))
            if last_session.get("end") is not None:
                end = format_date(last_session.get("end"))
                return end - start, False
            else:
                end = datetime.now()
                return end - start, True

        def get_project_names(self):
            return [p.get("project_name") for p in self.data.get("projects")]
        
        def get_total_timedelta(self, project_name):
            total = calculate_total(self.data, project_name)
            return total.get("completed_sessions")
        ## 
            
        def add_timestamp(self, project_name):
            #To add a timestamp (start/end) to the last working session of a project 
            p = get_project(project_name, self.data)
            p = add_timestamp(p)
            self.data = update_project(p, self.data)
            save_data(self.data, self.data_path)
            self.notify_update()

        def notify_update(self):
            for l in self.listeners:
                l.update_data(self.data)

    instance = None
    def __init__(self, data_path):
        if not State.instance:
            State.instance = State.__State(data_path)
        #else:
        #    State.instance.update_data_path(data_path)

    def __getattr__(self, name):
        return getattr(self.instance, name)