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

## Alternatives
* BusyBox have [httpd_indexcgi.c](https://github.com/mirror/busybox/blob/master/networking/httpd_indexcgi.c) which works without JS
* [metalx1000/Directory-Index-for-httpd](https://github.com/metalx1000/Directory-Index-for-httpd) more advanced
* [dir-index.cgi](https://gist.github.com/jow-/743363c332d09cb58a60dd1f216b6ee4) a Perl script
* [Making Our Own Indexes](https://docstore.mik.ua/orelly/linux/apache/ch07_02.htm) a tutorial how to make it yourself
