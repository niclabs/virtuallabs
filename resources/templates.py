from main import connection


class Templates:
    def __init__(self, regex):
        machines = connection.list_machines()
        self.templates = [i for i in machines if i.startswith(regex)]

    def get_template(self, template_id):
        return self.templates[template_id]

    def list_templates(self):
        return self.templates

    def __contains__(self, item):
        return item in self.templates

    def number(self):
        return len(self.templates)

    def add_template(self):
        pass


class OSTemplates(Templates):
    def __init__(self):
        Templates.__init__(self, 'template_os_')


class RouterTemplates(Templates):
    def __init__(self):
        Templates.__init__(self, 'template_router_')


class SwitchTemplates(Templates):
    def __init__(self):
        Templates.__init__(self, 'template_switch_')













