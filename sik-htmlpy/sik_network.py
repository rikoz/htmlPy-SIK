
# -*- coding: utf-8 -*-

import pyiw
from sik_wireless import sik_iface

iface_name = sik_iface()

def Search():
    pyiwlist = []

    cells = pyiw.Cell.all(iface_name)

    for cell in cells:
        pyiwlist.append(cell)

    return pyiwlist


def FindFromSearchList(ssid):
    pyiwlist = Search()

    for cell in pyiwlist:
        if cell.ssid == ssid:
            return cell

    return False


def FindFromSavedList(ssid):
    cell = pyiw.Scheme.find(iface_name, ssid)

    if cell:
        return cell

    return False


def Connect(ssid, password=None):
    cell = FindFromSearchList(ssid)

    if cell:
        savedcell = FindFromSavedList(cell.ssid)

        # Already Saved from Setting
        if savedcell:
            savedcell.activate()
            return cell

        # First time to conenct
        else:
            if cell.encrypted:
                if password:
                    scheme = Add(cell, password)

                    try:
                        scheme.activate()

                    # Wrong Password
                    except pyiw.exceptions.ConnectionError:
                        Delete(ssid)
                        return False

                    return cell
                else:
                    return False
            else:
                scheme = Add(cell)

                try:
                    scheme.activate()
                except pyiw.exceptions.ConnectionError:
                    Delete(ssid)
                    return False

                return cell
    
    return False


def Add(ssid, password=None):
	cell = FindFromSearchList(ssid)
	
	if not cell:
		return False

	scheme = pyiw.Scheme.for_cell(iface_name, ssid, cell, password)
	scheme.save()
	return scheme


def Delete(ssid):
    if not ssid:
        return False

    cell = FindFromSavedList(ssid)

    if cell:
        cell.delete()
        return True

    return False

"""
if __name__ == '__main__':
    # Search pyiw and return pyiw list
    print Search()

    # Connect pyiw with password & without password
    print Connect('Openwifi')
    print FindFromSearchList('#koz iPhone')
    print Add('#koz iPhone', 'omocc5n4jr7zn')
    print FindFromSavedList('#koz iPhone')
    print Connect('#koz iPhone', 'omocc5n4jr7zn')

    # Delete pyiw from auto connect list
    #print Delete('Deletewifi')
"""