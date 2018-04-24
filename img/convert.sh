for fn in *.svg; do
  fnn=$(echo $fn| cut -f 1 -d '.')
  inkscape -D -z --file=$fn --export-pdf="$fnn".pdf
done
