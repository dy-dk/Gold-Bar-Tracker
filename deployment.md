# Deployment

## Windows deployment
```powershell
pyinstaller --onefile --windowed -i "PathToIcon" trackerLight.py
Copy-Item .\img\ .\dist\ -Recurse
Copy-Item .\data.json .\dist\
```
