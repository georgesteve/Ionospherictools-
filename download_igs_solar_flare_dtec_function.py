# -*- coding: utf-8 -*-


from find_file_in_folder import find_file
import numpy as np

import requests


def download_CCDIS_IGS_GPS(day,estacs=['sant','areq','tac'],year=2022):
	day="{0:0=3d}".format(day)
	year=str(year)
	estac_down=[]
	
	for i in estacs:
		#print(i)
		if find_file(i+day+'0.'+year[2:4]+'d.gz') == None:
			url = 'https://cddis.nasa.gov/archive/gnss/data/daily/'+year+'/'+day+'/'+year[2:4]+'d/'+i+day+'0.'+year[2:4]+'d.gz'
			print('Downloading... '+url)
			try:
				r = requests.get(url, stream=True,timeout=10)
				if r.status_code == 200:
					estac_down=np.append(estac_down,i+day+'0.'+year[2:4]+'d.gz')
					with open(i+day+'0.'+year[2:4]+'d.gz', 'wb') as fd:
						for chunk in r.iter_content(chunk_size=1000):
							fd.write(chunk)

					# Closes local file
					fd.close()
				#else:
				#	print('Data from station '+i+' couldnt be downloaded')
			except requests.exceptions.Timeout as e:
			    # Maybe set up for a retry
			    print e

			except requests.exceptions.RequestException as e:
			    print e

		else:
			estac_down=np.append(estac_down,i+day+'0.'+year[2:4]+'d.gz')
			print('Archive '+i+day+'0.'+year[2:4]+'d.gz Already exists')
	print('Downloading finisfhed')
	return estac_down