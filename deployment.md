# Deployment

## Windows deployment
```powershell
pyinstaller --onefile --windowed -i "PathToIcon" tracker.py
Copy-Item .\img\ .\dist\ -Recurse
Copy-Item .\data.json .\dist\
```

## Linux deployment
```bash
pyinstaller --onefile --windowed --hidden-import='PIL._tkinter_finder' tracker.py
cp -r img dist/; cp -r data.json dist/;
```
