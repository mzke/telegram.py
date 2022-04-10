source venv/bin/activate
rm -f -R build/*
pip3 freeze > requirements.txt
pip3 install -r requirements.txt --target build/
cp src/* build/
rm -R build/*.dist-info
python3 -m zipapp build/ -p "/usr/bin/env python3" -o dist/telegram.pyz -c