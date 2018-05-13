#! /usr/bin/env python
'''

main script

'''


#%% imports

import os
HOME = os.path.expanduser('~/')
import sys
sys.path.append(HOME+'Perso/GitHub/PublicGit/OC/CoursALaCarte/Flask/concevez_un_site_avec_flask-P1C1')


#%% run

from fbapp import app

if __name__ == "__main__":
    app.run(debug=True)






