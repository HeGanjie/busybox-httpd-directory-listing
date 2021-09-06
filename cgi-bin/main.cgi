#!/bin/sh
printf "Content-Type: text/plain\r\n\r\n"
ls -a --group-directories-first ..${REQUEST_URI#${SCRIPT_NAME}}