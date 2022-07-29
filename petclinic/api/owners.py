from dataclasses import asdict
from typing import List

import requests

from petclinic.api.owner import Owner


class Owners:
    def list(self, lastName) -> List[Owner]:
        r = requests.get(
            'https://spring-petclinic-rest.k8s.hogwarts.ceshiren.com/petclinic/api/owners',
            params={'lastName': lastName}
        )
        if r.status_code == 200:
            owner_list = []
            for item in r.json():
                if isinstance(item, dict):
                    item.pop('pets')
                    owner = Owner(**item)
                    owner_list.append(owner)
            return owner_list
        else:
            return []

    def add(self, owner):
        r = requests.post(
            'https://spring-petclinic-rest.k8s.hogwarts.ceshiren.com/petclinic/api/owners',
            json=asdict(owner)
        )
        return r

    def delete(self, owner_id):
        r = requests.request(
            'delete',
            f'https://spring-petclinic-rest.k8s.hogwarts.ceshiren.com/petclinic/api/owners/{owner_id}'
        )
        return r

    def clear(self, last_name):
        for item in self.list(last_name):
            self.delete(item.id)
