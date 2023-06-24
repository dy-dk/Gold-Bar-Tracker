# Deployment

## Compiling using pyinstaller
```powershell
pyinstaller --onefile --windowed -i "PathToIcon" trackerLight.py
Copy-Item .\img\ .\dist\ -Recurse
Copy-Item .\data.json .\dist\
```