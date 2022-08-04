import logging
from copy import copy
import pytest

from petclinic.api.owner import Owner
from petclinic.api.owners import Owners
from petclinic.tests.test_data import owner_common
from petclinic.tests.test_owner import TestOwner
from petclinic.utils.log import log


class TestOwnersAdd(TestOwner):
    def setup_class(self):
        super(TestOwnersAdd, self).setup_class(self)
        logging.debug("setup_class TestOwnersAdd")

        self.owners = Owners()
        self.owners.clear("herman")

    def teardown_class(self):
        self.owners.clear("herman")

    @pytest.mark.parametrize("owner", [
        {'telephone': '6085551234', 'city': 'shanghai'},
        {'telephone': '6085551235', 'city': 'beijing'}
    ])
    def test_add_success(self, owner):
        owner_data = Owner(**owner)
        owner_data.address = 'pudong'
        owner_data.firstName = 'cui'
        owner_data.lastName = 'herman'

        r = self.owners.add(owner_data)
        assert r.status_code == 201

    @pytest.mark.parametrize("owner", [
        {'telephone': '6085551023', 'firstName': ''},
        {'telephone': '6085551023', 'firstName': '11'},
        {'telephone': '6085551023', 'firstName': '1a'},
        {'telephone': '', 'firstName': 'hogwarts'},
        {'telephone': 'abfsfef', 'firstName': 'fffffff'},
    ])
    def test_add_fail(self, owner):
        owner_data = copy(owner_common)
        owner_param = Owner(**owner)
        owner_data.telephone = owner_param.telephone
        owner_data.firstName = owner_param.firstName
        r = self.owners.add(owner_data)

        log.debug(r.text)

        assert r.status_code != 201
