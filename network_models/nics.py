from config.default_values import default_nic
from network_models.nic import NIC


class NICs:
    def __init__(self, nics):
        self.nics = nics
        self.used_names = []
        self.next_id = 0

    def create_nics(self):
        nic_instances = []

        for n in self.nics:
            if 'name' in n:
                nic_instances.append(NIC(n))
            else:
                name = self.create_name()
                n['name'] = name
                nic_instances.append(NIC(n))

        return nic_instances

    def create_name(self):
        default = default_nic + str(self.next_id)

        while default in self.used_names:
            self.next_id += 1
            default = default_nic + str(self.next_id)

        self.next_id += 1

        return default
