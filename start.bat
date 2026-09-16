@echo off
title Naraito's Playbook Portal
echo ======================================================================
echo Launching Naraito's Playbook (0 Experience Edition)
echo ======================================================================
echo Starting local web server on http://localhost:8080 ...
start http://localhost:8080
python -m http.server 8080 --directory "%~dp0"
pause
