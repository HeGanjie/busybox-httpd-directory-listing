#!/bin/sh
printf "Content-Type: text/plain\r\n\r\n"
ls -A -p ..${REQUEST_URI#${SCRIPT_NAME}}