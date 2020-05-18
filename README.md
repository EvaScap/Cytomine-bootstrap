# Cytomine Bootstrap

> Cytomine bootstrap is the installer for Cytomine. The application can run on a server to allow remote users to access the web platform or locally on your own machine.

[![Build Status](https://travis-ci.com/Cytomine-ULiege/Cytomine-bootstrap.svg?branch=master)](https://travis-ci.com/Cytomine-ULiege/Cytomine-bootstrap)
[![GitHub release](https://img.shields.io/github/release/Cytomine-ULiege/Cytomine-bootstrap.svg)](https://github.com/Cytomine-ULiege/Cytomine-bootstrap/releases)
[![GitHub](https://img.shields.io/github/license/Cytomine-ULiege/Cytomine-bootstrap.svg)](https://github.com/Cytomine-ULiege/Cytomine-bootstrap/blob/master/LICENSE)

## Overview

[Cytomine](http://cytomine.org) is, to the best of our knowledge, the first open-source rich internet application to enable highly collaborative and multidisciplinary analysis of multi-gigapixel imaging data.

This bootstrap procedure allows you to configure your installation and generate an installer script based on this configuration. 
All Cytomine components run in kunernetes pods using microk8s and launch with Python, so that the only requirements are Docker, microk8s and Python.


## Install

**To install this release of Cytomine, follow this guide to install forked version by Eva Scapellato.** 

1. install Docker-Compose and Python:
* [install Docker](https://docs.docker.com/compose/install/)
* [Install Python 3](https://realpython.com/installing-python/)
* [Install MicroK8s](https://microk8s.io/#get-started)


2. Retrieve this version of Cytomine-Bootstrap using the following commands:
    * `mdkir Cytomine`
    * `cd Cytomine/`
    * `git clone https://github.com/EvaScap/Cytomine-bootstrap.git` 
    * `cd Cytomine-bootstrap`
    * `git checkout kubernetes`
    * `pip3 install -r requirements.txt`
3. generate the Core image working with docker-compose using the following commands:
    * `mdkir Cytomine`
    * `cd Cytomine/`
    * `git clone https://github.com/EvaScap/Cytomine-core.git` 
    * `cd Cytomine-core`
    * `git checkout Docker-Compose`
    * `docker build  -t cytomineuliege/core:dockercompose docker/`
3. Fill the `configurationBase.yml` file.
4. to start Cytomine, run: `python3 start.py`
5. to stop it: `python3 stop.py`
6. to restart the server, run `python3 restart.py`.

You may be interested in [Cytomine parameter configuration reference](https://doc.cytomine.be/display/PubOp/Cytomine+configuration+reference).

## Documentation

Full documentation can be found [online](https://doc.cytomine.be).

## References
When using our software, we kindly ask you to cite our website url and related publications in all your work (publications, studies, oral presentations,...). In particular, we recommend to cite (Marée et al., Bioinformatics 2016) paper, and to use our logo when appropriate. See our license files for additional details.

- URL: http://www.cytomine.org/
- Logo: [Available here](https://cytomine.coop/sites/cytomine.coop/files/inline-images/logo-300-org.png)
- Scientific paper: Raphaël Marée, Loïc Rollus, Benjamin Stévens, Renaud Hoyoux, Gilles Louppe, Rémy Vandaele, Jean-Michel Begon, Philipp Kainz, Pierre Geurts and Louis Wehenkel. Collaborative analysis of multi-gigapixel imaging data using Cytomine, Bioinformatics, DOI: [10.1093/bioinformatics/btw013](http://dx.doi.org/10.1093/bioinformatics/btw013), 2016.

## License

Apache 2.0
