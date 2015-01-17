# busybox httpd directory listing
## Usage
For example, sharing `image` folder
```
$ git clone git@github.com:HeGanjie/busybox-httpd-directory-listing.git
$ cp -r busybox-httpd-directory-listing/* image/
$ cd image/
$ chmod +x cgi-bin/main.cgi
$ busybox httpd -fvvvp 8080
```
then open the link http://httpdhost:8080
