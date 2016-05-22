#!/usr/bin/python
# -*- coding: utf-8 -*-
'''Wrapper de commande yum pour le user www'''
__author__      = u"DELGEHIER Cedric"
__email__       = u"cedric.delgehier@worldline.com"
__maintainer__  = [u"DELGEHIER Cedric", u"DENNETIERE Anthony", u"TIERS Christine"]
__date__        = u"20151230"
__version__     = u"0.3"

from sys import argv,exit
from subprocess import call,CalledProcessError
import os

#####PARAM#########
yum_bin = '/usr/bin/yum'

cmd = {
    'search'     : '{0} search       --disablerepo=* --enablerepo=pmu'.format(yum_bin),
    'install'    : '{0} install      --disablerepo=* --enablerepo=pmu'.format(yum_bin),
    'instally'   : '{0} install   -y --disablerepo=* --enablerepo=pmu'.format(yum_bin),
    'reinstall'  : '{0} install      --disablerepo=* --enablerepo=pmu'.format(yum_bin),
    'reinstally' : '{0} install   -y --disablerepo=* --enablerepo=pmu'.format(yum_bin),
    'update'     : '{0} update       --disablerepo=* --enablerepo=pmu'.format(yum_bin),
    'updatey'    : '{0} update    -y --disablerepo=* --enablerepo=pmu'.format(yum_bin),
    'downgrade'  : '{0} downgrade    --disablerepo=* --enablerepo=pmu'.format(yum_bin),
    'downgradey' : '{0} downgrade -y --disablerepo=* --enablerepo=pmu'.format(yum_bin),
    'clean'      : '{0} clean all    --disablerepo=* --enablerepo=pmu'.format(yum_bin),
    'list'       : '{0} list         --disablerepo=* --enablerepo=pmu --setopt=pmu.metadata_expire=0'.format(yum_bin),
    'list_dup'   : '{0} list         --disablerepo=* --enablerepo=pmu --setopt=pmu.metadata_expire=0 --showduplicates'.format(yum_bin),
    'remove'     : '{0} remove'.format(yum_bin),
}

erreurs = {
    1   : 'Arguments non suffisant',
    2   : 'La commande donnee n est pas prevu pour votre user',
    3   : 'Le nom du rpm ne correspond pas a la nomenclature en rigueur',
}

######FONCTIONS#####
def print_syntax(errno):
    '''
    Display the tool syntax
    '''
    print "\t{0} \033[1;31m{1} \033[1;30mrpm_name\033[1;m".format(argv[0], ",".join(sorted(cmd.keys())))
    print "\t{0}".format(erreurs[errno])

    exit(errno)

def check_number_arg(argv):
    if len(argv) == 3 or len(argv) == 2 and argv[1] == "clean":
        pass
    else:
        print_syntax(1)

def check_action(action):
    '''
    Check if the action paramater is known
    '''
    if action in cmd.keys() and len(action.split()) == 1:
        pass
    else:
        print_syntax(2)

def check_rpm_name(rpmname):
    '''
    Check if the rpm name respects the current nomenclature
    '''
    if rpmname == '' or rpmname.startswith( 'pmu-' ) and len(rpmname.split()) == 1:
        pass
    else:
        print_syntax(3)



######MAIN########
if __name__ == '__main__':

    check_number_arg(argv)

    action=argv[1]
    if action != "clean":
        rpm=argv[2]
    else:
        rpm=''

    check_action(action)
    check_rpm_name(rpm)

    commande = ' '.join("{0} {1}".format(cmd[action], rpm).split())
    #print '\t===> {0}'.format(commande)

    try:
        return_code = call(commande, shell=True)
    except OSError:
        print u'\t{0} n a pas ete trouvé'.format(yum_bin)
    except (CalledProcessError, Exception) as e:
        print '\t\033[0,32m===> \033[0,31m{0}\033[1;m'.format(commande)
        print '\tCette commande s est mal terminee'
        print

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
