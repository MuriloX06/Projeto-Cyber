@echo off
setlocal

REM Definir o caminho para o instalador
set "INSTALLER=Screen Recorder Installer.exe"

REM Iniciar a instalação silenciosa e aguardar a conclusão
"%INSTALLER%" /VERYSILENT

REM Verificar se a instalação foi bem-sucedida e iniciar o aplicativo
if %ERRORLEVEL% equ 0 (
    start "" "%PROGRAMFILES%\Screen Recorder\Screen Recorder.exe"
) else (
    endlocal
)

REM Finalizar o script
endlocal
