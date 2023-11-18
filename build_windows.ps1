try
{
    Write-Host "Build start."

    # remove previous build
    if (Test-Path -Path ".\dist")
    {
        Remove-Item -Path ".\dist" -Recurse
    }

    # run pyinstaller
    pyinstaller --onefile --windowed --clean --icon "src\img\peek.ico" src\tracker.py 

    # copy dependency  
    Copy-Item -Path "src\img\" -Destination ".\dist\" -Recurse
    Copy-Item -Path "src\data.json" -Destination ".\dist\"

    # clean up
    Remove-Item -Path ".\build" -Recurse
    Remove-Item -Path "tracker.spec"

    Write-Host "Build done."
}
catch
{
    Write-Host $_
    Write-Host $_.ScriptStackTrace
    Write-Host "Build failed."
}