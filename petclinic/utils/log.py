import logging

log = logging.getLogger("PetClinic")
log.setLevel(logging.DEBUG)

ch = logging.StreamHandler()
log.addHandler(ch)
