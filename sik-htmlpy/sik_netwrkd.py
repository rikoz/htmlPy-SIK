
# -*- coding: utf-8 -*-

import wifi
from sik_wireless import sik_iface

iface_name = sik_iface()

def Search():
    wifilist = []

    cells = wifi.Cell.all(iface_name)

    for cell in cells:
        wifilist.append(cell)

    return wifilist


def FindFromSearchList(ssid):
    wifilist = Search()

    for cell in wifilist:
        if cell.ssid == ssid:
            return cell

    return False


def FindFromSavedList(ssid):
    cell = wifi.Scheme.find(iface_name, ssid)

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
                    except wifi.exceptions.ConnectionError:
                        Delete(ssid)
                        return False

                    return cell
                else:
                    return False
            else:
                scheme = Add(cell)

                try:
                    scheme.activate()
                except wifi.exceptions.ConnectionError:
                    Delete(ssid)
                    return False

                return cell
    
    return False


def Add(ssid, password=None):
	cell = FindFromSearchList(ssid)
	
	if not cell:
		return False

	scheme = wifi.Scheme.for_cell(iface_name, ssid, cell, password)
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
    # Search wifi and return wifi list
    print Search()

    # Connect wifi with password & without password
    print Connect('Openwifi')
    print FindFromSearchList('koz..py')
    print Add('#koz iPhone', 'omocc5n4jr7zn')
    print FindFromSavedList('#koz iPhone')
    print Connect('#koz iPhone', 'omocc5n4jr7zn')

    # Delete wifi from auto connect list
    #print Delete('Deletewifi')
