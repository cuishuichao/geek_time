from dataclasses import asdict
from typing import List

from petclinic.api.owner import Owner
from petclinic.framework.http import Request
from petclinic.utils.log import log


class Owners:
    @staticmethod
    def list(lastName) -> List[Owner]:
        request = Request()
        request.host = 'https://spring-petclinic-rest.k8s.hogwarts.ceshiren.com'
        request.path = '/petclinic/api/owners'
        request.method = 'get'
        request.query = {'lastName': lastName}
        r = request.send()

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
        request = Request()
        request.host = 'https://spring-petclinic-rest.k8s.hogwarts.ceshiren.com'
        request.path = '/petclinic/api/owners'
        request.method = 'post'
        request.type = 'json'
        request.data = asdict(owner)
        r = request.send()

        log.debug(r.status_code)
        log.debug(r.text)
        return r

    def delete(self, owner_id):
        request = Request()
        request.method = 'delete'
        request.host = 'https://spring-petclinic-rest.k8s.hogwarts.ceshiren.com'
        request.path = f'/petclinic/api/owners/{owner_id}'
        r = request.send()
        log.debug(r)
        log.debug(r.text)
        return r

    def clear(self, last_name):
        for item in self.list(last_name):
            self.delete(item.id)
