# Deployment

## Windows deployment
```powershell
pyinstaller --onefile --windowed --clean --icon "src\img\peek.ico" src\tracker.py 
Copy-Item src\img\ .\dist\ -Recurse
Copy-Item src\data.json .\dist\
```

## Linux deployment
```bash
pyinstaller --onefile --windowed --hidden-import='PIL._tkinter_finder' tracker.py
cp -r img dist/; cp -r data.json dist/;
```
