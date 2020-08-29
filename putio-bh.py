#!/usr/bin/env python

import os
import logging
import glob
import shutil
import json
import putiopy

with open(os.path.join(os.environ['CONFIG_DIR'], 'config.json'), 'r') as f:
	config = json.load(f)

logging.basicConfig(level='INFO')

client = putiopy.Client(config['OAUTH_TOKEN'])
blackhole=config['BLACKHOLE_DIR']

if not os.path.exists(config['INCOMPLETE_DIR']):
	os.mkdir(config['INCOMPLETE_DIR'])

for dir, id in config['dirs'].items():
	dest_dir=os.path.join(config['COMPLETE_DIR'], dir)
	torrent_dir= os.path.join(blackhole, dir)
	logging.info('Checking dir %s for torrents', torrent_dir)
	torrents=glob.glob(os.path.join(torrent_dir, '*.torrent'))
	if not os.path.exists(dest_dir):
        	os.mkdir(dest_dir)
	for torrent in torrents:
		logging.info('Found torrent %s in %s', torrent, torrent_dir)
		try:
			logging.info('Adding torrent %s', torrent)
			client.Transfer.add_torrent(path=torrent, parent_id=id)
			os.unlink(torrent)
			logging.info('Added torrent %s', torrent)
		except Exception as e:
			logging.warning('Failed to add torrent %s: %s', torrent, e)
			continue
	logging.info('Checking dir %s for magnets', torrent_dir)
	magnets=glob.glob(os.path.join(torrent_dir, '*.magnet'))
	for magnet in magnets:
		logging.info('Found magnet %s in %s', magnet, torrent_dir)
		try:
			logging.info('Adding magnet %s', magnet)
			client.Transfer.add_torrent(path=magnet, parent_id=id)
			os.unlink(magnet)
			logging.info('Added torrent %s', magnet)
		except Exception as e:
			logging.warning('Failed to add magnet %s: %s', magnet, e)
			continue
	logging.info('Checking dir %s for files to download', dir)
	files = client.File.list(id)
	for file in files:
		logging.info('Will download file %s.', file.name)
		file.download(dest=config['INCOMPLETE_DIR'],delete_after_download=True)
		shutil.move(os.path.join(config['INCOMPLETE_DIR'], file.name), dest_dir)

client.close()
