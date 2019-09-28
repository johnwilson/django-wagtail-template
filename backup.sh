#!/bin/bash

app="<your app>"
today=`date '+%Y_%m_%d-%H_%M_%S'`;

# backup database
dbfile="/tmp/$app-db-$today.dump"
dokku postgres:export $app > $dbfile
rclone copy $dbfile gdrive:/cms_backups
rm $dbfile

# backup media dir
mediafile="/tmp/$app-media-$today.tar.gz"
tar -czf $mediafile -C / "home/dokku/$app/storage/media"
rclone copy $mediafile gdrive:/cms_backups
rm $mediafile

echo "done"