#!/bin/sh

echo "`wget -qO- http://www.insiteone.com/brianjsmysqlimage.php|xargs`\t`date +%s`"
