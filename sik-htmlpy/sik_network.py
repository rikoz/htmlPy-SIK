#network config man
#from PySide import QtCore, QtNetwork
#mgr = QtNetwork.QNetworkConfigurationManager()

# -*- coding: utf-8 -*-

import pyiw


def Search():
    pyiwlist = []

    cells = pyiw.Cell.all('wlp2s0')

    for cell in cells:
        pyiwlist.append(cell)

    return pyiwlist


def FindFromSearchList(ssid):
    pyiwlist = Search()

    for cell in pyiwlist:
        if cell.ssid == ssid:
            return cell.ssid # + " " + cell.encryption_type

    return False


def FindFromSavedList(ssid):
    cell = pyiw.Scheme.find('wlp2s0', ssid)

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

	scheme = pyiw.Scheme.for_cell('wlp2s0', cell, ssid, password)
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


if __name__ == '__main__':
    # Search pyiw and return pyiw list
    print Search()

    # Connect pyiw with password & without password
    print Connect('Openpyiw')
    print FindFromSearchList('MTN BB Mobile Hotspot 0448')
    print Add('MTN BB Mobile Hotspot 0448', 'erezi1405')
    print FindFromSavedList('MTN BB Mobile Hotspot 0448')
    print Connect('Closedpyiw', 'password')

    # Delete pyiw from auto connect list
    print Delete('Deletepyiw')